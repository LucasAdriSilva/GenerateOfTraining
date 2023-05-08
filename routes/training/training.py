from flask import Blueprint, render_template, session, request, jsonify, redirect, url_for
from model.db import Db
from basicFunction import getUrl
from model.exercicio import Exercises
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

  user_found = Db.get_login(session['login']).data

  if user_found:
    Db.update_data('Login',session['login'], 'chosenTraining', data)

  else:
    # Db.update_user(session['login'], {'chosenTraining': data})
    Db.update_data('Login',session['login'], 'chosenTraining', data)

  if 'login' in session:
    return getUrl('basicScreens.creatTraining', bool=True)
  else:
    return redirect(url_for('user.login'))

@training_bp.route('/bodybuilding')
def bodybuilding():
  data = [None, None,None, {'nav': None}]
  return render_template('bodybuilding.html', data=data)

@training_bp.route('/hybrid')
def hybrid():
  data = [None, None,None, {'nav': None}]
  return render_template('hybrid.html', data=data)

@training_bp.route('/exercice')
def exercice():
  all = Exercises.getExercisesBodyWeight()
  data = {
    'nav': 'creat',
    'allTreino': all
  }
  return getUrl("exercices.html", value = data)