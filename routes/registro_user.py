from flask import Blueprint, request,jsonify
from flask_cors import cross_origin
from routes.coneccion import db
from routes.encriptar import encript
insercion = Blueprint('insercion',__name__)

def idu1():
        database = db()
        cur = database.cursor()
        cur.execute("select count(distinct(num_u))+1 from registro_usuario where estado=0;")
        max = cur.fetchall()
        print(max)
        idu='U'+str(max[0][0])
        database.close()
        return(idu)    
        
def ides1():
        database = db()
        cur = database.cursor()
        cur.execute("select count(distinct(num_es))+1 from estudiante where estado=0;")
        max = cur.fetchall()
        ides='E'+str(max[0][0])
        database.close()
        return(ides) 

@insercion.route('/add_registro',methods=['POST'])        
@cross_origin()
def add_user():
    if request.method == 'POST':
        usuario = request.form['usuario']
        clave = request.form['password']
        password = encript(clave)
        token_cea = request.form['token_cea']
        #conneccion
        database = db()
        cur = database.cursor()
        # registrouser
        idu = idu1()
        if cur.execute("""insert into registro_usuario(num_u,usuario,password,token_cea,id_roles,estado) 
                                        values(%s,%s,%s,%s,1,0);""",(idu,usuario,password,token_cea)) ==True:
            return ('1')
        else:
            return('0')

@insercion.route('/add_estudiante',methods=['POST'])
@cross_origin()
def add_estudiante():
    if request.method == 'POST':
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
        
        #conneccion
        database = db()
        cur = database.cursor()
        #estudiante//
        idu=idu1()
        cur.execute("SELECT id_u FROM registro_usuario where estado=0 and num_u=%s;", (idu,))
        id_registro=cur.fetchall()
        ides=ides1()
        print(ides)
        if cur.execute("""insert into estudiante(num_es,nombres,apellidos,carnet,email,fecha_nac,telf,edad,genero,direccion,departamento,id_registro,estado)
                                   values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,0);"""
                                   ,(ides,nombres,apellidos,int(carnet),email,fecha_nac,telf,int(edad),genero,direccion,departamento,id_registro[0][0]))==True:
            database.commit()
            database.close()
            return ('1')
        else:
            database.close()
            return('0')

#=====AREA DOCENTE Y ADMIN=======================================================================================#    

@insercion.route('/especialidad',methods=['POST'])        
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
        return('ERROR')
    
def idd1():
    database = db()
    cur = database.cursor()
    cur.execute("select count(distinct(num_dd))+1 from detalle_personal where estado=0;")
    max = cur.fetchall()
    idD='DP'+str(max[0][0])
    database.close()
    return(idD)    
        
@insercion.route('/add_docente',methods=['POST'])
@cross_origin()
def add_docente():
    if request.method == 'POST':
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
        
        usuario = request.form['usuario']
        clave = request.form['password']
        password = encript(clave)
        token_cea = request.form['token_cea']
        
        curriculum = request.form['curriculum']
        academia_pertenece = request.form['academia_pertenece']
        fecha_antiguedad = request.form['fecha_antiguedad']
        
        name_especialidad = request.form['name_especialidad']
        id_especialidad = ides1(name_especialidad)

        #conneccion
        database = db()
        cur = database.cursor()
        #registro user
        idu=idu1()
        cur.execute("""insert into registro_usuario(num_u,usuario,password,token_cea,id_roles,estado) 
                                        values(%s,%s,%s,%s,2,0);""",(idu,usuario,password,token_cea))
        #detalle_user
        idd = idd1()
        cur.execute("""insert into detalle_personal(num_dd,curriculum,academia_pertenece,fecha_antiguedad,id_especialidad,estado) 
                                        values(%s,%s,%s,%s,%s,0);""",(idd,curriculum,academia_pertenece,fecha_antiguedad,id_especialidad))
        #estudiante//
        cur.execute("SELECT id_u FROM registro_usuario where estado=0 and num_u=%s;", (idu,))
        id_registro=cur.fetchall()
        cur.execute("SELECT id_dd FROM detalle_personal where estado=0 and num_dd=%s;", (idd,))
        id_detalle=cur.fetchall()
        ides=ides1()
        if cur.execute("""insert into docentes(num_do,nombres,apellidos,carnet,email,fecha_nac,telf,edad,genero,direccion,departamento,id_registro,id_detalle,id_reportes,estado)
                                   values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,NULL,0);"""
                                   ,(ides,nombres,apellidos,int(carnet),email,fecha_nac,telf,int(edad),genero,direccion,departamento,id_registro[0][0],id_detalle[0][0]))==True:
            database.commit()
            database.close()
            return ('1')
        else:
            database.close()
            return('0')

def idadm1():
    database = db()
    cur = database.cursor()
    cur.execute("select count(distinct(num_adm))+1 from personal_admininistrativo where estado=0;")
    max = cur.fetchall()
    idadm='AD'+str(max[0][0])
    database.close()
    return(idadm)  

@insercion.route('/add_admin',methods=['POST'])
@cross_origin()
def add_admin():
    if request.method == 'POST':
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
        
        usuario = request.form['usuario']
        clave = request.form['password']
        password = encript(clave)
        token_cea = request.form['token_cea']
        
        curriculum = request.form['curriculum']
        academia_pertenece = request.form['academia_pertenece']
        fecha_antiguedad = request.form['fecha_antiguedad']
        
        name_especialidad = request.form['name_especialidad']
        id_especialidad = ides1(name_especialidad)

        #conneccion
        database = db()
        cur = database.cursor()
        #registro user
        idu=idu1()
        cur.execute("""insert into registro_usuario(num_u,usuario,password,token_cea,id_roles,estado) 
                                        values(%s,%s,%s,%s,3,0);""",(idu,usuario,password,token_cea))
        #detalle_user
        idd = idd1()
        cur.execute("""insert into detalle_personal(num_dd,curriculum,academia_pertenece,fecha_antiguedad,id_especialidad,estado) 
                                        values(%s,%s,%s,%s,%s,0);""",(idd,curriculum,academia_pertenece,fecha_antiguedad,id_especialidad))
        #estudiante//
        cur.execute("SELECT id_u FROM registro_usuario where estado=0 and num_u=%s;", (idu,))
        id_registro=cur.fetchall()
        cur.execute("SELECT id_dd FROM detalle_personal where estado=0 and num_dd=%s;", (idd,))
        id_detalle=cur.fetchall()
        idadm=idadm1()
        if cur.execute("""insert into personal_administrativo(num_do,nombres,apellidos,carnet,email,fecha_nac,telf,edad,genero,direccion,departamento,id_registro,id_detalle,id_reportes,estado)
                                   values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,NULL,0);"""
                                   ,(idadm,nombres,apellidos,int(carnet),email,fecha_nac,telf,int(edad),genero,direccion,departamento,id_registro[0][0],id_detalle[0][0]))==True:
            database.commit()
            database.close()
            return ('1')
        else:
            database.close()
            return('0')