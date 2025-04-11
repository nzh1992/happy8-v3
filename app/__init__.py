# -*- coding: utf-8 -*-
"""
Author: niziheng
Created Date: 2025/4/7
Last Modified: 2025/4/7
Description: 
"""
from flask import Flask

from app.extensions import db
from app.config import CONFIG_MAPPING
from app.utils.log import logger


def add_extensions(app):
    """
    添加扩展插件
    :param app: Flask. Flask App实例
    :return:
    """
    # flask-sqlalchemy 扩展
    db.init_app(app)


def register_blueprints(app):
    """
    注册蓝图
    :param app: Flask. Flask应用实例
    :return:
    """
    from app.api.history_data import history_data_bp

    app.register_blueprint(history_data_bp)


def load_models(app):
    """
    加载模型，并生成数据库表
    :return:
    """
    from app.models.lottery_number import LotteryNumberModel

    with (app.app_context()):
        db.create_all()
        logger.debug("数据库表加载完成")


def create_app(env):
    app = Flask(__name__)

    # 加载配置
    config_cls = CONFIG_MAPPING.get(env, "development")
    app.config.from_object(config_cls)
    logger.debug(f"加载环境配置完成，{env}环境")

    # 添加扩展
    add_extensions(app)

    # 注册路由
    register_blueprints(app)

    # 加载模型，并生成数据库表
    load_models(app)

    return app
