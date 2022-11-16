from flask import Blueprint
import hashlib
encriptar = Blueprint('encriptar',__name__)

def encript(texto):
    clave = str(texto).encode('utf-8')
    sha256 = hashlib.sha256(clave).hexdigest()
    print("Hash SHA256: %s" % str(sha256))
    return(sha256)

def decript(encriptado,llave):
    clave = str(llave).encode('utf-8')
    sha256 = hashlib.sha256(clave).hexdigest()
    print(sha256)
    if encriptado==sha256:
        return(llave)
    else:
        return('fallo')
