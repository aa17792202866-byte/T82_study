import pymysql
con = pymysql.connect(host="localhost",port=3306,user="root",password="123456",database="ceshi",charset="utf8")
print(con)
cu = con.cursor()
print(cu)
