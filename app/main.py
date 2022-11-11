from flask import Flask
from routes.login import login
from flask_cors import CORS
app = Flask(__name__)

CORS(app)
app.register_blueprint(login)





