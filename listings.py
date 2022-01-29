#!C:\xampp\htdocs\options\venv\Scripts\python.exe
import cgi,cgitb,pymysql
from model import Option, options_chain
cgitb.enable()

# Create instance of FieldStorage
form = cgi.FieldStorage()
ticker = form.getvalue('ticker')

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
print("}")
print("</style>")
print("<title>{0} Listings</title>".format(ticker))
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
print("    <th>Delta</th>")
print("    <th>Gamma</th>")
print("    <th>Vega</th>")
print("    <th>Theta</th>")
print("    <th>Rho</th>")
print("    <th>Calculated Price</th>")
print("  </tr>")

cur.execute("SELECT * FROM `{0}` WHERE 1".format(ticker))
for row in cur.fetchall() :
    print("<tr>", end="")
    for x in range(0, len(row)):
        print("<td>", end="")
        if (x == 0):
            print("<a href='contract.py?ticker={1}&contract={0}'>{0}</a>".format(str(row[x]), str(ticker)))
        else:
            print(str(row[x]))
        print("</td>")
    print("</tr>", end="")

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
print("<p class='bottom'><a href='index.html'>Back</a></p>")

print("</body>")
print("</html>")
