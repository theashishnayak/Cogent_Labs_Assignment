import logging

def setup_logger(name, log_file='test.log', level=logging.INFO):
    """Sets up a custom logger."""

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    handler = logging.FileHandler(log_file)
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger

logger = setup_logger('playwright_automation')