# -*- coding:utf-8 -*-
# @Time : 2022/6/14 14:08
# Auther : shenyuming
# @File : searchproductpage.py
# @Software : PyCharm
from common.basePage import BasePage

class BrandManagePage(BasePage):
     def get_listproduct_names(self):
         """
         获得所有品牌名字
         :return:
         """
         return self.get_elements_text(self.all_brand_name_txt,desc='所有品牌名称')



     def get_search_rand(self,name):
         """
         搜索品牌
         :param name:
         :return:
         """
         self.input_text(self.search_input,name,desc='输入品牌名字')
         self.click_element(self.search_button,desc='搜索')

