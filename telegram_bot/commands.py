import lights

userid = None

def engega(bot, update):
    if (update.message.chat_id == userid):
        bot.send_message(chat_id=update.message.chat_id, reply_to_message_id=update.message.message_id, text="Engegant els llums...")
        lights.turnon()
        

def apaga(bot, update):
    if (update.message.chat_id == userid):
        bot.send_message(chat_id=update.message.chat_id, reply_to_message_id=update.message.message_id, text="Apagant els llums...")
        lights.turnoff()
