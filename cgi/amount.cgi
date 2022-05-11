#!/usr/bin/python3
import cgi
import subprocess
import mysql.connector
import cgitb
cgitb.enable()


print('Content-Type: text/html\n\n')
print('<html>')


print('<head>')
print('<meta charset="UTF-8">')
print('<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no" />')

print('<link rel="stylesheet" href="./style.css">')


print('</head>')
print('<body class="normal">')
print('<div class="normal">')

print('<br>')


print('<form action="kind1.cgi" method="post">')

print('amount:&nbsp</div>')
print('<div class="botn"><input type="text" inputmode="decimal" name="amount" class="box">')
print('</div><div class="normal"><br>comment:&nbsp')

print('</div><div class="botn"><input type="text" name="comment" class="box">')

print('</div>')

print('<div class="botn">')

print('<br><input type="submit" value="next" class="btn">')
print('</form>')
print('</div>')


print('</body>')
print('</html>')






