from flask import Blueprint, request,jsonify
from flask_cors import cross_origin
from routes.coneccion import db
mostrar = Blueprint('mostrar',__name__)
#mysql-mysqlwithpython.alwaysdata.net
#3306
#282543_1
@mostrar.route('/usuarios')
@cross_origin()
def Index():
    database = db()
    row = None
    try:
        cur = database.cursor()
        cur.execute('SELECT * FROM login where estado=0')
        row = cur.fetchall()
        database.close()
    except Exception as e:
        print(e)
    i=0
    usuarios=[]
    for n in row:
        usuarios.append({"nombre":row[i][1],"email":row[i][2],"pasword":row[i][3]})
        i=i+1
    return jsonify(usuarios)