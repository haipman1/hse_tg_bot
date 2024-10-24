import telebot
from telebot import types

import CDatabase

bot = telebot.TeleBot('5389806380:AAEIjAV6ndIqu-ZND2024HmQK67tQP2XIQQ')


def telebotmain():
    def get_text(message):
        name = message.text
        bot.send_message(message.chat.id, name)

    @bot.callback_query_handler(func=lambda call: True)
    def callback_worker(call):
        cd = CDatabase
        if call.data == "btc_add_on_check":
            bot.send_message(call.message.chat.id, 'Select price trigger[BTC]')
            bot.register_next_step_handler(call.message, cd.add_trigger, "BTC", call.message.chat.id)

        elif call.data == "ltc_add_on_check":
            bot.send_message(call.message.chat.id, 'Select price trigger[LTC]')
            bot.register_next_step_handler(call.message, cd.add_trigger, "LTC", call.message.chat.id)
        elif call.data == "eth_add_on_check":
            bot.send_message(call.message.chat.id, 'Select price trigger[ETH]')
            bot.register_next_step_handler(call.message, cd.add_trigger, "ETH", call.message.chat.id)
        elif call.data == "sol_add_on_check":
            bot.send_message(call.message.chat.id, 'Select price trigger[SOL]')
            bot.register_next_step_handler(call.message, cd.add_trigger, "SOL", call.message.chat.id)
        elif call.data == "trx_add_on_check":
            bot.send_message(call.message.chat.id, 'Select price trigger[TRX]')
            bot.register_next_step_handler(call.message, cd.add_trigger, "TRX", call.message.chat.id)
        elif call.data == "xrp_add_on_check":
            bot.send_message(call.message.chat.id, 'Select price trigger[XRP]')
            bot.register_next_step_handler(call.message, cd.add_trigger, "XRP", call.message.chat.id)
        elif call.data == "dot_add_on_check":
            bot.send_message(call.message.chat.id, 'Select price trigger[DOT]')
            bot.register_next_step_handler(call.message, cd.add_trigger, "DOT", call.message.chat.id)
        elif call.data == "atom_add_on_check":
            bot.send_message(call.message.chat.id, 'Select price trigger[ATOM]')
            bot.register_next_step_handler(call.message, cd.add_trigger, "ATOM", call.message.chat.id)
        elif call.data == "waves_add_on_check":
            bot.send_message(call.message.chat.id, 'Select price trigger[WAVES]')
            bot.register_next_step_handler(call.message, cd.add_trigger, "WAVES", call.message.chat.id)

    @bot.message_handler(content_types=['text'])
    def start(message):
        if message.text == '/start':
            isNew = CDatabase.is_new_user(message.from_user.id)
            if isNew:
                bot.send_message(message.from_user.id, "Welcome!")
                CDatabase.reg_new_user(message.from_user.id)
            if not isNew:
                bot.send_message(message.from_user.id, "Hello")
        elif message.text == '/add_trigger' or message.text == '/at':
            crypto_acts = ["BTC", "LTC", "ETH", "SOL", "TRX", "XRP", "DOT", "ATOM", "WAVES"]

            CDatabase.is_new_user_and_reg(message.from_user.id)
            keyboard = types.InlineKeyboardMarkup()
            for i in crypto_acts:
                call_data_text = str.lower(i) + '_add_on_check'
                key_yes = types.InlineKeyboardButton(text=i, callback_data=call_data_text)
                keyboard.add(key_yes)

            bot.send_message(message.from_user.id, "Select trigger", reply_markup=keyboard)
        elif message.text == '/print_all' or message.text == '/pa':
            data = CDatabase.get_all_user_data(message.from_user.id)
            bot.send_message(message.from_user.id, str(data))
        elif message.text == '/reset_all' or message.text == '/ra':
            CDatabase.reset_all(message.from_user.id)
        elif message.text[0] == '/':
            print('ep')
            bot.send_message(message.from_user.id, "You can use commands: \n/start\n"
                                                   "/add_trigger\n/print_all\n/reset_all\n")

    bot.polling(none_stop=True, interval=0)