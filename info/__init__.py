import logging
from logging.handlers import RotatingFileHandler

from flask import Flask
from config import Config,config_map
from flask_sqlalchemy import SQLAlchemy
import redis
from flask_session import Session
from flask_wtf.csrf import CSRFProtect
# 记录日志的记录等级
logging.basicConfig(level=logging.DEBUG)
# 创建日志记录器指明日志保存的路径、每个日志文件的最大大小、保存的日志文件个数上线。
file_log_handler = RotatingFileHandler("logs/log", maxBytes=1024*1024*2, backupCount=10)
# 创建日志记录的格式，日志等级，输入日志信息的文件名，行数，日志信息
formatter = logging.Formatter('%(levelname)s %(filename)s:%(lineno)d %(message)s')
# 为刚创建的日志记录器设置日志记录格式
file_log_handler.setFormatter(formatter)
# 为全局的日志工具对象（flask app使用的）添加日志记录器
logging.getLogger().addHandler(file_log_handler)

db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)

    # 根据字典的key，获取字典的value
    config_class = config_map.get(config_name)

    app.config.from_object(config_class)
    db.init_app(app)

    redis_store = redis.StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT, decode_responses=True)
    Session(app)
    CSRFProtect(app)

    # 注册首页的蓝图
    from info.index import index_bule
    app.register_blueprint(index_bule)

    return app

















