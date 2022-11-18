from flask import Blueprint, request,jsonify
from flask_cors import cross_origin
from routes.coneccion import db
from routes.encriptar import encript
session = Blueprint('session',__name__)

def llave(user,clave):
        database = db()
        cur = database.cursor()
        cur.execute("""select num_u from registro_usuario where estado=0 and usuario=%s and password =%s;""",(user,clave))
        max = cur.fetchall()
        database.close()
        return(max[0][0])    
def id_reg(user,clave):
        database = db()
        cur = database.cursor()
        cur.execute("""select id_u from registro_usuario where estado=0 and usuario=%s and password =%s;""",(user,clave))
        max = cur.fetchall()
        database.close()
        return(max[0][0]) 

@session.route('/inicio_session',methods = ['POST'])
@cross_origin()
def inicio_session():
    database = db()
    if request.method == 'POST':
        usuario = request.form['usuario']
        clave = request.form['password']
        password = encript(clave)
        cur = database.cursor()
        num_u = llave(usuario,password)
        
        if num_u!= None:
            num_dl='D'+str(num_u)
            print(num_dl)
            # se crea session
            id_registro = id_reg(usuario,password)
            cur.execute("""insert into detalle_login(num_dl,id_registro,fecha_finalisar,estado)
                                    values(%s,%s,NULL,0);""",(num_dl,id_registro))
            database.commit()
            database.close()
            codigo=num_dl
            return jsonify({'clave':codigo})
        else:
            return('0')

#Deves retornarme el num_dl que te mande para cerrar la session 
@session.route('/cierre_session',methods = ['POST'])
@cross_origin()
def cierre_session():
    if request.method == 'POST':
        codigo = request.form['clave']
        num_dl = codigo
        database = db()
        cur = database.cursor()
        cur.execute("""select id_dl from detalle_login 
                    where num_dl=%s and estado=0;""",(num_dl,))
        id_dl = cur.fetchall()
        #UPDATE detalle_login  set estado = 1 ,fecha_finalisar = NOW() WHERE id_dl=3;
        cur.execute("""UPDATE detalle_login set estado = 1 ,fecha_finalisar = NOW() 
                        WHERE id_dl=%s;""",(id_dl[0][0]))
        database.commit()
        database.close()
        return ('1')