from flask import Flask, Blueprint, session, request, flash, jsonify, render_template, Response, redirect, url_for
from model.db import Db
from werkzeug.security import generate_password_hash, check_password_hash
from model.exercicio import Exercises
import json, datetime
from model.logs import Logs
from model.response import Response as res
from basicFunction import random_generator, send_email

api = Blueprint('api', __name__, template_folder='templates')


@api.route("/getExercisesMusc")
def getExercisesMusc():
  res = Exercises.getExercisesMusc()
  response = json.dumps(res)
  return response, 200


@api.route("/getExercisesBodyWeight")
def getExercisesBodyWeight():
  allExer = Exercises.getExercisesBodyWeight()
  response = json.dumps(allExer)
  return response, 200


@api.route('/saveDU', methods=["POST"])
def saveDU():
  data = request.get_data().decode()
  data = json.loads(data.replace("'", "\""))

  TrainingDays = None
  for i, item in enumerate(data):
    if item['name'] == 'Days':
      TrainingDays = int(item['value'])
      del data[i]
      break

  Db.update_data('Login', session['login'], 'Requireds', json.dumps(data))
  Db.update_data('Login', session['login'], 'TrainingDays', TrainingDays)

  session['Requireds'] = json.dumps(data)
  session['TrainingDays'] = TrainingDays

  response_data = {"message": "Requireds saved in session successfully."}
  return jsonify(response_data), 200


@api.route('/saveTrainingTracker', methods=["POST"])
def saveTrainingTracker():
  data = request.get_data().decode()
  data = json.loads(data.replace("'", "\""))
  user_found = Db.get_login(session['login']).data
  now = datetime.datetime.now()
  date_str = now.strftime("%d/%m/%Y")
  # date_str = '30/05/2023'


  if len(data) == 3:
    data['lastDate'] = date_str

  historyTrainig = user_found[-1]
  tr = {}

  # Verifica o ultimo treino se tiver acrescentra se nao cria
  if historyTrainig is not None:
    historyTrainig = json.loads(historyTrainig)

    newTraining = json.loads(user_found[7])

    for rotina in newTraining:
      if rotina.upper() == user_found[-2].upper():
        newTraining[rotina] = data

    if date_str in historyTrainig:
      print('Já treino hoje')
      response_data = {"message": "Não é autorizado 2 treinos no mesmo dia"}
      return jsonify(response_data), 200
    else:
      historyTrainig[date_str] = newTraining
  else:
    newTraining = json.loads(user_found[7])

    for rotina in newTraining:
      if rotina.upper() == user_found[-2].upper():
        newTraining[rotina] = data
    tr = {date_str: newTraining}

  if tr == {}:
    tr = historyTrainig
  chosen = user_found[-2]
  oldTraining = json.loads(user_found[-3])

  for name in oldTraining:
    if name.upper() == chosen.upper():
      oldTraining[name] = data

  userData = json.loads(user_found[3])
  userData['TrainingInExecution'] = "false"

  Db.update_data('Login', session['login'], 'historyTraining', tr)
  Db.update_data('Login', session['login'], 'Training', oldTraining)
  Db.update_data('Login', session['login'], 'UserData', userData )


  response_data = {"message": "Training saved successfully."}
  return jsonify(response_data), 200


#Webhook para salvar os usuarios enviado da Guru
@api.route('/webhook/registerUser', methods=["POST"])
def webhookRegisterUser():

  data = request.get_data().decode()
  data = json.loads(data)

  data['FirstAcess'] = True
  data['TrainingInExecution'] = False

  if data["status"] == "approved":
    email = data['contact']['email']

    newPassword = random_generator()
    password_hash = generate_password_hash(newPassword)
    user = Db.get_login(email).data

    if user is None:
      print('Novo User -- Email enviado')
      content = f"Senha para acessar o Tracker BWA {newPassword}"
      subject = "Tracker BWA"
      send_email('api@gmail.com', content, subject)
    
    newUser = {'Login': email, 'Password': password_hash, 'UserData': data}
    Db.newUser(newUser)

  response = Response()
  response.status_code = 200
  response.data = "Sucesso!"
  return response


@api.route('/create/<name>/<password>', methods=['GET'])
def create_user(name, password):
  info = {
    "contact": {
      "id": "9747b5ff-5126-44e8-8807-7beb947fc31e",
      "name": name,
      "company_name": "",
      "email": f"{name}@gmail.com",
      "doc": "1111111111",
      "phone_number": "9999999999",
      "phone_local_code": "55",
      "address_country": "BR"
    },
    "FirstAcess": "true",
    "TrainingInExecution": "false"
  }
  data = {
    'Login': name,
    'Password': generate_password_hash(password),
    'UserData': info
  }
  Db.newUser(data)

  response = Response()
  response.status_code = 200
  response.data = "Sucesso!"
  return response


@api.route('/getLastTraining')
def getLastTraining():
  response = Response()
  if 'login' in session:
    user_found = Db.get_login(session['login']).data
    if user_found[-1] is not None:
      data = json.loads(user_found[-1])
    else:
      print('Não estou achando, o ultimo treino')
      response.data = json.dumps({'message': 'No data found'})
      response.status_code = 200
      return response

    history = []
    for date in data:
      for rotina in data[date]:
        if rotina.upper() == user_found[8].upper():
          tr = data[date][rotina]
          if len(tr) == 3:
            for day in tr:
              x = tr['chosenDay']
              if day == f"d{x}":
                history.append({'date': date, 'training': tr[day]})
          else:
            history.append({'date': date, 'training': tr})

  if data:
    response.data = json.dumps(history)
    response.status_code = 200
  else:
    response.data = {'message': 'No data found'}
    response.status_code = 400
  return response


@api.route('/getData', methods=['POST'])
def getData():
    try:
      if 'login' in session:
        data = Db.get_login(session['login']).data
        chaves = ['Ip', 'Login', 'Password', 'UserData', 'BaseTraining', 'TrainingDays', 'Requireds', 'Training', 'ChosenTraining', 'HistoryTraining']
        data = dict(zip(chaves, data))

        userData = json.loads(data['UserData'])
        trainingInExecution = userData.get('TrainingInExecution', [])  # Se 'TrainingInExecution' não estiver presente, atribui uma lista vazia

        if data['Training'] is not None:
            response_data = {'Training': data['Training'], 'ChosenTraining': data['ChosenTraining'], 'TrainingDays': data['TrainingDays'], 'Requireds': data['Requireds'], 'TrainingInExecution': trainingInExecution}
        else:
            response_data = {'Training': data['BaseTraining'], 'ChosenTraining': data['ChosenTraining'], 'TrainingDays': data['TrainingDays'], 'Requireds': data['Requireds'], 'TrainingInExecution': trainingInExecution}
        
        return jsonify(response_data), 200
      else:
        response_data = {'message': "Usuário não logado"}
        return jsonify(response_data), 400


    except Exception as e:
      response_data = {'message': f"Erro na requisição -> {e}"}
      return jsonify(response_data), 400

@api.route('/saveIncomplet', methods=['POST'])
def saveIncomplet():
  try:
      if 'login' in session:

        trainingIncomplet = request.get_json()
        data = Db.get_login(session['login']).data
        chaves = ['Ip', 'Login', 'Password', 'UserData', 'BaseTraining', 'TrainingDays', 'Requireds', 'Training', 'ChosenTraining', 'HistoryTraining']
        data = dict(zip(chaves, data))

        userData = json.loads(data['UserData'])

        userData['TrainingInExecution'] = trainingIncomplet

        Db.update_data('Login', session['login'], 'UserData', userData )

        
        return 'Save data', 200
      else:
        response_data = {'message': "Usuário não logado"}
        return 'Not Save Data', 400

  except Exception as e:
    response_data = {'message': f"Erro na requisição -> {e}"}
    return 'Err in request', 400


@api.route('/Delet/TrainingInExecution', methods=['POST'])
def DelTrainingInExecution():
  try:
      if 'login' in session:

        data = Db.get_login(session['login']).data
        chaves = ['Ip', 'Login', 'Password', 'UserData', 'BaseTraining', 'TrainingDays', 'Requireds', 'Training', 'ChosenTraining', 'HistoryTraining']
        data = dict(zip(chaves, data))

        userData = json.loads(data['UserData'])

        userData['TrainingInExecution'] = "false"

        Db.update_data('Login', session['login'], 'UserData', userData )
        
        
        return json.dumps('Sucess Delet'), 200
      else:
        response_data = {'message': "Usuário não logado"}
        return 'Not Save Data', 400

  except Exception as e:
    response_data = {'message': f"Erro na requisição -> {e}"}
    return 'Err in request', 400