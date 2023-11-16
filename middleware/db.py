import mysql.connector

def get_mysql_connection():
    app_config = {
        'MYSQL_HOST': '127.0.0.1',
        'MYSQL_USER': '-----',
        'MYSQL_PASSWORD': '-----',
        'MYSQL_DB': 'rivandy'
    }

    connection = mysql.connector.connect(
        host=app_config['MYSQL_HOST'],
        user=app_config['MYSQL_USER'],
        password=app_config['MYSQL_PASSWORD'],
        database=app_config['MYSQL_DB']
    )

    return connection