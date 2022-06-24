import logging


logger = logging.getLogger('error_logger')
logger.setLevel(logging.ERROR)
handler = logging.FileHandler('./logs/error.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s : %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

def errorLogger(message):
    logger.error(message)