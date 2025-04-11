# -*- coding: utf-8 -*-
"""
Author: niziheng
Created Date: 2025/4/7
Last Modified: 2025/4/7
Description:
"""
import os

from loguru import logger


# 日志存放路径
log_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))), "logs")
log_fp = os.path.join(log_dir, "log_{time:YYYY-MM-DD}.log")

if not os.path.exists(log_dir):
    # 若日志存放目录不存在，则创建
    os.makedirs(log_dir, exist_ok=True)

logger.add(log_fp, rotation="1 days", compression="zip")

# 引入限制
__all__ = ["logger"]
