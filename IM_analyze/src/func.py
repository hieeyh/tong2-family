#coding=utf-8
'''
Created on 2016.10.14

@author: xiaoq
'''
import math
# 该模块提供对正则表达式的支持
import re   

def getSimilarity(user1, user2):
    '''
    计算两个用户之间的亲密度
    
    通过将用户的发言密度向量化，以向量内积的方式计算用户亲密度
    '''
    similarity = 0
    vectorLen1 = 0
    vectorLen2 = 0 
    for i in range(len(user1.featureVector)):
        similarity = similarity + user1.featureVector[i] * user2.featureVector[i]
        vectorLen1 = vectorLen1 + user1.featureVector[i] * user1.featureVector[i]
        vectorLen2 = vectorLen2 + user2.featureVector[i] * user2.featureVector[i]
    
    return similarity / math.sqrt(vectorLen1) / math.sqrt(vectorLen2)

def getAtInfo(QQ_id2index, name2QQ_id, users):
    '''
    获取用户之间互相@的计数
    '''
    atCount = [([0] * len(users)) for i in range(len(users))]  #用户@计数
    for user in users.values():
        for friendName in user.aRecords:
            for name in name2QQ_id.keys():
                result = re.search(friendName, name)
                if result:
                    print friendName
                    print name
                    atCount[QQ_id2index[name2QQ_id[user.name]]][QQ_id2index[name2QQ_id[name]]] = atCount[QQ_id2index[name2QQ_id[user.name]]][QQ_id2index[name2QQ_id[name]]] + 1
                    break
    return atCount  

def store(obj, objName):
    import json
    
    with open(objName + '.json', 'w') as f:
        f.write(json.dumps(obj))              
                