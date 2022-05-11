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
cur.execute("insert into paid (kind,amount,comment,date) values ((select k_constraint.id from k_constraint inner join kind1 on k_constraint.kind1=kind1.id inner join kind2 on k_constraint.kind2=kind2.id where kind1.id=%s and kind2.id=%s),%s,%s,cast(now() as datetime))  " ,  (kind1,kind2, amount, comment))
sql.commit()
cur.execute("select kind1.kind,kind2.kind,paid.amount, paid.comment from paid inner join k_constraint on k_constraint.id=paid.kind inner join kind1 on k_constraint.kind1=kind1.id inner join kind2 on k_constraint.kind2=kind2.id where paid.id=(select last_insert_id())")
kind = cur.fetchall()
cur.execute("select kind1.kind,kind2.kind from k_constraint inner join kind1 on k_constraint.kind1=kind1.id inner join kind2 on k_constraint.kind2=kind2.id where kind1.id='%s' and kind2.id='%s'" % (kind1,   kind2))
inp =  cur.fetchall()

cur.execute("select * from method where id='%s'" % source)
sour = cur.fetchall()
if int(source) != 1 :
 cur.execute("insert into paid (kind,amount,comment,date) values (%s,%s,%s,cast(now() as datetime))  " ,  (int(sour[0][2]), (-1)*int(amount), comment))
 sql.commit()


print('Content-Type: text/html\n\n')
print('<html>')

print('<head>')
print('<meta charset="UTF-8">')
print('<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no" />')

print('<link rel="stylesheet" href="./style.css">')
print('<script type="text/javascript">') 
print(' setTimeout(function(){') 
print(' window.location.href = \'https://61.194.9.135/cgi-bin/3iw9gvifqge9butf/brows.cgi\'') 
print(' }, 1*1000);') 
print(' </script>')
print('</head>')
print('<body class="normal">')
print('<div class="normal">')

print(str(kind[0][0]))
print('<br>')
print(str(inp[0][0]))
print('<hr width="400" size="10" align="center">') 
print(str(kind[0][1]))
print('<br>')
print(str(inp[0][1]))
print('<hr width="400" size="10" align="center">')
print('amount:<br>')
print(kind[0][2])
print('<br>')
print(amount)
print('<hr width="400" size="10" align="center">')
print('comment:<br>')
print(str(kind[0][3]))
print('<br>')
print(comment)
print('<hr width="400" size="10" align="center">')
print('source:<br>')
print(sour[0][1])


print('</div>')

print('</body>')
print('</html>')

cur.close()
sql.close()

