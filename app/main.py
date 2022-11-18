from flask import Flask
from routes.mostrar import mostrar
from routes.registro_user import registro
from routes.session import session
from routes.modificar import modificar
from routes.inscripcion import inscripcion
from pymysql import connect   #//por si falla la coneccion al DB
from flask_cors import CORS
app = Flask(__name__)

CORS(app)
app.register_blueprint(registro)
app.register_blueprint(session)
app.register_blueprint(modificar)
app.register_blueprint(inscripcion)
app.register_blueprint(mostrar)




