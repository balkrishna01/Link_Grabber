import logging
import os

log_path = os.path.join('Logs', 'execution.log')


class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename=log_path, format='%(asctime)s: %(levelname)s: %(message)s',
                            datefmt='%m/%d/%Y %I:%M:%S %p')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
