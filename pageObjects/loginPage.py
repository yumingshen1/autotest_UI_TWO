# -*- coding:utf-8 -*-
# @Time : 2022/6/13 17:15
# Auther : shenyuming
# @File : loginPage.py
# @Software : PyCharm
from common.basePage import BasePage
from pageObjects.mainPage import MainPage


class LoginPage(BasePage):

    def open_loginpage(self,url):
        """
        访问url
        :param url:
        :return:
        """
        self.open_url(url)
        return self  ## 用于链式调用

    def login_polly(self,username,password):
        """
        登录系统
        :param username:
        :param password:
        :return:
        """
        self.input_text(self.username_input,username,desc='用户名')
        self.input_text(self.password_input,password,desc='密码')
        self.click_element(self.login_button,desc='登录按钮')
        return MainPage()

    def click_yonghu(self):
        self.click_element(self.personal_center_button,desc='点击用户中心')
        self.click_element(self.logout_button,desc='退出')


if __name__ == '__main__':
    l = LoginPage()
    print(l.username_input)