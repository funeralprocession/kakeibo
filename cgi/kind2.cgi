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
amount = form.getvalue('amount')
comment = form.getvalue('comment')
kind1 = form.getvalue('kind1')

cur = sql.cursor()
cur.execute("select kind2.* from k_constraint inner join kind1 on k_constraint.kind1=kind1.id inner join kind2 on k_constraint.kind2=kind2.id where kind1.id='%s'" % kind1)
k2 = cur.fetchall()

cur.execute("select kind from kind1 where id = '%s'" % kind1)
k1 = cur.fetchall()


print('Content-Type: text/html\n\n')
print('<html>')


print('<head>')
print('<meta charset="UTF-8">')
print('<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no" />')

print('<link rel="stylesheet" href="./style.css">')


print('</head>')
print('<body class="normal">')
print('')
print('<div class="normal">')


print('<form action="source.cgi" method="post">')
print(k1[0][0])
print('</div><div class="botn"><select name="kind2" class="btn">')

for a in k2:
 print('<option value="' + str(a[0]) + '">' +
 str(a[1]) +
 '</option>')


print('</select>')
print('<input type="hidden" name="amount" value="%s">' % amount)
print('<input type="hidden" name="comment" value="%s">' % comment)
print('<input type="hidden" name="kind1" value="%s">' % kind1)
print('<input type="submit" value="next" class="btn">')
print('</form>')
print('</div>')

print('<div class="normal">')
print('amount:&nbsp')
print(amount)

print('<br>comment:&nbsp')
print(comment)
print('</div>')



print('</body>')
print('</html>')





cur.close()

sql.close()

