import os
import requests
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

# Logging configuration
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

# --- Diamond ပမာဏအလိုက် ဒေါ်လာဈေးနှုန်းများ (ဒါကို စိတ်ကြိုက်ပြင်နိုင်ပါတယ်) ---
DIAMOND_USD_PRICES = {
    "86 Diamonds": 1.15,
    "172 Diamonds": 2.30,
    "257 Diamonds": 3.45,
    "706 Diamonds": 9.20,
    "Weekly Diamond Pass": 1.99
}

def get_real_time_rate():
    try:
        # ကမ္ဘာ့ပေါက်ဈေး API မှ ဈေးနှုန်းယူခြင်း
        url = "https://api.exchangerate-api.com/v4/latest/USD"
        response = requests.get(url)
        data = response.json()
        official_rate = data['rates']['MMK']
        
        # မြန်မာပြည်ပြင်ပပေါက်ဈေးနှင့် နီးစပ်စေရန် ၅၀၀ ကျပ် ထပ်ပေါင်းခြင်း (လိုအပ်သလို ပြင်နိုင်ပါတယ်)
        market_rate = official_rate + 700 
        return round(market_rate)
    except Exception as e:
        logging.error(f"Error fetching rate: {e}")
        return 5300  # API အလုပ်မလုပ်ပါက အရန်သုံးရန်ဈေးနှုန်း

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("မင်္ဂလာပါ! လက်ရှိဒေါ်လာပေါက်ဈေးဖြင့် MLBB Diamond ဈေးနှုန်းကြည့်ရန် /price ကို နှိပ်ပါ။")

async def price(update: Update, context: ContextTypes.DEFAULT_TYPE):
    current_rate = get_real_time_rate()
    
    msg = f"📊 လက်ရှိဒေါ်လာပေါက်ဈေး (ခန့်မှန်း): 1 USD = {၄၈၀၀} MMK\n"
    msg += "━━━━━━━━━━━━━━━━━━\n"
    msg += " MLBB Diamond Price List \n\n"
    
    for name, usd_price in DIAMOND_USD_PRICES.items():
        # မြန်မာကျပ်ငွေတွက်ချက်ခြင်း
        mmk_price = round(usd_price * current_rate)
        # အနီးစပ်ဆုံး ၅၀ သို့မဟုတ် ၁၀၀ ပြည့်အောင် ညှိခြင်း (ဥပမာ ၂၀၄၃ ကို ၂၀၅၀ လုပ်ခြင်း)
        final_price = (mmk_price + 50) // 100 * 100
        
        msg += f"🔹 {name} - {final_price:,} MMK\n"
    
    msg += "\n━━━━━━━━━━━━━━━━━━\n"
    msg += "⚠️ ဈေးနှုန်းသည် ဒေါ်လာပေါက်ဈေးပေါ်မူတည်၍ အပြောင်းအလဲ ရှိနိုင်ပါသည်။"
    msg += "\nဝယ်ယူရန် ဆက်သွယ်ပါ - [သင့် Link/Ph ထည့်ရန်]"
    
    await update.message.reply_text(msg)

if __name__ == '__main__':
    if not TOKEN:
        logging.error("No Token Found!")
    else:
        app = ApplicationBuilder().token(TOKEN).build()
        app.add_handler(CommandHandler('start', start))
        app.add_handler(CommandHandler('price', price))
        app.run_polling()
        
