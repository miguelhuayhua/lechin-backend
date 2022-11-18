from flask import Blueprint, request,jsonify
from flask_cors import cross_origin
from routes.coneccion import db
from routes.encriptar import encript
registro = Blueprint('registro',__name__)

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

@registro.route('/registro_estudiante',methods=['POST'])        
@cross_origin()
def registro_estudiante():
    if request.method == 'POST':
        iduser = request.form['iduser']
        usuario = request.form['usuario']
        clave = request.form['password']
        password = encript(clave)
        token_cea = request.form['token_cea']
        #conneccion
        database = db()
        cur = database.cursor()
        # registrouser
        if cur.execute("""insert into registro_usuario(num_u,usuario,password,token_cea,id_roles,estado) 
                                        values(%s,%s,%s,%s,1,0);""",(iduser,usuario,password,token_cea)) ==True:
            cur.execute("SELECT id_u FROM registro_usuario where estado=0 and num_u=%s;", (iduser,))
            id_registro=cur.fetchall()
            cur.execute("SELECT max(id_es) FROM estudiante where estado=0;")
            id_es=cur.fetchall()
            cur.execute("UPDATE estudiante set id_registro = %s WHERE id_es = %s;", (id_registro,id_es))
            return ('1')
        else:
            return('0')

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
        edad = request.form['edad']
        genero = request.form['genero']
        direccion = request.form['direccion']
        departamento = request.form['departamento']
        
        #conneccion
        database = db()
        cur = database.cursor()
        ides=ides1()
        print(ides)
        if cur.execute("""insert into estudiante(num_es,nombres,apellidos,carnet,email,fecha_nac,telf,edad,genero,direccion,departamento,id_registro,estado)
                                   values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,NULL,0);"""
                                   ,(ides,nombres,apellidos,int(carnet),email,fecha_nac,telf,int(edad),genero,direccion,departamento))==True:
            database.commit()
            database.close()
            idu = idu1()
            return jsonify(idu)
        else:
            database.close()
            return('0')

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
    cur.execute("select count(distinct(num_dd))+1 from detalle_personal where estado=0;")
    max = cur.fetchall()
    idD='DP'+str(max[0][0])
    database.close()
    return(idD)    
      
@registro.route('/registro_docente',methods=['POST'])        
@cross_origin()
def registro_docente():
    if request.method == 'POST':
        iduser = request.form['iduser']
        usuario = request.form['usuario']
        clave = request.form['password']
        password = encript(clave)
        token_cea = request.form['token_cea']
        #conneccion
        database = db()
        cur = database.cursor()
        # registrouser
        if cur.execute("""insert into registro_usuario(num_u,usuario,password,token_cea,id_roles,estado) 
                                        values(%s,%s,%s,%s,1,0);""",(iduser,usuario,password,token_cea)) ==True:
            cur.execute("SELECT id_u FROM registro_usuario where estado=0 and num_u=%s;", (iduser,))
            id_registro=cur.fetchall()
            cur.execute("SELECT max(id_do) FROM docentes where estado=0;")
            id_do=cur.fetchall()
            cur.execute("UPDATE docentes set id_registro = %s WHERE id_do = %s;", (id_registro,id_do))
            return ('1')
        else:
            return('0')

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
                return ('1')
            else:
                return('0')

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
            return ('1')
        else:
            database.close()
            return('0')
    
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
        edad = request.form['edad']
        genero = request.form['genero']
        direccion = request.form['direccion']
        departamento = request.form['departamento']

        #conneccion
        database = db()
        cur = database.cursor()
        idd=idd1()
        if cur.execute("""insert into docentes(num_do,nombres,apellidos,carnet,email,fecha_nac,telf,edad,genero,direccion,departamento,id_registro,id_detalle,id_reportes,estado)
                                   values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,NULL,NULL,NULL,0);"""
                                   ,(idd,nombres,apellidos,int(carnet),email,fecha_nac,telf,int(edad),genero,direccion,departamento))==True:
            database.commit()
            database.close()
            idu = idu1()
            return ({'iduser':idu})
        else:
            database.close()
            return('0')

# -------------- ADMIN ---------------------------------------------------------
def idadm1():
    database = db()
    cur = database.cursor()
    cur.execute("select count(distinct(num_adm))+1 from personal_admininistrativo where estado=0;")
    max = cur.fetchall()
    idadm='AD'+str(max[0][0])
    database.close()
    return(idadm)  

@registro.route('/add_admin',methods=['POST'])
@cross_origin()
def add_admin():
    return('0')