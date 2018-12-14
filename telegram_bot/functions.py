import commands
import logging
import handlers
from telegram.ext import MessageHandler, CommandHandler

def logs():
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
    logger = logging.getLogger(__name__)
    return logger

def handlersProcess(updater, dispatcher):
    # Dictionary containing all the command handlers
    handlers_dict = dict(engega=CommandHandler('engega', commands.engega),
                         apaga=CommandHandler('apaga', commands.apaga))

    # Adding the handlers to the dispatcher.
    for command in handlers_dict:
        dispatcher.add_handler(handlers_dict[command])

    # Error handler
    dispatcher.add_error_handler(handlers.error)

    # Entry and exit handler
    dispatcher.add_handler(MessageHandler(None, handlers.entryAndExit))

    # Start the bot
    updater.start_polling()

    # Wait for Ctrl-C or other SIGs to end the process
    updater.idle()
