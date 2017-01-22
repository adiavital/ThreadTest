import mysql.connector

#THE CONNECTION DETAILS WILL BE IN A CONFIG FILE IN THE FUTURE
server_host = 'localhost'
user = 'root'
password = 'adiavital8717003'
database = 'insta'

def select_data():
    conn = mysql.connector.connect(user=user, password=password, host=server_host, database=database)
    cursor = conn.cursor()
    sql = """SELECT name,id FROM mydata WHERE processed = 0 and date<sysdate()-3/24 and id in (SELECT id FROM mydata WHERE processed = 0 and date<sysdate()-3/24) FOR UPDATE """
    cursor.execute(sql)
    result = cursor.fetchmany(size=2)
    conn.close()
    return result


def update_data(user_id):
    conn = mysql.connector.connect(user=user, password=password, host=server_host, database=database)
    cursor = conn.cursor()
    sql = """UPDATE mydata SET processed = 1 WHERE id = %s""" % (user_id)
    try:
        cursor.execute(sql)
        conn.commit()
    except:
        conn.rollback()
    conn.close()


def update_name(new_name, user_id):
    conn = mysql.connector.connect(user=user, password=password, host=server_host, database=database)
    cursor = conn.cursor()
    sql = """UPDATE mydata SET name = '%s' WHERE id = '%s'"""  % (new_name, user_id)
    try:
        cursor.execute(sql)
        conn.commit()
    except Exception as e:
        conn.rollback()
        print(e)
    conn.close()



#----------------------
def reset():
    conn = mysql.connector.connect(user=user, password=password, host=server_host, database=database)
    cursor = conn.cursor()
    sql = """UPDATE mydata SET processed = 0 """
    try:
        cursor.execute(sql)
        conn.commit()
    except Exception as e:
        conn.rollback()
        print(e)
    conn.close()


# reset()
# print(select_data())