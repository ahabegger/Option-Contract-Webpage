import pymysql
from model import Option, options_chain


def sql_upload(ticker):
    db = pymysql.connect(host="localhost",  # your host
                         user="habegger",  # username
                         passwd="JzZCLgeDj.TJyo9f",  # password
                         db="Options")  # name of the database

    cur = db.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS `{0}` "
                "(`Contract_Name` varchar(150) NOT NULL,"
                "`Ticker` varchar(20) NOT NULL,"
                "`Underlying_Asset_Price` float NOT NULL,"
                "`Call / Put` varchar(10) NOT NULL,"
                "`Expire_Date` varchar(150) NOT NULL,"
                "`Days_Until_Expire` int(11) NOT NULL,"
                "`Last_Trade_Date` varchar(150) NOT NULL,"
                "`Strike_Price` float NOT NULL,"
                "`Last_Price` float NOT NULL,"
                "`Bid` float NOT NULL,"
                "`Volume` int(11) NOT NULL,"
                "`Open_Interest` float NOT NULL,"
                "`Implied_Volatility` float NOT NULL,"
                "`In_The_Money` tinyint(1) NOT NULL,"
                "`Delta` float NOT NULL,"
                "`Gamma` float NOT NULL,"
                "`Vega` float NOT NULL,"
                "`Theta` float NOT NULL,"
                "`Rho` float NOT NULL,"
                "`Calculated_Price` float NOT NULL) "
                "ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;".format(ticker))

    option_list = options_chain(ticker)
    cur.execute("SELECT `Contract_Name` FROM `{0}` WHERE 1;".format(ticker))
    completed_option_list = []

    for row in cur.fetchall():
        for x in range(0, len(row)):
            completed_option_list.append(str(row[x]))

    underlying_asset_price = option_list[0].updateAssetPrice()

    for option in option_list:
        if (option.contractSymbol not in completed_option_list):
            try:
                in_the_money = 1
                if (option.strike >= underlying_asset_price):
                    in_the_money = 0

                print("execute {0}".format(option.contractSymbol))
                cur.execute("INSERT INTO `{20}`(`Contract_Name`, `Ticker`, `Underlying_Asset_Price`,"
                            " `Call / Put`, `Expire_Date`, `Days_Until_Expire`, `Last_Trade_Date`, "
                            "`Strike_Price`, `Last_Price`, `Bid`, `Volume`, `Open_Interest`, "
                            "`Implied_Volatility`, `In_The_Money`, `Delta`, `Gamma`, `Vega`, "
                            "`Theta`, `Rho`, `Calculated_Price`) VALUES ('{0}','{1}',"
                            "{2},'{3}','{4}','{5}','{6}','{7}',"
                            "'{8}','{9}','{10}','{11}','{12}',"
                            "'{13}','{14}','{15}','{16}','{17}',"
                            "'{18}','{19}')".format(str(option.contractSymbol), str(option.ticker),
                                                    float(underlying_asset_price), str(option.type),
                                                    str(option.expire), int(option.daysUntilExpire()),
                                                    str(option.lastTradeDate), float(option.strike),
                                                    float(option.lastPrice), float(option.bid),
                                                    int(option.volume), float(option.openInterest),
                                                    float(option.impliedVolatility), in_the_money,
                                                    float(option.delta()), float(option.gamma()),
                                                    float(option.vega()), float(option.theta()),
                                                    float(option.rho()), float(option.calculated_price()),
                                                    str(ticker)))
                db.commit()
                print("Sent {0}".format(option.contractSymbol))
            except:
                print("error in {0}".format(option.contractSymbol))

    cur.close()
    del cur
    db.close()


def clear_all_tables():
    db = pymysql.connect(host="localhost",  # your host
                         user="habegger",  # username
                         passwd="JzZCLgeDj.TJyo9f",  # password
                         db="Options")  # name of the database

    cur = db.cursor()
    cur.execute("SHOW TABLES;")

    for row in cur.fetchall():
        for x in range(0, len(row)):
            print("Deleting {0}".format(row[x]))
            cur.execute("DELETE FROM `{0}` WHERE 1;".format(str(row[x])))
            db.commit()

    cur.close()
    del cur
    db.close()


def clear_table(tablename):
    db = pymysql.connect(host="localhost",  # your host
                         user="habegger",  # username
                         passwd="JzZCLgeDj.TJyo9f",  # password
                         db="Options")  # name of the database

    cur = db.cursor()
    cur.execute("DELETE FROM `{0}` WHERE 1;".format(tablename))
    db.commit()

    cur.close()
    del cur
    db.close()


if __name__ == "__main__":
    sql_upload("SPY")

