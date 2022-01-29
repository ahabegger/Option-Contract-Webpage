#!C:\xampp\htdocs\options\venv\Scripts\python.exe
import cgi,cgitb,pymysql
from model import Option, options_chain
cgitb.enable()

# Create instance of FieldStorage
form = cgi.FieldStorage()
contract = form.getvalue('contract')
ticker = form.getvalue('ticker')
value = form.getvalue('value')

db = pymysql.connect(host="localhost",  # your host
                     user="habegger",       # username
                     passwd="JzZCLgeDj.TJyo9f",     # password
                     db="Options")   # name of the database


cur = db.cursor()

print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<style>")
print("table, th, td {")
print("  border: 1px solid black;")
print("  border-collapse: collapse;")
print("  text-align: center;")
print("  width: 50%")
print("}")
print("</style>")
print("<title>Delta - {0}</title>".format(contract))
print("</head>")
print("<body>")
print("<table>")
print("  <tr>")
print("    <th>Contract Name</th>")
print("    <th>Ticker</th>")
print("    <th>Delta</th>")
print("  </tr>")
print("<tr>", end="")
print("<td>{0}</td>".format(contract))
print("<td>{0}</td>".format(ticker))
print("<td>{0}</td>".format(value))
print("</tr>", end="")
print("</table>")

print("<style>")
print(".symbol {")
print("  margin-top:25px;")
print("  text-align:center;")
print("  font-size:70px;")
print("  font-weight: bold;")
print("  margin-bottom:0px;")
print("}")
print("</style>")
print("<p class='symbol'>&Delta;</p>")

if ('C' in contract):
    print("<h2>Delta Call Options</h2>")
    print("<ul>")
    print("   <li>Call options have a positive Delta that can range from 0.00 to 1.00.</li>")
    print("   <li>At-the-money options usually have a Delta near 0.50.</li>")
    print("   <li>The Delta will increase (and approach 1.00) as the option gets deeper ITM.</li>")
    print("   <li>The Delta of ITM call options will get closer to 1.00 as expiration approaches.</li>")
    print("   <li>The Delta of out-of-the-money call options will get closer to 0.00 as expiration approaches.</li>")
    print("</ul>")
else:
    print("<h2>Delta Put Options</h2>")
    print("<ul>")
    print("   <li>Put options have a negative Delta that can range from 0.00 to –1.00.</li>")
    print("   <li>At-the-money options usually have a Delta near –0.50.</li>")
    print("   <li>The Delta will decrease (and approach –1.00) as the option gets deeper ITM.</li>")
    print("   <li>The Delta of ITM put options will get closer to –1.00 as expiration approaches.</li>")
    print("   <li>The Delta of out-of-the-money put options will get closer to 0.00 as expiration approaches.</li>")
    print("</ul>")


cur.close()
del cur
db.close()

print("<style>")
print(".bottom {")
print("  margin-top:35px;")
print("  text-align:right;")
print("  margin-right:25px;")
print("}")
print("</style>")
print("<p class='bottom'><a href='contract.py?ticker={0}&contract={1}'>Back</a></p>".format(ticker, contract))

print("</body>")
print("</html>")
