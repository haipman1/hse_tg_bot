import time

from textblob import TextBlob

import CDatabase
import CCrypto
import telebot


bot = telebot.TeleBot('5389806380:AAEIjAV6ndIqu-ZND2024HmQK67tQP2XIQQ')
cd = CDatabase
cc = CCrypto


def check_database():
    crypto_acts = ["", "", "BTC", "LTC", "ETH", "SOL", "TRX", "XRP", "DOT", "ATOM", "WAVES"]
    for_i = 2

    recs = CDatabase.get_records()

    for rec in recs:
        user_id = rec[0]
        while for_i <= 10:
            if rec[for_i] != 0:
                price = CCrypto.get_crypto_price(crypto_acts[for_i])
                print(price, 'price')
                trigger_price = float(rec[for_i])

                if rec[for_i] > 0:
                    if price >= trigger_price:
                        message = f"{crypto_acts[for_i]} was crossed the {trigger_price} line"
                        bot.send_message(user_id, message)
                        CDatabase.reset_curr(user_id, crypto_acts[for_i])

                if trigger_price < 0:
                    trigger_price = float(trigger_price) * (-1)
                    if price <= trigger_price:
                        message = f"{crypto_acts[for_i]} was crossed the {trigger_price} line"
                        bot.send_message(user_id, message)
                        CDatabase.reset_curr(user_id, crypto_acts[for_i])
            for_i += 1
        for_i = 2


if __name__ == '__main__':
    text = 'I love u very much!!!!!! :('
    blob = TextBlob(text)
    #print(blob.classify())

    print('Crypto Checker was enabled!')
    while True:
        check_database()
        time.sleep(30)
