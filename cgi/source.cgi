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
kind2 = form.getvalue('kind2')


cur = sql.cursor()
cur.execute("select * from method")
sour = cur.fetchall()


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


print('<form action="confirm.cgi" method="post">')
print('source')
print('</div><div class="botn"><select name="source" class="btn">')

for a in sour:
 print('<option value="' + str(a[0]) + '">' +
 str(a[1]) +
 '</option>')


print('</select>')
print('<input type="hidden" name="amount" value="%s">' % amount)
print('<input type="hidden" name="comment" value="%s">' % comment)
print('<input type="hidden" name="kind1" value="%s">' % kind1)
print('<input type="hidden" name="kind2" value="%s">' % kind2)

print('<input type="submit" value="next" class="btn">')
print('</form>')
print('</div>')


print('</body>')
print('</html>')





cur.close()

sql.close()

