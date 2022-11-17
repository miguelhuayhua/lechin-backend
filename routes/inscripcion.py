from flask import Blueprint, request,jsonify
from flask_cors import cross_origin
from routes.coneccion import db
from routes.encriptar import encript
inscripcion = Blueprint('inscripcion',__name__)

def idtipo1():
        database = db()
        cur = database.cursor()
        cur.execute("select count(distinct(num_u))+1 from tipo where estado=0;")
        max = cur.fetchall()
        idT='T'+str(max[0][0])
        database.close()
        return(idT)    

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
            return ('1')
        else:
            database.close()
            return('0')

@inscripcion.route('/add_semestre',methods=['POST'])        
@cross_origin()
def add_semestre():
    if request.method == 'POST':
        area = request.form['nombre']
        database = db()
        cur = database.cursor()
        if cur.execute("""insert into semestre(nombre,estado)
                       values(%s,estado));""",(area,))==True:
            database.commit()
            database.close()
            cur.execute("""select max(id_s) from semestre where estado=0 and nombre=%s;""",(area,))
            ids = cur.fetchall()
            return jsonify({'idsemestre':ids})
        else:
            database.close()
            return('0')

@inscripcion.route('/add_materia',methods=['POST'])        
@cross_origin()
def add_materia():
    if request.method == 'POST':
        nombre = request.form['nombre']
        url = request.form['url']
        grado = request.form['grado']
        costo = request.form['costo']
        idsemestre = request.form['idsemestre']
        database = db()
        cur = database.cursor()
        if cur.execute("""insert into materia(nombre,url,grado,costo,id_semestre,estado)
                       values(%s,%s,%s,%s,%s,0));""",(nombre,url,grado,costo,idsemestre[0][0]))==True:
            database.commit()
            database.close()
            return ('1')
        else:
            database.close()
            return('0')


