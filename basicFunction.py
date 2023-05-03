from flask import Flask, render_template, session, redirect, url_for
from model.db import Db
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import shutil, os
import smtplib
import email.message
import random, string


# model de textDefault
# textDefault = [
#       Primeira letra do nome do usuário,
#       rota que sera redirecionado se estiver logado,
#       True ou False se vai ter logout,
#       Objeto com os valores trado pelo backend
#     ]

#  Para usar no html vai precisar {{data[3].........}}


def getUrl(url, prop='', value='', bool=False):
  if "login" in session:
    name = session['login']
    user_found =  Db.get_login(name).data
    name = user_found[1]

    textDefault = [
      name[0],
      "/login",
      True,
      value
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