import config
import telebot

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start'])
def send_welcome_for_start(message):
	bot.send_message(message.chat.id, "G'day, " + message.chat.first_name + "! How are you doing? I can do all the things in this world. Just write down what you want.")

@bot.message_handler(commands=['help'])
def send_help_message(message):
	bot.send_message(message.chat.id, "If you want to do 1, just do 1. \nIf you want to do 2, just do 2.")

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    bot.send_message(message.chat.id, message.chat.first_name + ', you sent this message: ' + message.text)

if __name__ == '__main__':
     bot.polling(none_stop=True)