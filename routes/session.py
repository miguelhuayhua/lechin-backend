from flask import Blueprint, request,jsonify
from flask_cors import cross_origin
from routes.coneccion import db
login = Blueprint('login',__name__)

@login.route('/inicio_session',methods = ['POST'])
@cross_origin()
def inicio_session():
    database = db()
    if request.method == 'POST':
        usuario = request.form['usuario']
        password = request.form['password']
        cur = database.cursor()
        if cur.execute("""select id_l from login where estado=0 and usuario=%s and password =%s;""",(usuario,password))==True:
            id_dlogin = cur.fetchall()
        
            cur.execute("""select substring(num_l,2) from login 
                    where usuario=%s and password = %s;""",(usuario,password))
            num_l = cur.fetchall()
            num_dl='DL'+str(num_l[0][0])
            print(num_dl)
            # se crea session
            cur.execute("""insert into detalle_login(num_dl,id_login,fecha_finalisar,estado)
                                    values(%s,%s,NULL,0);""",(num_dl,id_dlogin[0][0]))
            database.commit()
            print(num_dl)
            database.close()
            return jsonify({"id_clave":num_dl})
        else:
            return('Paswword o user no existe')

#Deves retornarme el num_dl que te mande para cerrar la session 
@login.route('/cierre_session',methods = ['POST'])
@cross_origin()
def cierre_session():
    if request.method == 'POST':
        num_dl = request.form['num_dl']
        database = db()
        cur = database.cursor()
        cur.execute("""select max(id_dl) from detalle_login 
                    where num_dl=%s and estado=0;""",(num_dl,))
        id_dl = cur.fetchall()
        cur.execute("""UPDATE detalle_login set estado = 1 ,fecha_finalisar = NOW() 
                        WHERE id_dl=%s;""",(id_dl[0][0]))
        database.commit()
        database.close()
        return ('/Abandonando session')