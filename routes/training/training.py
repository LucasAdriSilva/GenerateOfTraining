from flask import Blueprint, render_template, session, request, jsonify
from model.db import Db
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

  if session['ip'] is not None:
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

    response_data = {"message": "Training saved successfully."}
    return jsonify(response_data), 200


@training_bp.route('/saveTrainingTracker', methods=["POST"])
def saveTrainingTracker():
  data = request.get_data().decode()
  data = json.loads(data.replace("'", "\""))

  now = datetime.datetime.now()
  date_str = now.strftime("%d/%m/%Y")

  ip_found = Db.get_ip(session['ip']).data

  historyTrainig = ip_found[-1]
  
  # Verifica se tem algum treino se tiver acrecenta se não add pela primeira vez
  if historyTrainig is not None:
    historyTrainig.append({date_str: data})
  else:
    historyTrainig = [{date_str: data}]

  Db.update_data(session['ip'], 'historyTraining', historyTrainig)
  Db.update_data(session['ip'], 'Training', data)

  response_data = {"message": "Training saved successfully."}
  return jsonify(response_data), 200
