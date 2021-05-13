import telebot
import time
from hashlib import sha256

# sorry for shit code :)

bot = telebot.TeleBot("BOT TOKEN", parse_mode=None)  # paste your telegram bot token

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to ByteToken Core")
    bot.reply_to(message, "/mine - start mining")
    bot.reply_to(message, "/import - import your last balance")


@bot.message_handler(commands=['mine'])
def send_money(message):
    balance = float
    balance = 0.0
    i = 1
    while i > 0:
        time.sleep(0.5)
        reward = float
        reward = 0.0001  # mining reward
        balance = balance + reward
        blnc = str(balance) + "Key Password (Change to your own)"  # don`t forget to change it!!!
        cid10 = message.chat.id
        balancekey = sha256(blnc.encode('utf-8')).hexdigest()
        bot.send_message(cid10, "Your new balance - "+ str(balance)+" BYTE")
        bot.send_message(cid10, "Your new balance key - " + str(balancekey))
        time.sleep(3.5)

@bot.message_handler(commands=['import'])
def send_a(message):
    try:
        cid20 = message.chat.id
        blnc = bot.send_message(cid20, "Type your balance:")
        bot.register_next_step_handler(blnc, echo_i)
    except Exception:
        bot.reply_to(message, "Error")
        pass
def echo_i(message):
    try:
        blncd = message.text
        blnc_pkk = blncd + "Key Password (Change to your own)"  # don`t forget to change it!!!
        pkeyy = sha256(blnc_pkk.encode('utf-8')).hexdigest()
        cid30 = message.chat.id
        addrkeyy = bot.send_message(cid30, "Type your balance key:")
        bot.register_next_step_handler(addrkeyy, echo_ii, pkeyy, blncd)
    except Exception:
        bot.reply_to(message, "Error")
        pass
def echo_ii(message , pkeyy , blncd):
        if message.text == pkeyy:
            bot.reply_to(message, "Wallet imported successful!")
            bot.reply_to(message, "Your balance - " + str(blncd) + " BYTE")
            balance = float(blncd)
            i = 1
            while i > 0:
                time.sleep(0.5)
                reward = float
                reward = 0.0001  # mining reward
                cid100 = message.chat.id
                balance = balance + reward
                blnc = str(balance) + "Key Password (Change to your own)"  # don`t forget to change it!!!
                balancekey = sha256(blnc.encode('utf-8')).hexdigest()
                bot.send_message(cid100, "Your new balance - " + str(balance) + " BYTE")
                bot.send_message(cid100, "Your new balance key - " + str(balancekey))
                time.sleep(3.5)
        else:
            bot.reply_to(message, "Fail")
bot.polling()