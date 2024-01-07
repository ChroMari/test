from getpass import getpass

def bd_connect_root():
    user_bd =  input("Введите пользователя: ")
    password_db = getpass("Введите пароль для подключения: ")

    return {
        "host_bd": "localhost",
        "name_db": "stock",
        "password_db": password_db,
        "user_bd": user_bd,
        "table_name": "transport"
    }
