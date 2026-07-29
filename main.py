
import telebot
from telebot import types

TOKEN = "8898956969:AAEacEpaeSDeaWRXd8Ij16v4ZmsT528qf_U"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_mesaji(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    
    btn_stok = types.InlineKeyboardButton('📦 Ürün Stok', url='https://t.me/+BIITaF5_eJA5Yjk0')
    btn_market = types.InlineKeyboardButton('🛍️ Market', url='https://t.me/+tJihrf02AOo2ZjU0')
    btn_referans = types.InlineKeyboardButton('⭐ Referanslar', url='https://t.me/+VIp0VyjFBR5mMDI0')
    
    markup.add(btn_stok, btn_market, btn_referans)
    mesaj_metni = (
        "🛒 CARLOSTALLONE MARKET\n"
        "━━━━━━━━━━━━━━━━━━━━\n\n"
        "Aşağıdaki butonları ullanarak kanallarımıza ulaşabilirsiniz:\n\n"

    "━━━━━━━━━━━━━━━━━━━━"
    )
            
    
    bot.send_message(message.chat.id, mesaj_metni, reply_markup=markup)

bot.infinity_polling()
