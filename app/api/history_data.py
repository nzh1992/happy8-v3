# -*- coding: utf-8 -*-
"""
Author: niziheng
Created Date: 2025/4/7
Last Modified: 2025/4/7
Description: 历史数据相关接口
"""
from flask import Blueprint

from app.data_source.cwl import HistoryData
from app.models.lottery_number import LotteryNumberModel
from app.utils.response import make_response
from app.utils.log import logger


history_data_bp = Blueprint('history_data', __name__, url_prefix='/history_data')


@history_data_bp.route('/update', methods=['POST'])
def update_history_data():
    """更新历史数据接口"""
    try:
        LotteryNumberModel.update_from_remote()
    except Exception as e:
        logger.error(e)

    return make_response(200, "OK")


@history_data_bp.route('/test', methods=['POST'])
def test():
    """
    测试开发使用
    :return:
    """
    from app.data_source.cwl import HistoryData

    his_data = HistoryData()
    total = his_data.get_total_count()
    return make_response(200, "OK", {'total': total})