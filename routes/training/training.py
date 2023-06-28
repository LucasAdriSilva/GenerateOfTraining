from flask import Blueprint, render_template, session, request, jsonify, redirect, url_for, jsonify
from model.db import Db
from basicFunction import getUrl
from model.exercicio import Exercises
import datetime, json

training_bp = Blueprint('training', __name__, template_folder='templates')


@training_bp.route('/saveTraining', methods=["POST"])
def saveTraining():
    data = request.get_json()
    data = data.replace('"', '')

    user_found = Db.get_login(session['login']).data

    if user_found:
        Db.update_data('Login', session['login'], 'chosenTraining', data)
    else:
        Db.update_data('Login', session['login'], 'chosenTraining', data)

    return redirect(url_for('basicScreens.creatTraining'))

@training_bp.route('/bodybuilding')
def bodybuilding():
  if 'login' in session:
    user_found = Db.get_login(session['login']).data
    requireds = user_found[6]
    if requireds is None:
       new_data = [{"name": "Paralelas", "value": "false"}, {"name": "Barra Fixa", "value": "false"}, {"name": "Trx", "value": "false"}, {"name": "Rodinha Abdominal", "value": "false"}, {"name": "Argolas", "value": "false"}, {"name": "Superband", "value": "false"}, {"name": "Hours", "value": "0"}, {"name": "Min", "value": "40"}, {"name": "DaysChosen", "value": ["Seg", "Ter", "Quin", "Sex"]}]
       Db.update_data('Login', session['login'], 'Requireds', new_data)
  data = [None, None,None, {'nav': None}]
  return getUrl('bodybuilding.html', value=data)

@training_bp.route('/hybrid')
def hybrid():
  if 'login' in session:
    user_found = Db.get_login(session['login']).data
    requireds = user_found[6]
    if requireds is None:
       new_data = [{"name": "Paralelas", "value": "false"}, {"name": "Barra Fixa", "value": "false"}, {"name": "Trx", "value": "false"}, {"name": "Rodinha Abdominal", "value": "false"}, {"name": "Argolas", "value": "false"}, {"name": "Superband", "value": "false"}, {"name": "Hours", "value": "0"}, {"name": "Min", "value": "40"}, {"name": "DaysChosen", "value": ["Seg", "Ter", "Quin", "Sex"]}]
       Db.update_data('Login', session['login'], 'Requireds', new_data)

  data = [None,None,None, {'nav': None}]
  return getUrl('hybrid.html', value=data)

@training_bp.route('/exercice')
def exercice():
  all = Exercises.getExercisesBodyWeight()
  data = {
    'nav': 'creat',
    'allTreino': all
  }
  return getUrl("exercices.html", value = data)