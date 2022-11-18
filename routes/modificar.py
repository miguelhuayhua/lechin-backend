from flask import Blueprint, request,jsonify
from flask_cors import cross_origin
from routes.coneccion import db
modificar = Blueprint('modificar',__name__)

@modificar.route('/update_estudiante/<id>',methods=['POST'])
def update_estudiante(id):
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
        return ('1')
    
@modificar.route('/update_docente/<id>',methods=['POST'])
def update_docente(id):
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
        return ('1')
    
@modificar.route('/update_admin/<id>',methods=['POST'])
def update_admin(id):
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
        return ('1')