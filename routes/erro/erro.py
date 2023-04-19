from flask import Flask, Blueprint, session, request, flash, jsonify, render_template
from model.db import Db



err = Blueprint('err', __name__, template_folder='templates')



@err.route("/off")
def pageUser():
  data = {'nav': None}
  return render_template("offline.html", data = data)




