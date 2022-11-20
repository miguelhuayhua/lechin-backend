from flask import Blueprint, request,jsonify
from flask_cors import cross_origin
from routes.coneccion import db
from routes.encriptar import encript
eliminar = Blueprint('eliminar',__name__)

@eliminar.route('/deleteEstudent',methods=['POST'])
@cross_origin()
def deleteEstudent():
     if request.method == 'POST':
        iduser = request.form['num_u']
        carnet = request.form['carnet']
        
        database = db()
        cur = database.cursor()
        cur.execute("""SELECT id_es FROM estudiante WHERE estado=0 and num_es=%s or carnet=%s;""",(iduser,carnet))
        ides = cur.fetchall()
        cur.execute("""SELECT id_registro FROM estudiante WHERE num_es=%s and estado=0;""",(iduser))
        idRegistro = cur.fetchall()
        cur.execute("""SELECT id_u FROM registro_usuario WHERE num_u=%s and estado=0;""",(idRegistro))
        idu = cur.fetchall()
        cur.execute("""
            UPDATE estudiante
            SET estado = 1, fecha_hasta = NOW()
            WHERE id_es = %s and estado = 0;
                """,(ides))
        cur.execute("""
            UPDATE registro_usuario
            SET estado = 1, fecha_hasta = NOW()
            WHERE id_u = %s and estado = 0;
                """,(idu))
        database.commit()
        database.close()
        return jsonify({'status':1})
#FALTA 
@eliminar.route('/deleteDocente',methods=['POST'])
@cross_origin()
def deleteDocente():
     if request.method == 'POST':
        iduser = request.form['num_u']
        carnet = request.form['carnet']
        
        database = db()
        cur = database.cursor()
        cur.execute("""SELECT id_do FROM decentes WHERE estado=0 and num_do=%s or carnet=%s;""",(iduser,carnet))
        iddo = cur.fetchall()
        cur.execute("""SELECT id_registro FROM decentes WHERE num_es=%s and estado=0;""",(iduser))
        idRegistro = cur.fetchall()
        cur.execute("""SELECT id_u FROM registro_usuario WHERE num_u=%s and estado=0;""",(idRegistro))
        idu = cur.fetchall()
        cur.execute("""
            UPDATE decentes
            SET estado = 1, fecha_hasta = NOW()
            WHERE id_do = %s and estado = 0;
                """,(iddo))
        cur.execute("""
            UPDATE registro_usuario
            SET estado = 1, fecha_hasta = NOW()
            WHERE id_u = %s and estado = 0;
                """,(idu))
        database.commit()
        database.close()
        return jsonify({'status':1})

@eliminar.route('/deleteMateria',methods=['POST'])
@cross_origin()
def deleteMateria():
     if request.method == 'POST':
        idm = request.form['id_m']
        
        database = db()
        cur = database.cursor()
        cur.execute("""SELECT id_m FROM materia WHERE estado=0 and num_m=%s;""",(idm))
        idmat = cur.fetchall()
        cur.execute("""
            UPDATE materia
            SET estado = 1, fecha_hasta = NOW()
            WHERE id_m = %s and estado = 0;
                """,(idmat))
        database.commit()
        database.close()
        return jsonify({'status':1})

@eliminar.route('/deleteEspeciality',methods=['POST'])
@cross_origin()
def deleteEspeciality():
     if request.method == 'POST':
        ides = request.form['id_es']
        
        database = db()
        cur = database.cursor()
        cur.execute("""SELECT id_e FROM especialidad WHERE estado=0 and num_e=%s;""",(ides))
        id = cur.fetchall()
        cur.execute("""
            UPDATE especialidad
            SET estado = 1, fecha_hasta = NOW()
            WHERE id_e = %s and estado = 0;
                """,(id))
        database.commit()
        database.close()
        return jsonify({'status':1})

@eliminar.route('/deleteReportes',methods=['POST'])
@cross_origin()
def deleteReportes():
     if request.method == 'POST':
        idr = request.form['id_rep']
        
        database = db()
        cur = database.cursor()
        cur.execute("""SELECT id_r FROM reportes WHERE estado=0 and num_r=%s;""",(idr))
        id = cur.fetchall()
        cur.execute("""
            UPDATE reportes
            SET estado = 1, fecha_hasta = NOW()
            WHERE id_r = %s and estado = 0;
                """,(id))
        database.commit()
        database.close()
        return jsonify({'status':1})
