from flask import Blueprint, request,jsonify
from flask_cors import cross_origin
from routes.coneccion import db
from routes.encriptar import encript
inscripcion = Blueprint('inscripcion',__name__)

@inscripcion.route('/especialidad',methods=['POST'])        
@cross_origin()
def add_especialidad():
    if request.method == 'POST':
        name_especialidad = request.form['name_especialidad']
        database = db()
        cur = database.cursor()
        if cur.execute("""insert into especialidad(nombre,estado)
                       values(%s,0);""",(name_especialidad,))==True:
            database.commit()
            database.close()
            return ('1')
        else:
            database.close()
            return('0')