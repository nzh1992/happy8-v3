# -*- coding: utf-8 -*-
"""
Author: niziheng
Created Date: 2025/4/7
Last Modified: 2025/4/7
Description: 测试数据获取模块
"""
from app.data_source.cwl import HistoryData
from app.utils.log import logger


class TestHistoryData:
    def test_get_data(self):
        """
        测试获取数据方法
        """
        period_count = 5
        data = HistoryData().get_data(period_count)
        assert isinstance(data, dict)
        assert data.get('state') == 0
        assert data.get('message') == "查询成功"
        logger.debug("test_get_data")
