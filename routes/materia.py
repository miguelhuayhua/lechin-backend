from flask import Blueprint, request, jsonify
from flask_cors import cross_origin
from routes.coneccion import db
import dateutil.parser as parser

materia = Blueprint('materia', __name__)


@materia.route('/add_materia', methods=['POST'])
@cross_origin()
def addMateria():
    if request.method == 'POST':
        nombre = request.form['nombre']
        url = request.form['url']
        costo = request.form['costo']
        descripcion = request.form['descripcion']
        f_inicio = parser.parse(request.form['f_inicio'])
        f_final = parser.parse(request.form['f_final'])
        duracion = request.form['duracion']
        hora_inicio = request.form['hora_inicio']
        hora_salida = request.form['hora_salida']
        database = db()
        cur = database.cursor()
        if (cur.execute("""INSERT INTO materia(nombre,url,costo,descripcion,f_inicio,f_final,duracion,hora_inicio,hora_salida,estado)
                    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,0)""", (nombre, url, costo, descripcion, f_inicio, f_final, duracion, hora_inicio, hora_salida))):
            cur.execute(
                'SELECT id_m,nombre,url,costo,descripcion,f_inicio,f_final,duracion,hora_inicio,hora_salida FROM materia WHERE estado = 0 ORDER BY id_m DESC LIMIT 1')
            id_m, nombre, url, costo, descripcion, f_inicio, f_final, duracion, hora_inicio, hora_salida = cur.fetchone()
            cur.close()
            database.commit()
            database.close()
            return jsonify({"id_m": id_m, "nombre": nombre, "url": url, "costo": costo, "descripcion": descripcion, "f_inicio": f_inicio, "f_final": f_final, "duracion": duracion, "hora_inicio": hora_inicio, "hora_salida": hora_salida})
        else:
            database.close()
            return jsonify({"status": 0})


@materia.route('/updateMateria', methods=['POST'])
@cross_origin()
def updateMateria():
    if request.method == 'POST':
        id_m = request.form['id_m']
        nombre = request.form['nombre']
        url = request.form['url']
        costo = request.form['costo']
        descripcion = request.form['descripcion']
        f_inicio = parser.parse(request.form['f_inicio'])
        f_final = parser.parse(request.form['f_final'])
        duracion = request.form['duracion']
        hora_inicio = request.form['hora_inicio']
        hora_salida = request.form['hora_salida']
        database = db()
        cur = database.cursor()
        if cur.execute("""UPDATE materia SET nombre = %s, url = %s, costo = %s,
                    descripcion = %s, f_inicio = %s, duracion = %s, hora_inicio = %s, hora_salida = %s,
                    f_final = %s WHERE estado = 0 AND id_m = %s""", (nombre, url, costo, descripcion, f_inicio, duracion, hora_inicio, hora_salida, f_final, id_m)):
            database.commit()
            cur.close()
            database.close()
            return jsonify({'status': 1})
        else:
            database.close()
            return jsonify({'status': 0})


@materia.route('/getEstudiantesMateria', methods=['POST'])
@cross_origin()
def getEstudiantesMateria():
    if request.method == 'POST':
        id_m = request.form['id_m']
        database = db()
        cur = database.cursor()
        if cur.execute("""SELECT
	e.nombres,e.apellidos,e.carnet,e.email,e.fecha_nac, e.telf, e.edad,e.genero,e.direccion, e.departamento, e.num_es FROM
	materia m INNER JOIN detalle_inscripcion dt ON (dt.id_m = m.id_m)
              INNER JOIN inscripcion i ON (dt.id_i = i.id_i) 
              INNER JOIN estudiante e ON (e.num_es = i.num_es) WHERE m.id_m = %s;""", (id_m)):
            estudiantes = cur.fetchall()
            listaEstudiantes = [{'nombres': est[0], 'apellidos':est[1], 'carnet':est[2], 'email':est[3], 'fecha_nac':est[4], 'telf':est[5], 'edad':est[6], 'genero':est[7], 'direccion':est[8], 'departamento':est[9], 'num_u':est[10]}
                                for est in estudiantes]
            cur.close()
            database.close()
            return jsonify(listaEstudiantes)
        else:
            return jsonify([])

@materia.route('/getMateriasADE', methods=['POST'])
@cross_origin()
def getMateriasEstudiante():
    if request.method == 'POST':
        num_u = request.form['num_u']
        database = db()
        cur = database.cursor()
        if cur.execute("""SELECT
	m.id_m, m.nombre, m.url, m.costo, m.descripcion, m.num_do, m.id_t, m.id_turno, m.f_inicio, m.duracion, 
	m.hora_inicio, m.hora_salida, m.f_final FROM materia m INNER JOIN detalle_inscripcion di ON (m.id_m = di.id_m) INNER JOIN inscripcion i ON (di.id_i = i.id_i) 
INNER JOIN estudiante e ON (i.num_es = e.num_es) WHERE e.num_es = %s""", (num_u)):
            materias = cur.fetchall()
            listaMaterias = [{'id_m': mat[0], 'nombre':mat[1], 'url':mat[2], 'costo':mat[3], 'descripcion':mat[4], 'num_do':mat[5],
                              'id_t':mat[6], 'id_turno':mat[7], 'f_inicio':mat[8], 'duracion':mat[9], 'hora_inicio':mat[10], 'hora_salida':mat[11],
                              'f_final':mat[12]}
                                for mat in materias]
            cur.close()
            database.close()
            return jsonify(listaMaterias)
        else:
            database.close()
            return jsonify([])

@materia.route('/getDocenteMateria', methods=['POST'])
@cross_origin()
def getDocenteMateria():
    if request.method == 'POST':
        id_m = request.form['id_m']
        database = db()
        cur = database.cursor()
        if cur.execute("""SELECT d.num_do, d.nombres, d.apellidos, d.carnet, d.fecha_nac,d.telf, d.edad,
        d.genero, d.direccion,d.departamento, d.email FROM docentes d INNER JOIN materia m ON (m.num_do = d.num_do) WHERE m.id_m = %s""", (id_m)):
            doc = cur.fetchone()
            cur.close()
            database.close()
            if doc != None:
                docente = {'num_u': doc[0], 'nombres': doc[1], 'apellidos': doc[2], 'carnet': doc[3], 'fecha_nac': doc[4],
                          'telf': doc[5], 'edad': doc[6], 'genero': doc[7], 'direccion': doc[8], 'departamento': doc[9], 'email': doc[10]}
                return jsonify(docente)
            else:
                return jsonify({'status':0})
        else:
            database.close()
            return jsonify({'status':0})