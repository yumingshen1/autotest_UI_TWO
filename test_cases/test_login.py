# -*- coding:utf-8 -*-
# @Time : 2022/6/13 17:16
# Auther : shenyuming
# @File : test_login.py
# @Software : PyCharm
import os

import allure
import pytest
import pytest_assume
from pageObjects.loginPage import LoginPage
from ENV.env import Env
from test_datas.login_test_data import USERNAME1,PASSWORD1,USERNAME2,PASSWORD2
from common.login_element import LoginElement
from time import sleep

from utils.handles_path import test_datas_path,report_path
from utils.handles_yml import get_yml_datas


@allure.epic('保利商城自动化测试')
@allure.feature('保利商城登录页面')
class TestLogin:
    @pytest.mark.skip()
    def test_login_001(self):
        """
        普通登录
        :return:
        """
        test_login = LoginPage()
        test_login.open_loginpage(Env.POLLY_URL)
        test_login.login_polly(USERNAME1,PASSWORD1)
        assert test_login.get_element_text(LoginElement.MAINPAGE_TEXT) == '首页'

    @pytest.mark.skip()
    @pytest.mark.parametrize('username,password',[(USERNAME1,PASSWORD1),(USERNAME2,PASSWORD2)])
    def test_login_002(self,username,password):
        """
        参数化
        :return:
        """
        test_login = LoginPage()
        test_login.open_loginpage(Env.POLLY_URL)
        test_login.login_polly(username,password)
        assert test_login.get_element_text(LoginElement.MAINPAGE_TEXT) == '首页'
        #点击用户中心
        test_login.click_yonghu()
        sleep(3)
        ### 每执行一次用例就打开一个新的浏览器，---》 解决：浏览器类中继承单例模式


    test_login_data = get_yml_datas(test_datas_path / 'all_login_data.yml')
    @pytest.mark.parametrize('title,username,password,locator,expeted',test_login_data)
    @allure.story('五条混合用例')
    @allure.title('{title}')
    def test_login_003(self,title,username,password,locator,expeted):
        """
        读取yml数据，失败继续跑，allure
        :return：
        """
        with allure.step('1,打开网页'):
            test_login = LoginPage()
            test_login.open_loginpage(Env.POLLY_URL)
        with allure.step('2,打开商城'):
            test_login.login_polly(username, password)
        with allure.step('3,断言{locator}的值是不是在expted中'):
            with pytest.assume: ##失败继续跑
                assert test_login.get_element_text(locator) == expeted
        with allure.step('4,点击用户中心'):
            if test_login.driver.current_url == Env.POLLU_URL_PAGE:
                test_login.click_yonghu()
                sleep(2)


if __name__ == '__main__':
    # pytest.main(['-sq',__file__])
    pytest.main(['test_login.py','-sq','--alluredir',f'{report_path}','--clean-alluredir'])
    os.system(f'allure serve {report_path}')