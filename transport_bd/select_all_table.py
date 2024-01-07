from mysql.connector import connect, Error

def select_all_table(bd_connect):
    try:
        with connect(
            host = bd_connect["host_bd"],
            user = bd_connect["user_bd"],
            password = bd_connect["password_db"],
            database = bd_connect["name_db"],
        ) as connection:
            select_movies_query = f"SELECT * FROM {bd_connect['table_name']}"
            with connection.cursor() as cursor:
                cursor.execute(select_movies_query)
                result = cursor.fetchall()
                
                return result
    except Error as e:
        print(e)
