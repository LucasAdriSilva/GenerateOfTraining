from flask import Flask, Blueprint, session, request, flash, jsonify, render_template, redirect, url_for
from model.db import Db
import json, datetime
from model.exercicio import Exercises
from model.db import Db
from model.week import week
from werkzeug.security import check_password_hash
from basicFunction import getUrl
user = Blueprint('user', __name__, template_folder='templates')

@user.route("/user")
def userRoute():
  if 'login' in session:
    ip_found = Db.get_login(session['login']).data

    name = json.loads(ip_found[3])
    name = name["contact"]["name"]

    numbertraining = ip_found[-1]
    if numbertraining is not None:
      numbertraining = json.loads(numbertraining)

    if ip_found[6] is not None:
      reqireds = json.loads(ip_found[6])
      print('1')

      equip = []
      for req in reqireds:
        if req['value'] == 'true':
            index = reqireds.index(req)
            equip.append(reqireds[index]['name'])  

      days = ip_found[5]
      training = json.loads(ip_found[7])
      chosen = ip_found[8]

      if chosen.upper() == 'FULLBODY':
        chosenTraining = training['fullbody']

      if chosen.upper() == 'PUSHPULL':
        chosenTraining = training['pushPull']

      if chosen.upper() == 'UPPERLOWER':
        chosenTraining = training['upperLower']

      if numbertraining is None:
        countTraining = 0
        data = {
          'nav': 'user',
          'training': chosenTraining,
          'days': days,
          'chosenTraining': chosen,
          'equip': equip,
          'name': name,
          'countTraining': countTraining
        }
      else:
        countTraining = len(numbertraining)
        data = {
          'nav': 'user',
          'training': chosenTraining,
          'days': days,
          'chosenTraining': chosen,
          'equip': equip,
          'name': name,
          'numbertraining': numbertraining,
          'countTraining': countTraining
        }  
      return getUrl("user.html", value = data)
    else:
      print('2')
      data = {
        'nav': 'home'
      }
      return getUrl("firstAcess.html", value= data)
  else:
    data = {'nav': 'home'}
    return getUrl("firstAcess.html", value= data)

@user.route("/pageUser")
def pageUser():
  data = {'nav': None}
  return getUrl("pageUser.html", value = data)

@user.route('/tracker',  methods=["POST"])
def tracker():
  data = request.form['data']
  data = json.loads(data)

  fullTraining = data

  user_found = Db.get_login(session['login']).data

  requireds =json.loads(user_found[6])
  print(type(requireds[name]))
  daysChosen = week.convertDays(requireds[8].value)
  
  #Verifica se tem algum treino em execução
  if 'TrainingInExecution' in request.form:
    if request.form['TrainingInExecution'] == 'true':
      pass
    else:
      userData = json.loads(user_found[3])
      userData['TrainingInExecution'] = "false" 
      
      Db.update_data('Login', session['login'], 'UserData', userData)

  chosen = user_found[-2] #ChosenTrainig -- string

  if user_found[-1] is not None:
    historyTraining = json.loads(user_found[-1])
    now = datetime.datetime.now()
    date = now.strftime("%d/%m/%Y") 
    # date = '30/05/2023'

    if date in historyTraining:
      data= {
            'nav': 'home', 
            'dayTraining': user_found[5],
            'nameRotina': user_found[-2],
            'erro': 'Não é permitido treinar 2 vezes no mesmo dia',
            'training': data,
          }   
      return getUrl("home.html", value = data) 

  if request.form['chosenDay']:
    chosenDay = request.form['chosenDay']
    if int(chosenDay) >=1:
      if len(data) == 1:
        for date in data:
          for rotina in data[date]:
              if rotina.upper() == user_found[8].upper():
                tr = data[date][rotina]
                for day in tr:
                  x = tr['chosenDay']
                  if day == f"d{x}":
                    data = tr[day]
      else:
        for rotina in data:
            if rotina.upper() == chosen.upper():
              # data = data[rotina][f"d{chosenDay}"]
              tr = data[rotina]
              for day in tr:
                  x = chosenDay
                  if day == f"d{x}":
                    data = tr[day]
        
  for d in data:
    if d == 'chosenDay' and data[d] == '1':
      index = '2'
      for exer in data[f'd{index}']:
        if 'newExer' in exer:
          if exer['newExer'] == True:
            name = exer['name']
            listExer = Exercises.getSuggestionExerLight(name)
            exer['newExer'] =  listExer
    if d == 'chosenDay' and data[d] == '2':
      index = '1'
      for exer in data[f'd{index}']:
        if 'newExer' in exer:
          if exer['newExer'] == True:
            name = exer['name']
            listExer = Exercises.getSuggestionExerLight(name)
            exer['newExer'] =  listExer   


  if chosenDay == '0':
    inf = {'training': data['fullbody'], 'chosenDay': f"d{chosenDay}", 'chosenTraining':chosen, 'fullTraining': fullTraining}
  else:
    inf = {'training': data, 'chosenDay': f"d{chosenDay}", 'chosenTraining':chosen, 'fullTraining': fullTraining}
  return getUrl('tracker.html', value=inf)


@user.route('/login', methods=["GET", "POST"])
def login():
  if request.method == "POST":
    # PEga os dados do formulário
    login = request.form['login']
    password = request.form['password']
    url = request.form['url']

    #Pesquisa o usuário no banco 
    user_found = Db.get_login(login).data
  
    if user_found:
      authorization_password = check_password_hash(user_found[2], password)
      if authorization_password:
        session['login'] = user_found[1]

        # user = Db.get_ip(session['ip'])

        # Db.update_data(login, paran, value)

        session.pop('ip', None)
        # redirect(url_for('basicScreens.creatTraining'))
        if url:
          return getUrl(url, bool=True)
        else:
          return getUrl('basicScreens.index', bool=True)
      else:
        data = [None,None,None, {'nav': 'home', 'erro': 'Senha incorreta', 'user': user_found[1]}]
        return render_template("login.html", data = data)
    else:
      data = [None,None,None, {'nav': 'home', 'erro': 'Usuário nao encontado'}]
      return render_template("login.html", data = data)
  else: 
    return getUrl("basicScreens.index", bool=True)
 
@user.route('/logout')
def logout():
  session.pop('login',1)
  data = {'nav': 'home'}
  return getUrl("firstAcess.html", value = data)