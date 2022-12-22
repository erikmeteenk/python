import mysql.connector as msql
from mysql.connector import Error
from key import password_sql 
import json 
#https://qiita.com/skokado/items/caa31d3845df23bc0913

def update_database(database, table, dict):
    try:
        config = {
        'host': 'localhost',
        'user': 'root',
        'password': password_sql,
        'database': database
        }
        #https://www.geeksforgeeks.org/args-kwargs-python/
        conn = msql.connect(**config) 
        if conn.is_connected():
            cursor = conn.cursor()
            query = f'''UPDATE spelers SET naam=%s WHERE spelersnr=%s'''
            val = tuple(dict.values())
            cursor.execute(query,val)
            conn.commit()
            #The db.commit() in the above code is important. It is used to commit the changes made to the table. Without using commit(), no changes will be made in the table.
            conn.close()

    except Error as e:
        print("Error while connecting to MySQL", e)


update_database('tennisdb',"spelers", { "naam": "A1", "spelersnr": 2})

