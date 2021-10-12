import datetime
import time

import tweepy
import os
import pprint
import requests

CONSUMER_API_KEY = os.environ.get('CONSUMER_API_KEY')
CONSUMER_API_SECRET = os.environ.get('CONSUMER_API_SECRET')
ACCESS_API_KEY = os.environ.get('ACCESS_API_KEY')
ACCESS_API_SECRET = os.environ.get('ACCESS_API_SECRET')

auth = tweepy.OAuthHandler(CONSUMER_API_KEY, CONSUMER_API_SECRET)
auth.set_access_token(ACCESS_API_KEY, ACCESS_API_SECRET)
pprint = pprint.PrettyPrinter()

list_low_price = []
last_sold = ""

def send_t(message, image_url=None):
    if CONSUMER_API_SECRET and CONSUMER_API_KEY and ACCESS_API_SECRET and ACCESS_API_KEY:
        auth = tweepy.OAuthHandler(CONSUMER_API_KEY, CONSUMER_API_SECRET)
        auth.set_access_token(ACCESS_API_KEY, ACCESS_API_SECRET)

        filename = './temp.png'
        request = requests.get(image_url, stream=True)
        if request.status_code == 200:
            with open(filename, 'wb') as image:
                for chunk in request:
                    image.write(chunk)

        api = tweepy.API(auth)
        api.update_with_media(filename, status=message)

        # image_file = Image.open(filename)
        # image_file.save(filename, quality=5)
        # api.update_profile_image(filename)
        os.remove(filename)
    else:
        print('message not sent')

    print(f'--------------- message messaged send: {message}---------------')


def send_message(number, price_bnb, price_usd, buyer, txhash):
    global  list_low_price
    global last_sold
    message = f"""
PancakeSquad {number} has been sold for {price_bnb:.3f} $BNB (~{price_usd:.3f} $) placed by {buyer}
🐰 https://pancakeswap.finance/nfts/collections/0x0a8901b0E25DEb55A87524f0cC164E9644020EBA/{number} 🐰
🔗 https://www.bscscan.com/tx/{txhash} 🔗

#PancakeSquad #PancakeSwap #binanceChain
"""
    url = f"https://static-nft.pancakeswap.com/mainnet/0x0a8901b0E25DEb55A87524f0cC164E9644020EBA/pancake-squad-{number}-1000.png"
    if number != last_sold:
        send_t(message, url)
    last_sold = number
