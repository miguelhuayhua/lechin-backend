from flask import Blueprint, request,jsonify
from flask_cors import cross_origin
from routes.coneccion import db
modificar = Blueprint('modificar',__name__)