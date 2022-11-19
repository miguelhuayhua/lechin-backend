from flask import Blueprint, request,jsonify
from flask_cors import cross_origin
from routes.coneccion import db
from routes.encriptar import encript
documents = Blueprint('documents',__name__)