from pymysql import connect

def con():
    db = connect(
        host='localhost',
        user='root', 
        password = "",
        db='pweb_python',
        )
    cur = db.cursor()
    return (cur)
def commit():
    db = connect(
        host='localhost',
        user='root', 
        password = "",
        db='pweb_python',
        )
    commit = db.connect.commit()
    return(commit)
    