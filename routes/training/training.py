from flask import Blueprint, render_template, session, request, jsonify, redirect, url_for
from model.db import Db
from basicFunction import getUrl
import datetime, json

training_bp = Blueprint('training', __name__, template_folder='templates')


@training_bp.route('/training')
def training():
  if session['ip'] is not None:
    ip_found = Db.get_ip(session['ip']).data
    print(ip_found)
    if ip_found is not None:
      data = {'nav': None}

      return render_template('training.html', data=data)
    else:
      data = {'nav': 'home'}
      return render_template('firstAcess.html', data=data)


@training_bp.route('/saveTraining', methods=["POST"])
def saveTraining():
  data = request.get_data().decode()

  if 'ip' in session:
    ip_found = Db.get_ip(session['ip']).data

    if ip_found:
      chosen = data

      treino = json.loads(ip_found[4])
 
      if chosen == 'Fullbody':
        chosenTraining = treino['fullbody']

      if chosen == 'PushPull':
        chosenTraining = treino['pushPull']

      if chosen == 'UpperLower':
        chosenTraining = treino['upperLower']

      Db.update_data(session['ip'],'Training', chosenTraining)
      Db.update_data(session['ip'], 'chosenTraining', data)

    else:
      # Db.update_user(session['ip'], {'chosenTraining': data})
      Db.update_data(session['ip'], 'chosenTraining', data)

    if 'login' in session:
      response_data = {"message": "Training saved successfully."}
      return jsonify(response_data), 200
    else:
      return redirect(url_for('user.login'))
  else:
    ip_found = Db.get_login(session['login']).data

    if ip_found:
      chosen = data

      treino = json.loads(ip_found[4])
 
      if chosen == 'Fullbody':
        chosenTraining = treino['fullbody']

      if chosen == 'PushPull':
        chosenTraining = treino['pushPull']

      if chosen == 'UpperLower':
        chosenTraining = treino['upperLower']

      Db.update_data('Login',session['login'],'Training', chosenTraining)
      Db.update_data('Login',session['login'], 'chosenTraining', data)

    else:
      # Db.update_user(session['login'], {'chosenTraining': data})
      Db.update_data('Login',session['login'], 'chosenTraining', data)

    if 'login' in session:
      # response_data = {"message": "Training saved successfully."}
      # return jsonify(response_data), 200
      return getUrl('basicScreens.creatTraining', bool=True)
    else:
      return redirect(url_for('user.login'))

@training_bp.route('/bodybuilding')
def bodybuilding():
  data = {'nav': None}
  return render_template('bodybuilding.html', data=data)

@training_bp.route('/hybrid')
def hybrid():
  data ={
    'nav': None
  }
  return render_template('hybrid.html', data=data)