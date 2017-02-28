import sys
sys.path.append("/var/www/brat/myscript/script_py")
import common.config as config
import MySQLdb

db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="riks2501",
                     db="encyclopedia",
                     charset='utf8')

cur = db.cursor()

# Use all the SQL you like

f = open(config.dataPath+"tmp.txt")
lines = f.readlines()

for line in lines:
    data = line.strip().replace(")","").split("(")
#    print(data[0].decode("utf-8"))
    cur.execute("INSERT INTO category (name, code) VALUES (%s, %s)", (data[0].decode('utf-8'), data[1].decode('utf-8')))
db.commit()

"""
for row in cur.fetchall():
    print(row[0])
"""
db.close()