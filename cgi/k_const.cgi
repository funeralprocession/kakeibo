#!/usr/bin/python3
import cgi
import subprocess
import mysql.connector


sql = mysql.connector.connect(
    host =  'localhost',
    port =  3306,
    user =  'user',
    password = 'passwd',
    database = 'kakeibo',
)

cur = sql.cursor()
cur.execute("select * from kind2")
k2 = cur.fetchall()

cur.execute("select * from kind1")
k1 = cur.fetchall()

cur.execute("select kind1.kind, kind2.kind  from k_constraint inner join kind1 on kind1.id=k_constraint.kind1 inner join kind2 on kind2.id=k_constraint.kind2 order by kind1.kind asc")
kind = cur.fetchall()



print('Content-Type: text/html\n\n')
print('<html>')


print('<head>')
print('<meta charset="UTF-8">')
print('<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no" />')




print('</head>')
print('<body>')
print('<form action="save.cgi" method="post">')


print('<select name="kind1">')

for a in k1:
 print('<option value="' + str(a[0]) + '">' + 
 str(a[1]) + 
 '</option>')


print('</select>')

print('<select name="kind2">')

for a in k2:
 print('<option value="' + str(a[0]) + '">' +
 str(a[1]) +
 '</option>')


print('</select>')

print('<input type="submit" value="save">')
print('</form>')

print('<br>')

for a in kind:
 print(str(a[0]) + '&nbsp;&nbsp;&nbsp;&nbsp;' + str(a[1]) + '<br>')

print('<br><br>')
print('<br><br>')
print('')
print('</body>')
print('</html>')





cur.close()

sql.close()

