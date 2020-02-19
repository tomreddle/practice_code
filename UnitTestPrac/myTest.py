# unittest 和 ddt
# 导入包
import os
import time
import unittest
from UnitTestPrac.myFun import *
from ddt import ddt, data, unpack
import HTMLTestRunner


@ddt
class TestFun(unittest.TestCase):

    # 所有用例前执行
    @classmethod
    def setUpClass(cls):
        print('所有测试方法前准备工作')

    # 每个用例前执行
    def setUp(self):
        print('每个用例前执行准备工作')

    def test_func1(self):
        my_function1()

    def test_func2(self):
        my_function2()

    @data((1, 2), (2, 3))
    @unpack
    def test_fun3(self, a, b):
        self.assertEqual(3, my_function3(a, b))

    # 每个用例执行后的清理工作
    def tearDown(self):
        print('每个用例执行后的清理工作')

    # 所有用例执行后清理工作
    @classmethod
    def tearDownClass(cls):
        print('所有用例执行后清理工作')


# 整合测试用例
discover = unittest.defaultTestLoader.discover(start_dir='.', pattern='*Test.py', top_level_dir=None)
# 定义报告生成路径
report_dir = os.path.dirname(os.path.abspath(__file__)) + '\\' + 'report' + time.strftime('%Y%m%d%H%M%S') + '.html'
print(report_dir)
# 打开文件
file_write = open(report_dir, 'wb')
# 定义报告
runner = HTMLTestRunner.HTMLTestRunner(stream=file_write, title='测试报告', description='测试用例执行结果')
# 运行测试用例
runner.run(discover)
# 关闭报告
file_write.close()
