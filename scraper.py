import requests
import smtplib
import time
from bs4 import BeautifulSoup

# Given url, in future i plan on submitting these through forms
URL = 'https://www.amazon.com/Alexa-Developer-T-Shirt-August-2016/dp/B07P76X1C7/ref=pd_ybh_a_3?_encoding=UTF8&psc=1&refRID=1Z8B3PH0Z6VZNVZQ9R50'


# google chrome user agent
headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}

# as title states it checks the price of a given object
def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'lxml')

    title = soup.find(id='productTitle').get_text()

    price = soup.find(id='priceblock_ourprice').get_text()
# converts string price to float
    converted_price = float(price[1:5])
    if(converted_price < 15):
        send_mail()

# uses smtp to send mail 
def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('igleciasjoseph@gmail.com', 'disttejimiheaotp')

    subject = 'Price fell down!'
    body = f'Check the amazon link {URL}'

    msg = f'Subject: {subject}\n\n{body}'

    server.sendmail(
        'igleciasjoseph@gmail.com',
        'igleciasjoseph@gmail.com',
        msg
    )
    print('EMAIL HAS BEEN SENT')
    server.quit()

# will check both methods and if they are true it will send mail
while(True):
    check_price()
    time.sleep(10)