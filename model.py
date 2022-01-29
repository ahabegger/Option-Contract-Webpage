'''
Name : Alex Habegger
Link : https://pypi.org/project/yfinance/
Goal: Experiment with Black Scholes in Python
'''

import pandas as pd
import numpy as np
import yfinance as yf
from blackscholes import *
from datetime import date, datetime

class Option:
    def __init__(self, symbol, expire, type, contractSymbol, lastTradeDate, strike, lastPrice, bid, ask, volume, openInterest, impliedVolatility, inTheMoney):
        self.ticker = symbol
        self.assetPrice = 0
        self.expire = expire
        self.type = type
        self.contractSymbol = contractSymbol
        self.lastTradeDate = lastTradeDate
        self.strike = strike
        self.lastPrice = lastPrice
        self.bid = bid
        self.volume = volume
        self.openInterest = openInterest
        self.impliedVolatility = impliedVolatility
        self.inTheMoney = inTheMoney

    def print(self):
        print("Ticker: {0}".format(self.ticker))
        print("Expire: {0}".format(self.expire))
        print("Type: {0}".format(self.type))
        print("contractSymbol: {0}".format(self.contractSymbol))
        print("lastTradeDate: {0}".format(self.lastTradeDate))
        print("strike: {0}".format(self.strike))
        print("lastPrice: {0}".format(self.lastPrice))
        print("bid: {0}".format(self.bid))
        try:
            print("ask: {0}".format(self.ask))
        except:
            pass
        print("volume: {0}".format(self.volume))
        print("openInterest: {0}".format(self.openInterest))
        print("impliedVolatility: {0}".format(self.impliedVolatility))
        print("inTheMoney: {0}".format(self.inTheMoney))

    def calculated_price(self):
        self.updateAssetPrice()
        if(self.type == "Call"):
            return call_price(self.assetPrice, self.strike, self.daysUntilExpire(), self.impliedVolatility, .04, 0)
        else:
            return put_price(self.assetPrice, self.strike, self.daysUntilExpire(), self.impliedVolatility, .04, 0)

    def delta(self):
        self.updateAssetPrice()
        if(self.type == "Call"):
            return call_delta(self.assetPrice, self.strike, self.daysUntilExpire(), .04, self.impliedVolatility)
        else:
            return put_delta(self.assetPrice, self.strike, self.daysUntilExpire(), .04, self.impliedVolatility)

    def gamma(self):
        self.updateAssetPrice()
        if(self.type == "Call"):
            return call_gamma(self.assetPrice, self.strike, self.daysUntilExpire(), .04, self.impliedVolatility)
        else:
            return put_gamma(self.assetPrice, self.strike, self.daysUntilExpire(), .04, self.impliedVolatility)

    def vega(self):
        self.updateAssetPrice()
        if(self.type == "Call"):
            return call_vega(self.assetPrice, self.strike, self.daysUntilExpire(), .04, self.impliedVolatility)
        else:
            return put_vega(self.assetPrice, self.strike, self.daysUntilExpire(), .04, self.impliedVolatility)

    def theta(self):
        self.updateAssetPrice()
        if(self.type == "Call"):
            return call_theta(self.assetPrice, self.strike, self.daysUntilExpire(), .04, self.impliedVolatility)
        else:
            return put_theta(self.assetPrice, self.strike, self.daysUntilExpire(), .04, self.impliedVolatility)

    def rho(self):
        self.updateAssetPrice()
        if(self.type == "Call"):
            return call_rho(self.assetPrice, self.strike, self.daysUntilExpire(), .04, self.impliedVolatility)
        else:
            return put_rho(self.assetPrice, self.strike, self.daysUntilExpire(), .04, self.impliedVolatility)

    def implied_volatility(self, price):
        self.updateAssetPrice()
        if(self.type == "Call"):
            return call_implied_volatility(price, self.assetPrice, self.strike, self.daysUntilExpire(), .04)
        else:
            return put_implied_volatility(price, self.assetPrice, self.strike, self.daysUntilExpire(), .04)

    def updateAssetPrice(self):
        stock = yf.Ticker(self.ticker)
        price = stock.info['regularMarketPrice']
        self.assetPrice = price
        return price

    def daysUntilExpire(self):
        today = date.today()
        currentDate = today.strftime("%Y-%m-%d")
        d1 = datetime.strptime(self.expire, "%Y-%m-%d")
        d2 = datetime.strptime(currentDate, "%Y-%m-%d")
        daysLeft = abs((d2 - d1).days)
        return daysLeft


def options_chain(symbol):
    tk = yf.Ticker(symbol)
    expire_dates = tk.options
    created_options = []

    for expire in expire_dates:
        opts = tk.option_chain(expire)
        calls = opts.calls
        contractSymbol = calls['contractSymbol']
        lastTradeDate = calls['lastTradeDate']
        strike = calls['strike']
        lastPrice = calls['lastPrice']
        bid = calls['bid']
        ask = calls['ask']
        volume = calls['volume']
        openInterest = calls['openInterest']
        impliedVolatility = calls['impliedVolatility']
        inTheMoney = calls['inTheMoney']

        for x in range(0, int(contractSymbol.size-1)):
            created_option = Option(symbol, expire, "Call",contractSymbol[x], lastTradeDate[x], strike[x], lastPrice[x], bid[x], ask[x], volume[x], openInterest[x], impliedVolatility[x], inTheMoney[x])
            created_options.append(created_option)

    for expire in expire_dates:
        opts = tk.option_chain(expire)
        puts = opts.puts
        contractSymbol = puts['contractSymbol']
        lastTradeDate = puts['lastTradeDate']
        strike = puts['strike']
        lastPrice = puts['lastPrice']
        bid = puts['bid']
        ask = puts['ask']
        volume = puts['volume']
        openInterest = puts['openInterest']
        impliedVolatility = puts['impliedVolatility']
        inTheMoney = puts['inTheMoney']

        for x in range(0, int(contractSymbol.size-1)):
            created_option = Option(symbol, expire, "Put", contractSymbol[x], lastTradeDate[x], strike[x], lastPrice[x], bid[x], ask[x], volume[x], openInterest[x], impliedVolatility[x], inTheMoney[x])
            created_options.append(created_option)

    return created_options


if __name__ == "__main__":
    options_chain("AAPL")
