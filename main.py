import telebot
from pytube import YouTube

bot = telebot.TeleBot("KEY_DO_BOT_AQUI")

@bot.message_handler(commands=['download']) #Quando o usuário enviar /download o decorator é acionado
def pede_info(message):
  bot.reply_to(message, "Informe a URL do video:")

@bot.message_handler(func=lambda message: True) #Quando o usuário envia a URL esse decorator é chamado
def recebe_info(message):
  # URL do vídeo do YouTube que você deseja baixar
  video_url = message.text #Pega a URL
  yt = YouTube(video_url)
  yt.title = "video" #Altera o titulo do video para um valor fixo
  video = yt.streams.get_highest_resolution()
  video.download()
  with open('video.mp4', 'rb') as image_file: #Realiza o envio do video no chat
    bot.send_video(message.chat.id, image_file)


bot.infinity_polling()
