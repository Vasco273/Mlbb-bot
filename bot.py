import os
import telebot

# Railway Variables ထဲက TOKEN ကို ဖတ်ခိုင်းတာပါ
TOKEN = os.getenv('TOKEN')
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "🤩 MLBB Diamonds Bot မှ ကြိုဆိုပါတယ်ဗျာ!\n\nဈေးနှုန်းမေးမြန်းရန် /price ကို နှိပ်ပါ။")

@bot.message_handler(commands=['price'])
def send_price(‌price):
    prices = (
        "💎 MLBB Diamonds Price List 💎\n\n"
        "86 Diamonds - 2,500 MMK\n"
        "172 Diamonds - 4,800 MMK\n"
        "257 Diamonds - 7,200 MMK\n\n"
        "ဝယ်ယူလိုပါက Admin ကို ဆက်သွယ်ပါ!"
    )
    bot.reply_to(message, prices)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(, "ခ‌ဏတော့စောင့်ပေးပါဗျ")

# Bot ကို စတင် Run ခိုင်းတာပါ
if __name__ == "__အ‌ေကာင့်__ID(sever)__":
    print("Bot is starting...")
    bot.infinity_polling()
    
