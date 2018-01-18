#!/usr/bin/python
# -*- utf-8 -*-
# 对匹配正则表达式进行测试
import re
import sys
import string
import os
import time
import calendar
# currworkspace = os.getcwd()
# print("当前工作目录:%s" %(currworkspace))
# for root, dirs, files in os.walk(currworkspace):
    # print("当前目录路径: %s" %(root)) #当前目录路径
    # print("当前路径下所有子目录: %s" %(dirs)) #当前路径下所有子目录
    # print("当前路径下所有非目录子文件: %s" %(files)) #当前路径下所有非目录子文件
#     # 获取files列表中后缀名为log的文件
#     for filename in files:
#         index = filename.rfind('.')
#         if filename[index+1:] == "log":
#             print("有log文件哦：%s" %(filename))
#             print("--------------------------")

# 跳到下一级指定目录
# def changeToNextSpecialDirectory(nextTargetDirectory):
#     currworkspace = os.getcwd()
#     print("当前工作目录是 :%s " % (currworkspace))
#     for root, dirs, files in os.walk(currworkspace):
#         for dir in dirs:
#             if dir == nextTargetDirectory:  # 可以根据实际项目来更改目录
#                 nowPath = currworkspace + "\\" + dir
#                 print("切换到新的工作目录:%s" % (nowPath))
#                 os.chdir(nowPath)
#                 print("新的工作目录为 :%s" % (os.getcwd()))
#                 return
#         print("老子没有找到目录%s，让管理员去检查!" %(nextTargetDirectory))
#         return
# changeToNextSpecialDirectory("log")
# localtime = time.strftime("%Y%m%d",time.localtime())
# print(localtime)
# changeToNextSpecialDirectory(localtime)


# currentworkspace = os.getcwd()
# #获取当前日期,格式化为20180129
# localtime = time.strftime("%Y%m%d",time.localtime())
# for root, dirs, files in os.walk(currentworkspace):
#     for dir in dirs:
#         if dir == localtime:
#             print("已找到目标子目录: %s" % (dir))  # 当前路径下所有子目录
#             print("该目录的根目录为：%s" %(root))
#             workpath = root +'\\' +dir #仅适用于windows系统，linux系统的路径表示不一样
#             os.chdir(workpath)
#             print("正切换到工作目录 %s" %(os.getcwd()))
#             sys.exit(0)
# print("没有找到当日的日志文件目录%s" %(localtime))

try:
    logfile = open("rmsglog0.log", 'r', encoding='gb18030', errors='ignore')
except IOError:
    print("读日志文件出错,请检查文件是否存在或文件读取失败")
    sys.exit(0)
test = 10
testn = len(logfile.readlines())
print(testn)
logfile.seek(0)
test2 = len(logfile.readlines())
print(test2)
print(type(len(logfile.readlines())))




# str="[20180116-080000][  -988519801][2514-3c38][ 1] KADPKingdomWrapper:Req:L0380404,0120000000000000000010171101711000000050569E    KCXP00  GV2gODkBbGg=20180116080000000000000404L038040400517000000KGOB1     108_CA=2.3&_ENDIAN=1&F_EXT_OP_CODE=&F_OP_USER=63013&F_OP_USER_ENC=wns9koYZBXQ@3D&END_DATE=2018-01-15&F_OP_ROLE=2&F_CUST_ORG_CODE=3013&serverid=1&ACCOUNT=301320097813&g_serverid=1&OPER_CONVERT=1&F_CHANNEL=0&F_REAL_CODE_ENC=&BGN_DATE=2018-01-15&YGT_VIRTUAL_OP_CODE=63013&CUSTOMER=150136979&F_OP_SITE=&F_OP_SRC=0&F_OP_ORG=0&F_RUNTIME=&F_EXT_SESSION=&F_FUNCTION "
# # 获取包含[]内的所有内容
# r = re.compile('\[([^\]]+)\]')
# result = r.findall(str)
# print(result[0])
# contentindex = str.rfind(']')
# print(contentindex)
# print(str[contentindex+1:].strip())

