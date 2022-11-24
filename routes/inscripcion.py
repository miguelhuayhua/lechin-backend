from flask import Blueprint, request,jsonify
from flask_cors import cross_origin
from routes.coneccion import db
from routes.encriptar import encript
inscripcion = Blueprint('inscripcion',__name__)

def idtipo1():
        database = db()
        cur = database.cursor()
        cur.execute("select count(distinct(num_t))+1 from tipo where estado=0;")
        max = cur.fetchall()
        idT='T'+str(max[0][0])
        database.close()
        return(idT)    

def idsemestre1():
        database = db()
        cur = database.cursor()
        cur.execute("select count(distinct(num_u))+1 from semestre where estado=0;")
        max = cur.fetchall()
        print(max)
        idu='S'+str(max[0][0])
        database.close()
        return(idu)    

def idmateria1():
        database = db()
        cur = database.cursor()
        cur.execute("select count(distinct(num_u))+1 from semestre where estado=0;")
        max = cur.fetchall()
        print(max)
        idu='S'+str(max[0][0])
        database.close()
        return(idu)    

def idnum():
    database = db()
    cur = database.cursor()
    cur.execute("select count(distinct(num_i))+1 from inscripcion where estado=0;")
    max = cur.fetchall()
    idI='I'+str(max[0][0])
    database.close()
    return(idI)   

def idCalificacion():
    database = db()
    cur = database.cursor()
    cur.execute("select count(distinct(num_ca))+1 from calificacion where estado=0;")
    max = cur.fetchall()
    idC='C'+str(max[0][0])
    database.close()
    return(idC) 

@inscripcion.route('/add_tipo',methods=['POST'])        
@cross_origin()
def add_tipo():
    if request.method == 'POST':
        area = request.form['area']
        nivel = request.form['nivel']
        especialidad = request.form['especialidad']
        database = db()
        cur = database.cursor()
        idtipo = idtipo1()
        if cur.execute("""insert into tipo(num_t,area,nivel,especialidad,estado)
                       values(num_t,area,nivel,especialidad,estado);""",(idtipo,area,nivel,especialidad))==True:
            database.commit()
            database.close()
            return jsonify({'status':1})
        else:
            return jsonify({'status':0})

@inscripcion.route('/tipos')        
@cross_origin()
def tipos():
    database = db()
    cur = database.cursor()
    if cur.execute("""SELECT id_t, area, nivel FROM tipo WHERE estado = 0""",()):
        tipos = cur.fetchall()
        listaTipos = [{"id_t":tipo[0], "area":tipo[1],"nivel":tipo[2]} for tipo in tipos]
        cur.close()
        database.close()
        return jsonify(listaTipos)
    else:
        return jsonify({"error":1})

@inscripcion.route('/turnos')        
@cross_origin()
def turnos():
    database = db()
    cur = database.cursor()
    if cur.execute("""SELECT id_t, turno, paralelo FROM turno WHERE estado = 0""",()):
        turnos = cur.fetchall()
        listaTurnos = [{"id_t":turno[0], "turno":turno[1],"paralelo":turno[2]} for turno in turnos]
        cur.close()
        database.close()
        return jsonify(listaTurnos)
    else:
        return jsonify({"error":1})

@inscripcion.route('/addTurno',methods=['POST'])        
@cross_origin()
def addTurno():
    if request.method == 'POST':
        nombre = request.form['nombre']
        paralelo = request.form['paralelo']
        database = db()
        cur = database.cursor()

        if cur.execute("""insert into turno(nombre,paralelo)
                       values(%s,%s,0);""",(nombre,paralelo))==True:
            database.commit()
            database.close()
            return jsonify({'status':1})
        else:
            return jsonify({'status':0})

@inscripcion.route('/addInscripcion',methods=['POST'])        
@cross_origin()
def addInscripcion():
    if request.method == 'POST':
        fecha_inscripcion = request.form['fecha_inscripcion']
        costo_total = request.form['costo_total']

        database = db()
        cur = database.cursor()
        num_i = idnum()
        if cur.execute("""insert into inscripcion(num_i,fecha_inscripcion,costo_total,id_turno,id_materia,id_estudiante,id_docente,tipo_inscripcion,estado)
                       values(%s,%s,%s,id_turno,id_materia,id_estudiante,id_docente,tipo_inscripcion,0);""",(num_i,fecha_inscripcion,costo_total,id_turno,id_materia,id_estudiante,id_docente,tipo_inscripcion))==True:
            database.commit()
            database.close()
            return jsonify({'status':1})
        else:
            return jsonify({'status':0})

@inscripcion.route('/addCalificacion',methods=['POST'])        
@cross_origin()
def addCalificacion():
    if request.method == 'POST':
        fecha_calificacion = request.form['fecha_calificacion']
        e1parcial = request.form['e1parcial']
        e2parcial = request.form['e2parcial']
        e3parcial = request.form['e3parcial']
        nota_total = request.form['nota_total']
        promedio_semestre = request.form['promedio_semestre']
        promedio_general = request.form['promedio_general']

        database = db()
        cur = database.cursor()
        num_ca = idCalificacion()
        if cur.execute("""insert into calificacion(num_ca,fecha_calificacion,e1parcial,e2parcial,e3parcial,nota_total,promedio_semestre,promedio_general,estado)
                       values(%s,fecha_calificacion,e1parcial,e2parcial,e3parcial,nota_total,promedio_semestre,promedio_general,0);""",(num_ca,fecha_calificacion,e1parcial,e2parcial,e3parcial,nota_total,promedio_semestre,promedio_general))==True:
            database.commit()
            database.close()
            return jsonify({'status':1})
        else:
            return jsonify({'status':0})
