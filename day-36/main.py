import requests
import os
from newsapi import NewsApiClient
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
COMPANY = "Tesla"
STOCK_API_KEY = os.environ.get('STOCKAPIKEY')
NEWS_API_KEY = os.environ.get('NEWSAPIKEY')


account_sid = os.getenv('account_sid')
auth_token = os.getenv('auth_token')
client = Client(account_sid,auth_token)

stock_url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={STOCK}&apikey={STOCK_API_KEY}'
r = requests.get(stock_url)
data = r.json()

daily_data = data['Time Series (Daily)']

# Todo: Get Stock Price from Close Yesterday, and Close Today of Given Share

def check_fluctation(data):
    first_day = list(data.keys())[0]
    second_day = list(data.keys())[1]
    first_data = float(data[first_day]['4. close'])
    second_data = float(data[second_day]['4. close'])
    change = (second_data - first_data) / first_data * 100
    
    if change > 0:
        direction = '🔺'
    else:
        direction = '🔻'
    
    if change >= 1 or change <= -1:
        articles = get_news(first_day,second_day)
        
        
        message = f"""{STOCK}: {direction}{change}%
Headline: {articles[0]['title']}. 
Brief: {articles[0]['description']}"""
        
        client.messages \
                .create(
                     body=message,
                     from_='+17792092661',
                     to='+64272042978'
                 )

#Todo If fluctuation is greater than X% trigger the following steps

def get_news(first_day,second_day):
    news_url = 'https://newsapi.org/v2/everything'
    news_parameters = {
        "q": f"{COMPANY} stock price",
        "searchIn": "content",
        "from": second_day,
        "to": first_day,
        "language": "en",
        "sortBy": "relevancy",
        "apiKey": NEWS_API_KEY
    }
    news_r = requests.get(news_url,params=news_parameters)
    news_data = news_r.json()
    return news_data['articles'][:2]


check_fluctation(daily_data)
