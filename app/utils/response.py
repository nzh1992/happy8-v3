# -*- coding: utf-8 -*-
"""
Author: niziheng
Created Date: 2025/4/7
Last Modified: 2025/4/7
Description: 
"""


def make_response(code, msg, data=None):
    """
    API接口返回值构造函数

    :param code: int. 错误码
    :param msg: str. 错误信息
    :param data: dict or list or None. 数据
    :return:
    """
    resp = {
        'code': code,
        'msg': msg
    }

    if data is not None:
        resp.update({'data': data})

    return resp
