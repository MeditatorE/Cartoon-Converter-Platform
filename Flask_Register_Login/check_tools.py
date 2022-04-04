from database_config import DB

db = DB()

def is_null(username, password):
    if (username == '' or password == ''):
        return True
    else:
        return False

def is_existed(username, password):
    sql = "SELECT * FROM user WHERE username ='%s' and password ='%s'" % (username, password)
    db.connect()
    cur = db.query(sql)
    result = cur.fetchall()
    if (len(result) == 0):
        return False
    else:
        return True


def exist_user(username, password):
    sql = "SELECT * FROM user WHERE username ='%s'" % (username)
    db.connect()
    cur = db.query(sql)
    result = cur.fetchall()
    if (len(result) == 0):
        return False
    else:
        return True

def add_user(username, password):
    sql = "INSERT INTO user(username, password) VALUES ('%s','%s')" % (username, password)
    db.connect()
    cur = db.query(sql)
    db.commit()
