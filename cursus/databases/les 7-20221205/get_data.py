from mysql.connector import connect, Error
import json
from key import password

def getData(db, table):
    try:
        conn = connect(host='localhost', user='root', password=password, database= db)
        sql = f'''SELECT * FROM {table}'''
        cursor = conn.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
    except Error as e:
        print("Error while connecting to MySQL", e)

getData("tennisdb","spelers")
