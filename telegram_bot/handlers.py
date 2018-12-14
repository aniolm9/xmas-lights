import functions

def error(update, error):
    logger = functions.logs()
    logger.warning('Update "%s" caused error "%s"', update, error)
