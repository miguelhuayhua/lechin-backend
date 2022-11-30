from flask import Blueprint, request,jsonify
from flask_cors import cross_origin
from routes.coneccion import db
from routes.encriptar import encript
registro = Blueprint('registro',__name__)
        
def ides1():
        database = db()
        cur = database.cursor()
        cur.execute("select count(distinct(num_es))+1 from estudiante")
        max = cur.fetchall()
        ides='E'+str(max[0][0])
        database.close()
        return(ides) 

@registro.route('/registro_usuario',methods=['POST'])        
@cross_origin()
def registro_estudiante():
    if request.method == 'POST':
        iduser = request.form['num_u']
        usuario = request.form['usuario']
        clave = request.form['password']
        password = encript(clave)
        token_cea = request.form['token_cea'],
        tipo= int(request.form['tipo'])
        #conexion
        database = db()
        insertar = database.cursor()
        cur = database.cursor()
        # registrouser
        if insertar.execute("""insert into registro_usuario(num_u,usuario,password,token_cea,tipo) 
                                        values(%s,%s,%s,%s,%s);""",(iduser,usuario,password,token_cea,int(tipo))) ==True:
            cur.execute("SELECT id_u FROM registro_usuario where estado=0 and num_u=%s;", (iduser))
            user = cur.fetchone()
            id_u=user[0]
            if tipo == 3:
                cur.execute("UPDATE estudiante set id_registro = %s WHERE num_es = %s;", (id_u,iduser))
            elif tipo == 2:
                cur.execute("UPDATE docentes set id_registro = %s WHERE num_do = %s;", (id_u,iduser))
            else :
                cur.execute("UPDATE personal_administrativo set id_registro = %s WHERE num_ad = %s;", (id_u,iduser))
            database.commit()
            database.close()
            return jsonify({'status':1})
        else:
            return jsonify({'status':0})

@registro.route('/add_estudiante',methods=['POST'])
@cross_origin()
def add_estudiante():
    if request.method == 'POST':
        nombres = request.form['nombres']
        apellidos = request.form['apellidos']
        carnet = request.form['carnet']
        email = request.form['email']
        fecha_nac = request.form['fecha_nac']
        telf = request.form['telf']
        genero = request.form['genero']
        direccion = request.form['direccion']
        departamento = request.form['departamento']
        
        #conneccion
        database = db()
        cur = database.cursor()
        ides=ides1()
        if cur.execute("""insert into estudiante(num_es,nombres,apellidos,carnet,email,fecha_nac,telf,edad,genero,direccion,departamento,id_registro,estado)
                                   values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,NULL,0);"""
                                   ,(ides,nombres,apellidos,int(carnet),email,fecha_nac,telf,22,genero,direccion,departamento))==True:
            database.commit()
            database.close()
            return jsonify({'id':ides})
        else:
            database.close()
            return jsonify({'error':1})
#=====AREA DOCENTE Y ADMIN=======================================================================================#    
def iddo1():
        database = db()
        cur = database.cursor()
        cur.execute("select count(distinct(num_do))+1 from registro_usuario where estado=0;")
        max = cur.fetchall()
        iddo='D'+str(max[0][0])
        database.close()
        return(iddo)  

def idesp1(especiality):
    database = db()
    cur = database.cursor()
    cur.execute("select id_e from especialidad where estado=0 and nombre=%s;",(especiality,))
    max = cur.fetchall()
    if max[0][0]!=None:
        ide = max[0][0]
        database.close()
        return(ide)  
    else:
        return(None)
    
def idd1():
    database = db()
    cur = database.cursor()
    cur.execute("select count(distinct(num_do))+1 from docentes")
    max = cur.fetchall()
    idD='DP'+str(max[0][0])
    database.close()
    return(idD)    
      
@registro.route('/detalle_doc',methods=['POST'])        
@cross_origin()
def detalle_doc():
    if request.method == 'POST':
        curriculum = request.form['curriculum']
        academia_pertenece = request.form['academia_pertenece']
        fecha_antiguedad = request.form['fecha_antiguedad']
        
        name_especialidad = request.form['name_especialidad']
        id_especialidad = idesp1(name_especialidad)
        if id_especialidad != None:
        #conneccion
            database = db()
            cur = database.cursor()
            #detalle_user
            idd = idd1()
            if cur.execute("""insert into detalle_personal(num_dd,curriculum,academia_pertenece,fecha_antiguedad,id_especialidad,estado) 
                                        values(%s,%s,%s,%s,%s,0);""",(idd,curriculum,academia_pertenece,fecha_antiguedad,id_especialidad)) == True:                    
                cur.execute("SELECT id_dd FROM detalle_personal where estado=0 and num_u=%s;", (idd,))
                id_detalle=cur.fetchall()
                cur.execute("SELECT max(id_do) FROM docentes where estado=0;")
                id_do=cur.fetchall()
                cur.execute("UPDATE docentes set id_detalle = %s WHERE id_do = %s;", (id_detalle,id_do))
                return jsonify({'status':1})
            else:
                return jsonify({'status':0})
        else:
            return('Especialidad no existe, registre su especialidad al DB')

@registro.route('/especialidad',methods=['POST'])        
@cross_origin()
def especialidad():
    if request.method == 'POST':
        name_especialidad = request.form['name_especialidad']
        database = db()
        cur = database.cursor()
        if cur.execute("""insert into especialidad(nombre,estado)values(%s,0);""",(name_especialidad,))==True:
            database.commit()
            database.close()
            return jsonify({'status':1})
        else:
            return jsonify({'status':0})
    
@registro.route('/add_docente',methods=['POST'])
@cross_origin()
def add_docente():
    if request.method == 'POST':
        nombres = request.form['nombres']
        apellidos = request.form['apellidos']
        carnet = request.form['carnet']
        email = request.form['email']
        fecha_nac = request.form['fecha_nac']
        telf = request.form['telf']
        genero = request.form['genero']
        direccion = request.form['direccion']
        departamento = request.form['departamento']

        #conexion
        database = db()
        cur = database.cursor()
        idd=idd1()
        if cur.execute("""insert into docentes(num_do,nombres,apellidos,carnet,email,fecha_nac,telf,edad,genero,direccion,departamento,id_registro,id_detalle,id_reportes,estado)
                                   values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,NULL,NULL,NULL,0);"""
                                   ,(idd,nombres,apellidos,int(carnet),email,fecha_nac,telf,22,genero,direccion,departamento))==True:
            database.commit()
            database.close()
            return jsonify({'id':idd})
        else:
            database.close()
            return jsonify({'error':1})

# -------------- ADMIN ---------------------------------------------------------
def idadm1():
    database = db()
    cur = database.cursor()
    cur.execute("select count(distinct(num_ad))+1 from personal_administrativo where estado=0;")
    max = cur.fetchall()
    idadm='AD'+str(max[0][0])
    database.close()
    return(idadm)  

@registro.route('/detalle_admin',methods=['POST'])        
@cross_origin()
def detalle_admin():
    if request.method == 'POST':
        curriculum = request.form['curriculum']
        academia_pertenece = request.form['academia_pertenece']
        fecha_antiguedad = request.form['fecha_antiguedad']
        
        name_especialidad = request.form['name_especialidad']
        id_especialidad = idesp1(name_especialidad)
        if id_especialidad != None:
        #conneccion
            database = db()
            cur = database.cursor()
            #detalle_user
            idd = idd1()
            if cur.execute("""insert into detalle_personal(num_dd,curriculum,academia_pertenece,fecha_antiguedad,id_especialidad,estado) 
                                        values(%s,%s,%s,%s,%s,0);""",(idd,curriculum,academia_pertenece,fecha_antiguedad,id_especialidad)) == True:                    
                cur.execute("SELECT id_dd FROM detalle_personal where estado=0 and num_u=%s;", (idd,))
                id_detalle=cur.fetchall()
                cur.execute("SELECT max(id_ad) FROM personal_administrativo where estado=0;")
                id_adm=cur.fetchall()
                cur.execute("UPDATE personal_administrativo set id_detalle = %s WHERE id_ad = %s;", (id_detalle,id_adm))
                return jsonify({'status':1})
            else:
                return jsonify({'status':0})
        else:
            return('Especialidad no existe, registre su especialidad al DB')

@registro.route('/add_administrativo',methods=['POST'])
@cross_origin()
def add_administrativo():
    if request.method == 'POST':
        nombres = request.form['nombres']
        apellidos = request.form['apellidos']
        carnet = request.form['carnet']
        email = request.form['email']
        fecha_nac = request.form['fecha_nac']
        telf = request.form['telf']
        genero = request.form['genero']
        direccion = request.form['direccion']
        departamento = request.form['departamento']

        #conexion
        database = db()
        cur = database.cursor()
        idd=idadm1()
        if cur.execute("""insert into personal_administrativo(num_ad,nombres,apellidos,carnet,email,fecha_nac,telf,edad,genero,direccion,departamento,id_registro,id_detalle,id_reportes,estado)
                                   values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,NULL,NULL,NULL,0);"""
                                   ,(idd,nombres,apellidos,int(carnet),email,fecha_nac,telf,22,genero,direccion,departamento)):
            database.commit()
            database.close()
            return jsonify({'id':idd})
        else:
            database.close()
            return jsonify({'error':1})

#CONFIRM DATA USER

