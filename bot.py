import os
import requests
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

# Error logs ပြရန်
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

# --- ဒီနေရာမှာ ဒေါ်လာဈေးကို ကိုယ်တိုင် ပြင်ပေးရုံပါပဲ ---
CURRENT_USD_RATE = 4800 

# Diamond USD prices
DIAMOND_USD_PRICES = {
    "86 Diamonds": 1.20,
    "172 Diamonds": 2.38,
    "257 Diamonds": 3.54,
    "706 Diamonds": 9.28,
    "Weekly Diamond Pass": 2.35
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("မင်္ဂလာပါ! ဈေးနှုန်းကြည့်ရန် /price ကို နှိပ်ပါ။")

async def price(update: Update, context: ContextTypes.DEFAULT_TYPE):
    current_rate = CURRENT_USD_RATE
    
    # Channel Mg Chan Diamond Shop ကနေကြိုဆိုပါတယ်(Link ကို သင့် Channel link နဲ့ လဲလိုက်ပါ)
    msg = "📢 ကျွန်တော်တို့ရဲ့ Channel ကို join ထားပေးပါဦး!\n"
    msg += "👉 https://t.me/mgchanchannel\n"
    msg += "━━━━━━━━━━━━━━━━━━\n\n"
    
    msg += "━━━━━━━━━━━━━━━━━━\n"
    msg += "💎 MLBB Diamond Price List 💎\n\n"
    
    for name, usd_price in DIAMOND_USD_PRICES.items():
        mmk_price = round(usd_price * current_rate)
        # ၁၀၀ ပြည့်အောင် ညှိခြင်း
        final_price = (mmk_price + 500) // 200 * 100
        msg += f"🔹 {name} - {final_price:,} MMK\n"
    
    msg += "\n━━━━━━━━━━━━━━━━━━\n"
    msg += "⚠️ ဈေးနှုန်းသည် ဒေါ်လာပေါက်ဈေးပေါ်မူတည်၍ အပြောင်းအလဲ ရှိနိုင်ပါသည်။"
    
    await update.message.reply_text(msg)

if __name__ == '__main__':
    if TOKEN:
        app = ApplicationBuilder().token(TOKEN).build()
        app.add_handler(CommandHandler('start', start))
        app.add_handler(CommandHandler('price', price))
        app.run_polling()
    else:
        print("No Token Found!")
    
