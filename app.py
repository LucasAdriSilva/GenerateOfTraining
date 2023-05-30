from flask import Flask
from flask_socketio import SocketIO
from routes.ticket.ticket import ticket, register_chat_events
from waitress import serve
import os
from model.db import Db
from routes.basicScreens.basicScreens import basicScreens
from routes.user.user import user
from routes.training.training import training_bp
from routes.erro.erro import err
from routes.api.api import api

Db.createTable('user')

def create_app():
    app = Flask(__name__, template_folder='base', static_folder='base/assets')
    app.config["SECRET_KEY"] = os.environ.get('CONFIG')

    # Registrar os blueprints e configurar as rotas
    app.register_blueprint(basicScreens)
    app.register_blueprint(training_bp)
    app.register_blueprint(user)
    app.register_blueprint(err)
    app.register_blueprint(api)
    app.register_blueprint(ticket)

    # Inicializar o objeto SocketIO
    io = SocketIO(app, cors_allowed_origins='*')

    # Registrar os eventos do chat
    register_chat_events(io)

    return app, io

if __name__ == "__main__":
    app, io = create_app()
    # Use o objeto SocketIO para executar o servidor
    io.run(app, debug=True, port=8083)
    #serve(app, host="0.0.0.0", port=8080)
