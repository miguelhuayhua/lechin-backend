from flask import Blueprint, request, jsonify
from flask_cors import cross_origin
from routes.coneccion import db
import dateutil.parser as parser

materia = Blueprint('materia', __name__)

@materia.route('/add_materia',methods=['POST'])
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
                    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,0)""",(nombre,url,costo,descripcion,f_inicio,f_final,duracion,hora_inicio,hora_salida))):
            cur.execute('SELECT id_m,nombre,url,costo,descripcion,f_inicio,f_final,duracion,hora_inicio,hora_salida FROM materia WHERE estado = 0 ORDER BY id_m DESC LIMIT 1')
            id_m,nombre,url,costo,descripcion,f_inicio,f_final,duracion,hora_inicio,hora_salida = cur.fetchone()
            cur.close()
            database.commit()
            database.close()
            return jsonify({"id_m":id_m, "nombre":nombre,"url":url, "costo":costo,"descripcion":descripcion,"f_inicio":f_inicio,"f_final":f_final,"duracion":duracion,"hora_inicio":hora_inicio,"hora_salida":hora_salida})
        else:
            database.close()
            return jsonify({"status":0})
                

@materia.route('/update_materia_details',methods=['POST'])
@cross_origin()
def updateMateriaDetails():
    if request.method == 'POST':
        id_m = request.form['id_m']
        num_do = request.form['num_do']
        id_t = request.form['id_t']
        id_turno = request.form['id_turno']
        database = db()
        cur = database.cursor()
        if (cur.execute("""UPDATE materia SET num_do = %s, id_t = %s, id_turno = %s WHERE id_m = %s AND estado = 0""",
                    (num_do,id_t,id_turno,id_m))):
            cur.close()
            database.commit()
            database.close()
            return jsonify({'status':1})
        else:
            return jsonify({'status':0})