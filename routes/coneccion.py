from pymysql import connect

def db():
    db = connect(
        host='localhost',
        user='root', 
        password = "",
        db='pweb_python',
        )
    return (db)
    