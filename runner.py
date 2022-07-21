import unittest
# from HTMLTestRunner import HTMLTestRunner
from BeautifulReport import BeautifulReport
# import zmail

#获取批量的测试用例
cases = unittest.defaultTestLoader.discover(start_dir='./testcases',pattern='t_*.py')
#一、定义文本测试执行器
# runner = unittest.TextTestRunner()
# runner.run(cases)
#二、定义html测试报告路径并打开
# filename=r'G:\软件测试一阶段\班级\T109\web自动化测试\web自动化框架\unittest_f\testresult\测试报告.html'
# f=open(filename,'wb')
#定义html执行器
# runner=HTMLTestRunner(stream=f,title='测试报告',description='报告描述')
#执行测试用例
# runner.run(cases)
#三、beautifulreport
#定义beautifulreport的执行器
result=BeautifulReport(cases)
#执行并生成report
result.report(description='SIT测试',filename='回归测试报告',report_dir='./testresult')
# report_path=r'G:\软件测试一阶段\班级\T109\web自动化测试\web自动化框架\unittest_f_POM _data\testresult\回归测试报告.html'


# mail={
#     'subject':'测试结果',
#     'content_text':'测试邮件',
#     'attachments':report_path
# }
# server=zmail.server('fengyun2020_01@163.com','PDYFIFIVZTBVMCAP',smtp_host='smtp.163.com',smtp_port=994)
# #zmail.server('发件人地址','授权码',smtp_host='邮件服务地址',smtp_port=邮件服务端口)
# server.send_mail('fengyun2020_01@163.com',mail)
# #send_mail('接受人的地址’,邮件信息）