# getting the price of the bitcoin by their name
import math

from bs4 import BeautifulSoup
import  requests

import time

# getting the indian price of the internet
def inr_price():
    url = "https://www.xe.com/currencyconverter/convert/?Amount=1&From=USD&To=INR"
    html = requests.get(url)

    soup = BeautifulSoup(html.text, "html.parser")

    inr = soup.find('p', attrs={'class': "result__BigRate-sc-1bsijpp-1 iGrAod"}).text
    inr = math.floor(float(inr[:-14]))   #now the inr is the int
    return inr


def get_crypto_price(coin):
    url = f"https://coinmarketcap.com/currencies/{coin}/"  # here avalanche is the name of the coin
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'html.parser')

    text = soup.find('div', attrs={'class':"priceValue"}).text
    # text = soup.find('div', attrs={"class": "BNeawe iBp4i AP7Wnd"}).find('div',attrs={"class": "BNeawe iBp4i AP7Wnd"}).text
    price = text[1:]  #this remove the $
    price = price.replace(',','')
    price = float(price)
    return f"{price * inr_price()} Indian Rupees"

# print(get_crypto_price('bitcoin'))
# print(inr_price())
# print(type(inr_price()))