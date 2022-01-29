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
print("<title>Vega - {0}</title>".format(contract))
print("</head>")
print("<body>")
print("<table>")
print("  <tr>")
print("    <th>Contract Name</th>")
print("    <th>Ticker</th>")
print("    <th>Vega</th>")
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
print("<p class='symbol'>v</p>")

print("<h2>Vega Options</h2>")
print("<ul>")
print("   <li>Vega measures the rate of change in an option’s price per one-percentage-point change in the implied volatility of the underlying stock.</li>")
print("   <li>Volatility is one of the most important factors affecting the value of options.</li>")
print("   <li>A drop in Vega will typically cause both calls and puts to lose value.</li>")
print("   <li>An increase in Vega will typically cause both calls and puts to gain value.</li>")
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
