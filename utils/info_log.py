import logging


logger = logging.getLogger('info_logger')
logger.setLevel(logging.INFO)
handler = logging.FileHandler('./logs/info.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s : %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

def infoLogger(message):
    logger.info(message)