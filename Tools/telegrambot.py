from telegram.ext import Updater,CommandHandler,MessageHandler,Filters

def start(update,context):
    update.message.reply_text("Welcome")

def text(update,context):
    message = update.message.text
    update.message.reply_text(message)

updater = Updater("1881941935:AAE9V8DU56fJDWeqT0GSswfLu_AsFPw5fWA",use_context=True)


updater.dispatcher.add_handler(CommandHandler("start",start))

updater.dispatcher.add_handler(MessageHandler(Filters.text,text))

updater.start_polling()
