from flask import Blueprint, request,jsonify
from flask_cors import cross_origin
from routes.coneccion import db
login = Blueprint('login',__name__)
db = db()

@login.route('/inicio_session',methods = ['POST'])
@cross_origin()
def inicio_session():
    if request.method == 'POST':
        usuario = request.form['usuario']
        password = request.form['password']
#         select substring(num_l,2) from login where usuario='freddy' and password = 123;
# select max(id_l) from login where usuario='freddy' and password = 123;
        cur.execute("""select substring(num_l,2) from login 
                    where usuario=%s and password = %s;""",(usuario,password))
        num_l = cur.fetchall()
        num_dl='DL'+str(num_l[0][0])
        print(num_l)
        cur.execute("""select max(id_l) from login 
                    where estado=0 and usuario=%s and password =%s;""",(usuario,password))
        id_login = cur.fetchall()
        #insert into detalle_login(num_dl,id_login,fecha_finalisar,estado) values('DL10',1,NULL,0);
        cur.execute("""insert into detalle_login(num_dl,id_login,fecha_finalisar,estado)
                                    values(%s,%s,NULL,0);""",(num_dl,id_login[0][0]))
        commit()
        return('INICIO SESSION')

@login.route('/cierre_session',methods = ['POST'])
@cross_origin()
def cierre_session():
    if request.method == 'POST':
        usuario = request.form['usuario']
        password = request.form['password']
#         select substring(num_l,2) from login where usuario='freddy' and password = 123;
# select max(id_l) from login where usuario='freddy' and password = 123;
        cur.execute("""select substring(num_l,2) from login 
                    where usuario=%s and password = %s;""",(usuario,password))
        num_l = cur.fetchall()
        num_dl='DL'+str(num_l[0][0])
        print(num_l)
        cur.execute("""select id_dl from detalle_login 
                    where num_dl=%s and estado=0;""",(num_dl,))
        id_dl = cur.fetchall()
        #UPDATE detalle_login  set estado = 1 ,fecha_finalisar = NOW() WHERE id_dl=3;
        cur.execute("""UPDATE detalle_login set estado = 1 ,fecha_finalisar = NOW() 
                        WHERE id_dl=%s;""",(id_dl[0][0]))
        commit()
        return('FINALISO SESSION')






# @login.route('/login',methods = ['POST','GET'])
# @cross_origin()
# def handleLogin():
#     if request.method == 'POST':
#         print(request.form['usuario'])
#         print(request.form['password'])
#         return jsonify({'nombre':'hola'})
#     elif request.method == 'GET':
#         return 'ESTE ES UN GET'