# -*- coding:utf-8 -*-
# @Time : 2022/6/13 16:35
# Auther : shenyuming
# @File : login_element.py
# @Software : PyCharm
'''
调试用的选择器
'''

class LoginElement:
    #LoginPage
    USERNAME_INPUT = ('id','username')
    PASSWORD_INPUT = ('id','password')
    LOGIN_BUTTON = ('id','btnLogin')

    #MAINPAGE
    MAINPAGE_TEXT = ('css selector','.no-redirect') #首页文本
    PERSONAL_CENTER_BUTTON = ('css selector','.user-avatar') #用户中心
    LOGOUT_BUTTON = ('css selector',"a+li+li>span") # 退出按钮