#!/usr/bin/python
# -*- coding:utf-8 -*-
# 用于将kdop的当天的日志转化为JSon格式
# 读取log日志文件，写入json文件
# author：程龙,email:chenglong@szkingdom.com
import sys
import time
import re
import os
import platform
import json


# 定义将源文件进行转换json
def translogToJson(sourceLogFile, info):
    # 1.打开原日志文件（只读)
    try:
        logfile = open(sourceLogFile, 'r')
    except IOError:
        print("Something wrong happend when read the log file,Please check the file and system!")
        sys.exit(0)
    print("Reading the logfile......")
    # 2创建转换后日志文件（写+模式）
    try:
        jsonLogfile = open("tmpjson.json", "a")
    except IOError:
        print("Creating target file wrong,please check!")
        sys.exit(0)
    # 3.循环读取每1行，对每一个行进行解析(将每一行转换为JSon串并追加到tranferlogfile）
    print("start analysis the file......")
    start = time.clock()
    for line in logfile.readlines():
        # 去掉行首或者行尾的空格
        line = line.strip()
        # 判断是否是空行或注释行
        if line.startswith('#'):
            continue
        if line.strip() == '':
            continue
        # 定义字典，接收解析后的数据
        dictStr = {}
        # 获取[]内的所有内容
        r = re.compile('\[([^\]]+)\]')
        result = r.findall(line)
        # 如果匹配获得的字符串为空，则结束循环
        if not len(result):
            break
        # 1.获取第一个时间区段
        dictStr['DateTime'] = result[0]
        # 2.获取MSg_ID
        dictStr['MSG_ID'] = result[2]
        # 3.消息类型ID -988519801
        dictStr['MsgType'] = result[1]
        # 4.获取MSG
        contentindex = line.rfind(']')  # 从右开始查找到第一个]的索引位置
        dictStr['MSG'] = line[contentindex + 1:].strip()  # 获取的内容去除前后空格
        # 5.append到指定的文件写入
        json.dump(dictStr, jsonLogfile, ensure_ascii=False, sort_keys=True)
        jsonLogfile.write('\n')
        # 6.处理行的信息记录到处理信息中
        info['processLine'] = info['processLine'] + 1
    end = time.clock()
    costtimes = (end - start)
    print("End of analysis!!!")
    print("The process cost :：%fs" % (costtimes))
    # 文件解析正确性检查 确保原文件行数与解析后写入的行数相等，若不相等，则重新进行操作
    # 记录处理文件信息
    info['fileNum'] = info['fileNum'] + 1
    # 关闭日志文件的访问
    logfile.close()
    jsonLogfile.close()
    return


# 验证环节
def valideprocessInfo(processInfo):
    try:
        jsonLogfile = open("tmpjson.json", "r")
    except IOError:
        print("There is something Error in opening the temporary json file ,please check the file,make sure it's ok!")
        sys.exit(0)
    print("------Now validating the temporary json file------")
    print("Already Processed logfile : %s，Analysis the line number of log file is : %s" % (
        processInfo['fileNum'], processInfo['processLine']))
    print("Transfered to json format file,The line number is ：%s" % (len(jsonLogfile.readlines())))
    jsonLogfile.seek(0)
    if len(jsonLogfile.readlines()) == processInfo['processLine']:
        print("Pass the validate process,Parse the log file correctly!")
        print("------Pass validate------")
    else:
        print("Something wrong happened in transfer process! Please rerun the python script!!!")
    # 关闭日志文件访问
    jsonLogfile.close()
    return


# 不同操作系统（win and linux）拼接目录路径
def concatedirstronos(source, target):
    """在不同操作系统上将souce目录和target目录进行拼接
    :rtype: string
    """
    sysstr = platform.system()
    if sysstr == 'Windows':
        return source + '\\' + target
    else:
        return source + '/' + target
    return


# 获取全路径上目录
def getdirectorynameFromFullName(fullDirectoryName):
    """获取不同操作系统上全路径的目录名"""
    sysstr = platform.system()
    if sysstr == 'Windows':
        return fullDirectoryName[fullDirectoryName.rfind('\\') + 1:]
    else:
        return fullDirectoryName[fullDirectoryName.rfind('/') + 1:]  # linux系统


# 检查上一次执行情况并执行对应操作
def checklastresult():
    # 若存在tmpJson.json文件，则删除
    if os.path.exists('tmpjson.json'):
        print('Detect the target json file,Now deleting the file......')
        os.remove('tmpjson.json')
        print('Alreay delete the target file!！！！！！！')
    return


# 对生成的临时json文件进行合并，合并后对文件进行校验，校验成功后删除临时文件
def processtmpjsonfile(sourcejson, targetjson):
    # 读json文件
    try:
        tarjsonfile = open(sourcejson, 'rU')
    except IOError:
        print("Io errors")
        sys.exit(0)
    # JSOn进行合并后的json文件
    # 检查是否存在目标文件，如果存在就删除
    if os.path.exists(targetjson):
        print('Detect the last file,Now deleting the file......')
        os.remove(targetjson)
        print('Alreay delete the target file!！！！！！！')
    try:
        lastJsonfile = open(targetjson, "a")
    except IOError:
        print("Io errors")
        sys.exit(0)
    # 初始化
    line = tarjsonfile.next()
    line = json.loads(unicode(line, errors='ignore'))
    preline = line  # 第一行为初始化行
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
            break
    # 关闭文件
    tarjsonfile.close()
    lastJsonfile.close()
    print("Process tmp Json file is done!!!")


# 返回list之中的相同值的索引
def find_all_index(arr, item):
    return [i for i, a in enumerate(arr) if a == item]


# 验证合并后的json文件
def validatelastjsonfile(sourcefile):
    """如果存在有相同的msg_id 和msg—type，则说明json合并过程中出错"""
    # 通过set的不可重复性，来判断
    msgtypelist = []
    msgidlist = []
    try:
        jsonfile = open(sourcefile, 'rU')
    except IOError:
        print("In validate last json file process: open the file error")
    # 获取目标json的总行数
    totallines = len(jsonfile.readlines())
    # 文件指针置于文件开头
    jsonfile.seek(0)
    # 读取json每一行，提取msg_Type到元组内
    for line in jsonfile.readlines():
        sline = json.loads(unicode(line, errors='ignore'))
        msgtypelist.append(sline['MsgType'].strip())
        msgidlist.append(sline['MSG_ID'].strip())
    # 对相同的msg type再比较msg_id
    for msgtype in msgtypelist:
        if msgtypelist.count(msgtype) >= 2:
            # 将所有相同msg_type的index给找到
            sametypevalueindex = find_all_index(msgtypelist, msgtype)
            tmpmsgidlist = []
            # 找到相同type的msgID
            for i in sametypevalueindex:
                tmpmsgidlist.append(msgidlist[i])
            # 如果 tmpmsgidlist 的值是否有相同
            for j in tmpmsgidlist:
                if tmpmsgidlist.count(j) >= 2:
                    print("Target json is not right,Rerun the python script,or check the algorithm!")
                    break
    print("validate the target json,pass the validate process!!!!")


# 遍历指定目录并转换为JSON文件
def loopandtransforjson(currentworkspace, localtime, processDirector, targetjsonfilename):
    # 开始时间
    startpy = time.clock()
    # 处理的文件数目、行数记录等信息
    processInfo = dict(fileNum=0, processLine=0)
    # 沿当前脚本所在目录向下遍历，找到当日的日期命名的文件
    for root, dirs, files in os.walk(currentworkspace):
        for dir in dirs:
            if dir == localtime:
                # 检验根目录是否是需要处理的根目录（不能将其他非特定目标系统的日志进行转换）
                rootdirectory = getdirectorynameFromFullName(root)
                if rootdirectory in processDirector:
                    print("================== IN THE DIRECTORY:%s ==================" % rootdirectory)
                    print("Already found the target child directory: %s" % dir)  # 当前路径下所有子目录
                    print("The root directory of the current directory is :：%s" % root)
                    # workpath = root + '\\' + dir  # 仅适用于windows系统，linux系统的路径表示不一样
                    workpath = concatedirstronos(root, dir)
                    os.chdir(workpath)
                    print("Changed the work space to  %s" % (os.getcwd()))
                    # 检查当前目录，删除上一次生成的文件
                    checklastresult()
                    # 遍历日志目录下所有log文件并转换成JSON
                    for rootd, ndirs, nfiles in os.walk(workpath):
                        for filename in nfiles:
                            index = filename.rfind('.')
                            if filename[index + 1:] == "log":
                                print("------Detecting the log file :：%s ------" % filename)
                                print("Start to transform log file %s to json format ......" % filename)
                                translogToJson(filename, processInfo)
                    # 转换完毕，进入校验环节
                    valideprocessInfo(processInfo)
                    # 临时JSOn校验通过后，对临时JSON文件进行MSG_ID合并操作
                    processtmpjsonfile("tmpjson.json", targetjsonfilename)
                    # 对最终Json文件进行验证
                    validatelastjsonfile(targetjsonfilename)
                    # 删除临时json文件
                    os.remove("tmpjson.json")
                    endpy = time.clock()
                    print("In the %s  Total run time ：%fs" % (rootdirectory, endpy - startpy))
                    print("================== IN THE DIRECTORY:%s END END END ==================" % rootdirectory)
                else:
                    for targetdirectory in processDirector:
                        print("The directory %s is not under the target Directory %s" % (dir, targetdirectory))


# 获取当前工作目录(脚本所在目录)
currentworkspace = os.getcwd()
# 获取当前日期,格式化为20180129
localtime = time.strftime("%Y%m%d", time.localtime())
# 需要处理的目录（只遍历该目录下的日志）
processDirector = ('msg','rmsg')  # ','后面的逗号不能少（否则会当做字符串处理）
# 目标日志文件名
targetjsonfilename = "msg_" + localtime + ".json"
# 运行时间间隔(秒为基本单位）
delay = 20
# 运行计数
countperday = 0
# 开始运行脚本
while True:
    # 开始转换
    loopandtransforjson(currentworkspace, localtime,  processDirector, targetjsonfilename)
    print("After %s seconds ,Transforpocess will be start,please wait!" % delay)
    # 开始延时
    time.sleep(delay)
    countperday +=1
    print("The script already run %s times" % countperday)



