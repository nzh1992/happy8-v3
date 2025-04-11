# -*- coding: utf-8 -*-
"""
Author: niziheng
Created Date: 2025/4/7
Last Modified: 2025/4/7
Description: 
"""
from app import create_app


if __name__ == '__main__':
    app = create_app(env='test')
    app.run()