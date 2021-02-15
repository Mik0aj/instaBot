import mysql.connector
from mysql.connector import Error


def extract_credetials(file_name):
    file = open(file_name, 'r')
    lines = file.readlines()
    for i,line in enumerate(lines):
        lines[i]=line.strip()
    return lines
def create_connection(host_name, user_name, user_password,database):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database = database
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

