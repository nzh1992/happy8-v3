# -*- coding: utf-8 -*-
"""
Author: niziheng
Created Date: 2025/4/7
Last Modified: 2025/4/7
Description: 开奖号码模型
"""
from app import db
from app.data_source.cwl import HistoryData
from app.utils.log import logger


class LotteryNumberModel(db.Model):
    """开奖号码"""
    __tablename__ = 'lottery_number'

    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(10), unique=True, index=True, nullable=False, comment="期号")
    red1 = db.Column(db.Integer, nullable=False, comment="开奖号码1")
    red2 = db.Column(db.Integer, nullable=False, comment="开奖号码2")
    red3 = db.Column(db.Integer, nullable=False, comment="开奖号码3")
    red4 = db.Column(db.Integer, nullable=False, comment="开奖号码4")
    red5 = db.Column(db.Integer, nullable=False, comment="开奖号码5")
    red6 = db.Column(db.Integer, nullable=False, comment="开奖号码6")
    red7 = db.Column(db.Integer, nullable=False, comment="开奖号码7")
    red8 = db.Column(db.Integer, nullable=False, comment="开奖号码8")
    red9 = db.Column(db.Integer, nullable=False, comment="开奖号码9")
    red10 = db.Column(db.Integer, nullable=False, comment="开奖号码10")
    red11 = db.Column(db.Integer, nullable=False, comment="开奖号码11")
    red12 = db.Column(db.Integer, nullable=False, comment="开奖号码12")
    red13 = db.Column(db.Integer, nullable=False, comment="开奖号码13")
    red14 = db.Column(db.Integer, nullable=False, comment="开奖号码14")
    red15 = db.Column(db.Integer, nullable=False, comment="开奖号码15")
    red16 = db.Column(db.Integer, nullable=False, comment="开奖号码16")
    red17 = db.Column(db.Integer, nullable=False, comment="开奖号码17")
    red18 = db.Column(db.Integer, nullable=False, comment="开奖号码18")
    red19 = db.Column(db.Integer, nullable=False, comment="开奖号码19")
    red20 = db.Column(db.Integer, nullable=False, comment="开奖号码20")

    def __init__(self, code, red_list):
        self.code = code
        self._red_list = red_list

        for idx, red in enumerate(red_list):
            attr_name = f"red{idx + 1}"
            setattr(self, attr_name, red)

    def __repr__(self):
        return f"<LotteryNumberModel id={self.id}, code={self.code}>, red_list={self._red_list}"

    def get_red_list(self):
        """
        获取本期开奖号码列表
        :return:
        """
        red_list = []
        for idx in range(1, 21):
            red_list.append(getattr(self, f"red{idx}"))

        return red_list

    @staticmethod
    def get_all_codes(reverse=False):
        """
        获取所有期的code列表
        :param reverse: bool. 如果为False，表示倒序排列，如果为True，表示升序排列。
        :return:
        """
        if not reverse:
            reverse_condition = LotteryNumberModel.code.desc()
        else:
            reverse_condition = LotteryNumberModel.code.asc()

        number_models = LotteryNumberModel.query.order_by(reverse_condition).all()
        all_codes = [number.code for number in number_models]
        return all_codes

    @classmethod
    def update_from_remote(cls):
        """
        从CWL获取数据，并更新至数据库。
            更新逻辑：根据期号，补全开奖表中缺失的期数数据。
        :return:
        """
        logger.debug("正在检查更新...")

        all_codes = cls.get_all_codes(reverse=False)
        logger.debug(f"当前数据库期数列表长度：{len(all_codes)}, 最后一期期号：{all_codes[-1] if all_codes else None}")

        # 存放待写入数据库的数据
        waiting_list = []

        data_list = HistoryData().get_data().get("result")

        # 将历史数据调整为，根据期数升序排列
        data_list = sorted(data_list, key=lambda x: x['code'])

        for data in data_list:
            code = data.get("code")
            if code not in all_codes:
                red_data = data.get("red")
                red_list = [int(r) for r in red_data.split(",")]
                lottery_model = cls(code, red_list)
                waiting_list.append(lottery_model)
                logger.debug(f"正在更新第{code}期数据...")

        db.session.add_all(waiting_list)
        db.session.commit()
        logger.debug(f"更新完成，共写入{len(waiting_list)}条记录")