import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# Token ကို Render ရဲ့ Environment Variable ကနေ ဖတ်မှာဖြစ်ပါတယ်
TOKEN = os.environ.get('BOT_TOKEN')

# Diamond ဈေးနှုန်းဇယား
PRICES = {
    🤩 MLBB Diamonds
💎86    😀5500  
💎172   😀10900
💎257   😀15900 (Recharge 250မပြည့်ပါ)     
💎343   😀21400  
💎429   😀26800
💎514   😀31800
💎600  😀37300
💎706  😀42800
💎1049 😀64200
💎2195 😀129500
💎3688 😀216500 
💎5532 😀326000 
💎9288 😀541000 

💎Weekly Pass ➡️6800
﻿💎Double Diamonds
💎50+50 😀3500
💎150+150 😀10500
💎250+250 😀17000
💎500+500 😀34500
⚠️မိမိအကောင့်ထဲတွင်၀ယ်ယူလိုသည့်dia ပမာဏပုံ၌ First Recharge စာသားပါမပါဦးစွာစစ်ဆေးပါ
Special Bundles_

🎁Monthly Elite Bundle - 18000
(💎275 + 🌠180 + Rare skin fragment 10) (တစ်လတစ်ခါဖြည့်လို့ရ)

🎁Weekly Elite Bundle - 3500
(💎55 + 🌠20 + Rare skin fragment 2) (တစ်ပတ်တစ်ခါဖြည့်လို့ရ)
﻿🎁Miya Twilight Pass - 34500
}


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("💎 Diamond ဈေးနှုန်းကြည့်ရန်", callback_data='view_prices')],
        [InlineKeyboardButton("📞 Admin ဆက်သွယ်ရန်", url='https://t.me/mgchandiamond343')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Mobile Legends Diamond အရောင်း Bot မှ ကြိုဆိုပါတယ်!', reply_markup=reply_markup)

async def button_click(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == 'view_prices':
        text = "လက်ရှိ Diamond ဈေးနှုန်းများ -\n"
        keyboard = []
        for key, price in PRICES.items():
            text += f"• {key.replace('_', ' ')}: {price}\n"
            keyboard.append([InlineKeyboardButton(f"ဝယ်ယူမယ် ({key.replace('_', ' ')})", callback_data=f"buy_{key}")])
        
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(text=text, reply_markup=reply_markup)

    elif query.data.startswith('buy_'):
        item = query.data.split('_')[1]
        await query.edit_message_text(f"သင် {item} diamonds ကို ရွေးချယ်ထားပါတယ်။\n\nငွေပေးချေမှုအတွက် Admin ဆီသို့ Game ID နဲ့ Server ID ပို့ပေးပါ။")

def main():
    if not TOKEN:
        print("Error: BOT_TOKEN variable is not set!")
        return

    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_click))
    
    print("Bot is running...")
    app.run_polling()

if __name__ == '__main__':
    main()
                              
