from flask import Flask
from routes.usuarios import usuario
from routes.mostrar import mostrar
from routes.registro_user import insercion
from routes.session import login
from pymysql import connect   #//por si falla la coneccion al DB
from routes.login import login
from flask_cors import CORS
app = Flask(__name__)

CORS(app)
app.register_blueprint(login)
app.register_blueprint(mostrar)
app.register_blueprint(usuario)
app.register_blueprint(login)
app.register_blueprint(insercion)





