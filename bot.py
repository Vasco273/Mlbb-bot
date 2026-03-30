import os
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("မင်္ဂလာပါ! Mg Chan Diamond Bot မှ ကြိုဆိုပါတယ်။")

async def price(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = "MLBB Price List \n\n10 Diamonds - 200 MMK\n20 Diamonds - 400 MMK"
    await update.message.reply_text(msg)

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('price', price))
    app.run_polling()
    
