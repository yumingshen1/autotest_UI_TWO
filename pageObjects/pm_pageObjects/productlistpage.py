# -*- coding:utf-8 -*-
# @Time : 2022/6/14 10:45
# Auther : shenyuming
# @File : productlistpage.py
# @Software : PyCharm
from common.basePage import BasePage


class ProductListPage(BasePage):
    """
    获得商品列表第一个商品名称信息
    """
    def get_first_productname(self):
        return self.get_element_text(self.first_productname)
