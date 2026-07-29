import telebot

BOT_TOKEN = "8898940935:AAGkUaphu76k_Sq-kKjPIkx2hC1FZQIKVvE"

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(message, "✅ অতি শিগ্রই নাম্বার যুক্ত হবে..!")

@bot.message_handler(func=lambda message: True)
def echo(message):
    bot.reply_to(message, f"আপনি লিখেছেন: {message.text}")

print("Bot is running...")
bot.infinity_polling()