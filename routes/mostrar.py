from flask import Blueprint, jsonify, request
from flask_cors import cross_origin
from routes.coneccion import db
mostrar = Blueprint('mostrar', __name__)


@mostrar.route('/usuario_todo')
@cross_origin()
def usuario_todo():
    database = db()
    cur = database.cursor()
    cur.execute('SELECT * FROM registro_usuario where estado=0')
    row = cur.fetchall()
    usuarios = []
    for n in row:
        print(n)
        usuarios.append({"num_u": n[1], "usuario": n[2]})
    database.commit()
    database.close()

    return jsonify(usuarios)


@mostrar.route('/usuario_xid', methods=['POST'])
@cross_origin()
def usuario_xid():
    if request.method == 'POST':
        id_user = request.form['id_user']
        database = db()
        cur = database.cursor()
        cur.execute("""SELECT num_u,usuario FROM registro_usuario 
                    where estado=0 and num_u=%s or usuario=%s""", (id_user,))
        row = cur.fetchall()
        database.close()
        i = 0
        usuarios = []
        for n in row:
            usuarios.append({"num_u": row[i][2], "usuario": row[i][1]})
            i = i+1
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
    i = 0
    usuarios = []
    for n in row:
        usuarios.append({"num_es": row[i][0], "nombres": row[i][1], "apellidos": row[i][2], "carnet": row[i][3], "email": row[i][4], "fecha_nac": row[i]
                        [5], "telf": row[i][6], "edad": row[i][7], "genero": row[i][8], "direccion": row[i][9], "departamento": row[i][10], "usuario": row[i][11]})
        i = i+1
    return jsonify(usuarios)


@mostrar.route('/estudiante_xid', methods=['POST'])
@cross_origin()
def estudiante_xid():
    if request.method == 'POST':
        idestudiante = request.form['idestudiante']
        # conneccion
        database = db()
        cur = database.cursor()
        cur.execute("""SELECT num_es,nombres,apellidos,carnet,email,fecha_nac,telf,edad,genero,direccion,departamento,r.usuario
                FROM estudiante e join registro_usuario r 
                ON e.id_registro = r.id_u
                where e.estado=0 and num_es=%s or carnet=%s;""", (idestudiante,))
        row = cur.fetchall()
        database.close()
        i = 0
        usuarios = []
        for n in row:
            usuarios.append({"num_es": row[i][0], "nombres": row[i][1], "apellidos": row[i][2], "carnet": row[i][3], "email": row[i][4], "fecha_nac": row[i]
                            [5], "telf": row[i][6], "edad": row[i][7], "genero": row[i][8], "direccion": row[i][9], "departamento": row[i][10], "usuario": row[i][11]})
            i = i+1
        return jsonify(usuarios)


@mostrar.route('/docentes')
@cross_origin()
def docente_todo():
    database = db()
    cur = database.cursor()
    cur.execute("""SELECT num_do,nombres,apellidos,carnet,email,fecha_nac,telf,edad,genero,direccion,departamento,disponible
                FROM docentes where estado=0;""")
    docentes = cur.fetchall()
    cur.close()
    database.close()
    listaDocentes = []
    for docente in docentes:
        listaDocentes.append({"num_u": docente[0], "nombres": docente[1], "apellidos": docente[2], "carnet": docente[3], "email": docente[4], "fecha_nac": docente[5],
                             "telf": docente[6], "edad": docente[7], "genero": docente[8], "direccion": docente[9], "departamento": docente[10], "disponible": docente[11]})
    return jsonify(listaDocentes)


@mostrar.route('/estudiantes')
@cross_origin()
def estudiantes():
    database = db()
    cur = database.cursor()
    cur.execute("SELECT num_es, nombres, apellidos, carnet, email, fecha_nac, telf, edad, genero, direccion, departamento FROM estudiante WHERE estado = 0")
    estudiantes = cur.fetchall()
    cur.close()
    listaEstudiantes = []
    for estudiante in estudiantes:
        listaEstudiantes.append({"num_u": estudiante[0], "nombres": estudiante[1], "apellidos": estudiante[2], "carnet": estudiante[3], "email": estudiante[4],
                                "fecha_nac": estudiante[5], "telf": estudiante[6], "edad": estudiante[7], "genero": estudiante[8], "direccion": estudiante[9], "departamento": estudiante[10]})
    database.close()
    return jsonify(listaEstudiantes)


@mostrar.route('/materias')
@cross_origin()
def materias():
    database = db()
    cur = database.cursor()
    cur.execute('SELECT id_m, nombre, url,costo,descripcion, f_inicio,f_final, duracion, hora_inicio,hora_salida FROM materia where estado=0')
    materias = cur.fetchall()
    cur.close()
    listaMaterias = []
    for mat in materias:
        listaMaterias.append({"id_m": mat[0], "nombre": mat[1], "url": mat[2], "costo": mat[3], "descripcion": mat[4],
                             "f_inicio": mat[5], "f_final": mat[6], "duracion": mat[7], "hora_inicio": mat[8], "salida": mat[9]})
    database.close()
    return jsonify(listaMaterias)


@mostrar.route('/docente_xid', methods=['POST'])
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
                where d.estado=0 and d.num_do=%s or d.carnet=%s;""", (iddocente,))
        row = cur.fetchall()
        database.close()
        i = 0
        usuarios = []
        for n in row:
            usuarios.append({"num_do": row[i][0], "nombres": row[i][1], "apellidos": row[i][2], "carnet": row[i][3], "email": row[i][4], "fecha_nac": row[i][5], "telf": row[i][6], "edad": row[i][7],
                            "genero": row[i][8], "direccion": row[i][9], "departamento": row[i][10], "usuario": row[i][11], "academia_pertenece": row[i][12], "fecha_antiguedad": row[i][13], "especialidad": row[i][14]})
            i = i+1
        return jsonify(usuarios)


@mostrar.route('/docente', methods=['POST'])
@cross_origin()
def obtenerDocente():
    if request.method == 'POST':
        num_u = request.form['num_u']
        database = db()
        cur = database.cursor()
        cur.execute("""SELECT nombres, apellidos, carnet, email, fecha_nac, telf, edad, genero, direccion, departamento, id_registro 
                fROM docentes WHERE num_do = %s""", (num_u))
        doc = cur.fetchone()
        docente = {'nombres': doc[0], 'apellidos': doc[1], 'carnet': doc[2], 'email': doc[3], 'fecha_nac': doc[4],
                   'telf': doc[5], 'edad': doc[6], 'genero': doc[7], 'direccion': doc[8], 'departamento': doc[9], 'id_registro': doc[10]}
        cur.close()
        database.close()
        return jsonify(docente)


@mostrar.route('/estudiante_xapellido')
@cross_origin()
def estudiante_xapellido():
    cur = db.cursor()
    cur.execute(
        'SELECT nombres,apellidos,carnet,email,fecha_nac FROM estudiante where estado=0 and apellidos')
    row = cur.fetchall()
    i = 0
    usuarios = []
    for n in row:
        usuarios.append(
            {"num_u": row[i][1], "usuario": row[i][2], "pasword": row[i][3]})
        i = i+1
    return jsonify(usuarios)


@mostrar.route('/calificacion')
@cross_origin()
def calificacion():
    database = db()
    cur = database.cursor()
    cur.execute('SELECT * FROM calificacion where estado=0')
    row = cur.fetchall()
    i = 0
    usuarios = []
    for n in row:
        usuarios.append(
            {"num_u": row[i][1], "usuario": row[i][2], "pasword": row[i][3]})
        i = i+1
        database.close()
        database.commit()
    return jsonify(usuarios)


@mostrar.route('/materia', methods=['POST'])
@cross_origin()
def obtenerMateria():
    if request.method == 'POST':
        id_m = request.form['id']
        database = db()
        cur = database.cursor()
        cur.execute(
            'SELECT * FROM materia WHERE id_m = %s AND estado = 0', (id_m))
        mat = cur.fetchone()
        cur.close()
        materia = {"id_m": mat[0], "nombre": mat[1], "url": mat[2], "grado": mat[3], "costo": mat[4],
                   "id_semestre": mat[5], "estado": mat[6], "fecha_desde": mat[7], "fecha_hasta": mat[8], "descripcion": mat[9]}
        database.close()
        return jsonify(materia)


@mostrar.route('/carreras')
@cross_origin()
def especialidad():
    database = db()
    cur = database.cursor()
    cur.execute('SELECT id_e,nombre,universidad FROM carrera where estado=0')
    carreras = cur.fetchall()
    listaCarreras = [{'id_e': carrera[0], 'nombre':carrera[1],
                      'universidad':carrera[2]} for carrera in carreras]
    cur.close()
    database.close()
    return jsonify(listaCarreras)


@mostrar.route('/estudiante', methods=['POST'])
@cross_origin()
def obtenerEstudiante():
    if request.method == 'POST':
        num_u = request.form['num_u']
        database = db()
        cur = database.cursor()
        cur.execute("""SELECT nombres, apellidos, carnet, email, fecha_nac, telf, edad, genero, direccion, departamento, id_registro 
                fROM estudiante WHERE num_es = %s""", (num_u))
        est = cur.fetchone()
        estudiante = {'nombres': est[0], 'apellidos': est[1], 'carnet': est[2], 'email': est[3], 'fecha_nac': est[4],
                      'telf': est[5], 'edad': est[6], 'genero': est[7], 'direccion': est[8], 'departamento': est[9], 'id_registro': est[10]}
        cur.close()
        database.close()
        return jsonify(estudiante)


@mostrar.route('/usuario', methods=['POST'])
@cross_origin()
def obtenerUsuario():
    if request.method == 'POST':
        num_u = request.form['num_u']
        database = db()
        cur = database.cursor()
        cur.execute(
            """SELECT usuario, token_cea FROM registro_usuario WHERE num_u = %s """, (num_u))
        us = cur.fetchone()
        usuario = {'usuario': us[0], 'token_cea': us[1]}
        cur.close()
        database.close()
        return jsonify(usuario)


@mostrar.route('/first_login', methods=['POST'])
@cross_origin()
def firstLogin():
    if request.method == 'POST':
        token = request.form['token']
        database = db()
        cur = database.cursor()
        cur.execute("""SELECT E.num_es, E.nombres, E.apellidos, E.carnet, E.fecha_nac,E.telf, E.edad,
        E.genero, E.direccion,E.departamento, E.email  FROM estudiante E INNER JOIN registro_usuario U WHERE E.num_es = U.num_u AND E.estado = 0 AND U.token_cea = %s """, (token))
        est = cur.fetchone()
        cur.close()
        database.close()
        if est != None:
            estudiante = {'num_u': est[0], 'nombres': est[1], 'apellidos': est[2], 'carnet': est[3], 'fecha_nac': est[4],
                          'telf': est[5], 'edad': est[6], 'genero': est[7], 'direccion': est[8], 'departamento': est[9], 'email': est[10]}
            return jsonify(estudiante)
        else:
            return {'error': 1}
