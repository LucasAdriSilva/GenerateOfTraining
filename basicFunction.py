from flask import Flask, render_template, session, redirect, url_for
from model.db import Db
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from model.exercicio import Exercises 
import smtplib, email.message, random, string, json, shutil, os



# model de textDefault
# textDefault = [
#       Primeira letra do nome do usuário,
#       rota que sera redirecionado se estiver logado,
#       True ou False se vai ter logout,
#       Objeto com os valores tratado pelo backend
#     ]

#  Para usar no html vai precisar {{data[3].........}}
def getUrl(url, value='', bool=False):
  if "login" in session:
    name = session['login']
    user_found =  Db.get_login(name).data
    name = user_found[1]
    chosentraining = user_found[-2]

    if value =='' and user_found[-3] is not None:
      value = user_found[-3]

    if user_found[-3] is None:
      menuShow = False
    else:
      menuShow = True
       
    textDefault = [
      name,
      "/login",
      True,
      value,
      chosentraining,
      menuShow
    ]
    if bool:
      return redirect(url_for(url, data = textDefault))
    else:
      return render_template( url , data = textDefault)
    
  else:
    textDefault = [
      "Faça login",
      url,
      False,
      value
    ]
    return render_template('login.html', data = textDefault)
  
def send_email(emails, content, subject):
    try:  
        corpo_email = content

        msg = email.message.Message()
        msg['Subject'] = subject
        msg['From'] = 'agenciamktm@gmail.com'
        msg['To'] = emails
        password = 'vqslnaabrctovbbm' 
        msg.add_header('Content-Type', 'text/html')
        msg.set_payload(corpo_email )

        s = smtplib.SMTP('smtp.gmail.com: 587')
        s.starttls()
        # Login Credentials for sending the mail
        s.login(msg['From'], password)
        s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
        print('Email enviado')
    except Exception as e:
        print(f"Erro ao enviat email: {e}")
    
def random_generator(size=6, chars=string.ascii_uppercase + string.digits):
 return ''.join(random.choice(chars) for _ in range(size))

def remove_repeated_items_in_list(input_list):
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list