from flask import Blueprint,jsonify,request
from flask_cors import cross_origin
from routes.coneccion import db
mostrar = Blueprint('mostrar',__name__)

@mostrar.route('/usuarios')
@cross_origin()
def usuarios():
    database = db()
    cur = database.cursor()
    cur.execute('SELECT * FROM registro_usuario where estado=0')
    row = cur.fetchall()
    i=0
    usuarios=[]
    for n in row:
        usuarios.append({"num_u":row[i][1],"usuario":row[i][2],"pasword":row[i][3]})
        i=i+1
        database.close()
        database.commit()
    return jsonify(usuarios)

@mostrar.route('/estudiante_todo')
@cross_origin()
def estudiante_xfecha():
    cur = db.cursor()
    cur.execute("""SELECT num_es,nombres,apellidos,carnet,email,fecha_nac,telf,edad,genero,direccion,departamento,r.usuario
                FROM estudiante e join registro_usuario r 
                ON e.id_registro = r.id_u
                where e.estado=0;""")
    row = cur.fetchall()
    i=0
    usuarios=[]
    for n in row:
        usuarios.append({"num_es":row[i][0],"nombres":row[i][1],"apellidos":row[i][2],"carnet":row[i][3],"email":row[i][4],"fecha_nac":row[i][5],"telf":row[i][6],"edad":row[i][7],"genero":row[i][8],"direccion":row[i][9],"departamento":row[i][10],"usuario":row[i][11]})
        i=i+1
    return jsonify(usuarios)

@mostrar.route('/estudiante_xapellido')
@cross_origin()
def estudiante_xapellido():
    cur = db.cursor()
    cur.execute('SELECT nombres,apellidos,carnet,email,fecha_nac FROM estudiante where estado=0 and apellidos')
    row = cur.fetchall()
    i=0
    usuarios=[]
    for n in row:
        usuarios.append({"num_u":row[i][1],"usuario":row[i][2],"pasword":row[i][3]})
        i=i+1
    return jsonify(usuarios)

@mostrar.route('/materia')
@cross_origin()
def materia():
    database = db()
    cur = database.cursor()
    cur.execute('SELECT * FROM materia where estado=0')
    row = cur.fetchall()
    i=0
    usuarios=[]
    for n in row:
        usuarios.append({"num_u":row[i][1],"usuario":row[i][2],"pasword":row[i][3]})
        i=i+1
        database.close()
        database.commit()
    return jsonify(usuarios)

@mostrar.route('/especialidad')
@cross_origin()
def especialidad():
    database = db()
    cur = database.cursor()
    cur.execute('SELECT * FROM especialidad where estado=0')
    row = cur.fetchall()
    i=0
    usuarios=[]
    for n in row:
        usuarios.append({"num_u":row[i][1],"usuario":row[i][2],"pasword":row[i][3]})
        i=i+1
        database.close()
        database.commit()
    return jsonify(usuarios)

@mostrar.route('/docentes')
@cross_origin()
def docentes():
    database = db()
    cur = database.cursor()
    cur.execute('SELECT * FROM docentes where estado=0')
    row = cur.fetchall()
    i=0
    usuarios=[]
    for n in row:
        usuarios.append({"num_u":row[i][1],"usuario":row[i][2],"pasword":row[i][3]})
        i=i+1
        database.close()
        database.commit()
    return jsonify(usuarios)

@mostrar.route('/calificacion')
@cross_origin()
def calificacion():
    database = db()
    cur = database.cursor()
    cur.execute('SELECT * FROM calificacion where estado=0')
    row = cur.fetchall()
    i=0
    usuarios=[]
    for n in row:
        usuarios.append({"num_u":row[i][1],"usuario":row[i][2],"pasword":row[i][3]})
        i=i+1
        database.close()
        database.commit()
    return jsonify(usuarios)

# def ejemplo():
#     database = db()
#     cur = database.cursor()
#     cur.execute('SELECT * FROM roles where estado=0;')
#     row = cur.fetchall()
#     i=0
#     print(row)
#     usuarios=[]
#     for n in row:
#         usuarios.append({"nombre":row[i][1],"email":row[i][2]})
#         i=i+1
#     return jsonify(usuarios)