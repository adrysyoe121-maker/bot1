import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = "8588265971:AAGuflB6jHm_Fpb42ii-CT3udPDQ4n6W3fU"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_heart(message):
    markup = InlineKeyboardMarkup()
    btn_heart = InlineKeyboardButton(text='❤️', callback_data='like')
    markup.add(btn_heart)
    
    bot.send_message(
        message.chat.id,
        "اضغط على القلب للإعجاب! ❤️",
        reply_markup=markup
    )

@bot.callback_query_handler(func=lambda call: call.data == 'like')
def handle_like(call):
    bot.answer_callback_query(call.id, "شكراً لك! 😊")
    bot.edit_message_reply_markup(
        call.message.chat.id,
        call.message.message_id,
        reply_markup=None
    )
    bot.send_message(call.message.chat.id, "تم استلام قلبك! 💖")

bot.polling()