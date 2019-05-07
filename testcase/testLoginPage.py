#coding=utf-8
#author:zhengying

import unittest
import importlib,sys
import time

from selenium import webdriver
from pages.loginPage import LoginPage
import pdb

importlib.reload(sys)


# 伊巢登录测试
class TestLoginPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def testLogin(self):
        driver = self.driver
        url = u"http://m.ianjia.com/"

        # 搜索文本
        text = u"15800680259"
        # 期望验证的元素文本
        assert_text = u"15800680259"
        print (assert_text)

        login_Page = LoginPage(driver, url)

        # 启动浏览器，访问伊巢，进入登录页面
        login_Page.gotoIanjiaPage()
        login_Page.gotoMyPage()
        driver.switch_to.frame('initpage.html')
        login_Page.gotoLoginPage()
        driver.switch_to.default_content()

        # 输入 用户名
        login_Page.input_login_text(text)

        # 单击 免注册登录 按钮
        login_Page.click_login_btn()

        # 验证元素文本
        time.sleep(3)
        driver.switch_to.frame('initpage.html')
        print(login_Page.get_login_text())
        self.assertEqual(login_Page.get_login_text(), assert_text)

    def tearDown(self):
        self.driver.quit()