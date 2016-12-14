#coding=utf-8
'''
Created on 2016.10.14

@author: xiaoq, houge
'''
import re
import datetime, time

def read_file(filepath):
    '''
    #读取文件，用list来储存聊天记录
    '''
    records = []
    f = open(filepath, "r")
    lines = f.readlines()
    flag = False
    record = {}
    startTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    for line in lines:
        #解析文本
        line = line.decode('utf-8')
        timestamp = re.search("^\d*-\d*-\d*\s\d*:\d*:\d*", line)
        if timestamp:
            if flag and len(record) == 5 and str(record["QQ_id"]).find("0000") < 0:
                #剔除系统消息
                records.append(record)
            nowTime = time.strptime(timestamp.group(),"%Y-%m-%d %H:%M:%S")  #格式化时间戳
            record = {"timestamp": nowTime}
            if not flag:
                #记录第一条发言的日期，并以当天的零点作为左右发言时间的起点
                startTime = time.strptime(timestamp.group()[0:11] + "00:00:00", "%Y-%m-%d %H:%M:%S")
            record["timeInSec"] = getTimeInSec(nowTime, startTime)  #获取发言的时间，以第一条发言当天的零点开始计秒
            
            #利用正则表达式来解析出QQ号、昵称、时间戳等信息
            name = re.search(":\d\d\s[\s\S]*\(", line)
            if name:
                record["name"] = name.group()[4:-1]
            QQ_id = re.search("\(\S*\)", line)
            if QQ_id:
                record["QQ_id"] = int(QQ_id.group()[1:-1])
            flag = True
        elif flag:
            if record.has_key("words"):
                record["words"] = record["words"] + line
            else:
                record["words"] = line
    print len(records)
    return records

def getTimeInSec(timestamp, start):
    #将时间转换为从2016.5.24开始的秒数
    return int(time.mktime(timestamp)) - int(time.mktime(start))

def getWeek(timeInSec):
    #根据以秒计数的时间戳获取星期
    timeInSec = timeInSec % (7 * 24 * 3600)
    timeInSec = timeInSec / (24 * 3600)
    return 2 + timeInSec
    
