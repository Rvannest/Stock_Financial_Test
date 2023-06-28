import requests


def fetch_financial_data(symbol):
    api_key = ''
    url = f'https://www.alphavantage.co/query?function=OVERVIEW&symbol={symbol}&apikey={api_key}'

    response = requests.get(url)
    data = response.json()

    # Extract the relevant financial data from the API response
    return data


def print_financial_data(symbol):
    financial_data = fetch_financial_data(symbol)

    print(financial_data)

    # stock_symbol = financial_data['Symbol']
    # current_price = financial_data['Price']
    # week_52_high = financial_data['52WeekHigh']
    # week_52_low = financial_data['52WeekLow']
    # current_ratio = financial_data['CurrentRatio']
    # return_on_equity = financial_data['ReturnOnEquity']
    # price_to_earnings_ratio = financial_data['PERatio']
    EPS = float(financial_data['EPS'])
    T_PE = float(financial_data['TrailingPE'])

    current_shareprice = EPS * T_PE

    # # Print the extracted financial data
    # print(f"Stock Symbol: {stock_symbol}")
    # # print(f"Current Price: {Global Quote}")
    # print(f"52 Week High: {week_52_high}")
    # print(f"52 Week Low: {week_52_low}")
    # print(f"Current Ratio: {current_ratio}")
    # print(f"Return on Equity: {return_on_equity}")
    # print(f"Price to Earnings Ratio: {price_to_earnings_ratio}")
    print(f"Current Share Price: {current_shareprice}")


# Call the function with the desired stock symbol
print_financial_data('AAPL')
