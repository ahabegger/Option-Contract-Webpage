#README.md
##Black Scholes Model in Python
This is a Python implementation of the Black Scholes Model for option pricing, along with a collection of helper functions for calculating option Greeks and implied volatility. The code also includes a basic MySQL database interaction to upload option data.

##Overview
The Black-Scholes Model is a mathematical model for pricing European options. It makes certain assumptions:

* No dividends are paid out during the life of the option.
* Markets are random (i.e., market movements cannot be predicted).
* There are no transaction costs in buying the option.
* The risk-free rate and volatility of the underlying asset are known and constant.
* The returns on the underlying asset are log-normally distributed.
* The option is European and can only be exercised at expiration.
Usage

The main functions provided by this code are:

* black_scholes(s, k, t, v, rf, div, cp): Price an option using the Black-Scholes model.
* call_price(s, k, t, v, rf, div): Calculate the price of a call option.
* put_price(s, k, t, v, rf, div): Calculate the price of a put option.
* call_delta, call_gamma, call_vega, call_theta, call_rho: Calculate the Greeks for call options.
* put_delta, put_gamma, put_vega, put_theta, put_rho: Calculate the Greeks for put options.
* call_implied_volatility(Price, S, K, T, r): Calculate the implied volatility for call options.
* put_implied_volatility(Price, S, K, T, r): Calculate the implied volatility for put options.

##Database Interaction
The code includes functions to interact with a MySQL database:

* sql_upload(ticker): Upload options data for a given ticker to a MySQL database.
* clear_all_tables(): Clear all tables in the MySQL database.
* clear_table(tablename): Clear a specific table in the MySQL database.

##Author
**Alex Habegger**
print("Num : {0}".format(test1))
print("Num : {0}".format(test2))
print("Num : {0}".format(test3))
Requirements
Python 3.x
scipy library
pymysql library
Author
Alex Habegger
