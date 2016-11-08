#coding=utf-8
'''
Created on 2016.10.13

@author: xiaoq
'''

import json
from file_reader import read_file
from user import *
from func import *


if __name__ == '__main__':
    records = read_file("data.txt")
    name2QQ_id = {}
    users = {}
    for record in records:
        #循环处理聊天记录
        #record是一个字典，包括QQ_id,name,timestamp,words等keys
        QQ_id = record["QQ_id"]
        #生成新用户，并不断更新用户name
        if not users.has_key(QQ_id):
            newUser = User(QQ_id, record["name"])
            name2QQ_id[record["name"]] = QQ_id
            newUser.addRecord(record)
            users[QQ_id] = newUser
        else:
            users[QQ_id].name = record["name"]
            name2QQ_id[record["name"]] = QQ_id
            users[QQ_id].addRecord(record)
    #建立QQ号和昵称之间的映射，以及index与QQ号之间的映射
    index2QQ_id = {}
    QQ_id2index = {}
    index2name = {}
    index = 0
    for userID in users.keys():
        index2QQ_id[index] = userID
        index2name[index] = users[userID].name
        QQ_id2index[userID] = index
        index = index + 1
    
    similarityMatrix = [([0] * len(users)) for i in range(len(users))]  #用户相似度矩阵
    
    maxSimilarity = 0
    #计算用户之间的亲密度
    for user1 in users.keys():
        for user2 in users.keys():
            if user1 != user2:
                similarity = getSimilarity(users[user1], users[user2])  #计算亲密度
                if similarity > maxSimilarity:
                    maxSimilarity = similarity  #记录相似度的最大值，用于归一化
                similarityMatrix[QQ_id2index[user1]][QQ_id2index[user2]] = similarity
                similarityMatrix[QQ_id2index[user2]][QQ_id2index[user1]] = similarity
    #归一化处理
    for i in range(len(users)):
        for j in range(len(users)):
            similarityMatrix[i][j] = int(float(similarityMatrix[i][j]) / maxSimilarity * 100)
            
    atCount = getAtInfo(QQ_id2index, name2QQ_id, users) #用户互相@计数
    
    dayVectors = []
    for i in range(len(users)):
        dayVectors.append(users[index2QQ_id[i]].dayVector)
        
    
    print index2name  
    store(index2QQ_id, 'index2QQ_id')  
    store(dayVectors, 'dayVectors')
    store(similarityMatrix, 'similarityMatrix')    
    store(atCount, 'atCount')   
    print "!!!!"
    