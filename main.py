#coding=utf-8
import unittest
import importlib,sys

from common import HTMLTestRunner
from testcase.testLoginPage import TestLoginPage

importlib.reload(sys)


if __name__ == '__main__':
    testunit = unittest.TestSuite()
    testunit.addTest(TestLoginPage('testLogin'))

    # 定义报告输出路径
    htmlPath = u"page_test_Report.html"
    fp = open(htmlPath, "wb")

    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
           title=u"测试报告",
           description=u"测试用例结果")

    runner.run(testunit)

    fp.close()