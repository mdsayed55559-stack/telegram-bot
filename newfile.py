import telebot

# এখানে তোমার Bot Token বসাও
BOT_TOKEN = "8898940935:AAGkUaphu76k_Sq-kKjPIkx2hC1FZQIKVvE"

bot = telebot.TeleBot(BOT_TOKEN)


# /start
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(
        message,
        "👋 স্বাগতম!\nআমি তোমার Telegram Bot."
    )


# /help
@bot.message_handler(commands=['help'])
def help_cmd(message):
    bot.reply_to(
        message,
        "/start - Bot চালু\n"
        "/help - সাহায্য"
    )


# ছবি গ্রহণ
@bot.message_handler(content_types=['photo'])
def photo(message):
    bot.reply_to(message, "📷 ছবি পেয়েছি!")


# ফাইল গ্রহণ
@bot.message_handler(content_types=['document'])
def document(message):
    file_name = message.document.file_name
    bot.reply_to(message, f"📄 ফাইল পেয়েছি!\nনাম: {file_name}")


# সাধারণ লেখা
@bot.message_handler(func=lambda message: True)
def echo(message):
    bot.reply_to(message, f"তুমি লিখেছ:\n{message.text}")


print("Bot is running...")
bot.infinity_polling()
