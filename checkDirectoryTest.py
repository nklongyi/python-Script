#!/usr/bin/python
# -*- coding:utf-8 -*-
# 遍历特定目录，确定其根目录
import os
import time
import platform

def getdirectorynameFromFullName(fullDirectoryName):
    """获取不同操作系统上全路径的目录名"""
    sysstr = platform.system()
    if sysstr == 'Windows':
        return fullDirectoryName[fullDirectoryName.rfind('\\') + 1:]
    else:
        return fullDirectoryName[fullDirectoryName.rfind('/') + 1:]  # linux系统


localtime = time.strftime("%Y%m%d", time.localtime())
currentworkspace = os.getcwd()
processDirector = ('log', 'log2')
for root, dirs, files in os.walk(currentworkspace):
    for dir in dirs:
        if dir == localtime:
            print("当前路径下所有子目录: %s" % dir)  # 当前路径下所有子目录
            print("根目录 is :：%s" % root)
            #对根目录处理下只获取目录
            rootdirectory = getdirectorynameFromFullName(root)
            if rootdirectory in processDirector:
                print('fuck it!')
            # workpath = root + '\\' + dir  # 仅适用于windows系统，linux系统的路径表示不一样

