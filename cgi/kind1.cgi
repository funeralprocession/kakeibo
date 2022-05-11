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



form = cgi.FieldStorage()
amount = form.getvalue('amount')
comment = form.getvalue('comment')



cur = sql.cursor()

cur.execute("select * from kind1")
k1 = cur.fetchall()




print('Content-Type: text/html\n\n')
print('<html>')


print('<head>')
print('<meta charset="UTF-8">')
print('<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no" />')


print('<link rel="stylesheet" href="./style.css">')


print('</head>')
print('<body class="normal">')

print('<div class="botn">')

print('<form action="kind2.cgi" method="post">')


print('<select name="kind1" class="btn">')

for a in k1:
 print('<option value="' + str(a[0]) + '">' + 
 str(a[1]) + 
 '</option>')


print('</select>')

print('<input type="hidden" name="amount" value="%s">' % amount)
print('<input type="hidden" name="comment" value="%s">' % comment)
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

