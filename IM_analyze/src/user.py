#coding=utf-8
'''
Created on 2016.10.14.

@author: xiaoq
'''

import re

class User(object):
    '''
    classdocs
    '''
    #用户描述类
    
    #储存用户的特性
    '''
    '''
    statisticUnit = 6  #统计单元（分钟）
    

    def __init__(self, QQ_id_, name_):
        '''
        Constructor
        '''
        self.QQ_id = QQ_id_ #QQ号
        self.name = name_   #昵称
        self.names = set()
        self.records = []   #该用户的所有原始聊天记录
        self.aRecords = []  #该用户@的行为记录
        self.words = "" #该用户的所有发言
        self.recordCount = 0    #该用户的发言总次数
        self.featureVector = [0] * (141 * 24 * 60 / self.statisticUnit)    #该用户的发言密度描述向量，最小统计单元为6分钟
        self.dayVector = [0] * (24 * 60 / self.statisticUnit)  #该用户平均每天的聊天密度，最小统计单元为6分钟
        
    def addRecord(self, record):
        '''
        #记录一条发言
        '''
        self.names.add(record["name"])
        self.records.append(record)
        self.getAfriend(record["words"])
        self.words = self.words + record["words"]
        self.recordCount = self.recordCount + 1
        timeInSec = record["timeInSec"]
        #计算发言密度
        self.featureVector[timeInSec / (self.statisticUnit * 60)] = self.featureVector[timeInSec / (self.statisticUnit * 60)] + 1
        timeInSecInTheDay = timeInSec % (24 * 3600)
        self.dayVector[timeInSecInTheDay / (self.statisticUnit * 60)] = self.dayVector[timeInSecInTheDay / (self.statisticUnit * 60)] + 1
        
    def getAfriend(self, words):  
        friend = re.search("(@\S*\s)|(@\S*$)", words)
        if friend and len(friend.group()) < 3:
            friend = re.search("(@\s*\S*\s)|(@\s*\S*$)", words)
        if friend:
            print words
            name = friend.group()[1:-1]
            self.aRecords.append(name)
            print name
            