from flask import Flask
from waitress import serve
import os
from model.db import Db

from routes.basicScreens.basicScreens import basicScreens
from routes.user.user import user
from routes.training.training import training_bp
from routes.erro.erro import err
from routes.api.api import api

Db.createTable('user')

app = Flask(__name__, template_folder='base', static_folder='base/assets')
app.config["SECRET_KEY"] = os.environ.get('CONFIG')

app.register_blueprint(basicScreens)
app.register_blueprint(training_bp)
app.register_blueprint(user)
app.register_blueprint(err)
app.register_blueprint(api)

if __name__ == "__main__":
  app.run(debug=True,port=8083)
  #serve(app, host="0.0.0.0", port=8080)