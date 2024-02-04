class Config:
    SECRET_KEY = 'B!1w8NAt1T^%kvhUI*S^' #flash


class DevelopmentConfig(Config):
    DEBUG = True
    PORT = 5000
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'mundolibre'
    MYSQL_DB = 'chkdsk7$sistemaelecciones'

config = {
    'development': DevelopmentConfig
}