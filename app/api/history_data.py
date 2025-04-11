# -*- coding: utf-8 -*-
"""
Author: niziheng
Created Date: 2025/4/7
Last Modified: 2025/4/7
Description: 历史数据相关接口
"""
from flask import Blueprint

from app.utils.response import make_response
from app.utils.log import logger


history_data_bp = Blueprint('history_data', __name__, url_prefix='/history_data')


@history_data_bp.route('/update', methods=['POST'])
def update_history_data():
    """更新历史数据接口"""
    pass

    return make_response(200, "OK")