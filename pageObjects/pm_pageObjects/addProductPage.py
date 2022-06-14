# -*- coding:utf-8 -*-
# @Time : 2022/6/13 22:33
# Auther : shenyuming
# @File : addProductPage.py
# @Software : PyCharm
from common.basePage import BasePage


class AddProductPage(BasePage):
    def addproductpage(self,kid1,kid2,text1,text2,kid3):
        ##点击商品分类
        self.click_element(self.product_kind_select,desc='商品分类')
        ## 商品分类一级菜单
        self.product_kind_select_index1[-1] = self.product_kind_select_index1[-1].format(kid1)
        self.click_element(self.product_kind_select_index1,desc='商品分类一级菜单')
        ##商品分类二级菜单
        self.product_kind_select_index2[-1] = self.product_kind_select_index2[-1].format(kid2)
        self.click_element(self.product_kind_select_index2,desc='商品分类二级菜单')
        #商品名称
        self.input_text(self.product_name,text1,desc='商品名称')
        #副标题
        self.input_text(self.product_subtitle,text2,desc='副标题')
        #商品品牌
        self.click_element(self.product_brand_select,desc='商品品牌')
        #商品品牌一级菜单
        self.product_brand_select_idx[-1] = self.product_brand_select_idx[-1].format(kid3)
        self.click_element(self.product_brand_select_idx,desc='商品品牌一级菜单')
        ##点击下一步促销商品
        self.click_element(self.next_commodity_promotion_btn,desc='点击下一步促销商品')
        #点击下一步填写商品属性
        self.click_element(self.next_product_attribute_btn,desc='点击下一步填写商品属性')
        #点击下一步，商品关联
        self.click_element(self.netxt_product_related_btn,desc='点击下一步，商品关联')
        #完成 提交商品
        self.click_element(self.comple_button,desc='完成 提交商品')
        #确定
        self.click_element(self.subit_button,desc='确定')

    def get_homepage(self):
        self.click_element(self.home_button,desc='首页菜单')

