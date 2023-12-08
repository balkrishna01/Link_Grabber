import configparser
import os


ini_file_path = os.path.join(os.getcwd(), 'Configurations', 'config.ini')
config = configparser.RawConfigParser()
config.read(ini_file_path)


class ReadConfig:
    @staticmethod
    def getURL():
        app_url = config.get('app info', 'base_url')
        return app_url

    @staticmethod
    def getEmail():
        email = config.get('credentials', 'email_id')
        return email

    @staticmethod
    def getPassword():
        password = config.get('credentials', 'password')
        return password
