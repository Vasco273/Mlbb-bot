import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

# Error တွေကို Railway Log မှာ မြင်ရအောင် လုပ်ခြင်း
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # စာသားတွေကို function ထဲမှာ စနစ်တကျ စုပေးထားပါတယ်
    wel_msg = "MLBB Diamonds Bot မှ ကြိုဆိုပါတယ်ဗျာ!\n\n"
    wel_msg += "စျေးနှုန်းမေးမြန်းရန် /price ကို နှိပ်ပါ သို့မဟုတ် ရိုက်ထည့်ပါ။"
    await context.bot.send_message(chat_id=update.effective_chat.id, text=wel_msg)

async def price(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # စျေးနှုန်းစာရင်း (Line 14 ဝန်းကျင်က error တက်တဲ့နေရာကို ပြင်ထားတာပါ)
    price_list = "MLBB Diamonds Price List\n\n"
    price_list += "10 Diamonds - 200 MMK\n"
    price_list += "20 Diamonds - 400 MMK\n\n"
    price_list += "ဝယ်ယူရန် ဆက်သွယ်ပါ!"
    await context.bot.send_message(chat_id=update.effective_chat.id, text=price_list)

if __name__ == '__main__':
    if TOKEN:
        application = ApplicationBuilder().token(TOKEN).build()
        
        # Command တွေကို ချိတ်ဆက်ခြင်း
        application.add_handler(CommandHandler('start', start))
        application.add_handler(CommandHandler('price', price))
        
        print("Bot is starting...")
        application.run_polling()
    else:
        print("Error: TOKEN မရှိပါဘူး။ Railway Variables ထဲမှာ စစ်ပေးပါ။")
        g()
    
