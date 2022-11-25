from flask import Blueprint, request,jsonify
from flask_cors import cross_origin
from routes.coneccion import db
modificar = Blueprint('modificar',__name__)
#ACABADO    
@modificar.route('/updateUserEstudent',methods=['POST'])
@cross_origin()
def updateUserEstudent():
     if request.method == 'POST':
        usuario = request.form['usuario']
        password = request.form['password']
        database = db()
        cur = database.cursor()
        cur.execute("""SELECT num_u,usuario,password,token_cea,id_roles,estado FROM registro_usuario WHERE usuario=%s;""",(usuario))
        dato = cur.fetchall()
        cur.execute("""SELECT id_u FROM registro_usuario WHERE usuario=%s;""",(usuario))
        id = cur.fetchall()
        cur.execute("""
            UPDATE registro_usuario
            SET estado =1, fecha_hasta=NOW()
            WHERE id_u = %s and estado = 0;
                """,(id))
        cur.execute("""
                    INSERT INTO registro_usuario(num_u,usuario,password,token_cea,id_roles,estado)
                    VALUES (num_u,%s,%s,token_cea,%s,0)
                    """,(dato[0][0],usuario,password,dato[0][3],dato[0][4]))
        cur.execute("""SELECT id_u FROM registro_usuario WHERE estado=0 and num_u=%s;""",(dato[0][0]))
        id_u = cur.fetchall()
        cur.execute("""
            UPDATE estudiante
            SET id_registro=%s
            WHERE id_registro = %s and estado = 0;
                """,(id_u[0][0]))
        database.commit()
        database.close()
        return jsonify({'status':1})
#ACABADO    
@modificar.route('/updateUserDocente',methods=['POST'])
@cross_origin()
def updateUserDocente():
     if request.method == 'POST':
        usuario = request.form['usuario']
        password = request.form['password']
        database = db()
        cur = database.cursor()
        cur.execute("""SELECT num_u,usuario,password,token_cea,id_roles,estado FROM registro_usuario WHERE usuario=%s;""",(usuario))
        dato = cur.fetchall()
        cur.execute("""SELECT id_u FROM registro_usuario WHERE usuario=%s;""",(usuario))
        id = cur.fetchall()
        cur.execute("""
            UPDATE registro_usuario
            SET estado =1, fecha_hasta=NOW()
            WHERE id_u = %s and estado = 0;
                """,(id))
        cur.execute("""
                    INSERT INTO registro_usuario(num_u,usuario,password,token_cea,id_roles,estado)
                    VALUES (num_u,%s,%s,token_cea,%s,0)
                    """,(dato[0][0],usuario,password,dato[0][3],dato[0][4]))
        cur.execute("""SELECT id_u FROM registro_usuario WHERE estado=0 and num_u=%s;""",(dato[0][0]))
        id_u = cur.fetchall()
        cur.execute("""
            UPDATE docentes
            SET id_registro=%s
            WHERE id_registro = %s and estado = 0;
                """,(id_u[0][0],id))
        database.commit()
        database.close()
        return jsonify({'status':1})
#ACABADO    
@modificar.route('/updateEstudent',methods=['POST'])
@cross_origin()
def updateEstudent():
     if request.method == 'POST':
        iduser = request.form['num_u']
        nombres = request.form['nombres']
        apellidos = request.form['apellidos']
        carnet = request.form['carnet']
        email = request.form['email']
        fecha_nac = request.form['fecha_nac']
        telf = request.form['telf']
        edad = request.form['edad']
        genero = request.form['genero']
        direccion = request.form['direccion']
        departamento = request.form['departamento']
        
        database = db()
        cur = database.cursor()
        cur.execute("""SELECT id_es FROM estudiante WHERE num_es=%s and estado=0;""",(iduser))
        id = cur.fetchall()
        cur.execute("""SELECT id_registro FROM estudiante WHERE num_es=%s and estado=0;""",(iduser))
        idRegistro = cur.fetchall()
        cur.execute("""
            UPDATE estudiante
            SET estado = 1, fecha_hasta = NOW()
            WHERE id_es = %s and estado = 0;
                """,(id))
        cur.execute("""
                    INSERT INTO estudiante(num_es,nombres,apellidos,carnet,email,fecha_nac,telf,edad,genero,direccion,departamento,id_registro,estado)
                    VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,0)
                    """,(iduser,nombres,apellidos,int(carnet),email,fecha_nac,telf,int(edad),genero,direccion,departamento,idRegistro[0][0]))
        cur.execute("""SELECT id_es FROM estudiante WHERE num_es=%s and estado=0;""",(iduser))
        newid = cur.fetchall()
        cur.execute("""
            UPDATE inscripcion
            SET id_estudiante=%s
            WHERE id_estudiante = %s and estado = 0;
                """,(newid[0][0],id))
        cur.execute("""
            UPDATE calificacion
            SET id_estudiante=%s
            WHERE id_estudiante = %s and estado = 0;
                """,(newid[0][0],id))
        database.commit()
        database.close()
        return jsonify({'status':1})
#FALTA 
@modificar.route('/updateAdmin',methods=['POST'])
@cross_origin()
def updateAdmin():
     if request.method == 'POST':
        usuario = request.form['usuario']
        password = request.form['password']
        database = db()
        cur = database.cursor()
        cur.execute("""SELECT num_u,usuario,password,token_cea,id_roles,estado FROM registro_usuario WHERE usuario=%s;""",(usuario))
        dato = cur.fetchall()
        cur.execute("""SELECT id_u FROM registro_usuario WHERE usuario=%s;""",(usuario))
        id = cur.fetchall()
        cur.execute("""
            UPDATE registro_usuario
            SET estado =1, fecha_hasta=NOW()
            WHERE id_u = %s;
                """,(id))
        cur.execute("""
                    INSERT INTO registro_usuario(num_u,usuario,password,token_cea,id_roles,estado)
                    VALUES (num_u,usuario,password,token_cea,%s,0)
                    """,(dato[0][0],usuario,password,dato[0][3],dato[0][4]))
        cur.execute("""SELECT id_u FROM registro_usuario WHERE estado=0 and num_u=%s;""",(dato[0][0]))
        id_u = cur.fetchall()
        cur.execute("""
            UPDATE estudiante
            SET id_registro=%s
            WHERE id_u = %s;
                """,(id_u[0][0]))
        database.commit()
        database.close()
        return jsonify({'status':1})
#FALTA        
@modificar.route('/updateDocente',methods=['POST'])
@cross_origin()
def updateDocente():
     if request.method == 'POST':
        num_dd = request.form['num_dd']
        antiguedad = int(request.form['antiguedad'])
        id_carrera = int(request.form['id_carrera'])
        database = db()
        cur = database.cursor()
        if cur.execute("""INSERT INTO detalle_personal (num_dd,antiguedad,id_carrera) VALUES (%s,%s,%s)""",
                    (num_dd,antiguedad,id_carrera)):
            database.commit()
            cur.execute("""SELECT id_dd FROM detalle_personal WHERE estado = 0 AND num_dd = %s""",
                        (num_dd))
            print(cur.fetchone())
            id_dd = cur.fetchone()[0]
            cur.execute("""UPDATE docentes SET id_detalle = %s WHERE estado = 0 AND num_do = %s""",
                        (id_dd,num_dd ))
            database.commit()
            cur.close()
            database.close()
            return jsonify({"status":1})
        else:
            return jsonify({"status":0})