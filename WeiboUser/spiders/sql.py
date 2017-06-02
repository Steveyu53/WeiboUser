import pymysql.cursors
from WeiboUser import settings

MYSQL_HOSTS = settings.MYSQL_HOSTS
MYSQL_USER = settings.MYSQL_USER
MYSQL_PASSWORD = settings.MYSQL_PASSWORD
MYSQL_PORT = settings.MYSQL_PORT
MYSQL_DB = settings.MYSQL_DB

config = {
    'host': MYSQL_HOSTS,
    'port': MYSQL_PORT,
    'user': MYSQL_USER,
    'password': MYSQL_PASSWORD,
    # 'db': MYSQL_DB,
    'charset': 'utf8mb4',
    'cursorclass': pymysql.cursors.DictCursor,
}

class Sql:
# Connect to the database
    @classmethod
    def create_database(cls):
        connection = pymysql.connect(**config)
        try:
            with connection.cursor() as cursor:

                sql = 'CREATE DATABASE if not EXISTS %s DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci' % (MYSQL_DB)

                cursor.execute(sql)

            connection.commit()
        finally:

            connection.close()

    @classmethod
    def create_tables(cls):
        config['db'] = MYSQL_DB

        connection = pymysql.connect(**config)
        try:
            with connection.cursor() as cursor:

                sql = 'CREATE TABLE IF NOT EXISTS %s ' \
                      '(`id` int(11) NOT NULL AUTO_INCREMENT,' \
                      '`screen_name` varchar(255) DEFAULT NULL,' \
                      '`verified_reason` varchar(255) DEFAULT NULL,' \
                      '`follow_count` int(11) DEFAULT \'0\',' \
                      '`followers_count` int(11) DEFAULT \'0\',' \
                      ' PRIMARY KEY (`id`))' \
                      ' ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;' % ('user')

                cursor.execute(sql)

            connection.commit()
        finally:

            connection.close()

    @classmethod
    def insert_dd_name(cls,screen_name,verified_reason,follow_count,followers_count):
        connection = pymysql.connect(**config)
        try:
            with connection.cursor() as cursor:
                # 执行sql语句，插入记录
                sql = 'INSERT INTO user (screen_name,verified_reason,follow_count,followers_count) VALUES (%s, %s, %s, %s)'

                cursor.execute(sql,(screen_name,verified_reason,follow_count,followers_count));
            # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
            connection.commit()

        finally:
            connection.close();