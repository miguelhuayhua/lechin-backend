from pymysql import connect

def db():
    try:
        db = connect(
        host='bvcpgguw0kpl5h91bxdy-mysql.services.clever-cloud.com',
        user='u4plexpe8n2igv8k', 
        password = "cgDOAUgJfonIDHUeJeqF",
        db='bvcpgguw0kpl5h91bxdy',
        )
    except(e):
        print(e)
    return (db)

    