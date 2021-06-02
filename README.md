# Simple Python script to get BEP-20 Refelction Token wallet balances

Reflection tokens are BEP-20 contracts that have a transaction tax, which gets distributed to every holder of that token when a transaction occurs, normally in the range of 2% to 5%

Trust Wallet is the popular means of holding wallet balances but it has no way of tracking over time how many additional tokens are added to your wallet address or any way of exporting this data

This simple script will do this in a CSV file, as well as log wallet value, over time. You'll need two API keys:

1. BSCscan to get your current wallet balance
2. CoinMarketCap API to get the latets quote price in USD

There are rate limits on these APIs. I have three scripts running via CRON every 30 minutes on an always on Raspberry PI Zero
