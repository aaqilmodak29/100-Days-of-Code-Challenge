import requests
import datetime as dt
from twilio.rest import Client

NOW = dt.datetime.now()

today = NOW.today()
yesterday = str(today - dt.timedelta(days=1))
day_before_yesterday = str(today - dt.timedelta(days=2))

YESTERDAY = yesterday.split()[0]
DAY_BEFORE_YESTERDAY = day_before_yesterday.split()[0]

account_sid = ""  # your twilio account sid
auth_token = ""  # your twilio account token

FUNCTION = "TIME_SERIES_DAILY"

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_API_KEY = ""  # your stock api key
NEWS_API_KEY = ""  # your news api key

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

news_parameters = {
    "q": STOCK,
    "apiKey": NEWS_API_KEY
}

stock_parameters = {
    "function": FUNCTION,
    "symbol": STOCK,
    "apikey": STOCK_API_KEY
}

news_response = requests.get(url=NEWS_ENDPOINT, params=news_parameters)
news_data = news_response.json()

stock_response = requests.get(url=STOCK_ENDPOINT, params=stock_parameters)
stock_data = stock_response.json()

yesterday_close_price = float(stock_data["Time Series (Daily)"][YESTERDAY]["4. close"])
day_before_yest_close_price = float(stock_data["Time Series (Daily)"][DAY_BEFORE_YESTERDAY]["4. close"])

difference = abs(yesterday_close_price - day_before_yest_close_price)
diff_percent = round((difference / yesterday_close_price), 2) * 100
change_in_price = (diff_percent / 100) * yesterday_close_price

if diff_percent < 5:
    if yesterday_close_price > day_before_yest_close_price:
        arrowhead = "🔺"
    else:
        arrowhead = "🔻"

    news = news_data["articles"][:3]
    for i in range(len(news)):
        article_title = news[i]["title"]
        article_desc = news[i]["description"]
        article_url = news[i]["url"]

        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(
            body=f"\n{STOCK} {arrowhead}{diff_percent}%\nHeadline: {article_title}\nDescription: {article_desc}"
                 f"\nUrl: {article_url}",
            from_='',  # your twilio number
            to=''  # your number
        )
        print(message.status)
