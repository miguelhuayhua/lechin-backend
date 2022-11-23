from flask import Blueprint, request,jsonify
from flask_cors import cross_origin
from routes.coneccion import db
from routes.encriptar import encript
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

@login.route('/confirm_user',methods=['POST'])
@cross_origin()
def handleConfirmUser():
    if request.method == 'POST':
        num_u = request.form['num_u']
        database = db()
        cur = database.cursor()
        cur.execute('UPDATE registro_usuario SET logged = 1 WHERE num_u = %s AND estado = 0',(num_u))
        database.commit()
        cur.execute("""SELECT usuario, token_cea, id_roles FROM registro_usuario WHERE num_u = %s """,(num_u))
        us = cur.fetchone()
        usuario = {'usuario':us[0],'token_cea':us[1],'id_roles':us[2]}
        cur.close()
        database.close()
        return jsonify(usuario)
    
@login.route('/changeFirstUser',methods=['POST'])
@cross_origin()
def changeFirstUser():
    if request.method == 'POST':
        num_u = request.form['num_u']
        new_password = encript(request.form['password'])
        new_user = request.form['new_user']
        token_cea = request.form['token_cea']
        usuario = request.form['usuario']
        print(num_u,new_password,new_user,token_cea,usuario)
        database = db()
        cur = database.cursor()
        if cur.execute('UPDATE registro_usuario SET usuario = %s, password = %s  WHERE num_u = %s AND usuario = %s AND token_cea = %s AND estado = 0',(new_user,new_password,num_u,usuario,token_cea)):
            
            database.commit()
            database.close()
            if cur.rowcount > 0:
                return jsonify({'status':1})
            else:
                return jsonify({'status':0})
        else:
            database.close()
            return jsonify({'status':0})
    
