from peewee import *

# python3 -m pwiz -e mysql -H localhost -p 3306 -u root -P 123456 -t t_game spring_admin > game.py 自动生产ORM 命令

database = MySQLDatabase('spring_admin', **{'charset': 'utf8', 'sql_mode': 'PIPES_AS_CONCAT', 'use_unicode': True, 'host': 'localhost', 'port': 3306, 'user': 'root', 'password': '123456'})


class UnknownField(object):
    def __init__(self, *_, **__): pass


class BaseModel(Model):
    class Meta:
        database = database


class TGame(BaseModel):
    active_notice_status = IntegerField(constraints=[SQL("DEFAULT 0")])
    ad_system = CharField(constraints=[SQL("DEFAULT ''")])
    af_app_id = CharField(constraints=[SQL("DEFAULT ''")])
    app_id = CharField(constraints=[SQL("DEFAULT ''")])
    app_store_id = CharField(constraints=[SQL("DEFAULT ''")])
    appsflyer_key = CharField(constraints=[SQL("DEFAULT ''")])
    bind_gold = CharField(constraints=[SQL("DEFAULT ''")])
    boundle_id = CharField(constraints=[SQL("DEFAULT ''")])
    client_id = CharField(constraints=[SQL("DEFAULT ''")])
    company_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    created_at = IntegerField(constraints=[SQL("DEFAULT 0")])
    default_pay = IntegerField(constraints=[SQL("DEFAULT 1")])
    dollar_change = IntegerField(constraints=[SQL("DEFAULT 0")])
    download_link = CharField(constraints=[SQL("DEFAULT ''")])
    facebook_app_id = CharField(constraints=[SQL("DEFAULT ''")])
    facebook_app_secret = CharField(constraints=[SQL("DEFAULT ''")])
    fb_open = IntegerField(constraints=[SQL("DEFAULT 1")])
    firebase_id = CharField(constraints=[SQL("DEFAULT ''")])
    force_update = IntegerField(constraints=[SQL("DEFAULT 0")])
    game_chinese_name = CharField(constraints=[SQL("DEFAULT ''")])
    game_coin = CharField(constraints=[SQL("DEFAULT ''")])
    game_id = IntegerField(constraints=[SQL("DEFAULT 0")], unique=True)
    game_key = CharField(constraints=[SQL("DEFAULT ''")])
    game_name = CharField(constraints=[SQL("DEFAULT ''")])
    game_order_gen_url = CharField(constraints=[SQL("DEFAULT ''")])
    game_version = CharField(constraints=[SQL("DEFAULT ''")])
    google_client_id = CharField(constraints=[SQL("DEFAULT ''")])
    google_login_key = TextField(null=True)
    gp_key = TextField(null=True)
    gp_type = IntegerField(constraints=[SQL("DEFAULT 0")])
    line_client_id = CharField(constraints=[SQL("DEFAULT ''")])
    line_key = CharField(constraints=[SQL("DEFAULT ''")])
    log_open = IntegerField(constraints=[SQL("DEFAULT 0")])
    login_call_back = CharField(constraints=[SQL("DEFAULT ''")])
    notice_begin_time = IntegerField(constraints=[SQL("DEFAULT 0")])
    notice_end_time = IntegerField(constraints=[SQL("DEFAULT 0")])
    notice_url = CharField(constraints=[SQL("DEFAULT ''")])
    one_client_id = CharField(constraints=[SQL("DEFAULT ''")])
    one_client_secret = TextField(null=True)
    one_store_srv_secret = TextField(null=True)
    os = IntegerField(constraints=[SQL("DEFAULT 0")])
    package_name = CharField(constraints=[SQL("DEFAULT ''")])
    password = CharField(constraints=[SQL("DEFAULT ''")])
    pay_call_back = CharField(constraints=[SQL("DEFAULT ''")])
    report = IntegerField(constraints=[SQL("DEFAULT 0")])
    roi_rate = DecimalField(constraints=[SQL("DEFAULT 1.00")])
    score_app_status = IntegerField(constraints=[SQL("DEFAULT 0")])
    score_app_url = CharField(constraints=[SQL("DEFAULT ''")])
    server_list_url = CharField(constraints=[SQL("DEFAULT ''")])
    status = IntegerField(constraints=[SQL("DEFAULT 0")])
    three_level_url = CharField(constraints=[SQL("DEFAULT ''")])
    timezone = IntegerField(constraints=[SQL("DEFAULT 0")])
    updated_at = IntegerField(constraints=[SQL("DEFAULT 0")])

    class Meta:
        table_name = 't_game'


for i in TGame.select():
    print(i.app_id)
