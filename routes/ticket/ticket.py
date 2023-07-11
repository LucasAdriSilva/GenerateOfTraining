from flask import Blueprint, render_template, request, redirect, url_for, current_app, session
from flask_socketio import emit
import datetime, json
from model.db import Db
import base64
import io as Io
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
    if 'login' not in session:
        return  getUrl('login.html')
    
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

                # Verificar se a mensagem já existe
                if user_name in messages:
                    return

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
            info = json.loads(user_found[3])
            if 'rooms' in info:
                for rooms in info['rooms']:
                    if rooms['name'] == data['name']:
                        rooms['activate'] = False
                        res = [info]
                        save = Db.update_data('Login', data['user'], 'UserData', res)

    @io.on('sendImage')
    def send_image_handler(data):
        room_name = data['room'].strip()
        image_data = data['image']
        user_name = f"{data['name']}--{datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"

        # Salvar os dados em base64 no banco de dados
        Db.attMsg(room_name, user_name, image_data)

        # Emitir o evento 'getImage' para todos os clientes na sala
        emit('getImage', {'image': image_data}, room=room_name)




    @io.on('loadingMessage')
    def handle_message2(user):         
        if user[0] == 'Suporte':
            user[0] = 'Lucas'   
        user_found = Db.get_login(user[0].strip()).data

        user_data = json.loads(user_found[3])

        roomSelect={}
        if user[0] == 'Lucas':
            roomSelect = Db.getNameTicket(user[1]).data[0]
        else:    
            for room in user_data['rooms']:
                if room['name'].strip() == user[1].strip():
                    roomSelect = room

        if 'messagens' in roomSelect:
            data = roomSelect['messagens']
            emit('loadingPage', data, broadcast=True)


    @io.on('Messagem')
    def handle_message(data):     

        room = Db.getNameTicket(data['room']).data[0]
        new_msg = room['messagens'][f'{data["user"]}--{data["timestamp"]}'] = data['message']
        
        Db.attMsg(data['room'], f"{data['user']}--{data['timestamp']}", new_msg)

        data = {'message': data['message'], 'user': data['user'], 'timestamp': data['timestamp']}
        emit('returnMessage', data ,broadcast=True)

    @io.on('image')
    def handle_image(image):
        timestamp = datetime.datetime.now().strftime('%H:%M:%S--%d/%m/%y')
        data = {'image': image, 'user': 'Usuário', 'timestamp': timestamp}
        emit('image', data, broadcast=True)