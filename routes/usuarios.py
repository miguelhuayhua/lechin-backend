from flask import Blueprint, request,jsonify
from flask_cors import cross_origin
from routes.coneccion import db
usuario = Blueprint('usuario',__name__)
db = db()

@usuario.route("/prueba")
@cross_origin()
def mostrar_historial():
    cur =db.cursor()
    cur.execute('SELECT * FROM estudiante where estado=0')
    row = cur.fetchall()
    db.close()

    i=0
    login=[]
    for n in row:
        login.append({"usuario":row[i][1],"password":row[i][2],"tocken_cea":row[i][3]})
        i=i+1
   
    return jsonify(login)