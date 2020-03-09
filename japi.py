import json
import urllib.request


def getStockData():
    infi = 1
    while infi == 1:
        sym = input('Enter a stock symbol: ')
        if sym != 'quit':
            nasdaqOgenURL = 'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=' + sym + '&outputsize=compact&apikey=VQ4HHVPG4QF7DFDP'
            connection = urllib.request.urlopen(nasdaqOgenURL)
            responseString = connection.read().decode()
            newresponseString = json.loads(responseString)
            print(responseString)
            print('The current price of ' + newresponseString['Global Quote']['01. symbol'] + ' is ' + newresponseString['Global Quote']['05. price'])
            with open('japi.out', 'a') as f:
                print(responseString, file=f)
        else:
            print('You have just quit.')
            break


if __name__ == '__main__':
    getStockData()
    print('Stock Quotes Retrieved Successfully')


# nasdaqOgenURL = 'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=OGEN&outputsize=compact&apikey=VQ4HHVPG4QF7DFDP'
# connection = urllib.request.urlopen(nasdaqOgenURL)
# responseString = connection.read().decode()
# print(responseString)


# def main():
#     while symbol is not 'quit':
#         symbol = input('Stock Symbol: ')
#         getStockData(symbol)

# alphaOgenURL = https://www.alphaavantage.co/query?function=BATCH_STOCK_QUOTES&symbols=OGEN&apikey=VQ4HHVPG4QF7DFDP


# from alpha_vantage.timeseries import *
# # Your key here
# key = 'VQ4HHVPG4QF7DFDP'
# ts = TimeSeries(key)
# aapl, meta = ts.get_daily(symbol='AAPL')
# print(aapl)
