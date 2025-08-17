import configparser
def get_config():
    config = configparser.ConfigParser()
    config.read("configuration.ini")
    return config

