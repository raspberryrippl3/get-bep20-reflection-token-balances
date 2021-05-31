#!/usr/bin/python3

import json
import requests
import csv
import arrow
from datetime import datetime

char_wallet = "<YOUR TRUST WALLET ADDRESS>"
char_contract = "0x6466849a30247d90f0c228a6c4b6b106ff18cab9"
bscscan_api_key = "<API KEY FOR BSCSCAN>"
cmc_api_key = "<COINMARKETCAP API KEY>"

charitas_balance_url = "https://api.bscscan.com/api?module=account&action=tokenbalance&contractaddress={0}&address={1}&tag=latest&apikey={2}".format(char_contract, char_wallet, bscscan_api_key)

# you will need to play with these division as different tokens required different conversions
charitas_balance = (float)(requests.get(charitas_balance_url).json()["result"]) / 1000000000000000000

charitas_prices_url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?CMC_PRO_API_KEY={}&symbol=CHAR".format(cmc_api_key)

response = requests.get(charitas_prices_url)
jsn = response.json()

pcs_timestamp = arrow.get( jsn["data"]["CHAR"]["quote"]["USD"]["last_updated"] )
value_usd = float(jsn["data"]["CHAR"]["quote"]["USD"]["price"]) * charitas_balance
value_usd = str(value_usd)

fields=[pcs_timestamp.to('Europe/London'), 'CHAR', charitas_balance, jsn["data"]["CHAR"]["quote"]["USD"]["price"], value_usd]

with open('charitas_balances.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(fields)
