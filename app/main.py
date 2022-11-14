from flask import Flask
<<<<<<< HEAD
from routes.login import login
=======
from routes.usuarios import usuario
from routes.mostrar import mostrar
from routes.registro_user import usuarios
from routes.session import login
from pymysql import connect   #//por si falla la coneccion al DB
>>>>>>> 7edb5654da79496948decb14d088ef0c7e97b09a
from flask_cors import CORS
app = Flask(__name__)

CORS(app)
<<<<<<< HEAD
app.register_blueprint(login)
=======
app.register_blueprint(mostrar)
app.register_blueprint(login)
app.register_blueprint(usuario)
>>>>>>> 7edb5654da79496948decb14d088ef0c7e97b09a




