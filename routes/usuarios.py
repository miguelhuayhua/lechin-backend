from flask import Blueprint, request,jsonify
from flask_cors import cross_origin
from routes.coneccion import con
usuarios = Blueprint('usuarios',__name__)

cur=con()
@usuarios.route("/")
@cross_origin()
def mostrar_historial():
    cur.execute('SELECT * FROM login where estado=0')
    row = cur.fetchall()
    i=0
    login=[]
    for n in row:
        login.append({"usuario":row[i][1],"password":row[i][2],"tocken_cea":row[i][3]})
        i=i+1
    print(login)
    return jsonify(login)