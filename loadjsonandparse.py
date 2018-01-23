#!/usr/bin/python
# -*- coding:utf-8 -*-
import os
import sys
import time
import re
import json

start = time.clock()
#读json文件
try:
    tarjsonfile = open('targetJson.json','rU')
except IOError:
    print("Io errors")
    sys.exit(0)
# JSOn进行合并后的json文件
# 检查是否存在目标文件，如果存在就删除
if os.path.exists('last.json'):
    print('Detect the last file,Now deleting the file......')
    os.remove('last.json')
    print('Alreay delete the target file!！！！！！！')
try:
    lastJsonfile = open("last.json", "a")
except IOError:
    print("Io errors")
    sys.exit(0)
# 初始化
line = tarjsonfile.next()
line = json.loads(unicode(line, errors='ignore'))
preline = line #第一行为初始化行
premsgid = preline['MSG_ID']
premsgtype = preline['MsgType'].strip()
strmsg = preline['MSG']

# 开始遍历
currentline = tarjsonfile.next()
while True:
    try:
        # 当前的行进行json load
        currentline = json.loads(unicode(currentline, errors='ignore'))
            # 如果消息ID与上一条消息不一致,则将上一条消息写入文本，同时将pre至于current，然后进行下一次遍历
        if premsgid != currentline['MSG_ID']:
            # 将preMSG的信息写入到文件
            json.dump(preline, lastJsonfile, ensure_ascii=False, sort_keys=True)
            lastJsonfile.write('\n')
            # 同时改变pre指向
            preline = currentline
            premsgid = currentline['MSG_ID']
            premsgtype = currentline['MsgType'].strip()
            strmsg = currentline['MSG'].strip()

            # 如果消息ID相等且消息类型相同，则进行MSg拼接，拼接后进行下一次遍历
        if premsgid == currentline['MSG_ID'] and premsgtype == currentline['MsgType'].strip():
            strmsg = strmsg + currentline['MSG'].strip()
            preline['MSG'] = strmsg

            # 如果消息ID相等但消息类型不相同,则将上一条消息写入到文本，同时将pre至于current，然后下一次遍历
        if premsgid == currentline['MSG_ID'] and premsgtype != currentline['MsgType'].strip():
            # 将preMSG的信息写入到文件
            json.dump(preline, lastJsonfile, ensure_ascii=False, sort_keys=True)
            lastJsonfile.write('\n')
            # 同时改变pre指向
            preline = currentline
            premsgid = currentline['MSG_ID']
            premsgtype = currentline['MsgType'].strip()
            strmsg = currentline['MSG'].strip()
        # 下一次遍历
        currentline = tarjsonfile.next()
    except StopIteration:
        # 将preMSG的信息写入到文件
        json.dump(preline, lastJsonfile, ensure_ascii=False, sort_keys=True)
        lastJsonfile.write('\n')
        print("已经处理到最后一行了！")
        break

# 关闭文件
tarjsonfile.close()
lastJsonfile.close()
end = time.clock()
print("Totoal cost time is:%s " %(end -start))
print("文件转换完毕，请检查")
