#coding=utf-8
#author:zhengying

import importlib,sys

from selenium.webdriver.common.by import By
from pages.basePage import Page

importlib.reload(sys)


# 伊巢登录page
class LoginPage(Page):
    # 元素集

    # 我的页面、登录页面、用户名
    login_input_my = (By.ID, u'login')
    login_input_login = (By.ID, u'header1')
    login_input = (By.ID, u'mobileAccount')
    login_input_vtext = (By.ID,u'my-phone')
    # 免注册登录 按钮
    login_button = (By.CLASS_NAME, u'login-btn')

    def __init__(self, driver, base_url=u"http://m.ianjia.com/"):
        Page.__init__(self, driver, base_url)

    def gotoIanjiaPage(self):
        print (u"打开首页: ", self.base_url)
        self.driver.get(self.base_url)

    def gotoMyPage(self):
        print (u"打开我的: ", self.base_url)
        self.click(self.login_input_my)

    def gotoLoginPage(self):
        print (u"打开登录页面: ", self.base_url)
        self.click(self.login_input_login)

    def input_login_text(self, text=u"15800680259"):
        print (u"输入手机号： 15800680259")
        self.input_text(self.login_input, text)

    def click_login_btn(self):
        print (u"点击 免注册登录  按钮")
        self.click(self.login_button)

    def get_login_text(self):
        print (u"验证是否已登录")
        return self.get_text(self.login_input_vtext)