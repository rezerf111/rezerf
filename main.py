from token import token
import telebot 


bot = telebot.TeleBot(token["Token"])

@bot.message_hendler(commands=["start"])
def start_func(message):
    bot.send_message(message.chat.id, "как тебя зовут?")


@bot.message_hendler(content_types=["text"])
def hello(message):
    msg = bot.send_message(message.chat.id, f"Привет, {message.text}")
    #msg = bot.register_next_step_handler(msg, name)



if __name__=='__main__':
    bot.polling(none_stop=True)


