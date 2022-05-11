#!/usr/bin/python3
import cgi
import subprocess
import mysql.connector
import time
import datetime
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
yr = form.getvalue('year') 
years = form.getvalue('years')
mt = form.getvalue('month')    
months = form.getvalue('months')
fixable = form.getvalue('fixable') 
essen = form.getvalue('essen')
noessen = form.getvalue('noessen')

cur = sql.cursor()

cur.execute("select * from kind2 order by id asc")
k2 = cur.fetchall()

cur.execute("select * from kind1 order by id asc")
k1 = cur.fetchall()

cur.execute("select distinct date_format(date,'%Y') from paid order by date desc")
year = cur.fetchall()

cur.execute("select distinct date_format(date,'%m') from paid order by date_format(date,'%m') asc")
month = cur.fetchall()

if str(kind1) == 'None':
 kd1 = 'any(select id from kind1)'
else:
 kd1 = '\'' + str(kind1) + '\''

if str(kind2) == 'None':
 kd2 = 'any(select id from kind2)'
else:
 kd2 = '\'' + str(kind2) + '\''

if str(yr) == 'None':
 if str(years) == 'None': 
  years = 1
  months = 0
 iyr = '> (now() - interval ' + str(years) + ' year - interval ' + str(months) + ' month)'
else:
 NOW = datetime.datetime.now()
 if str(mt) == 'None':
  mt = NOW.strftime("%m")
 iyr = '<= (select last_day(\'' + str(yr) + '-' + str(mt) + '-01\')) and paid.date >  (select last_day(\'' + str(yr) + '-' + str(mt) + '-01\'))  - interval ' + str(years) + ' year - interval ' + str(months) + ' month'

if str(fixable) == '1':
 fix = '1'
else:
 fix = '0'

if str(essen) == '1' and str(noessen) == '1': 
 ess1 = '3'
 ess2 = '3'
 ess3 = '3'
elif str(essen) == '1':
 ess1 = '1'
 ess2 = '1'
 ess3 = '1'
elif str(noessen) == '1': 
 ess1 = '2'
 ess2 = '2'
 ess3 = '2'
else:
 ess1 = '1'
 ess2 = '2'
 ess3 = '3'



cur = sql.cursor()
cur.execute("select sum(paid.amount) from paid inner join k_constraint on k_constraint.id=paid.kind inner join kind1 on k_constraint.kind1=kind1.id inner join kind2 on k_constraint.kind2=kind2.id where paid.fixable='%s' and kind1.charactor in (%s,%s,%s) and kind1.id=%s and kind2.id=%s and paid.date %s order by paid.date desc" % (fix, ess1, ess2, ess3, kd1, kd2, iyr))
amountall = cur.fetchall()

cur = sql.cursor()
cur.execute("select kind1.kind,kind2.kind,paid.amount, paid.comment, paid.date from paid inner join k_constraint on k_constraint.id=paid.kind inner join kind1 on k_constraint.kind1=kind1.id inner join kind2 on k_constraint.kind2=kind2.id where paid.fixable='%s' and kind1.charactor in (%s,%s,%s) and kind1.id=%s and kind2.id=%s and paid.date %s order by paid.date desc" % (fix, ess1, ess2, ess3, kd1, kd2, iyr))
brows = cur.fetchall()

print('Content-Type: text/html\n\n')
print('<html>')


print('<head>')
print('<meta charset="UTF-8">')
print('<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no" />')

print('<link rel="stylesheet" href="./style.css">')


print('</head>')
print('<body class="normal">')
print('<div class="botn">')

print('<form action="brows.cgi" method="post">')

if not kind1 :
 print('<select name="kind1" class="btn">')
 print('<option value=""></option>')
 for a in k1:
  print('<option value="' + str(a[0]) + '">' +
  str(a[1]) +
  '</option>')
 print('</select>')
else:
 print('</div>')
 print('<div class="inln">')
 for a in k1:
  if (a[0] == int(kind1)):
   k11 = a[1]
 print(k11)
 print('</div>')
 print('<div class="botn">')
 print('<input type="hidden" name="kind1" value="%s">' % kind1)

if not kind2:
 print('<select name="kind2" class="btn">')
 print('<option value=""></option>')
 for a in k2:
  print('<option value="' + str(a[0]) + '">' +
  str(a[1]) +
  '</option>')
 print('</select>')
else:
 print('</div>')
 print('<div class="inln">')
 for a in k2:
  if (a[0] == int(kind2)):
   k22 = a[1]
 print(k22)
 print('</div>')
 print('<div class="botn">')
 print('<input type="hidden" name="kind2" value="%s">' % kind2)

print('<br><select name="year" class="btn">')
print('<option value=""></option>')
for a in year:
 print('<option value="' + str(a[0]) + '">' +
 str(a[0]) +
 '</option>')
print('</select>')

print('<select name="month" class="btn">')
print('<option value=""></option>')
for a in month:
 print('<option value="' + str(a[0]) + '">' +
 str(a[0]) +
 '</option>')
print('</select>')

print('<br><select name="years" class="btn">')
print('<option value="0">0</option>')  
print('<option value="1" selected>1</option>')  
print('<option value="2">2</option>')  
print('<option value="3">3</option>')  
print('<option value="4">4</option>')  
print('<option value="5">5</option>')  
print('<option value="6">6</option>')

print('</select>')

print('<select name="months" class="btn">')
print('<option value="0">0</option>')  
print('<option value="1">1</option>') 
print('<option value="2">2</option>') 
print('<option value="3">3</option>') 
print('<option value="4">4</option>') 
print('<option value="5">5</option>') 
print('<option value="6">6</option>') 
print('<option value="7">7</option>') 
print('<option value="8">8</option>') 
print('<option value="9">9</option>') 
print('<option value="10">10</option>') 
print('<option value="11">11</option>')
print('</select>')


print('<br><input type="submit" value="browse" class="btn">')
print('<input type="checkbox" name="fixable" value="1">fixable')
print('<input type="checkbox" name="essen" value="1">essential')
print('<input type="checkbox" name="noessen" value="1">not&nbsp;essential')
print('</form>')

print('</div>')
print('<div class="normal">')
if str(yr) == 'None':
 print('Now - ' + str(years) + ' years ' + str(months) + ' months ago<br>')
else:
 print(str(yr) + '-' + str(mt) + ' - ' + str(years) + ' years ' + str(months) + ' months ago<br>')

print('amount:&nbsp;' + str(amountall[0][0]))
if str(fixable) == '1': 
 print('fixable')
print('<br></div>')
print('<hr width="400" size="10" align="center">')

print('<table border="2" align="center">')

i = 0
for lli in brows: 
 print('<tr>')

 for llist in brows[i]: 
  print('<td>')
  print(llist)
  print('</td>') 
 print('</tr>')
 i += 1
print('</table>')
print('</body>')
print('</html>')





cur.close()

sql.close()

