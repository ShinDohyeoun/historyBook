import pymysql
db = pymysql.connect(host="localhost",
                     user="root",
                     passwd="riks2501",
                     db="encyclopedia",
                     charset='utf8')

cur = db.cursor(pymysql.cursors.DictCursor)