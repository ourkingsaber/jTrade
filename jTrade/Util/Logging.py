import logging


def get_logger(loggername, filename):
    # create logger with loggername
    logger = logging.getLogger(loggername)
    logger.setLevel(logging.DEBUG)
    # create file handler which logs even debug messages
    fh = logging.FileHandler(filename)
    fh.setLevel(logging.DEBUG)
    # create console handler with a higher log level
    ch = logging.StreamHandler()
    ch.setLevel(logging.ERROR)
    # create formatter and add it to the handlers
    fhformatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    chformatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
    fh.setFormatter(fhformatter)
    ch.setFormatter(chformatter)
    # add the handlers to the logger
    logger.addHandler(fh)
    logger.addHandler(ch)
    return logger
