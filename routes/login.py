from flask import Blueprint, request
from flask_cors import cross_origin
login = Blueprint('login',__name__)

@login.route('/login',methods = ['POST','GET'])
@cross_origin()
def handleLogin():
    if request.method == 'POST':
        print(request.form['usuario'])
        return 'positivo'
    elif request.method == 'GET':
        return 'ESTE ES UN GET'