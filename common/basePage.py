# -*- coding:utf-8 -*-
# @Time : 2022/6/13 15:52
# Auther : shenyuming
# @File : basePage.py
# @Software : PyCharm
import traceback
from ENV.env import Env
from common.common_driver import Common_Driver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import strftime
from utils.handles_path import screenshot_path,common_element_path
from utils.handle_log import log
from common.login_element import LoginElement
from test_datas.login_test_data import USERNAME1,USERNAME2,PASSWORD1,PASSWORD2
from utils.handles_yml import get_yml_datas

class BasePage():
    """
    1，引入浏览器driver
    2,封装常用的方法
    """
    def __init__(self):
        """
        1，获取浏览器dirver
        2，通过类名获取每个业务类对应的loccator
        """
        self.driver = Common_Driver().get_driver()

        #获取页面元素
        self.locators = get_yml_datas(common_element_path / 'all_elements.yml')
        #获取页面元素类名
        self.locators = get_yml_datas(common_element_path / 'all_elements.yml')[self.__class__.__name__]
        ##把元素名当做当前实例的属性
        for element,locator in self.locators.items():
            setattr(self,element,locator)  #反射，给self设置一个element属性值为locator

    def open_url(self,url):
        """
        访问地址
        :param url:
        :return:
        """
        self.driver.get(url)

    def get_element(self,locator,desc=None):
        """
        定位元素
        :return:
        """
        try:
            return WebDriverWait(self.driver,Env.POLLY_TIMEOUT,Env.POLL_FREQUENCY).until(EC.visibility_of_element_located(locator))
        except:
            curtime = strftime('%Y%m%d%H%M%S')
            self.driver.save_screenshot(str(screenshot_path / f'{desc}{curtime}.png'))
            # log.error(f'{desc}元素定位不到')
            # log.error(traceback.format_exc())##记录堆栈信息

    def get_elements(self,locator,desc=None):
        """
        定位元素---一组
        :return:
        """
        try:
            return WebDriverWait(self.driver,Env.POLLY_TIMEOUT,Env.POLL_FREQUENCY).until(EC.visibility_of_all_elements_located(locator))
        except:
            curtime = strftime('%Y%m%d%H%M%S')
            self.driver.save_screenshot(str(screenshot_path / f'{desc}{curtime}.png'))
            # log.error(f'{desc}元素定位不到')
            # log.error(traceback.format_exc())##记录堆栈信息

    def input_text(self,locator,text,append=False,desc=None):
        """
        输入内容
        :param locator:
        :param text:
        :param append:
        :param desc:
        :return:
        """
        if not append:
            self.get_element(locator,desc=desc).clear()
            self.get_element(locator,desc=desc).send_keys(text)
        else:
            self.get_element(locator,desc=desc).send_keys(text)

    def click_element(self,locator,desc=None):
        """
        点击元素
        :param locator:
        :param desc:
        :return:
        """
        self.get_element(locator,desc=desc).click()

    def get_element_text(self,locator,desc=None):
        """
        获得元素文本
        :param locator:
        :param desc:
        :return:
        """
        return self.get_element(locator,desc=desc).text

    def get_elements_text(self, locator, desc=None):
        """
        获得元素文本-- 一组
        :param locator:
        :param desc:
        :return:
        """
        return [ele.text for ele in self.get_elements(locator,desc)]


if __name__ == '__main__':
    ## 验证封装的方法
    test_page = BasePage()
    test_page.open_url(Env.POLLY_URL)
    test_page.input_text(LoginElement.USERNAME_INPUT,USERNAME1,desc='用户名')
    test_page.input_text(LoginElement.PASSWORD_INPUT,PASSWORD1,desc='密码')
    test_page.click_element(LoginElement.LOGIN_BUTTON,desc='登录')