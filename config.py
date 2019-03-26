import redis
class Config(object):
    """工程配置信息"""
    SECRET_KEY = "EjpNVSNQTyGi1VvWECj9TvC/+kq3oujee2kTfQUs8yCM6xX9Yjq52v54g+HVoknA"
    DEBUG = True
    # 数据库的配置信息
    SQLALCHEMY_DATABASE_URI = "mysql://root:@127.0.0.1:3306/information"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # redis配置
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379
    # flask_session的配置信息
    SESSION_TYPE = "redis"  # 指定session保存到redis中
    SESSION_USE_SIGNER = True  # 让cookie中的session_id被加密签名处理
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)  # 使用redis的实例
    PERMANENT_SESSION_LIFETIME = 86400  # session的有效期，单位是秒

