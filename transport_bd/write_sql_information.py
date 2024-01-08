from mysql.connector import connect, Error
def write_sql_information(bd_connect, uid, owner, now_data):
    INSERT_QUERY = 'insert into ' + bd_connect["table_name"] + '(uid, owner, now_data) values(%s, %s, %s)'
    
    try:
        with connect(
            host = bd_connect["host_bd"],
            user = bd_connect["user_bd"],
            password = bd_connect["password_db"],
            database = bd_connect["name_db"],
        ) as connection:
            with connection.cursor() as cursor:
                cursor.execute(INSERT_QUERY, (uid, owner, now_data))
                connection.commit()
    except Error as e:
        print(e)
