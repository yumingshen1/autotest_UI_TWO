# -*- coding:utf-8 -*-
# @Time : 2022/6/14 11:29
# Auther : shenyuming
# @File : conftest.py
# @Software : PyCharm
import pytest

from ENV.env import Env
from pageObjects.loginPage import LoginPage
from test_datas.login_test_data import USERNAME1, PASSWORD1


@pytest.fixture(scope='session',autouse=False)
def pm_page_fix():
    print('\n登录开始')
    test_mainpage = LoginPage().open_loginpage(Env.POLLY_URL).login_polly(USERNAME1, PASSWORD1)
    yield test_mainpage
    print('\n结束！！')