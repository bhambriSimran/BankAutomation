#mport mysql.connector as sql
import pymysql as sql
def getCon():
    con=sql.connect(host='localhost',user='root',password='Simran@18967',database='bank',port=3310)
    return con
