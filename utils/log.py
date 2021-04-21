import os
import logging
from logging.handlers import RotatingFileHandler
from app.config import BaseConfig


base_config = BaseConfig()
LOGGING_CONFIG = {
"version" : 1,
"standard_log_format" : '[%(asctime)s][%(levelname)s][%(funcName)s][%(processName)-10s][%(threadName)-10.12s]: %(message)s'
}


def generate_logger(module_name, level=logging.INFO):
    logger_name = module_name + "_logger"
    dirname = os.path.join(base_config.LOG_LOCATION, module_name)
    # Log file name
    log_filename = f"{dirname}log.txt"

    if not os.path.exists(dirname):
        os.makedirs(dirname)

    logger = get_sized_rotating_logger(logger_name, log_filename, level)
    return logger


def get_sized_rotating_logger(logger_name, log_filename, level):
    # logger
    logger = logging.getLogger(logger_name)
    # Level
    logger.setLevel(level)
    # handler
    handler = RotatingFileHandler(log_filename=log_filename, maxBytes=100*1024*1024, backupCount=100)
    # formatter
    formatter = logging.Formatter(LOGGING_CONFIG['standard_log_format'])
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger
