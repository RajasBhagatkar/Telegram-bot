import telegram.ext
import pandas_datareader as web #this is to fetch the finance related data from the web
from CryptoCoin import *

# 2118270714:AAHsN9Tup5bARDNYa4I2RxTCmXgJurCIaH8
TOKEN = '2118270714:AAHsN9Tup5bARDNYa4I2RxTCmXgJurCIaH8'
# with open("Token.txt", 'r') as f:
#     TOKEN = f.read()

# print(TOKEN)

def start(update, context):
    update.message.reply_text(f"Hello! welcome to the Bot! "
                              f" here you will find all the cryptcoin prices..")

def help(update, context):
    update.message.reply_text("""
    The Following commands are available:
    /start -> Welcome Message
    /help -> This Message
    /content -> Information About Movies Content
    
    ***New***
    
    /coin -> get the price of the all the crypto coins
    '''IMP:all prices in INR enter the name correctly
     '''
    /stock -> gives the current price of the stock
    /contact -> Information about Contact
    """)
def content(update, context):
    update.message.reply_text("We have videos and books! Watch and read them!")

def contact(update, context):
    update.message.reply_text("you can contact Florien on Telegram")

updater = telegram.ext.Updater(TOKEN, use_context=True)
disp = updater.dispatcher

def handle_message(update, context):
    # update.message.reply_text(f"You said {update.message.text}")
    update.message.reply_text(f'sorry you said "{update.message.text}" invalid command try using "/" at the beging')


def stock(update, context):
    ticker = context.args[0]
    # /stock AAPL   second  third
    #        args[0] args[1] args[2]
    data = web.DataReader(ticker, 'yahoo')
    price = data.iloc[-1]['Close']
    update.message.reply_text(f"The current price of the {ticker} is {price:.2f}$!")

def coin(update, context):
   # return get_crypto_price(context.args[0])
   #  _coin = context.args[0]
   try:
       update.message.reply_text(get_crypto_price(context.args[0]))
   except:
       update.message.reply_text(f'sorry can\'t find {context.args[0]} pls check spelling')

disp.add_handler(telegram.ext.CommandHandler("coin",coin))
disp.add_handler(telegram.ext.CommandHandler("start", start))
disp.add_handler(telegram.ext.CommandHandler("help", help))
disp.add_handler(telegram.ext.CommandHandler("content",content))
disp.add_handler(telegram.ext.CommandHandler("contact",contact))
disp.add_handler(telegram.ext.CommandHandler('stock', stock))
disp.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, handle_message))



updater.start_polling()
updater.idle()

# print('its runing')