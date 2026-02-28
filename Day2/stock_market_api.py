#____________________________________________________________________________
# Example 1

# import requests

# API_KEY= "4IKJYCZOM9FEX5UL" 

# api_url = "https://www.alphavantage.co/"    

# def get_stock_market_data(symbol):

#     query = f"query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={API_KEY}"

#     response = requests.get(url=api_url + query)  
#     # print(response.json())  

#     for key,value in response.json().items():
#         # if key == "Time Series (Daily)":
#         #     for date, data in value.items():
#         #         print(f"Date: {date}")
#         #         print(f"Open: {data['1. open']}")
#         #         print(f"High: {data['2. high']}")
#         #         print(f"Low: {data['3. low']}")
#         #         print(f"Close: {data['4. close']}")
#         #         print(f"Volume: {data['5. volume']}")
#         #         print("-" * 30)
        
#         if key == "Meta Data":
#             print("Stock Symbol:", value["2. Symbol"])
#             print("Last Refreshed:", value["3. Last Refreshed"])
#             print("Time Zone:", value["5. Time Zone"])

# symbol = input("Enter the stock symbol you want for the stock market API eg. (AMZN, AAPL, MSFT, GOGL, IBM, etc): ")
# get_stock_market_data(symbol)


#____________________________________________________________________________
# Example 2

import requests

API_KEY= "4IKJYCZOM9FEX5UL" 

api_url = "https://www.alphavantage.co/"    

def get_stock_market_data(symbol,is_timeseries):
    if is_timeseries:
        query = f"query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={API_KEY}"
    else:
        query = f"query?symbol={symbol}&apikey={API_KEY}"

    response = requests.get(url=api_url + query)  
    # print(response.json())  

    for key,value in response.json().items():
        if is_timeseries:
            print(key,":", value)
        
        else:
            if key == "Time Series (Daily)":
                for date, data in value.items():
                    continue


symbol = input("Enter the stock symbol you want for the stock market API eg. (AMZN, AAPL, MSFT, GOGL, IBM, etc): ")
is_timeseries = True
get_stock_market_data(symbol,is_timeseries)