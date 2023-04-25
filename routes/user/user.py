from flask import Flask, Blueprint, session, request, flash, jsonify, render_template
from model.db import Db
import json
from model.exercicio import Exercicio
from model.db import Db
user = Blueprint('user', __name__, template_folder='templates')

@user.route("/user")
def userRoute():
  if session['ip'] is not None:
    ip_found = Db.get_ip(session['ip']).data


  if isinstance(ip_found, dict):
    days = ip_found['days']
    pairedSets = ip_found['pairedSets']
    chosen = ip_found['chosenTraining']

    if pairedSets == 'true':
      if chosen == 'Fullbody':
        chosenTraining = ip_found['Treino']['pairedSetsTraining']['fullbodyPS']

      if chosen == 'PushPull':
        chosenTraining = ip_found['Treino']['pairedSetsTraining']['pushPullPS']
  
      if chosen == 'UpperLower':
        chosenTraining = ip_found['Treino']['pairedSetsTraining']['upperLowerPS']
    else:
      if chosen == 'Fullbody':
        chosenTraining = ip_found['Treino']['regularTraining']['fullbody']

      if chosen == 'PushPull':
        chosenTraining = ip_found['Treino']['regularTraining']['pushPull']
  
      if chosen == 'UpperLower':
        chosenTraining = ip_found['Treino']['regularTraining']['upperLower']


    data = {
      'nav': 'user',
      'training': chosenTraining,
      'days': days,
      'pairedSets': pairedSets,
      'chosenTraining': chosen
    }
    return render_template("user.html", data = data)
  else:
    data = {
      'nav': 'user'
    }
    return render_template("user.html", data = data)


@user.route("/pageUser")
def pageUser():
  data = {'nav': None}
  return render_template("pageUser.html", data = data)


@user.route('/tracker',  methods=["POST"])
def tracker():
  data = request.form['data']
  ip = request.form['ip']
 
  data = eval(data)
  fullTraining = data
  ip_found = Db.get_ip(ip).data

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
        listExer = Exercicio.getSuggestionExerLight(name)
        d['newExer'] =  listExer
    
    inf = {'training': data, 'chosenDay': chosenDay, 'chosenTraining':chosen, 'fullTraining': fullTraining}
    return render_template('tracker.html', data=inf)


  return render_template('tracker.html', data=inf)