'''
Name : Alex Habegger
Link : https://pypi.org/project/yfinance/
Goal: Experiment with Black Scholes in Python
'''

import gspread
from oauth2client.service_account import ServiceAccountCredentials
from blackscholes import *
from model import Option, options_chain
import pandas as pd

def authorize(filename):
    scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

    # Assign credentials ann path of style sheet
    creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
    client = gspread.authorize(creds)
    return client.open(filename).sheet1






if __name__ == "__main__":
    sheet = authorize("Option_Pricing")
    option_list = options_chain("MSFT")


    df = pd.DataFrame()
    for option in option_list:
        d = {'contractSymbol' : [option.contractSymbol]}
        df_add = pd.DataFrame(data=d)
        df.append(df_add)

    print(df)

exit(1)
