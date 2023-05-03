from flask import Blueprint, render_template, request, redirect, url_for, make_response, session
import json
from model.exercicio import Exercises 
from model.db import Db 
from fpdf import FPDF
from basicFunction import getUrl


basicScreens = Blueprint('basicScreens', __name__, template_folder='templates')

@basicScreens.route("/")
def index():
  print(session)
  # Verifica se tem o ip e login na sessão
  if 'ip' in session or 'login' in session:

    if 'ip' in session:
      ip_found = Db.get_ip(session['ip']).data
    if 'login' in session:
      ip_found = Db.get_login(session['login']).data
   
    # Verifica o retorno do banco nao é null
    if ip_found is not None:

      # Verifica se é o priemiro treino
      if  ip_found[-1] is not None:
        # Pega o ultimo treino para montar o exercicio
        last_training =  json.loads(ip_found[-1])[-1]

        for value in last_training.keys():
          trainingValue = last_training[value]
        
        data= {
          'nav': 'home', 
          'ip': ip_found[0],
          'dayTraining': 3,
          'nameRotina': ip_found[-2],
          'training': trainingValue,
        }
        # return render_template("home.html", data = data)    
        return getUrl("home.html", prop = data, value = data)    
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
          return getUrl("home.html", prop = data , value = data)    
         
        else:
          data = {'nav': 'home'}
          return render_template("firstAcess.html", data = data)
    else:
       data = {'nav': 'home'}
    return render_template("firstAcess.html", data = data)
    # return render_template("home.html", data = data)
    
  else:
    # ip = request.remote_addr
    # session['ip'] = ip
    data = {'nav': 'home'}
    return render_template("firstAcess.html", data = data)

@basicScreens.route("/sendTraining", methods=["POST"])
def sendTraining():
    if request.method == "POST":
      treino = request.get_json()
      # data = {'treino': treino}
      session['training'] = treino
      return redirect(url_for('user.login'))
      # return getUrl('user.login', bool=True)

    # return render_template("home.html")
    return getUrl("home.html")

@basicScreens.route("/creatTraining" , methods=["GET"])
def creatTraining():
    if 'login' in  session:
      training  = Db.get_login(session['login']).data
      res = training[7]
      all = Exercises.getExercisesBodyWeight()
      if 'training' in  session:
        treino = session['training']
        
        # pega o valor dos requireds
        requireds = treino[-1]
        treino.pop(-1)

        #Tirar o Pared Sets
        treino.pop(-1)

        try:
          data_all = []
          new_order = []

          # Unindo o Treino com o All
          for a in all:
            for t in treino:
              if a["name"] == t["name"]:
                new_data = a.copy()
                new_data.update(t)
                data_all.append(new_data)
              
          # Cria um array qeu repete o num de veses de acordo com o exer, e add infos
          for e in data_all:
            repeated_e = [e.copy() for _ in range(e['rept'])]  # cria uma cópia do dicionário e "rept" vezes
            for i, d in enumerate(repeated_e):
                d['rept_num'] = i + 1  # adiciona um novo campo 'rept_num' com o número de repetição
                d['rest'] = '1:30'   # altera o campo 'reset' para '1:30'
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
          
          # Agrupa os objetos por categoria, sem ter erpetições
          grupCategories = {}
          for a in data_all:
            category = a["category"]
            if category not in grupCategories:
                grupCategories[category] = []
            grupCategories[category].append(a)

          # Criando a rotina FULLBODY intercalada
          array1 = [valor for par in zip(grupCategories['Push'], grupCategories['Core']) for valor in par]
          array2 = [valor for par in zip(grupCategories['Pull'], grupCategories['Legs']) for valor in par]
          array1.extend(array2)
          fullbody = array1

          # Criando a rotina Push/Pull intercalada
          array1 = [valor for par in zip(grupCategories['Push'], grupCategories['Legs']) for valor in par]
          array2 = [valor for par in zip(grupCategories['Pull'], grupCategories['Core']) for valor in par]
          pushPull = {'d1' : array1 , 'd2': array2}

          # Criando a rotina Upper/Lowe intercalada
          array1 = [valor for par in zip(grupCategories['Push'], grupCategories['Pull']) for valor in par]
          array2 = [valor for par in zip(grupCategories['Legs'], grupCategories['Core']) for valor in par]
          upperLower = {'d1' : array1 , 'd2': array2}

          Training = {'fullbody': fullbody,'pushPull':pushPull,'upperLower': upperLower}
        except Exception as e:
          print(f"{e}")
          

        for required in requireds:
          if required['name'] == 'Days':
            days = int(required['value'])
    
        print(session)

        # if 'ip' in session:
        #   user = {
        #       'ip': session['ip'], 
        #       'BaseTraining': Training, 
        #       'TrainingDays': days,
        #       'Requireds': requireds, 
        #       'Training': Training
        #     }

        #   if Db.get_ip(session['ip']).data == None:
        #     Db.save(user)
        #   else:
        #     attUser = {
        #       'ip': session['ip'], 
        #       'TrainingDays': days,
        #       'BaseTraining': Training, 
        #       'Requireds': requireds, 
        #       'Training': Training
        #     }
        #     Db.update_user(session['ip'], attUser)

        # Salvando os dados no banco
        if 'login' in session:
          Db.update_data('Login', session['login'], 'TrainingDays', days)    
          Db.update_data('Login', session['login'], 'BaseTraining', Training)    
          Db.update_data('Login', session['login'], 'Requireds', requireds)    
          Db.update_data('Login', session['login'], 'Training', Training)    
        
        user_found = Db.get_login(session['login']).data

        if user_found[-2] is None:
          data = {
              'nav': 'creat',
              'allTreinos': Training,
              'days': days
            }
        else:
          data = {
              'nav': 'creat',
              'allTreinos': Training,
              'days': days,
              'chosenTraining': user_found[-2]

            }
        # return render_template("creatTraining.html", data=data)
        return getUrl("creatTraining.html", value = data)
      else: 
        data = {
              'nav': 'creat',
              'allTreino': all
            }
        return render_template("exercices.html",  data = data)
    return getUrl('login.hmtl')

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
