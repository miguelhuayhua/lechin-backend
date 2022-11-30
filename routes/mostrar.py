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

@mostrar.route('/administrativo', methods=['POST'])
@cross_origin()
def obtenerAdministrativo():
    if request.method == 'POST':
        num_u = request.form['num_u']
        database = db()
        cur = database.cursor()
        cur.execute("""SELECT nombres, apellidos, carnet, email, fecha_nac, telf, edad, genero, direccion, departamento, id_registro 
                FROM personal_administrativo WHERE num_ad = %s""", (num_u))
        adm = cur.fetchone()
        administrativo = {'nombres': adm[0], 'apellidos': adm[1], 'carnet': adm[2], 'email': adm[3], 'fecha_nac': adm[4],
                   'telf': adm[5], 'edad': adm[6], 'genero': adm[7], 'direccion': adm[8], 'departamento': adm[9], 'id_registro': adm[10]}
        cur.close()
        database.close()
        return jsonify(administrativo)


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
            """SELECT id_m, nombre, url, costo, descripcion, num_do, id_t, id_turno, f_inicio,
            duracion,hora_inicio, hora_salida,f_final FROM materia WHERE id_m = %s AND estado = 0""", (id_m))
        mat = cur.fetchone()
        cur.close()
        materia = {"id_m": mat[0], "nombre": mat[1], "url": mat[2], "costo": mat[3],
                   "descripcion": mat[4], "num_do": mat[5], "id_t": mat[6], "id_turno": mat[7], "f_inicio": mat[8],
                   "duracion":mat[9],"hora_inicio":mat[10],"hora_salida":mat[11],"f_final":mat[12]}
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

@mostrar.route('/administrativos')
@cross_origin()
def obtenerAdministrativos():
    database = db()
    cur = database.cursor()
    if cur.execute(
        """SELECT num_ad, nombres, apellidos, carnet, email, fecha_nac, telf, edad, genero, direccion, departamento, disponible
                fROM personal_administrativo"""):
        administrativos = cur.fetchall()
        listaAdministrativos = [{"num_u": administrativo[0], "nombres": administrativo[1], "apellidos": administrativo[2], "carnet": administrativo[3], "email": administrativo[4], "fecha_nac": administrativo[5],
                             "telf": administrativo[6], "edad": administrativo[7], "genero": administrativo[8], "direccion": administrativo[9], "departamento": administrativo[10],"disponible":administrativo[11]}
                                for administrativo in administrativos]
        cur.close()
        database.close()
        return jsonify(listaAdministrativos)
    else:
        database.close()
        return jsonify({"status":0})
    
@mostrar.route('/first_login', methods=['POST'])
@cross_origin()
def firstLogin():
    if request.method == 'POST':
        token = request.form['token']
        database = db()
        cur = database.cursor()
        cur.execute("SELECT tipo FROM registro_usuario WHERE token_cea = %s",(token))
        tipo = cur.fetchone()[0]

        if(tipo==1):
            cur.execute("""SELECT a.num_ad, a.nombres, a.apellidos, a.carnet, a.fecha_nac,a.telf, a.edad,
            a.genero, a.direccion,a.departamento, a.email  FROM personal_administrativo a INNER JOIN registro_usuario U WHERE a.num_ad = U.num_u AND a.estado = 0 AND U.token_cea = %s """, (token))
        elif (tipo==2):
            cur.execute("""SELECT d.num_ad, d.nombres, d.apellidos, d.carnet, d.fecha_nac,d.telf, d.edad,
            d.genero, d.direccion,d.departamento, d.email  FROM docentes d INNER JOIN registro_usuario U WHERE d.num_doc = U.num_u AND d.estado = 0 AND U.token_cea = %s """, (token))
        else:
            cur.execute("""SELECT E.num_es, E.nombres, E.apellidos, E.carnet, E.fecha_nac,E.telf, E.edad,
            E.genero, E.direccion,E.departamento, E.email  FROM estudiante E INNER JOIN registro_usuario U WHERE E.num_es = U.num_u AND E.estado = 0 AND U.token_cea = %s """, (token))
        ade = cur.fetchone()
        cur.close()
        database.close()
        if ade != None:
            estudiante = {'num_u': ade[0], 'nombres': ade[1], 'apellidos': ade[2], 'carnet': ade[3], 'fecha_nac': ade[4],
                          'telf': ade[5], 'edad': ade[6], 'genero': ade[7], 'direccion': ade[8], 'departamento': ade[9], 'email': ade[10]}
            return jsonify(estudiante)
        else:
            return {'error': 1}


