from flask import Blueprint, render_template, request, redirect, url_for, make_response, session, jsonify
import json
from model.exercicio import Exercises 
from model.db import Db 
from fpdf import FPDF
from basicFunction import getUrl, remove_repeated_items_in_list


basicScreens = Blueprint('basicScreens', __name__, template_folder='templates')

@basicScreens.route("/")
def index():
  # Verifica se tem o ip e login na sessão
  if 'ip' in session or 'login' in session:

    if 'ip' in session:
      ip_found = Db.get_ip(session['ip']).data
    if 'login' in session:
      ip_found = Db.get_login(session['login']).data
   
    # Verifica o retorno do banco nao é null
    if ip_found is not None:

      if ip_found[-2] is None and ip_found[-3] is not None and ip_found[5] is not None:
        data = {
            'nav': 'creat',
            'allTreinos': json.loads(ip_found[-3]),
            'days': ip_found[-5]
          }
        # return render_template("creatTraining.html", data=data)
        return getUrl("creatTraining.html", value = data)
  
      # Verifica se é o priemiro treino
      if  ip_found[-1] is not None:
        # Pega o ultimo treino para montar o exercicio
        last_training =  json.loads(ip_found[-1])

        last_value = list(last_training.values())[-1]

        for rotina in last_value:
          if rotina.upper() == ip_found[-2].upper():
            last_value = last_value[rotina]  

        # for value in last_training.keys():
        #   trainingValue = last_training[value]
        
        data= {
          'nav': 'home', 
          'ip': ip_found[0],
          'dayTraining': 3,
          'nameRotina': ip_found[-2],
          'training': last_value,
        }
        # return render_template("home.html", data = data)    

        return getUrl("home.html", value = data)    
      else: 
        if ip_found[4] is not None:
        # pega o training base para montar o exercicio
          training = json.loads(ip_found[4])
          chosen = ip_found[-2]
          for choseName in training:
              if choseName.upper() == chosen.upper():
                training = training[choseName]
          data = {
            'nav': 'home', 
            'ip': ip_found[0],
            'dayTraining': ip_found[5],
            'nameRotina': chosen,
            'training':  training
          }  
          # return render_template("home.html", data = data)   
          return getUrl("home.html", value = data)    
         
        else:
          data = {'nav': 'home'}
          return getUrl("firstAcess.html", value = data)
    else:
       data = {'nav': 'home'}
    return getUrl("firstAcess.html", value=data)
    # return render_template("home.html", data = data)
    
  else:
    # ip = request.remote_addr
    # session['ip'] = ip
    data = {'nav': 'home'}
    return getUrl("firstAcess.html", value = data)

@basicScreens.route("/sendTraining", methods=["POST"])
def sendTraining():
    if request.method == "POST":
        treino = request.get_json()
        session['training'] = treino
        return redirect(url_for('basicScreens.index'))
 
@basicScreens.route("/creatTraining", methods=["GET"])
def creatTraining():
  if 'login' not in session:
    return getUrl('login.html')
  user_found = Db.get_login(session['login']).data
  all = Exercises.getExercisesBodyWeight()
  musc = Exercises.getExercisesMusc()

  if 'training' in session:
    treino = session['training']
  else:
    if user_found[-2] is not None:
      if user_found[-3] is not None:
        trainingOfDb = json.loads(user_found[-3])
        for rotina in  trainingOfDb:
          if rotina.upper() == user_found[-2].upper():
            treino = trainingOfDb[rotina]
      else:
        data = {'nav': 'home'}
        return getUrl("firstAcess.html", value=data)
    else:
      data = {'nav': 'home'}
      return getUrl("creatTraining.html", value=data)

  # pega o valor dos requireds
  if user_found[6] is not None:
    requireds = json.loads(user_found[6])
  else:
    if 'Requireds' in session:
      requireds = json.loads(session['Requireds'])

  try:
    data_all = []
    new_order = []

    # Unindo o Treino com o All

    if len(treino) > 4:
      for a in all:
        for t in treino:
          if isinstance(t, list) == False:
            if a["name"] == t["name"]:
              new_data = a.copy()
              new_data.update(t)
              data_all.append(new_data)

      for a in musc:
        for t in treino:
          if isinstance(t, list) == False:
            if a["name"] == t["name"]:             
              new_data = a.copy()
              new_data.update(t)
              data_all.append(new_data)
      
      data_all = remove_repeated_items_in_list(data_all)
    else:
      for a in all:
        for t in treino:
          for exer in treino[t]:
            if t == 'd1' or t == 'd2':
              if a["name"] == exer["name"]:
                new_data = a.copy()
                new_data.update(exer)
                data_all.append(new_data)
      for a in musc:
        for t in treino:
          for exer in treino[t]:
            if t == 'd1' or t == 'd2':
              if a["name"] == exer["name"]:
                new_data = a.copy()
                new_data.update(exer)
                data_all.append(new_data)

    # Cria um array qeu repete o num de veses de acordo com o exer, e add infos
    for e in data_all:
      repeated_e = [e.copy() for _ in range(e['rept'])
                    ]  # cria uma cópia do dicionário e "rept" vezes
      for i, d in enumerate(repeated_e):
        d['rept_num'] = i + 1  # adiciona um novo campo 'rept_num' com o número de repetição
        d['rest'] = '1:30'  # altera o campo 'reset' para '1:30'
      new_order.extend(repeated_e)

    #-----------------------------------------------------------------------------------------------------Treino com Paired Sets
    # Agrupa os objetos por categoria
    categories = {}
    for a in new_order:
      category = a["category"]
      if category not in categories:
        categories[category] = []
      categories[category].append(a)

    #  Cria 2 arrays para fazer a intecalação
    array1 = []
    array2 = []

    # Agrupa os objetos por categoria, sem ter repetições
    grupCategories = {}
    for a in data_all:
      category = a["category"]
      if category not in grupCategories:
        grupCategories[category] = []
      grupCategories[category].append(a)

    # Criando a rotina FULLBODY
    array1 = [
      valor for par in zip(grupCategories['Push'], grupCategories['Core'])
      for valor in par
    ]
    array2 = [
      valor for par in zip(grupCategories['Pull'], grupCategories['Legs'])
      for valor in par
    ]
    array1.extend(array2)
    fullbody = array1

    # Criando a rotina Push/Pull
    array1 = [
      valor for par in zip(grupCategories['Push'], grupCategories['Legs'])
      for valor in par
    ]
    array2 = [
      valor for par in zip(grupCategories['Pull'], grupCategories['Core'])
      for valor in par
    ]
    pushPull = {'d1': array1, 'd2': array2}

    # Criando a rotina Upper/Lowe
    array1 = [
      valor for par in zip(grupCategories['Push'], grupCategories['Pull'])
      for valor in par
    ]
    array2 = [
      valor for par in zip(grupCategories['Legs'], grupCategories['Core'])
      for valor in par
    ]
    upperLower = {'d1': array1, 'd2': array2}

    Training = {
      'fullbody': fullbody,
      'pushPull': pushPull,
      'upperLower': upperLower
    }
  except Exception as e:
    print(f"{e}")

  days = None
  for required in requireds:
    if required['name'] == 'Days':
      days = int(required['value'])

  if days == None:
    if 'TrainingDays' in session:
      days = session['TrainingDays']
    else:
      days = user_found[5]

  if 'login' in session:
    Db.update_data('Login', session['login'], 'TrainingDays', days)
    Db.update_data('Login', session['login'], 'BaseTraining', Training)
    Db.update_data('Login', session['login'], 'Requireds', requireds)
    Db.update_data('Login', session['login'], 'Training', Training)

  if user_found[-2] is None:
    if days == 3:
      Db.update_data('Login', session['login'], 'ChosenTraining', 'Fullbody')
      data = {
        'nav': 'creat',
        'allTreinos': Training,
        'days': days,
        'chosenTraining': 'Fullbody'
      }
    else:
      data = {'nav': 'creat', 'allTreinos': Training, 'days': days}
  else:
    data = {
      'nav': 'creat',
      'allTreinos': Training,
      'days': days,
      'chosenTraining': user_found[-2]
    }
  return getUrl("home.html", value=data)
 
@basicScreens.route("/download-pdf", methods=["POST"])
def download_pdf():
  # Recupera os dados enviados pelo formulário
  data = request.form['data']
  data = json.loads(data.replace("'", "\""))
  # Cria o arquivo PDF usando a biblioteca FPDF
  pdf = FPDF()
  pdf.add_page()
  pdf.set_font("Arial", size=12)
  
  x = 1
  for item in data:
    # pdf.cell(200, 10, f"{x} Exercicio - {str(item['name'])}. quantidade: {str(item['count'])}, serie: {str(item['rept'])}, descanso: {str(item['rest'])}", ln=1)
    pdf.cell(200, 10, f"Teste {item}", ln=1)
    x += 1
  pdf_name = 'Treino.pdf'
  pdf_bytes = pdf.output(dest='S').encode('latin1')  # converte o PDF para bytes
  response = make_response(pdf_bytes)
  response.headers.set('Content-Disposition', 'attachment', filename=pdf_name)  # adiciona o cabeçalho para download
  response.headers.set('Content-Type', 'application/pdf')  # define o tipo de conteúdo como PDF
  return response
