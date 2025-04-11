# -*- coding: utf-8 -*-
"""
Author: niziheng
Created Date: 2025/4/7
Last Modified: 2025/4/7
Description:
    中国福利彩票（China Welfare Lottery，CWL），也是模块名称的缩写，表明了数据来源。
"""
import json

import requests

from app.utils.log import logger


class HistoryData:
    """
    中国福利彩票，快乐8历史数据
    """
    def __init__(self):
        self.data_url = "http://www.cwl.gov.cn/cwl_admin/front/cwlkj/search/kjxx/findDrawNotice"

    @staticmethod
    def _make_headers():
        """
        构造查询历史数据API的请求头

        :return: dict.
        """
        headers = {
            "Cookie": ("HMF_CI=50c2774011b9f462867e5abaadff1245ca4ae4f3fad5563b356191d4088a1a399695cd9f192b80170f76f0"
                       "12e5e7f90e1952f76e7dd3f0c723d2412527c6ee6677; 21_vq=5"),
            "User-Agent": ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
                           "Chrome/114.0.0.0 Safari/537.36")
        }

        return headers

    @staticmethod
    def _make_params(page_size):
        """
        构造查询参数
        :param page_size: int. 查询期数，查询从今天往前多少期
        :return: dict
        """
        if not page_size:
            # 若未提供查询期数，默认只查询1条
            page_size = 1

        params = {
            "name": "kl8",
            "issueCount": "",
            "issueStart": "",
            "issueEnd": "",
            "dayStart": "",
            "dayEnd": "",
            "pageNo": "1",
            "pageSize": str(page_size),
            "week": "",
            "systemType": "PC"
        }

        return params

    def get_data(self, history_count):
        """
        获取历史数据

        :param history_count: int. 获取最新一期开始往前的多少期。
        :return: dict.
        """
        if not history_count:
            error_info = f"history_count参数错误，history_count：{history_count}"
            logger.error(error_info)
            raise Exception(error_info)

        query_params = self._make_params(history_count)
        headers = self._make_headers()

        try:
            resp = requests.get(self.data_url, params=query_params, headers=headers, verify=True)
        except Exception as e:
            error_info = f"调用中国福利彩票，获取历史数据API错误，错误信息：{e}"
            logger.error(error_info)
            raise Exception(error_info)
        else:
            logger.debug("调用中国福利彩票，获取历史数据API成功")
            return json.loads(resp.content)
