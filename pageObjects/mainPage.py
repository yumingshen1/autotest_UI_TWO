# -*- coding:utf-8 -*-
# @Time : 2022/6/13 22:27
# Auther : shenyuming
# @File : mainPage.py
# @Software : PyCharm
from common.basePage import BasePage
from pageObjects.pm_pageObjects.addProductPage import AddProductPage
from pageObjects.pm_pageObjects.productlistpage import ProductListPage
from pageObjects.pm_pageObjects.searchproductpage import BrandManagePage


class MainPage(BasePage):
    ##进入添加商品页面
    def goto_addproductpage(self):
        #点击商品管理
        # self.click_element(self.home_button,desc='打开菜单')
        self.click_element(self.shop_guanli,desc='商品管理')
        self.click_element(self.shop_add,desc='添加商品')

        return AddProductPage()

    def goto_productlistpage(self):
        #点击查下首页菜单
        self.click_element(self.home_button,desc='首页菜单')
        #点击商品列表
        self.click_element(self.shop_list,desc='商品列表')

        return ProductListPage()

    def goto_searchproduct(self):
        #点击商品管理
        self.click_element(self.shop_guanli, desc='商品管理')
        #点击品牌管理
        self.click_element(self.shop_anage,desc='品牌管理')

        return BrandManagePage()