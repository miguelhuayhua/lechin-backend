from flask import Blueprint, request,jsonify
from flask_cors import cross_origin
from routes.coneccion import db
mostrar = Blueprint('mostrar',__name__)
db = db()

@mostrar.route('/usuarios')
@cross_origin()
def Index():
    cur = db.cursor()
    cur.execute('SELECT * FROM login where estado=0')
    row = cur.fetchall()
    db.close()
    i=0
    usuarios=[]
    for n in row:
        usuarios.append({"nombre":row[i][1],"email":row[i][2],"pasword":row[i][3]})
        i=i+1
    return jsonify(usuarios)