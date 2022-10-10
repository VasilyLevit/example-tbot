
from pytube import YouTube
import telebot

bot = telebot.TeleBot('5499615048:AAFo2ioBn_aw3EKKSOM1nqzkFMUTUqYcEV0')

@bot.message_handler(commands = ['start'])
def start(message):
    link = f'{message.from_user.first_name}, введите ссылку на видео: '
    bot.send_message(message.chat.id, link)
    yt = YouTube(link)
    bot.send_message(message.chat.id, f'Длина видео: {yt.length} секунд')
    yt = yt.streams.get_by_itag("18")    #скачивание
    yt.download('Downloads')
    bot.send_message(message.chat.id, f'Видео скачано')
    bot.send_video(message.chat.id, str(yt) + '.mp4') #загрузка видео в чат

bot.polling(none_stop=True)


# from pytube import YouTube

# link = input("Введите ссылку на видео: ")
# yt = YouTube(link)
# print("Длина: ", yt.length, "секунд")
# yt = yt.streams.get_by_itag("18")
# yt.download('Downloads')
# print("Видео скачано")



# from telegram import Update
# from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


# async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     await update.message.reply_text(f'Hello {update.effective_user.first_name}')


# app = ApplicationBuilder().token("5499615048:AAFo2ioBn_aw3EKKSOM1nqzkFMUTUqYcEV0").build()
# print('server start')
# app.add_handler(CommandHandler("hello", hello))

# app.run_polling()