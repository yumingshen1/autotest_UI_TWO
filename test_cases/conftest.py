# -*- coding:utf-8 -*-
# @Time : 2022/6/13 21:52
# Auther : shenyuming
# @File : conftest.py
# @Software : PyCharm
import pytest
from common.common_driver import Common_Driver
from time import sleep

@pytest.fixture(scope='session',autouse=True) ##所有页面自动调用
def fix_all():
    print('\n自动化测试开始')
    yield
    comm_driver = Common_Driver()
    sleep(2)
    # comm_driver.driver.quit()
    comm_driver.get_driver().quit()
    print('\n自动化测试结束')
