import config
import telebot

bot = telebot.TeleBot(config.token)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    bot.send_message(message.chat.id, message.chat.first_name + ', you sent this message: ' + message.text)

if __name__ == '__main__':
     bot.polling(none_stop=True)