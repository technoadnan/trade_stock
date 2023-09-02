import requests, datetime
from twilio.rest import Client

# API keys
API_KEY_STOCK = "DLX7E9VOLXDYN078"
API_KEY_NEWS = "3ead2424d9cd4830b800b816ebe207c3"
STOCK = "TSLA"
COMPANY_NAME = "Tesla"

# fetching current date
dt = datetime.datetime.now()
today = datetime.date.today()
year = dt.year
yesterday = (today - datetime.timedelta(days=1)).strftime("%d")
# yesterday_month = "{:02d}".format(yesterday.month) 
yesterday_month = "{:02d}".format((today - datetime.timedelta(days=1)).month)
day_before_yesterday = (today - datetime.timedelta(days=2)).strftime("%d")
day_before_yesterday_month = "{:02d}".format((today - datetime.timedelta(days=2)).month)

# # STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News"). find the closing value

# parameters_alphavantage = {
#    "function" : "TIME_SERIES_DAILY",
#    "symbol" : STOCK,
#    "apikey" : API_KEY_STOCK,
#    "outputsize":"compact"
# }

# api_stock_response = requests.get("https://www.alphavantage.co/query", params=parameters_alphavantage)
# parased_value = api_stock_response.json()
# # print(parased_value)
# each_day = parased_value["Time Series (Daily)"]
# yesterday_stock = each_day[f"{year}-{yesterday_month}-{yesterday}"]["4. close"]
# day_before_yesterday_stock = each_day[f"{year}-{day_before_yesterday_month}-{day_before_yesterday}"]["4. close"]
# print(yesterday_stock)
# print("hello",day_before_yesterday_stock)
# difference = round(float(yesterday_stock) - float(day_before_yesterday_stock), 3)
# percentage = round((difference / float(day_before_yesterday_stock) ) * 100, 3)
# print(percentage)

# # STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

parameters_news_api = {
    "q" : COMPANY_NAME,
    "apikey" : API_KEY_NEWS,
	"pageSize" : 3,
	# "language" : "en"
}
api_news_response = requests.get("https://newsapi.org/v2/top-headlines", params=parameters_news_api)
parased_data_news = api_news_response.json()
article = parased_data_news["articles"]
headline = ""
brief = ""
# for j in article:
# 	if j["title"] != None:
# 	# print(f"Headline: {j['title']}")
# 		headline = headline + j["title"] + "\n"
# 	if j["description"] != None:
# 		# print(f"Brief: {j['description']}")
# 		brief = brief + j["description"] + "\n"
# 	# print("\n\n")
# print(headline)
# print(brief)

account_sid = 'AC4ef5bbcc86e56aabccdb845d40b66335'
auth_token = 'cf00da3c91ccbe9161bd01f65fd6ef35'
client = Client(account_sid, auth_token)
for j in article:
	percentage = 5
	if percentage >= 5 or percentage <= -5:
		headline = ""
		description = ""
		if j["title"] != None:
			headline = f"Headline: {j['title']}"
			# headline = headline + j["title"] + "\n"
		if j["description"] != None:
			description = f"Brief: {j['description']}"
			# brief = brief + j["description"] + "\n"
		
		print(headline,"\n",description)
	message = client.messages.create(
	from_='+18556574218',
	body=f"{headline}--{description}",
	to='+18455780882'
	)
		# print(message.sid)


## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 



#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

