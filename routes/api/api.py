from flask import Flask, Blueprint, session, request, flash, jsonify, render_template, Response
from model.db import Db
from werkzeug.security import generate_password_hash, check_password_hash
from model.exercicio import Exercises
import json, datetime
from model.logs import Logs
from basicFunction import random_generator, send_email

api = Blueprint('api', __name__, template_folder='templates')


@api.route("/getExercisesMusc")
def getExercisesMusc():
  # allExer = Exercises.getExercisesBodyWeight()
  res = Exercises.getExercisesMusc()
  # newTraing = []
  # newCore = []
  # #Pega todos o cores de level 3
  # for index, exer in enumerate(allExer):
  #     if exer['category'] == 'Core' and exer['nivel'] == 3:
  #         newTraing.append(allExer[index])
  # # Pega o exercicio sem required
  # for index, exer in enumerate(newTraing):
  #     if exer['required'] == '':
  #       exer_copy = exer.copy() # criando uma cópia do objeto original
  #       exer_copy['default'] = True # adicionando o novo campo na cópia
  #       newCore.append(exer_copy) # adicionando a cópia com o novo campo na nova lista

  # if len(newCore) >=2:
  #   res.extend([newCore[0]])
  # else:
  #   res.extend(newCore)

  # newTraing = []
  # newCore = []

  # for index, exer in enumerate(allExer):
  #     if exer['category'] == 'Core' and exer['nivel'] == 2:
  #         newTraing.append(allExer[index])
  # # Pega o exercicio sem required
  # for index, exer in enumerate(newTraing):
  #     if exer['required'] == '':
  #         newCore.append(newTraing[index])

  # if len(newCore) >=2:
  #   res.extend([newCore[0]])
  # else:
  #   res.extend(newCore)

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

  ip = {
    'ip': session['ip']
    # 'Requireds': json.dumps(data),
    # 'TrainingDays': TrainingDays
  }
  ip_found = Db.get_ip(session['ip']).data

  if ip_found is None:
    Db.save(ip)

  Db.update_data(session['ip'], 'Requireds', json.dumps(data))
  Db.update_data(session['ip'], 'TrainingDays', TrainingDays)

  response_data = {"message": "Requireds saved successfully."}
  return jsonify(response_data), 200


@api.route('/saveTrainingTracker', methods=["POST"])
def saveTrainingTracker():
  data = request.get_data().decode()
  data = json.loads(data.replace("'", "\""))

  now = datetime.datetime.now()
  date_str = now.strftime("%d/%m/%Y")

  ip_found = Db.get_login(session['login']).data

  historyTrainig = ip_found[-1]

  # Verifica se tem algum treino se tiver acrecenta se não add pela primeira vez
  if historyTrainig is not None:
    historyTrainig = json.loads(historyTrainig)
    historyTrainig.append({date_str: data})
  else:
    historyTrainig = [{date_str: data}]

  # Add treino no array

  chosen = ip_found[-2]
  oldTraining = json.loads(ip_found[-3])

  for name in oldTraining:
    if name.upper() == chosen.upper():
      oldTraining[name] = data

  Db.update_data('Login', session['login'], 'historyTraining', historyTrainig)
  Db.update_data('Login', session['login'], 'Training', oldTraining)

  response_data = {"message": "Training saved successfully."}
  return jsonify(response_data), 200


#Webhook para salvar os usuarios enviado da Guru
@api.route('/webhook/registerUser', methods=["POST"])
def webhookRegisterUser():
  data = request.get_data().decode()
  data = json.loads(data)

  print(data["status"])
  print(request)
  status = data["status"]
  if status == "approved":
    email = data['contact']['email']

    newPassword = random_generator()
    password_hash = generate_password_hash(newPassword)

    content = f"Senha para acessar o Tracker BWA {newPassword}"
    subject = "Tracker BWA"
    send_email('lucasadrisilva@gmail.com', content, subject)

    newUser = {'Login': email, 'Password': password_hash, 'UserData': [data]}
    Db.newUser(newUser)

  # info = {'Login': 'Lucas', 'Password': password_hash]}
  #Salvar dados enviado pelo webhook
  # Db.newUser(info)
  # string = json.dumps(newUser)
  # now = datetime.datetime.now()
  # content = f"{now} -- Usuario salvo -- dados ||| data = {string} |||"
  # log = Logs('logs', True, content, 'SaveUser')
  # Logs.saveLogs(log)

  response = Response()
  response.status_code = 200
  response.data = "Sucesso!"
  return response

@api.route('/creat')
def creat():
  data = {'Login': 'Lucas', 'Password': generate_password_hash('3517')}
  Db.newUser(data)

  response = Response()
  response.status_code = 200
  response.data = "Sucesso!"
  return response