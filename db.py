import mysql.connector
from mysql.connector import Error

def connection(database_name):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database= f"{database_name}"
        )

    return connection

def close_connection(connection):
    try:
        connection.close()
    except Error as e:
        print(f"The error '{e}' occurred when trying to close connection")

def try_execute(connection,sql_query):
    cursor = connection.cursor()
    try:
        cursor.execute(sql_query)
    except Error as e:
        print(f"The error '{e}' occurred")
        
    connection.commit()

def create_database(database_name):
        connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        )
        sql = f"""
        CREATE DATABASE IF NOT EXISTS {database_name};
        """
        try_execute(connection=connection,sql_query=sql)
        close_connection(connection)
def try_sql_query(connection,title,description,url,img_url,author,views,downloads,license,resolution,category,img_id):
    table_name = "image2"
    cursor = connection.cursor()
    sql_table = f"""
    CREATE TABLE IF NOT EXISTS {table_name}(
        IID INT NOT NULL AUTO_INCREMENT,
        image_title varchar(255) NOT NULL,
        description TEXT NOT NULL,
        url TEXT NOT NULL,
        img_url TEXT NOT NULL,
        author varchar(255) NOT NULL,
        views varchar(255) NOT NULL,
        downloads varchar(255) NOT NULL,
        license varchar(255) NOT NULL,
        resolution varchar(255) NOT NULL,
        category varchar(255) NOT NULL,
        img_id varchar(255) NOT NULL,
        PRIMARY KEY (IID)
    );
    """
    sql_insert = f"""
        INSERT INTO {table_name} (image_title, description, url, img_url, author, views, downloads,license,resolution,category,img_id)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
    """
    values = (title,description,url,img_url,author,views,downloads,license,resolution,category,img_id)
    try:
        cursor.execute(sql_table)
        cursor.execute(sql_insert,values)
    except Error as e:
        print(f"The error '{e}' occurred")
    connection.commit()


