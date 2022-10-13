import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API_KEY = "xxxxxxxxxxx"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = "xxxxxxxxxxxxxxxx"

# STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [
# new_value for (key, value) in dictionary.items()]
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}

response = requests.get(url=STOCK_ENDPOINT, params=stock_params)
response.raise_for_status()
stock_data = response.json()["Time Series (Daily)"]

# yesterdays_stock_data = stock_data["Time Series (Daily)"]["2022-10-12"]
# print(yesterdays_stock_data)
data_list = [value for (key, value) in stock_data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = float(yesterday_data["4. close"])

# Get the day before yesterday's closing stock price
day_before_data = data_list[1]
day_before_closing_price = float(day_before_data["4. close"])

# Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint:
# https://www.w3schools.com/python/ref_func_abs.asp
difference = yesterday_closing_price - day_before_closing_price
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

# Work out the percentage difference in price between closing price yesterday and closing price the day before
# yesterday.
diff_percent = (difference / yesterday_closing_price) * 100
print(diff_percent)
# If TODO4 percentage is greater than 5 then print("Get News").
# Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

news_params = {
    "qInTitle": COMPANY_NAME,
    "apikey": NEWS_API_KEY
}

if abs(diff_percent) > 1:
    response = requests.get(url=NEWS_ENDPOINT, params=news_params)
    response.raise_for_status()
    articles = response.json()["articles"]
    
    # Use Python slice operator to create a list that contains the first 3 articles. Hint:
    # https://stackoverflow.com/questions/509211/understanding-slice-notation
    
    # STEP 2: https://newsapi.org/
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
    three_articles = articles[:3]
    # STEP 3: Use twilio.com/docs/sms/quickstart/python
    # to send a separate message with each article's title and description to your phone number.

# Create a new list of the first 3 article's headline and description using list comprehension.
formatted_article = [
    f"{STOCK_NAME}:{up_down}{diff_percent}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for
    article in three_articles]

#Send each article as a separate message via Twilio.


client = Client(account_sid, auth_token)

for article in formatted_article:
    message = client.messages.create(
        body=article,
        from_='+15017122661',
        to='+15558675310'
    )
    print(message.status)

# Optional Format the message like this:
"""TSLA: 🔺2% Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. Brief: We at Insider Monkey have
gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings
show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or "TSLA: 🔻5% Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. Brief: We at Insider Monkey
have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F
filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus
market crash. """
