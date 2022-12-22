import mysql.connector as msql
from mysql.connector import Error
import json 
#https://qiita.com/skokado/items/caa31d3845df23bc0913
try:

    config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Raidersofthelostarc1',
    'database': 'tennisdb'
    }
    #https://www.geeksforgeeks.org/args-kwargs-python/
    conn = msql.connect(**config) 
    if conn.is_connected():

        cursor = conn.cursor()
        f = open('spelers.json')  
        data = json.load(f)

        # for i in data:
        #     spelersnr = i["SPELERSNR"]
        #     naam = i["NAAM"]
        #     voorletters = i["VOORLETTERS"]
        #     geb_datum = i["GEB_DATUM"]
        #     geslacht = i["GESLACHT"]
        #     jaartoe = i["JAARTOE"]
        #     straat = i["STRAAT"]
        #     huisnr = i["HUISNR"]
        #     postcode = i["POSTCODE"]
        #     plaats = i["PLAATS"]
        #     telefoon = i["TELEFOON"]
        #     bondsnr = i["BONDSNR"]

        #     query = f'''INSERT INTO spelers(spelersnr, naam, voorletters, geb_datum, geslacht, jaartoe, straat, huisnr, postcode, plaats, telefoon, bondsnr) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);'''
        #     val = (spelersnr, naam, voorletters, geb_datum, geslacht, jaartoe, straat, huisnr, postcode, plaats, telefoon, bondsnr)
        #     cursor.execute(query,val)

        # conn.commit()
        #The db.commit() in the above code is important. It is used to commit the changes made to the table. Without using commit(), no changes will be made in the table.
        conn.close()

except Error as e:
    print("Error while connecting to MySQL", e)