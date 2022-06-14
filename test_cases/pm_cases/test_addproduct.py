# -*- coding:utf-8 -*-
# @Time : 2022/6/13 22:23
# Auther : shenyuming
# @File : test_addproduct.py
# @Software : PyCharm
import os

import allure
import pytest
from time import sleep
from pageObjects.loginPage import LoginPage
from ENV.env import Env
from test_datas.login_test_data import USERNAME1,PASSWORD1
from utils.handles_path import report_path
from utils.handles_rand_str import get_rand_str

@allure.epic('保利商城自动化')
@allure.feature('保利商城-添加商品')
class TestAddproduct():
    @allure.story('添加商品并检查列表1')
    def test_addproduct_01(self,pm_page_fix):
        with allure.step('1,登录'):
            # test_mainpage = LoginPage().open_loginpage(Env.POLLY_URL).login_polly(USERNAME1,PASSWORD1)
            test_mainpage = pm_page_fix
        with allure.step('2,跳转到商品添加页面'):
            test_addproductpage = test_mainpage.goto_addproductpage()
        with allure.step('3,添加商品'):
            pname = '一级菜单01'+get_rand_str(6)
            stitle = '二级菜单01'+get_rand_str(6)
            test_addproductpage.addproductpage('1','1',pname,stitle,'1')
        with allure.step('4,点击首页按钮'):
            # test_addproductpage.click_element(test_addproductpage.home_button)
            test_addproductpage.get_homepage()
        with allure.step('5,点击商品列表'):
            test_productlistpage = test_mainpage.goto_productlistpage()
        with allure.step('6,获取列表第一个商品名字'):
            firstproduct_name = test_productlistpage.get_first_productname()
        with allure.step('7,断言'):
            assert firstproduct_name == pname

    sleep(2)
    @allure.story('添加商品并检查列表2')
    def test_addproduct_02(self,pm_page_fix):
        with allure.step('1,登录'):
            # test_mainpage = LoginPage().open_loginpage(Env.POLLY_URL).login_polly(USERNAME1, PASSWORD1)
            test_mainpage = pm_page_fix
        with allure.step('2,跳转到商品添加页面'):
            test_addproductpage = test_mainpage.goto_addproductpage()
        with allure.step('3,添加商品'):
            pname = '一级菜单02' + get_rand_str(6)
            stitle = '二级菜单02' + get_rand_str(6)
            test_addproductpage.addproductpage('1', '1', pname, stitle, '2')
        with allure.step('4,点击首页按钮'):
            # test_addproductpage.click_element(test_addproductpage.home_button)
            test_addproductpage.get_homepage()
        with allure.step('5,点击商品列表'):
            test_productlistpage = test_mainpage.goto_productlistpage()
        with allure.step('6,获取列表第一个商品名字'):
            firstproduct_name = test_productlistpage.get_first_productname()
        with allure.step('7,断言'):
            assert firstproduct_name == pname

if __name__ == '__main__':
    pytest.main(['-sv','test_addproduct.py','--alluredir',f'{report_path}','--clean-alluredir'])
    os.system(f'allure serve {report_path}')