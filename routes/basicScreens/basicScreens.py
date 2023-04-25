from flask import Blueprint, render_template, request, redirect, url_for, make_response, session
import json
from model.exercicio import Exercicio 
from model.db import Db 
from fpdf import FPDF


basicScreens = Blueprint('basicScreens', __name__, template_folder='templates')

@basicScreens.route("/")
def index():
  # Verifica se tem o ip na sessão
  if 'ip' in session:
    ip_found = Db.get_ip(session['ip']).data
    # Verifica o retorno do banco nao é null
    if ip_found is not None:

      # Verifica se é o priemiro treino
      if  ip_found[-1] is not None:
        last_training =  json.loads(ip_found[-1])[-1]  
        data= {
          'nav': 'home', 
          'ip': ip_found[0],
          'dayTraining': 3,
          'nameRotina': ip_found[-2],
          'training': last_training,
        }
      else: 
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
        return render_template("home.html", data = data)    

    else:
       data = {'nav': 'home'}
    return render_template("firstAcess.html", data = data)
    # return render_template("home.html", data = data)
  else:
    ip = request.remote_addr
    session['ip'] = ip
    data = {'nav': 'home'}
    return render_template("firstAcess.html", data = data)

@basicScreens.route("/sendTraining", methods=["GET", "POST"])
def teste():
    if request.method == "POST":
        treino = request.get_json()
        data = {'treino': treino}
        return redirect(url_for('basicScreens.creatTraining', data=data))

    return render_template("home.html")

@basicScreens.route("/creatTraining" , methods=["GET", "POST"])
def creatTraining():
    res = request.args.get('data')
    all = Exercicio.getAllExercicios()
    if res != None:
      treino = json.loads(res.replace("'", "\""))
      
      # pega o valor dos requireds
      requireds = treino['treino'][-1]
      # remove o requireds do array de treino
      treino['treino'].pop(-1)
      
      # pega o valor do Paired Sets
      pairedSets = treino['treino'][-1]
      # remove o Paired Sets do array de treino
      treino['treino'].pop(-1)

      try:
        data_all = []
        new_order = []

        # Unindo o Treino com o All
        for a in all:
          for t in treino['treino']:
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
  
      pairedSets = pairedSets['value']

      # Salvando usando IP
      if session['ip'] is not None:

        user = {
            'ip': session['ip'], 
            'BaseTraining': Training, 
            'TrainingDays': days,
            'Requireds': requireds, 
            'Training': Training
          }

        if Db.get_ip(session['ip']).data == None:
          Db.save(user)
        else:
          attUser = {
            'ip': session['ip'], 
            'TrainingDays': days,
            'BaseTraining': Training, 
            'Requireds': requireds, 
            'Training': Training
          }
          Db.update_user(session['ip'], attUser)

      data = {
          'nav': 'creat',
          'allTreinos': Training,
          'days': days
        }
      return render_template("creatTraining.html", data=data)
    else: 
      data = {
            'nav': 'creat',
            'allTreino': all
          }
      return render_template("exercices.html", data=data)


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
