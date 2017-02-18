#!/usr/bin/python
import mysql.connector
from mysql.connector import errorcode

try:
  cnx = mysql.connector.connect(user='yudongxiao', password='1980613',
                              host='127.0.0.1',
                              database='pets',
                              use_pure=False)

  cur = cnx.cursor()

  cur.execute("SELECT id,name,owner, birth FROM cats")

  for id, name,owner,birth in cur.fetchall():
      print id, name,owner,birth


except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
else:
  cnx.close()