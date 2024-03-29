from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import redis
from flask_wtf.csrf import CSRFProtect
from flask_session import Session
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
from info import create_app,db

"""
manage.py的作用是入口程序
"""
app = create_app("develop")



# class Config(object):
#     """工程配置信息"""
#     SECRET_KEY = "EjpNVSNQTyGi1VvWECj9TvC/+kq3oujee2kTfQUs8yCM6xX9Yjq52v54g+HVoknA"
#     DEBUG = True
#     # 数据库的配置信息
#     SQLALCHEMY_DATABASE_URI = "mysql://root:@127.0.0.1:3306/information"
#     SQLALCHEMY_TRACK_MODIFICATIONS = False
#     # redis配置
#     REDIS_HOST = "127.0.0.1"
#     REDIS_PORT = 6379
#     # flask_session的配置信息
#     SESSION_TYPE = "redis" #   指定session保存到redis中
#     SESSION_USE_SIGNER = True  # 让cookie中的session_id被加密签名处理
#     SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)  # 使用redis的实例
#     PERMANENT_SESSION_LIFETIME = 86400  # session的有效期，单位是秒
#
# app.config.from_object(Config)
# db = SQLAlchemy(app)
# CSRFProtect(app)
# Session(app)
# redis_store = redis.StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)
#
manager = Manager(app)
Migrate(app,db)
manager.add_command("mysql", MigrateCommand)

# @app.route('/index')
# def index():
#     return 'index'

if __name__ == '__main__':
    manager.run()