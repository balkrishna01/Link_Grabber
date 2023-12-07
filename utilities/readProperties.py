import configparser
import os


ini_file_path = os.path.join(os.getcwd(), 'Configurations', 'config.ini')
config = configparser.RawConfigParser()
config.read(ini_file_path)


class ReadConfig:
    pass
