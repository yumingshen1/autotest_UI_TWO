# -*- coding:utf-8 -*-
# @Time : 2022/6/14 12:02
# Auther : shenyuming
# @File : test_searchproduct.py
# @Software : PyCharm
import os

import allure
import random

import pytest
from time import sleep
from utils.handles_path import report_path


class TestSearchDouct:

    def test_search_01(self,pm_page_fix):
        with allure.step('1,登录'):
            test_mainpage = pm_page_fix
        with allure.step('2,进入品牌管理'):
            test_searchpage = test_mainpage.goto_searchproduct()
        with allure.step('3,获得所有品牌名称'):
            allproductname = test_searchpage.get_listproduct_names()
        with allure.step('4,从所有的品牌中随机捞一个品牌名字'):
            choice_name = random.choice(allproductname)
        with allure.step('5,搜索该品牌'):
            test_searchpage.get_search_rand(choice_name)
        with allure.step('6,列表中搜索结果'):
            sleep(2)
            result_data = test_searchpage.get_listproduct_names()
        with allure.step('7,断言'):
            ##方法1：
            # for i in result_data:
            #     if choice_name not in i:
            #         assert False
            # else:
            #     assert True

            #方法2：  filter 过滤
            assert len(list(filter(lambda x:choice_name in x,result_data))) == len(result_data)


if __name__ == '__main__':
    pytest.main(['-sv',__file__,'--alluredir',f'{report_path}','--clean-alluredir'])
    os.system(f'allure serve {report_path}')



