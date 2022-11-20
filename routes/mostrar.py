from flask import Blueprint,jsonify,request
from flask_cors import cross_origin
from routes.coneccion import db
mostrar = Blueprint('mostrar',__name__)

@mostrar.route('/usuario_todo')
@cross_origin()
def usuario_todo():
    database = db()
    cur = database.cursor()
    cur.execute('SELECT * FROM registro_usuario where estado=0')
    row = cur.fetchall()    
    usuarios=[]
    for n in row:
        print(n)
        usuarios.append({"num_u":n[1],"usuario":n[2]})
    database.commit()
    database.close()

    return jsonify(usuarios)

@mostrar.route('/usuario_xid',methods=['POST'])
@cross_origin()
def usuario_xid():
    if request.method == 'POST':
        id_user = request.form['id_user'] 
        database = db()
        cur = database.cursor()
        cur.execute("""SELECT num_u,usuario FROM registro_usuario 
                    where estado=0 and num_u=%s or usuario=%s""",(id_user,))
        row = cur.fetchall()
        database.close()
        i=0
        usuarios=[]
        for n in row:
            usuarios.append({"num_u":row[i][2],"usuario":row[i][1]})
            i=i+1
        return jsonify(usuarios)

@mostrar.route('/estudiante_todo')
@cross_origin()
def estudiante_todo():
    database = db()
    cur = database.cursor()
    cur.execute("""SELECT num_es,nombres,apellidos,carnet,email,fecha_nac,telf,edad,genero,direccion,departamento,r.usuario
                FROM estudiante e join registro_usuario r 
                ON e.id_registro = r.id_u
                where e.estado=0;""")
    row = cur.fetchall()
    database.close()
    i=0
    usuarios=[]
    for n in row:
        usuarios.append({"num_es":row[i][0],"nombres":row[i][1],"apellidos":row[i][2],"carnet":row[i][3],"email":row[i][4],"fecha_nac":row[i][5],"telf":row[i][6],"edad":row[i][7],"genero":row[i][8],"direccion":row[i][9],"departamento":row[i][10],"usuario":row[i][11]})
        i=i+1
    return jsonify(usuarios)

@mostrar.route('/estudiante_xid',methods=['POST'])
@cross_origin()
def estudiante_xid():
    if request.method == 'POST':
        idestudiante = request.form['idestudiante']
        #conneccion
        database = db()
        cur = database.cursor()
        cur.execute("""SELECT num_es,nombres,apellidos,carnet,email,fecha_nac,telf,edad,genero,direccion,departamento,r.usuario
                FROM estudiante e join registro_usuario r 
                ON e.id_registro = r.id_u
                where e.estado=0 and num_es=%s or carnet=%s;""",(idestudiante,))
        row = cur.fetchall()
        database.close()
        i=0
        usuarios=[]
        for n in row:
            usuarios.append({"num_es":row[i][0],"nombres":row[i][1],"apellidos":row[i][2],"carnet":row[i][3],"email":row[i][4],"fecha_nac":row[i][5],"telf":row[i][6],"edad":row[i][7],"genero":row[i][8],"direccion":row[i][9],"departamento":row[i][10],"usuario":row[i][11]})
            i=i+1
        return jsonify(usuarios)

@mostrar.route('/docente_todo')
@cross_origin()
def docente_todo():
    database = db()
    cur = database.cursor()
    cur.execute("""SELECT num_do,nombres,apellidos,carnet,email,fecha_nac,telf,edad,genero,direccion,departamento,r.usuario,p.academia_pertenece,p.fecha_antiguedad,e.nombre
                FROM docentes d join registro_usuario r 
                ON d.id_registro = r.id_u JOIN detalle_personal p
                ON d.id_detalle = p.id_dd JOIN especialidad e
                ON p.id_especialidad = e.id_e
                where d.estado=0;""")
    row = cur.fetchall()
    database.close()
    i=0
    usuarios=[]
    for n in row:
        usuarios.append({"num_do":row[i][0],"nombres":row[i][1],"apellidos":row[i][2],"carnet":row[i][3],"email":row[i][4],"fecha_nac":row[i][5],"telf":row[i][6],"edad":row[i][7],"genero":row[i][8],"direccion":row[i][9],"departamento":row[i][10],"usuario":row[i][11],"academia_pertenece":row[i][12],"fecha_antiguedad":row[i][13],"especialidad":row[i][14]})
        i=i+1
    return jsonify(usuarios)

@mostrar.route('/materias')
@cross_origin()
def materia():
    database = db()
    cur = database.cursor()
    cur.execute('SELECT * FROM materia where estado=0')
    materias = cur.fetchall()
    listaMaterias=[]
    for mat in materias:
        listaMaterias.append({"id_m":mat[0],"nombre":mat[1],"url":mat[2],"grado":mat[3],"costo":mat[4],"id_semestre":mat[5],"estado":mat[6], "fecha_desde":mat[7],"fecha_hasta":mat[8],"descripcion":mat[9]})
    database.close()
    return jsonify(listaMaterias)
@mostrar.route('/docente_xid',methods=['POST'])
@cross_origin()
def docente_xid():
    if request.method == 'POST':
        iddocente = request.form['iddocente'] 
        database = db()
        cur = database.cursor()
        cur.execute("""SELECT num_do,nombres,apellidos,carnet,email,fecha_nac,telf,edad,genero,direccion,departamento,r.usuario,p.academia_pertenece,p.fecha_antiguedad,e.nombre
                FROM docentes d join registro_usuario r 
                ON d.id_registro = r.id_u JOIN detalle_personal p
                ON d.id_detalle = p.id_dd JOIN especialidad e
                ON p.id_especialidad = e.id_e
                where d.estado=0 and d.num_do=%s or d.carnet=%s;""",(iddocente,))
        row = cur.fetchall()
        database.close()
        i=0
        usuarios=[]
        for n in row:
            usuarios.append({"num_do":row[i][0],"nombres":row[i][1],"apellidos":row[i][2],"carnet":row[i][3],"email":row[i][4],"fecha_nac":row[i][5],"telf":row[i][6],"edad":row[i][7],"genero":row[i][8],"direccion":row[i][9],"departamento":row[i][10],"usuario":row[i][11],"academia_pertenece":row[i][12],"fecha_antiguedad":row[i][13],"especialidad":row[i][14]})
            i=i+1
        return jsonify(usuarios)

@mostrar.route('/estudiante', methods=['POST'])
@cross_origin()
def obtenerEstudiante():
    if request.method == 'POST':
        num_es = request.form['num_es']
        database = db()
        cur = database.cursor()
        cur.execute("""SELECT nombres, apellidos, carnet, email, fecha_nac, telf, edad, genero, direccion, departamento, id_registro 
                fROM estudiante WHERE num_es = %s""",(num_es))
        est = cur.fetchone()
        estudiante = {'nombres':est[0],'apellidos':est[1],'carnet':est[2],'email':est[3],'fecha_nac':est[4], 'telefono':est[5], 'edad':est[6],'genero':est[7],'direccion':est[8],'departamento':est[9],'id_registro':est[10]}
        return jsonify(estudiante)

@mostrar.route('/docente', methods=['POST'])
@cross_origin()
def obtenerDocente():
    if request.method == 'POST':
        num_do = request.form['num_do']
        database = db()
        cur = database.cursor()
        cur.execute("""SELECT nombres, apellidos, carnet, email, fecha_nac, telf, edad, genero, direccion, departamento, id_registro 
                fROM docentes WHERE num_do = %s""",(num_do))
        est = cur.fetchone()
        docente = {'nombres':est[0],'apellidos':est[1],'carnet':est[2],'email':est[3],'fecha_nac':est[4], 'telefono':est[5], 'edad':est[6],'genero':est[7],'direccion':est[8],'departamento':est[9],'id_registro':est[10]}
        return jsonify(docente)


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

@mostrar.route('/materia')
@cross_origin()
def materia():
    database = db()
    cur = database.cursor()
    cur.execute('SELECT id_m,nombre,url,grado,costo FROM materia where estado=0')
    materias = cur.fetchall()
    i=0
    listaMaterias=[]
    for n in materias:
        listaMaterias.append({"id_m":materias[i][0],"nombre":materias[i][1],"url":materias[i][2],"grado":materias[i][3],"costo":materias[i][4]})
        i=i+1
        database.close()
        database.commit()
    return jsonify(listaMaterias)

@mostrar.route('/especialidad')
@cross_origin()
def especialidad():
    database = db()
    cur = database.cursor()
    cur.execute('SELECT id_e,nombre FROM especialidad where estado=0')
    row = cur.fetchall()
    i=0
    usuarios=[]
    for n in row:
        usuarios.append({"id_e":row[i][0],"especialidad":row[i][1]})
        i=i+1
        database.close()
        database.commit()
    return jsonify(usuarios)


@mostrar.route('/estudiante', methods=['POST'])
@cross_origin()
def obtenerEstudiante():
    if request.method == 'POST':
        num_es = request.form['num_es']
        database = db()
        cur = database.cursor()
        cur.execute("""SELECT nombres, apellidos, carnet, email, fecha_nac, telf, edad, genero, direccion, departamento, id_registro 
                fROM estudiante WHERE num_es = %s""",(num_es))
        est = cur.fetchone()
        estudiante = {'nombres':est[0],'apellidos':est[1],'carnet':est[2],'email':est[3],'fecha_nac':est[4], 'telf':est[5], 'edad':est[6],'genero':est[7],'direccion':est[8],'departamento':est[9],'id_registro':est[10]}
        cur.close()
        database.close()
        return jsonify(estudiante)
    
@mostrar.route('/usuario',methods=['POST'])
@cross_origin()
def obtenerUsuario():
    if request.method == 'POST':
        num_u = request.form['num_u']
        database = db()
        cur = database.cursor()
        cur.execute("""SELECT usuario, token_cea, id_roles FROM registro_usuario WHERE num_u = %s """,(num_u))
        us = cur.fetchone()
        usuario = {'usuario':us[0],'token_cea':us[1],'id_roles':us[2]}
        cur.close()
        database.close()
        return jsonify(usuario)
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
