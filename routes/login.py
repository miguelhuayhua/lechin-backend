from flask import Blueprint, request,jsonify
from flask_cors import cross_origin
login = Blueprint('login',__name__)

@login.route('/login',methods = ['POST','GET'])
@cross_origin()
def handleLogin():
    if request.method == 'POST':
        print(request.form['usuario'])
        print(request.form['password'])
        return jsonify({'nombre':'hola'})
    elif request.method == 'GET':
        return 'ESTE ES UN GET'