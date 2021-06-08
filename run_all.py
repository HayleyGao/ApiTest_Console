import  unittest
import os
from HTMLTestRunner import  HTMLTestRunner
import time


top_dir=os.path.dirname(os.path.abspath(__file__))
# print(top_dir)

report_dir=top_dir+os.sep+'report'
resport_file=os.path.join(top_dir,'report',str(int(time.time()))+'_report.html')
# print(resport_file)

case_dir=os.path.join(top_dir,'case')
# case_dir="/Users/hayleygao/PycharmProjects/ApiTest_Console/case"
print("case_dir",case_dir)




if __name__ == '__main__':
    loader = unittest.TestLoader() #实例化加载对象
    discover = loader.discover(start_dir=case_dir, pattern='test_*.py') #加载测试用例
    with open(resport_file,'wb') as f:
        runner=HTMLTestRunner(f,verbosity=2,title='console_api_test') #执行并生成测试报告
        runner.run(discover)







