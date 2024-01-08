HOST_BD = "localhost" 
NAME_BD = "stock" 
PASSWORD_BD = "01289" 
USER_BD = "root" 
TABLE_NAME = "transport"

def bd_connect_root():
    return {
        "host_bd": HOST_BD,
        "name_db": NAME_BD,
        "password_db": PASSWORD_BD,
        "user_bd": USER_BD,
        "table_name": TABLE_NAME
    }
