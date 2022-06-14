# -*- coding:utf-8 -*-
# @Time : 2022/6/13 15:23
# Auther : shenyuming
# @File : common_driver.py
# @Software : PyCharm

from selenium import webdriver
from ENV.env import Env

class Single(object):
    """
    单例模式，为了只生成一个浏览器
    """
    _instance = None
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
## Common_Driver 继承单例模式，是为了只启动一个浏览器
class Common_Driver(Single):
    driver = None      # Common_Driver中海油get_driver方法，也需要处理
    def get_driver(self,broswer_type=Env.BROSWER_TYPE,headless_flage=Env.HEADLESS_FLAGE):
        if self.driver is None: #如果没有浏览器就打开一个
            if not headless_flage:  #如果不等于false为真，走有头浏览器
                if broswer_type == 'chrome':
                    self.driver = webdriver.Chrome()
                elif broswer_type == 'firefox':
                    self.driver = webdriver.Firefox()
                else:
                    print('请重新输入')

            else: ##开启无头浏览器
                if broswer_type == 'chrome':
                    _options = webdriver.ChromeOptions()
                    _options.add_argument('--headless')
                    self.driver = webdriver.Chrome(options=_options)
                elif broswer_type == 'firefox':
                    _options = webdriver.FirefoxOptions()
                    _options.add_argument('--headless')
                    self.driver = webdriver.Firefox(options=_options)
                else:
                    print('请重新输入')

            self.driver.maximize_window()
            print(self.driver.name)
            self.driver.implicitly_wait(5)
        return self.driver  # 如果浏览器存在就直接返回

if __name__ == '__main__':
    Common_Driver().get_driver()
