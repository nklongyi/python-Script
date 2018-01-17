#!/usr/bin/python
# -*- utf-8 -*-
# 对匹配正则表达式进行测试
import re
import sys
import string
import os

currworkspace = os.getcwd()
print("当前工作目录:%s" %(currworkspace))
for root, dirs, files in os.walk(currworkspace):
    print("当前目录路径: %s" %(root)) #当前目录路径
    print("当前路径下所有子目录: %s" %(dirs)) #当前路径下所有子目录
    print("当前路径下所有非目录子文件: %s" %(files)) #当前路径下所有非目录子文件
    print("--------------------------")
# str="[20180116-080000][  -988519801][2514-3c38][ 1] KADPKingdomWrapper:Req:L0380404,0120000000000000000010171101711000000050569E    KCXP00  GV2gODkBbGg=20180116080000000000000404L038040400517000000KGOB1     108_CA=2.3&_ENDIAN=1&F_EXT_OP_CODE=&F_OP_USER=63013&F_OP_USER_ENC=wns9koYZBXQ@3D&END_DATE=2018-01-15&F_OP_ROLE=2&F_CUST_ORG_CODE=3013&serverid=1&ACCOUNT=301320097813&g_serverid=1&OPER_CONVERT=1&F_CHANNEL=0&F_REAL_CODE_ENC=&BGN_DATE=2018-01-15&YGT_VIRTUAL_OP_CODE=63013&CUSTOMER=150136979&F_OP_SITE=&F_OP_SRC=0&F_OP_ORG=0&F_RUNTIME=&F_EXT_SESSION=&F_FUNCTION "
# # 获取包含[]内的所有内容
# r = re.compile('\[([^\]]+)\]')
# result = r.findall(str)
# print(result[0])
# contentindex = str.rfind(']')
# print(contentindex)
# print(str[contentindex+1:].strip())

