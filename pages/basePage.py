#coding=utf-8
#author:zhengying

import importlib,sys
importlib.reload(sys)


# pages基类
class Page(object):
    """
        Page基类，所有page都应该继承该类
    """
    def __init__(self, driver, base_url=u"http://m.ianjia.com/"):
        self.driver = driver
        self.base_url = base_url
        self.timeout = 30

    def find_element(self, *loc):
        return self.driver.find_element(*loc)

    def input_text(self, loc, text):
        self.find_element(*loc).send_keys(text)

    def click(self, loc):
        self.find_element(*loc).click()

    def get_text(self,loc):
        return self.driver.find_element_by_id("my-phone").text