import peewee
from peewee import *

# https://docs.peewee-orm.com/en/latest/peewee/installation.html

db = MySQLDatabase("spring_admin", user='root', passwd="123456")

db.connect()


class T_GAME(Model):

    d

    # 变量 --> 属性
    username = peewee.CharField()
    email = peewee.CharField()

    class Meta:
        database = db # 使用上面的数据库


User.create_table()
# game = Game(company_id=1)
# game.save()
#
# for game in Game.filter(company_id=1):
#     print(game.app_id)

# app = Game.select().where(Game.company_id == 1).get()
#
# db.close()
#
# print(app)

# for game in Game.select():
#     print(game.app_id)

