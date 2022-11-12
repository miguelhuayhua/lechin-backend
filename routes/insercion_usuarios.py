from flask import Blueprint, request,jsonify
from flask_cors import cross_origin
from routes.coneccion import db
insercion = Blueprint('insercion',__name__)
db = db()

def idl1():
        cur = db.cursor()
        cur.execute("select max(substring(num_l,2)) from login;")
        max = cur.fetchall()
        idl='L'+str(int(max[0][0])+1)
        return(idl)
def idu1():
        cur = db.cursor()
        cur.execute("select max(substring(num_u,2)) from registro_usuario;")
        max = cur.fetchall()
        idu='U'+str(int(max[0][0])+1)
        return(idu)    
def idde1():
        cur = db.cursor()
        cur.execute("select max(substring(num_de,4)) from departamento;")
        max = cur.fetchall()
        idde='DE '+str(int(max[0][0])+1)
        return(idde) 
def idpa1():
        cur = db.cursor()
        cur.execute("select max(substring(num_pa,4)) from pais;")
        max = cur.fetchall()
        idpa='PA '+str(int(max[0][0])+1)
        return(idpa)  
def ides1():
        cur = db.cursor()
        cur.execute("select max(substring(num_es,2)) from estudiante;")
        max = cur.fetchall()
        ides='E'+str(int(max[0][0])+1)
        return(ides)  
    
@insercion.route('/insertar e',methods=['POST'])
def insertar_estudiante():
    if request.method == 'POST':
        nombres = request.form['nombres']
        apellidos = request.form['apellidos']
        carnet = request.form['carnet']
        email = request.form['email']
        telf = request.form['telf']
        edad = request.form['edad']
        genero = request.form['genero']
        foto = request.form['foto']
        direccion = request.form['direccion']
        
        departamento = request.form['departamento']
        pais = request.form['pais']
        
        usuario = request.form['usuario']
        password = request.form['password']
        token_cea = request.form['token_cea']
        
# img=open(foto,'rb').read()
# print(img)
        #conneccion
        cur = db.cursor()
        idl = idl1()
        #login
        cur.execute("""INSERT INTO login(num_l,usuario,password,token_cea,estado) 
                                    values(%s,%s,%s,%s,0);""",(idl,usuario,password,token_cea))
        #register user
        cur.execute("SELECT id_l FROM login where num_l=%s;", (idl,))
        id_login=cur.fetchall()
        idu = idu1()
        cur.execute("""insert into registro_usuario(num_u,id_login,id_roles,estado) 
                                        values(%s,%s,1,0);""",(idu,id_login[0][0]))
        #   department
        idde = idde1()
        cur.execute("""insert into departamento(num_de,nombre,estado) 
                                        values(%s,%s,0);""",(idde,departamento))
        #   state
        idpa = idpa1()
        cur.execute("""insert into pais(num_pa,nombre,estado)
                                        values(%s,%s,0);""",(idpa,pais))
        #   empleado
        cur.execute("SELECT max(id_pa) FROM pais where num_pa=%s;", (idpa,))
        id_pais=cur.fetchall() 
        print(id_pais)
        cur.execute("SELECT max(id_de) FROM departamento where num_de=%s;", (idde,))
        id_departamento=cur.fetchall()
        print(id_departamento)
        cur.execute("SELECT max(id_u) FROM registro_usuario where num_u=%s;", (idu,))
        id_registro=cur.fetchall()
        print(id_registro)
        ides=idde1()
        print(ides)
        cur.execute("""insert into estudiante(num_es,nombres,apellidos,carnet,email,telf,edad,genero,foto,direccion,id_pais,id_departamento,id_registro,estado)
                                   values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,0);"""
                                   ,(ides,nombres,apellidos,int(carnet),email,telf,int(edad),genero,foto,direccion,id_pais[0][0],id_departamento[0][0],id_registro[0][0]))
        db.commit()
        return ('INsercion con exito estudiantes')

#============================================================================================#    

def iddo1():
        cur = db.cursor()
        cur.execute("select max(substring(num_do,2)) from docentes;")
        max = cur.fetchall()
        iddo='D'+str(int(max[0][0])+1)
        return(iddo)  

@insercion.route('/insertar d',methods=['POST'])
def insertar_docente():
    if request.method == 'POST':
        nombres = request.form['nombres']
        apellidos = request.form['apellidos']
        carnet = request.form['carnet']
        email = request.form['email']
        telf = request.form['telf']
        edad = request.form['edad']
        genero = request.form['genero']
        foto = request.form['foto']
        direccion = request.form['direccion']
        
        departamento = request.form['departamento']
        pais = request.form['pais']
        
        usuario = request.form['usuario']
        password = request.form['password']
        token_cea = request.form['token_cea']   
# img=open(foto,'rb').read()
# print(img)
        cur = db.cursor()
        #   login
        idl = idl1()
        cur.execute("""INSERT INTO login(num_l,usuario,password,token_cea,estado) 
                                    values(%s,%s,%s,%s,0);""",(idl,usuario,password,token_cea))
        # registrouser
        cur.execute("SELECT id_l FROM login where num_l=%s;", (idl,))
        id_login=cur.fetchall()
        idu = idu1()
        cur.execute("""insert into registro_usuario(num_u,id_login,id_roles,estado) 
                                        values(%s,%s,1,0);""",(idu,id_login[0][0]))
        #   department
        idde = idde1()
        cur.execute("""insert into departamento(num_de,nombre,estado) 
                                        values(%s,%s,0);""",(idde,departamento))
        #   state
        idpa = idpa1()
        cur.execute("""insert into pais(num_pa,nombre,estado)
                                        values(%s,%s,0);""",(idpa,pais))
        #   empleado//insert into DOCENTES(num_do,nombres,apellidos,carnet,email,telf,edad,genero,foto,direccion,id_pais,id_departamento,id_registro,estado) 
				#values('D10','CARLOS','GUTIERRES',9910926,'@gmail.com','73503177',24,'MASCULINO',NULL,'ZONA MARISCAL',1,1,1,0);
        cur.execute("SELECT max(id_pa) FROM pais where num_pa=%s;", (idpa,))
        id_pais=cur.fetchall() 
        print(id_pais)
        cur.execute("SELECT max(id_de) FROM departamento where num_de=%s;", (idde,))
        id_departamento=cur.fetchall()
        print(id_departamento)
        cur.execute("SELECT max(id_u) FROM registro_usuario where num_u=%s;", (idu,))
        id_registro=cur.fetchall()
        print(id_registro)
        iddo=iddo1()
        cur.execute("""insert into DOCENTES(num_do,nombres,apellidos,carnet,email,telf,edad,genero,foto,direccion,id_pais,id_departamento,id_registro,estado)
                                   values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,0);"""
                                   ,(iddo,nombres,apellidos,int(carnet),email,telf,int(edad),genero,foto,direccion,id_pais[0][0],id_departamento[0][0],id_registro[0][0]))
        db.commit()
        return ('INsercion con exito docentes')

def idadm1():
        cur = db.cursor()
        cur.execute("select max(substring(num_adm,2)) from personal_admininistrativo;")
        max = cur.fetchall()
        idadm='D'+str(int(max[0][0])+1)
        return(idadm)  

@insercion.route('/insertar d',methods=['POST'])
def insertar_docente():
    if request.method == 'POST':
        nombres = request.form['nombres']
        apellidos = request.form['apellidos']
        carnet = request.form['carnet']
        email = request.form['email']
        telf = request.form['telf']
        edad = request.form['edad']
        genero = request.form['genero']
        foto = request.form['foto']
        direccion = request.form['direccion']
        
        departamento = request.form['departamento']
        pais = request.form['pais']
        
        usuario = request.form['usuario']
        password = request.form['password']
        token_cea = request.form['token_cea']   
# img=open(foto,'rb').read()
# print(img)
        cur = db.cursor()
        #   login
        idl = idl1()
        cur.execute("""INSERT INTO login(num_l,usuario,password,token_cea,estado) 
                                    values(%s,%s,%s,%s,0);""",(idl,usuario,password,token_cea))
        # registrouser
        cur.execute("SELECT id_l FROM login where num_l=%s;", (idl,))
        id_login=cur.fetchall()
        idu = idu1()
        cur.execute("""insert into registro_usuario(num_u,id_login,id_roles,estado) 
                                        values(%s,%s,1,0);""",(idu,id_login[0][0]))
        #   department
        idde = idde1()
        cur.execute("""insert into departamento(num_de,nombre,estado) 
                                        values(%s,%s,0);""",(idde,departamento))
        #   state
        idpa = idpa1()
        cur.execute("""insert into pais(num_pa,nombre,estado)
                                        values(%s,%s,0);""",(idpa,pais))
        #   empleado//insert into DOCENTES(num_do,nombres,apellidos,carnet,email,telf,edad,genero,foto,direccion,id_pais,id_departamento,id_registro,estado) 
				#values('D10','CARLOS','GUTIERRES',9910926,'@gmail.com','73503177',24,'MASCULINO',NULL,'ZONA MARISCAL',1,1,1,0);
        cur.execute("SELECT max(id_pa) FROM pais where num_pa=%s;", (idpa,))
        id_pais=cur.fetchall() 
        print(id_pais)
        cur.execute("SELECT max(id_de) FROM departamento where num_de=%s;", (idde,))
        id_departamento=cur.fetchall()
        print(id_departamento)
        cur.execute("SELECT max(id_u) FROM registro_usuario where num_u=%s;", (idu,))
        id_registro=cur.fetchall()
        print(id_registro)
        idadm=idadm1()
        cur.execute("""insert into personal_admininistrativo(num_adm,nombres,apellidos,carnet,email,telf,edad,genero,foto,direccion,id_pais,id_departamento,id_registro,estado)
                                   values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,0);"""
                                   ,(idadm,nombres,apellidos,int(carnet),email,telf,int(edad),genero,foto,direccion,id_pais[0][0],id_departamento[0][0],id_registro[0][0]))
        db.commit()
        return ('INsercion con exito administardor')