#-*- coding: utf-8 -*-

import sys
sys.path.append("/var/www/brat/myscript/script_py")
import common.config as config
import common.parse as parse
import common.db as db
import controller.exportAnnotation
import json

#config파일의 categoryCode입력
query = "select * from category"
db.cur.execute(query)
rows = db.cur.fetchall()

for row in rows:
    config.categoryCode[row['code']] = row['name']


controller.exportAnnotation.exportAnnotation()
