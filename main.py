from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler

bot = Bot(token = '5863649836:AAF_x6Q8-vNKwjSK3SxerxNKWvdP9QogZJ0')
updater = Updater(token = '5863649836:AAF_x6Q8-vNKwjSK3SxerxNKWvdP9QogZJ0')
dispahather = updater.dispatcher  

def start(update, context):
    context.bot.send_message(update.effective_chat.id, "Привет! Этот бот умеет удалять из текста все слова, содержащие 'абв'\nВведите текст, чтобы это проверить")

def redactor(update, context):
    text = update.message.text
    res = list(filter(lambda item: 'абв' not in item, text.split()))
    context.bot.send_message(update.effective_chat.id, ' '.join(res)) #Если не использовать join, то вывод будет не строкой, а списом. Из-за этого в ТГ некорректный вовод при вводе на рус яз
    
start_handler = CommandHandler("start", start)
redactor_handler = MessageHandler(Filters.text, redactor)

dispahather.add_handler(start_handler)
dispahather.add_handler(redactor_handler)

updater.start_polling()
updater.idle()

