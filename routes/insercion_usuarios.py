from flask import Blueprint, request,jsonify
from flask_cors import cross_origin
from routes.coneccion import con,commit
insercion = Blueprint('insercion',__name__)

cur=con()
def idl1():
        cur.execute("select max(substring(num_l,2)) from login;")
        max = cur.fetchall()
        idl='L'+str(int(max[0][0])+1)
        return(idl)

def id_login1(idl):
        cur.execute("SELECT id_l FROM login where num_l=%s;", (idl,))
        id_login=cur.fetchall()
        return(id_login)
def idu1():
        cur = mysql.connection.cursor()
        cur.execute("select max(substring(num_u,2)) from registro_usuario;")
        max = cur.fetchall()
        idu='U'+str(int(max[0][0])+1)
        return(idu)    
def idde1():
        cur.execute("select max(substring(num_de,4)) from departamento;")
        max = cur.fetchall()
        idde='DE '+str(int(max[0][0])+1)
        return(idde) 
def idpa1():
        cur.execute("select max(substring(num_pa,4)) from pais;")
        max = cur.fetchall()
        idpa='PA '+str(int(max[0][0])+1)
        return(idpa)    
def id_pais1(idpa):
        cur.execute("SELECT id_pa FROM pais where num_pa=%s;", (idpa,))
        id_pais=cur.fetchall()        
        return(id_pais)  
def id_departamento1(idde):
        cur.execute("SELECT id_de FROM departamento where num_de=%s;", (idde,))
        id_departamento=cur.fetchall()
        return(id_departamento)  
def id_registro1(idu):
        cur.execute("SELECT id_u FROM registro_usuario where num_u=%s;", (idu,))
        id_registro=cur.fetchall()      
        return(id_registro)    
def ides1():
        cur.execute("select max(substring(num_es,2)) from estudiante;")
        max = cur.fetchall()
        ides='E'+str(int(max[0][0])+1)
        return(ides)    

@insercion.route('/add_estudent',methods=['POST'])
@cross_origin()
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
        #roles ya tenemos
        #   login
        idl = idl1()
        cur.execute("""INSERT INTO login(num_l,usuario,password,token_cea,estado) 
                                    values(%s,%s,%s,%s,0);""",(idl,usuario,password,token_cea))
        # registrouser
        id_login = id_login1(idl)
        idu = idu1()
        cur.execute("""insert into registro_usuario(num_u,id_login,id_roles,estado) 
                                        values(%s,%s,1,0);""",(idu,id_login[0][0]))
        #   department//insert into departamento(num_de,nombre,estado) values('DE 1','LA PAZ',0);
        idde = idde1()
        cur.execute("""insert into departamento(num_de,nombre,estado) 
                                        values(%s,%s,0);""",(idde,departamento))
        #   state//insert into pais(num_pa,nombre,estado) values('PA 1','BOLIVIA',0);
        idpa = idpa1()
        cur.execute("""insert into pais(num_pa,nombre,estado)
                                        values(%s,%s,0);""",(idpa,pais))
        #   empleado//insert into ESTUDIANTE(num_es,nombres,apellidos,carnet,email,telf,edad,genero,foto,direccion,id_pais,id_departamento,id_registro,estado) 
				#values('E20','CARLOS','GUTIERRES',9910926,'@gmail.com','73503177',24,'MASCULINO',NULL,'ZONA MARISCAL',1,1,1,0);
        id_pais = id_pais1(idpa) 
        id_departamento = id_departamento1(idde)
        id_registro = id_registro1(idu)
        ides = ides1()
        cur.execute("""insert into ESTUDIANTE(num_es,nombres,apellidos,carnet,email,telf,edad,genero,foto,direccion,id_pais,id_departamento,id_registro,estado)
                                   values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,0);"""
                                   ,(ides,nombres,apellidos,int(carnet),email,telf,int(edad),genero,foto,direccion,id_pais[0][0],id_departamento[0][0],id_registro[0][0]))
        commit()
        return ('REGISTRO FINALISADO')