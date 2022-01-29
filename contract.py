#!C:\xampp\htdocs\options\venv\Scripts\python.exe
import cgi,cgitb,pymysql
from model import Option, options_chain
cgitb.enable()

# Create instance of FieldStorage
form = cgi.FieldStorage()
contract = form.getvalue('contract')
ticker = form.getvalue('ticker')

db = pymysql.connect(host="localhost",  # your host
                     user="habegger",       # username
                     passwd="JzZCLgeDj.TJyo9f",     # password
                     db="Options")   # name of the database


cur = db.cursor()
cur.execute("SELECT * FROM `{0}` WHERE `Contract_Name` = '{1}';".format(ticker, contract))
sql_results = cur.fetchall()

print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<style>")
print("table, th, td {")
print("  border: 1px solid black;")
print("  border-collapse: collapse;")
print("  text-align: center;")
print("}")
print("</style>")
print("<title>{0} Contract</title>".format(contract))
print("</head>")
print("<body>")
print("<table>")
print("  <tr>")
print("    <th>Contract Name</th>")
print("    <th>Ticker</th>")
print("    <th>{0} Asset Price</th>".format(ticker))
print("    <th>Call / Put</th>")
print("    <th>Expire Date</th>")
print("    <th>Days Until Expire</th>")
print("    <th>Last Trade Date</th>")
print("    <th>Strike Price</th>")
print("    <th>Last Price</th>")
print("    <th>Bid</th>")
print("    <th>Volume</th>")
print("    <th>Open Interest</th>")
print("    <th>Implied Volatility</th>")
print("    <th>In The Money</th>")
print("    <th>Delta (<a href='delta.py?"
      "ticker={1}&contract={2}&value={0}'>"
      "&Delta;</a>)</th>".format(float(sql_results[0][14]),
                           ticker, contract))
print("    <th>Gamma (<a href='gamma.py?"
      "ticker={1}&contract={2}&value={0}'>"
      "&Gamma;</a>)</th>".format(float(sql_results[0][15]),
                           ticker, contract))
print("    <th>Vega (<a href='vega.py?"
      "ticker={1}&contract={2}&value={0}'>"
      "v</a>)</th>".format(float(sql_results[0][16]),
                           ticker, contract))
print("    <th>Theta (<a href='theta.py?"
      "ticker={1}&contract={2}&value={0}'>"
      "&Theta;</a>)</th>".format(float(sql_results[0][17]),
                           ticker, contract))
print("    <th>Rho (<a href='rho.py?"
      "ticker={1}&contract={2}&value={0}'>"
      "&Rho;</a>)</th>".format(float(sql_results[0][18]),
                           ticker, contract))
print("    <th>Calculated Price</th>")
print("  </tr>")

for row in sql_results :
    print("<tr>", end="")
    for x in range(0, len(row)):
        print("<td>", end="")
        print(str(row[x]))
        print("</td>")
    print("<tr>", end="")

print("</table>")

cur.close()
del cur
db.close()

print("<style>")
print(".bottom {")
print("  margin-top:20px;")
print("  text-align:right;")
print("  margin-right:25px;")
print("}")
print("</style>")
print("<p class='bottom'><a href='listings.py?ticker={0}'>Back</a></p>".format(ticker))

print("</body>")
print("</html>")
