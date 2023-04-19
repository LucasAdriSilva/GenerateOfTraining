from flask import Flask, Blueprint, session, request, flash, jsonify, render_template
from model.db import Db
import json
from model.exercicio import Exercicio
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
  # data = json.loads(data.replace("'", "\""))
  data = eval(data)
  teste = data['d1']
  teste2 = data['d2']
  toggleExer = []
#   for d in data:
#     if d.get('newExer') == True: 
#       print( d.get('newExer')) # Verifica se o dicionário tem o valor 'newExer' igual a True
#  # Verifica se o dicionário tem o valor 'newExer' igual a True
#       last_key = list(d.keys())[-1]  # Obtém a última chave do dicionário
#       last_value = d[last_key]  # Obtém o valor da última chave do dicionário
#       listExer = Exercicio.getSuggestionExerLight(d['name'])
#       toggleExer.append({'sugestToggleExer':  listExer})

#       print(toggleExer)
  if len(data) > 1:   
    for d in data['d1']:
      if 'newExer' in d and d['newExer']:
        if d['newExer'] == True:
          name = d['name']
          listExer = Exercicio.getSuggestionExerLight(name)
          d['newExer'] =  listExer

    for d in data['d2']:
      if 'newExer' in d and d['newExer']:
        if d['newExer'] == True:
          name = d['name']
          listExer = Exercicio.getSuggestionExerLight(name)
          d['newExer'] =  listExer
      
  else:
    for d in data:
      if 'newExer' in d and d['newExer']:
        if d['newExer'] == True:
          name = d['name']
          listExer = Exercicio.getSuggestionExerLight(name)
          d['newExer'] =  listExer

  return render_template('tracker.html', data=data)