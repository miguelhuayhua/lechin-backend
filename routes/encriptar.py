from flask import Blueprint
import hashlib

def encript(texto):
    clave = str(texto).encode('utf-8')
    sha256 = hashlib.sha256(clave).hexdigest()
    return(sha256)

def decript(encriptado,llave):
    clave = str(llave).encode('utf-8')
    sha256 = hashlib.sha256(clave).hexdigest()
    if encriptado==sha256:
        return(llave)
    else:
        return('fallo')
