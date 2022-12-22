import mysql.connector as msql
from mysql.connector import Error
from key import password_sql #dit is een klasse die ik heb gemaakt en mijn password in zit als een variable

try:
    conn = msql.connect(host='localhost', user='root', password=password_sql)#give ur username, password
    if conn.is_connected():
        cursor = conn.cursor()
        print('Creating table....')
# in the below line please pass the create table statement which you want #to create
        cursor.execute("use tennisdb; CREATE TABLE spelers ("+
                        "SPELERSNR int(6) NOT NULL AUTO_INCREMENT,"+
                        "NAAM varchar(30) DEFAULT NULL," +
                        "VOORLETTERS varchar(3) DEFAULT NULL," +
                        "GEB_DATUM Date," +
                        "GESLACHT char(1)," +
                        "JAARTOE int(6)," +
                        "STRAAT varchar(15)," +
                        "HUISNR varchar(4)," +
                        "POSTCODE varchar(6)," +
                        "PLAATS varchar(10)," +
                        "TELEFOON varchar(10)," +
                        "BONDSNR varchar(4)," +
                        "Primary Key(`SPELERSNR`))")
        
        print("Table is created....")
except Error as e:
    print("Error while connecting to MySQL", e)