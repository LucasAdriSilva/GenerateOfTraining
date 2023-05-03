from flask import Flask, Blueprint, session, request, flash, jsonify, render_template, redirect, url_for
from model.db import Db
import json
from model.exercicio import Exercises
from model.db import Db
from werkzeug.security import check_password_hash
from basicFunction import getUrl
user = Blueprint('user', __name__, template_folder='templates')

@user.route("/user")
def userRoute():
  if 'login' in session:
    print('1')
    ip_found = Db.get_login(session['login']).data


    days = ip_found[5]
    training = json.loads(ip_found[7])
    chosen = ip_found[8]

    if chosen.upper() == 'FULBODY':
      chosenTraining = training['fullbody']

    if chosen.upper() == 'PUSHPULL':
      chosenTraining = training['pushPull']

    if chosen.upper() == 'UPPERLOWER':
      chosenTraining = training['upperLower']


    data = {
      'nav': 'user',
      'training': chosenTraining,
      'days': days,
      'chosenTraining': chosenTraining
    }
    return getUrl("user.html", value = data)
  else:
    print('2')
    data = {
      'nav': 'user'
    }
    return getUrl("user.html", value= data)


@user.route("/pageUser")
def pageUser():
  data = {'nav': None}
  return getUrl("pageUser.html", value = data)


@user.route('/tracker',  methods=["POST"])
def tracker():
  data = request.form['data']
 
  data = eval(data)
  fullTraining = data
  ip_found = Db.get_login(session['login']).data

  chosen = ip_found[-2] #ChosenTrainig -- string

  
  if request.form['chosenDay']:
    chosenDay = request.form['chosenDay']
    if int(chosenDay) >=1:
      data = data[f"d{chosenDay}"]

  # for rotina in data:
  #   if rotina.upper() == chosen.upper():
  #     # Acessar o valor correspondente ao índice de string em um dicionário
  #     rotina_dict = data['regularTraining'][rotina]
  #     training2 = rotina_dict
  #     # for a in rotina_dict:
  #     #     print(a)


# #  print(toggleExer)
#   if len(training1) > 1:   
#     for d in training1['d1']:
#       if 'newExer' in d and d['newExer']:
#         if d['newExer'] == True:
#           name = d['name']
#           listExer = Exercicio.getSuggestionExerLight(name)
#           d['newExer'] =  listExer

#     for d in training1['d2']:
#       if 'newExer' in d and d['newExer']:
#         if d['newExer'] == True:
#           name = d['name']
#           listExer = Exercicio.getSuggestionExerLight(name)
#           d['newExer'] =  listExer
      
#   else:
  for d in data:
    if 'newExer' in d and d['newExer']:
      if d['newExer'] == True:
        name = d['name']
        listExer = Exercises.getSuggestionExerLight(name)
        d['newExer'] =  listExer
    
    inf = {'training': data, 'chosenDay': chosenDay, 'chosenTraining':chosen, 'fullTraining': fullTraining}
    return getUrl('tracker.html', value=inf)


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
          return getUrl('basicScreens.creatTraining', bool=True)
      else:
        err = 'Senha incorreta'
        return getUrl('login.html', prop='erro', value=err, bool=False)
    else:
      err = 'Usuário nao encontado'
      return getUrl('login.html', prop='erro', value=err, bool=False)
  else:  
    return getUrl("basicScreens.creatTraining", bool=True)