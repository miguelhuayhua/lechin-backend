from flask import Blueprint, request,jsonify
from flask_cors import cross_origin
from routes.coneccion import db
adicionar = Blueprint('adicionar',__name__)
db = db()

    #creamos ruta(registramos al usuario)
@adicionar.route('/add_materia',methods=['POST'])
def add_materia():
    if request.method == 'POST':
        nombre = request.form['nombre']
        grado = request.form['grado']
        #cursor es para manejar nuestra coneccion
        cur = db.cursor()
        if cur.execute('select * from materia where nombre=%s and grado=%s and estado=0;',(nombre,grado))!=True:
            cur.execute("""INSERT INTO materia(nombre,grado,estado) 
                                    VALUES(%s,%s,0);""",(nombre,grado))
            db.commit()
            return('Nueva Materia insertada')
        else:
            return('Ya existe materia')
#============================================================================================#
#add_pais_dep