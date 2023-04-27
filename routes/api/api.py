from flask import Flask, Blueprint, session, request, flash, jsonify, render_template
from model.db import Db
from model.exercicio import Exercises
import json, datetime



api = Blueprint('api', __name__, template_folder='templates')


@api.route("/getExercisesMusc")
def getExercisesMusc():
    allExer = Exercises.getExercisesBodyWeight()
    res = Exercises.getExercisesMusc()

    newTraing = []
    newCore = []
    #Pega todos o cores de level 3
    for index, exer in enumerate(allExer):
        if exer['category'] == 'Core' and exer['nivel'] == 3:
            newTraing.append(allExer[index])
    # Pega o exercicio sem required
    for index, exer in enumerate(newTraing):
        if exer['required'] == '':
            newCore.append(newTraing[index])

    if len(newCore) >=2:
      res.extend([newCore[0]])
    else:
      res.extend(newCore)

    newTraing = []
    newCore = []
    
    for index, exer in enumerate(allExer):
        if exer['category'] == 'Core' and exer['nivel'] == 2:
            newTraing.append(allExer[index])
    # Pega o exercicio sem required
    for index, exer in enumerate(newTraing):
        if exer['required'] == '':
            newCore.append(newTraing[index])
          
    if len(newCore) >=2:
      res.extend([newCore[0]])
    else:
      res.extend(newCore)
    
    response = json.dumps(res)
    return response, 200 

@api.route("/getExercisesBodyWeight")
def getExercisesBodyWeight():
    allExer = Exercises.getExercisesBodyWeight()
    response = json.dumps(allExer) 
    return response, 200 
  
@api.route('/saveDU' ,  methods=["POST"])
def saveDU():
  data = request.get_data().decode()
  data = json.loads(data.replace("'","\""))
  
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

  Db.update_data(session['ip'] , 'Requireds', json.dumps(data))
  Db.update_data(session['ip'] , 'TrainingDays', TrainingDays)

  response_data = {"message": "Requireds saved successfully."}
  return jsonify(response_data), 200  

@api.route('/saveTrainingTracker', methods=["POST"])
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