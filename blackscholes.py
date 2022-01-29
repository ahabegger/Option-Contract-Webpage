'''
Name : Alex Habegger
Link : https://miamioh.instructure.com/courses/160636/files/folder/Project?preview=23048333
Goal: Experiment with Black Scholes in Python
'''

from scipy import stats
from scipy.stats import norm
import math

'''
The Black-Scholes model makes certain assumptions:
 - No dividends are paid out during the life of the option.
 - Markets are random (i.e., market movements cannot be predicted).
 - There are no transaction costs in buying the option.
 - The risk-free rate and volatility of the underlying asset are known and constant.
 - The returns on the underlying asset are log-normally distributed.
 - The option is European and can only be exercised at expiration.
'''
def black_scholes(s, k, t, v, rf, div, cp):
    '''
    Price an option using the  Black-Scholes model

    :param s: initial stock price
    :param k: strike price
    :param t: expiration time
    :param v: volatility
    :param rf: risk-free rate
    :param div: dividend
    :param cp: +1 / -1 for call/put
    :return: option price
    '''

    d1 = (math.log(s/k)+(rf-div+0.5*math.pow(v,2))*t)/(v*math.sqrt(t))
    d2 = d1 - v*math.sqrt(t)
    optprice = cp*s*math.exp(-div*t)*stats.norm.cdf(cp*d1) - cp*k*math.exp(-rf*t)*stats.norm.cdf(cp*d2)

    return optprice

''' HELPER FUNCTIONS '''

def d1(S,K,T,r,sigma):
    return(math.log(S/K)+(r+sigma**2/2.)*T)/(sigma*math.sqrt(T))

def d2(S,K,T,r,sigma):
    return d1(S,K,T,r,sigma)-sigma*math.sqrt(T)


''' CALLS '''

def call_price(s, k, t, v, rf, div):
    return black_scholes(s, k, t, v, rf, div, 1)

''' THE GREEKS (CALLS) '''

def call_delta(S, K, T, r, sigma):
    '''
    S = spot price of an asset
    K = strike price
    r = risk-free interest rate
    t = time to maturity
    σ = volatility of the asset
    '''
    return norm.cdf(d1(S, K, T, r, sigma))

def call_gamma(S, K, T, r, sigma):
    return norm.pdf(d1(S, K, T, r, sigma)) / (S * sigma * math.sqrt(T))

def call_vega(S, K, T, r, sigma):
    return 0.01 * (S * norm.pdf(d1(S, K, T, r, sigma)) * math.sqrt(T))

def call_theta(S, K, T, r, sigma):
    return 0.01 * (-(S * norm.pdf(d1(S, K, T, r, sigma)) * sigma) / (2 * math.sqrt(T)) - r * K * math.exp(-r * T) * norm.cdf(
        d2(S, K, T, r, sigma)))

def call_rho(S, K, T, r, sigma):
    return 0.01 * (K * T * math.exp(-r * T) * norm.cdf(d2(S, K, T, r, sigma)))

def call_implied_volatility(Price, S, K, T, r):
    sigma = 0.001
    while sigma < 1:
        Price_implied = S * \
            norm.cdf(d1(S, K, T, r, sigma))-K*math.exp(-r*T) * \
            norm.cdf(d2(S, K, T, r, sigma))
        if Price-(Price_implied) < 0.001:
            return sigma
        sigma += 0.001
    return "Not Found"


''' PUTS '''

def put_price(s, k, t, v, rf, div):
    return black_scholes(s, k, t, v, rf, div, -1)

''' THE GREEKS (PUTS) '''

def put_delta(S, K, T, r, sigma):
    return -norm.cdf(-d1(S, K, T, r, sigma))

def put_gamma(S, K, T, r, sigma):
    return norm.pdf(d1(S, K, T, r, sigma)) / (S * sigma * math.sqrt(T))

def put_vega(S, K, T, r, sigma):
    return 0.01 * (S * norm.pdf(d1(S, K, T, r, sigma)) * math.sqrt(T))

def put_theta(S, K, T, r, sigma):
    return 0.01 * (-(S * norm.pdf(d1(S, K, T, r, sigma)) * sigma) / (2 * math.sqrt(T)) + r * K * math.exp(-r * T) * norm.cdf(
        -d2(S, K, T, r, sigma)))

def put_rho(S, K, T, r, sigma):
    return 0.01 * (-K * T * math.exp(-r * T) * norm.cdf(-d2(S, K, T, r, sigma)))

def put_implied_volatility(Price, S, K, T, r):
    sigma = 0.001
    while sigma < 1:
        Price_implied = K*math.exp(-r*T)-S+bs_call(S, K, T, r, sigma)
        if Price-(Price_implied) < 0.001:
            return sigma
        sigma += 0.001
    return "Not Found"


if __name__ == "__main__":
    test1 = black_scholes(100.0, 100.0, 1.0, 0.3, 0.03, 0.0, -1)
    test2 = call_price(100.0, 100.0, 1.0, 0.3, 0.03, 0.0)
    test3 = put_price(100.0, 100.0, 1.0, 0.3, 0.03, 0.0)

    print("Num : {0}".format(test1))
    print("Num : {0}".format(test2))
    print("Num : {0}".format(test3))

