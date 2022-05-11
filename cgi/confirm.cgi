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
amount = form.getvalue('amount') 
comment = form.getvalue('comment') 
source = form.getvalue('source')

cur = sql.cursor()
cur.execute("select kind1.kind,kind2.kind from k_constraint inner join kind1 on k_constraint.kind1=kind1.id inner join kind2 on k_constraint.kind2=kind2.id where kind1.id='%s' and kind2.id='%s'" % (kind1,   kind2))
kind = cur.fetchall()

cur.execute("select method from method where id='%s'" % source)
sour = cur.fetchall()


print('Content-Type: text/html\n\n')
print('<html>')


print('<head>')
print('<meta charset="UTF-8">')
print('<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no" />')

print('<link rel="stylesheet" href="./style.css">')


print('</head>')
print('<body class="confirm">')
print('<div class="confirm">')

print(kind[0][0])
print('<br>')
print(kind[0][1])

print('<br><br>amount:&nbsp')
print(amount)

print('<br>comment:&nbsp')
print(comment)

print('<br>source:&nbsp')
print(sour[0][0])

print('<form action="result.cgi" method="post">')
print('<input type="hidden" name="kind2" value="%s">' % kind2)
print('<input type="hidden" name="kind1" value="%s">' % kind1)
print('<input type="hidden" name="amount" value="%s">' % amount)
print('<input type="hidden" name="comment" value="%s">' % comment)
print('<input type="hidden" name="source" value="%s">' % source)
print('</div>')
print('<div class="botn">')

print('<br><input type="submit" value="confirm" class="btn">')
print('</form>')
print('</div>')


print('</body>')
print('</html>')





cur.close()

sql.close()

