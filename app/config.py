# -*- coding: utf-8 -*-
"""
Author: niziheng
Created Date: 2025/4/7
Last Modified: 2025/4/7
Description: 配置文件
"""


class BaseConfig:
    pass


class DevelopmentConfig(BaseConfig):
    """
    开发环境配置
    """
    DEBUG = True
    PORT = 8080
    HOST = '0.0.0.0'
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123456@127.0.0.1:3306/happy8-v3"


class TestConfig(BaseConfig):
    """
    测试环境配置
    """
    DEBUG = True
    PORT = 8080
    HOST = '0.0.0.0'
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123456@127.0.0.1:3306/happy8-v3"


class ProductConfig(BaseConfig):
    """
    生产环境配置
    """
    DEBUG = False
    PORT = 8080
    HOST = '0.0.0.0'
    SQLALCHEMY_DATABASE_URI = ""


CONFIG_MAPPING = {
    'development': DevelopmentConfig,
    'test': TestConfig,
    'product': ProductConfig
}