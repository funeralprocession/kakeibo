#!/usr/bin/python3
import cgi
import subprocess
import mysql.connector
import cgitb
cgitb.enable()

sql = mysql.connector.connect(
    host =  'localhost',
    port =  3306,
    user =  'user',
    password = 'passwd',
    database = 'kakeibo',
)


form = cgi.FieldStorage()
kind1 = form.getvalue('kind1')
kind2 = form.getvalue('kind2')



cur = sql.cursor()
cur.execute("select * from kind2")
k2 = cur.fetchall()

cur.execute("select * from kind1")
k1 = cur.fetchall()

cur.execute("select kind1.kind, kind2.kind  from k_constraint inner join kind1 on kind1.id=k_constraint.kind1 inner join kind2 on kind2.id=k_constraint.kind2 order by kind1.kind asc")
kind = cur.fetchall()

cur.execute("insert into k_constraint (kind1,kind2) values (%s,%s )", (kind1,kind2))
sql.commit()

print('Content-Type: text/html\n\n')
print('<html>')


print('<head>')
print('<meta charset="UTF-8">')
print('<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no" />')

print('<meta http-equiv="refresh" content="1;URL=k_const.cgi">')


print('</head>')
print('<body>')

print('wait redirect')



print('</body>')
print('</html>')





cur.close()

sql.close()

