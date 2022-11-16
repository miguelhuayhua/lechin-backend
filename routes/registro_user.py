from flask import Blueprint, request,jsonify
from flask_cors import cross_origin
from routes.coneccion import db
insercion = Blueprint('insercion',__name__)

def idu1():
        database = db()
        cur = database.cursor()
        cur.execute("select count(distinct(num_u)) from registro_usuario where estado=0;")
        max = cur.fetchall()
        print('el valor')
        print(max)
        if max[0][0] != None:
                idu='U'+str(int(max[0][0])+1)
                database.close()
                print('hay valores')
                return(idu)    
        else:
                print('NO hay valores')
                return('U1')
        
def idde1():
        database = db()
        cur = database.cursor()
        cur.execute("select count(distinct(num_de)) from departamento where estado=0;")
        max = cur.fetchall()
        if max[0][0] != None:
                idde='DE '+str(int(max[0][0])+1)
                database.close()
                print('hay valores')
                return(idde) 
        else:
                print('NO hay valores')
                return('DE 1')
        
def idpa1():
        database = db()
        cur = database.cursor()
        cur.execute("select count(distinct(num_pa)) from pais where estado=0;")
        max = cur.fetchall()
        if max[0][0] != None:
                idpa='PA '+str(int(max[0][0])+1)
                database.close()
                return(idpa)  
        else:
                print('NO hay valores')
                return('PA 1')
        
def ides1():
        database = db()
        cur = database.cursor()
        cur.execute("select count(distinct(num_es)) from estudiante where estado=0;")
        max = cur.fetchall()
        if max[0][0] != None:
                ides='E'+str(int(max[0][0])+1)
                database.close()
                return(ides) 
        else:
                print('NO hay valores')
                return('E1') 
        
@usuarios.route('/insertar e',methods=['POST'])
@cross_origin()
def insertar_estudiante():
    if request.method == 'POST':
        fecha_nac = request.form['fecha_nac']
        nombres = request.form['nombres']
        apellidos = request.form['apellidos']
        carnet = request.form['carnet']
        email = request.form['email']
        telf = request.form['telf']
        edad = request.form['edad']
        edad = 12
        genero = request.form['genero']
        foto = request.form['foto']
        direccion = request.form['direccion']
        
        departamento = request.form['departamento']
        pais = request.form['pais']
        
        usuario = request.form['usuario']
        clave = request.form['password']
        password = encript(clave)
        token_cea = request.form['token_cea']
        
# img=open(foto,'rb').read()
# print(img)
        #conneccion
        database = db()
        cur = database.cursor()
        #mysql.connection.commit()
        # registrouser//insert into registro_usuario(num_u,id_roles,id_login,estado) values('U10',1,1,0);
        idu = idu1()
        cur.execute("""insert into registro_usuario(num_u,usuario,password,token_cea,id_roles,estado) 
                                        values(%s,%s,%s,%s,1,0);""",(idu,usuario,password,token_cea))
        #mysql.connection.commit()
        #   department//insert into departamento(num_de,nombre,estado) values('DE 1','LA PAZ',0);
        idde = idde1()
        cur.execute("""insert into departamento(num_de,nombre,estado) 
                                        values(%s,%s,0);""",(idde,departamento))
        #mysql.connection.commit()
        #   state//insert into pais(num_pa,nombre,estado) values('PA 1','BOLIVIA',0);
        idpa = idpa1()
        cur.execute("""insert into pais(num_pa,nombre,estado)
                                        values(%s,%s,0);""",(idpa,pais))
        #mysql.connection.commit()
        #   empleado//insert into ESTUDIANTE(num_es,nombres,apellidos,carnet,email,telf,edad,genero,foto,direccion,id_pais,id_departamento,id_registro,estado) 
				#values('E20','CARLOS','GUTIERRES',9910926,'@gmail.com','73503177',24,'MASCULINO',NULL,'ZONA MARISCAL',1,1,1,0);
        cur.execute("SELECT max(id_pa) FROM pais where num_pa=%s;", (idpa,))
        id_pais=cur.fetchall() 
        print(id_pais)
        cur.execute("SELECT max(id_de) FROM departamento where num_de=%s;", (idde,))
        id_departamento=cur.fetchall()
        print(id_departamento)
        cur.execute("SELECT max(id_u) FROM registro_usuario where num_u=%s;", (idu,))
        id_registro=cur.fetchall()
        print(id_registro)
        ides=ides1()
        print(ides)
        cur.execute("""insert into estudiante(fecha_nac,num_es,nombres,apellidos,carnet,email,telf,edad,genero,foto,direccion,id_pais,id_departamento,id_registro,estado)
                                   values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,0);"""
                                   ,(fecha_nac,ides,nombres,apellidos,int(carnet),email,telf,int(edad),genero,foto,direccion,id_pais[0][0],id_departamento[0][0],id_registro[0][0]))
        database.commit()
        database.close()
        return ('1')
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
        fecha_nac = request.form['fecha_nac']
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
        cur.execute("""insert into DOCENTES(id_registro,fecha_nac,num_do,nombres,apellidos,carnet,email,telf,edad,genero,foto,direccion,id_pais,id_departamento,id_registro,estado)
                                   values(NULL,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,0);"""
                                   ,(fecha_nac,iddo,nombres,apellidos,int(carnet),email,telf,int(edad),genero,foto,direccion,id_pais[0][0],id_departamento[0][0],id_registro[0][0]))
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
        fecha_nac = request.form['fecha_nac']
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
        cur.execute("""insert into personal_admininistrativo(id_registro,fecha_nac,num_adm,nombres,apellidos,carnet,email,telf,edad,genero,foto,direccion,id_pais,id_departamento,id_registro,estado)
                                   values(NULL.%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,0);"""
                                   ,(fecha_nac,idadm,nombres,apellidos,int(carnet),email,telf,int(edad),genero,foto,direccion,id_pais[0][0],id_departamento[0][0],id_registro[0][0]))
        db.commit()
        return ('Insercion con exito administardor')