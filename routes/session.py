from flask import Blueprint, request, jsonify
from flask_cors import cross_origin
from routes.coneccion import db
from routes.encriptar import encript
session = Blueprint('session', __name__)


def llave(user, clave):
    database = db()
    cur = database.cursor()
    cur.execute(
        """select num_u from registro_usuario where estado=0 and usuario=%s and password =%s;""", (user, clave))
    max = cur.fetchall()
    database.close()
    return (max[0][0])


def id_reg(user, clave):
    database = db()
    cur = database.cursor()
    cur.execute(
        """select id_u from registro_usuario where estado=0 and usuario=%s and password =%s;""", (user, clave))
    max = cur.fetchall()
    database.close()
    return (max[0][0])


@session.route('/getUserToken', methods=['POST'])
@cross_origin()
def inicio_session():
    database = db()
    if request.method == 'POST':
        token = request.form['token']
        database = db()
        cur = database.cursor()
        if cur.execute("""SELECT
    u.usuario, u.tipo, u.logged,u.num_u FROM
	registro_usuario u INNER JOIN detalle_login dl ON (dl.num_u = u.num_u) WHERE dl.login_token = %s""", (token)):
            u = cur.fetchone()
            usuario = {'usuario': u[0], 'tipo': u[1],
                       'logged': u[2], 'num_u': u[3]}
            cur.close()
            database.close()
            return jsonify(usuario)
        else:
            database.close()
            return jsonify({'status': 0})


# Deves retornarme el num_dl que te mande para cerrar la session


@session.route('/cierre_session', methods=['POST'])
@cross_origin()
def cierre_session():
    if request.method == 'POST':
        codigo = request.form['clave']
        num_dl = codigo
        database = db()
        cur = database.cursor()
        cur.execute("""select id_dl from detalle_login 
                    where num_dl=%s and estado=0;""", (num_dl,))
        id_dl = cur.fetchall()
        # UPDATE detalle_login  set estado = 1 ,fecha_finalisar = NOW() WHERE id_dl=3;
        cur.execute("""UPDATE detalle_login set estado = 1 ,fecha_finalisar = NOW() 
                        WHERE id_dl=%s;""", (id_dl[0][0]))
        database.commit()
        database.close()
        return jsonify({'status': 1})
