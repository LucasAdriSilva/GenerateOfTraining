from flask import Blueprint, render_template, request, redirect, url_for, current_app, session
from flask_socketio import emit
import datetime, json
from model.db import Db
from basicFunction import getUrl, random_generator

ticket = Blueprint('ticket', __name__, template_folder='templates')

@ticket.route('/suport')
def suporte():
    if 'login' not in session:
        return getUrl('login.html')
    #Se for um ADM ele irá ver todas as conversar
    if session['login'] == 'Lucas':
        rooms = Db.getTickets().data
        response = []
        for room in rooms:
            if room['messagens'] != {}:                
                last_key, last_value = list(room['messagens'].items())[-1]
                last_key_parts = last_key.split('--')
                last_datetime = datetime.datetime.strptime(last_key_parts[-1], "%Y-%m-%d-%H-%M-%S")
                last_time = last_datetime.strftime("%H:%M")
                last_message = last_value
                newData = {'id': room['id'], 'name': room['name'], 'latest_message': last_message, 'last_time': last_time}
                response.append(newData)
            else:
                newData = {'id': room['id'],'name': room['name'], 'latest_message': '', 'last_time': ''}
                response.append(newData)
        return getUrl('index.html', value=response)
    
    #Se for um usuario ele vai ver apenas as suas conversar
    else:
        user_found = Db.get_login(session['login']).data
        user_found = json.loads(user_found[3])
        response = []

        if 'rooms' in user_found:
            for room in user_found['rooms']:              
                if room['messagens'] != {}:                
                    last_key, last_value = list(room['messagens'].items())[-1]
                    last_key_parts = last_key.split('--')
                    last_datetime = datetime.datetime.strptime(last_key_parts[-1], "%Y-%m-%d-%H-%M-%S")
                    last_time = last_datetime.strftime("%H:%M")
                    last_message = last_value
                    newData = {'id': room['id'],'name': room['name'], 'latest_message': last_message, 'last_time': last_time}
                    response.append(newData)
                else:
                    newData = {'id': room['id'],'name': room['name'], 'latest_message': '', 'last_time': ''}
                    response.append(newData)
            return getUrl('index.html', value=response)      
        return getUrl('index.html')

@ticket.route('/create_room', methods=['POST'])
def create_room():
    ticket_name = request.form.get('ticket_name')
    id = random_generator(size=8)

    tickets = Db.getTickets().data

    if tickets:
        ticket_ids = [ticket['id'] for ticket in tickets]
    else:
        ticket_ids = []

    
    while id in ticket_ids:
        id = random_generator(size=8)

    newData = {'id': id, 'name': ticket_name, 'messagens': {}, 'activate': True}

    if 'login' in session:
        Db.addTicket('Login', session['login'], newData)
    
    return redirect(url_for('.room', ticket_name=ticket_name))

@ticket.route('/room/<ticket_name>')
def room(ticket_name):
    teste = Db.getNameTicket(ticket_name).data[0]
    id = teste['id']
    res = {'name': ticket_name, 'user': session['login'], 'id': id}
    return render_template('ticket.html', data=res)

def register_chat_events(io):
    @io.on('sendMessage')
    def send_message_handler(msg):
        rooms = Db.getTickets().data
        for room in rooms:
            if room['name'] == msg['room'].strip():
                nameRoom = room['name']
                UserData = room 
                messages = UserData['messagens']
                user_name = f"{msg['name']}--{datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"
                messages[user_name] = msg['msg']
                UserData['messagens'] = messages
                Db.attMsg(UserData['name'], user_name,  msg['msg'])
                emit('getMessages', messages, broadcast=True)
                       

    @io.on('message')
    def message_handler(ticket_name):
        rooms = Db.getTickets().data
        room_messages = [msg['messagens'] for msg in rooms if msg['name'] == ticket_name]
        emit('getMessages', room_messages)

    @io.on('desactivateChat')
    def desactivateChat(data):
        print(data)
        user_found = Db.get_login(data['user']).data
        if user_found[3] is not None:
            info = json.loads(user_found[3])[0]
            if 'rooms' in info:
                for rooms in info['rooms']:
                    if rooms['name'] == data['name']:
                        rooms['activate'] = False
                        res = [info]
                        save = Db.update_data('Login', data['user'], 'UserData', res)
                
