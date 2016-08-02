# -*- coding: utf-8 -*-
import json
import os

filedir = "/Users/wangyanghua/Desktop"

poiFeatureMap = {3: "a", 4: "d"}

userFeatureMap = {1: "a", 2: "f"}


def parseConf(str):
    str = str.replace("\\", "")
    str = str.replace("\"[", "[")
    str = str.replace("]\"", "]")
    if recorcNum == 1:
        print str
    dataDict = json.loads(str)
    if dataDict["param2"] == "2":
        for p in dataDict["param1"]:
            poiData[p["feature_id"]] += 1
    else:
        for u in dataDict["param1"]:
            userData[u["feature_id"]] += 1


def printResult():
    print "poi feature click statistics:\n"
    sorted_poiData = sorted(poiData.iteritems(), key=lambda x: x[1], reverse=True)
    for p in sorted_poiData:
        print 'poi feature %s is clicked %d times' % (poiFeatureMap[p[0]], p[1])

    print "\n***************************************\n"

    print "user feature click statistics:"
    sorted_userData = sorted(userData.iteritems(), key=lambda x: x[1], reverse=True)
    for u in sorted_userData:
        print 'user feature %s is clicked %d times' % (userFeatureMap[u[0]], u[1])


def outputResult():
    os.getcwd()
    with open(filedir + "/poiFeatureOut", "wb") as fo:
        fo.write("poi feature click statistics:\n")
        sorted_poiData = sorted(poiData.iteritems(), key=lambda x: x[1], reverse=True)
        for t in sorted_poiData:
            fo.write('poi feature %s is clicked %d times\n' % (poiFeatureMap[t[0]], t[1]))

    with open(filedir + "/userFeatureOut", "wb") as fo:
        fo.write("user feature click statistics:\n")
        sorted_userData = sorted(userData.iteritems(), key=lambda x: x[1], reverse=True)
        for t in sorted_userData:
            fo.write('user feature %s is clicked %d times\n' % (userFeatureMap[t[0]], t[1]))


def init():
    for i in poiFeatureMap:
        poiData[i] = 0
    for i in userFeatureMap:
        userData[i] = 0


if __name__ == '__main__':
    recorcNum = 0
    bugNum = 0
    poiData = {}
    userData = {}
    init()
    with open(filedir + "/myfile") as myfile:
        for line in myfile:
            recorcNum += 1
            line.strip()
            try:
                if line != "" and line != "\n" and line != "params":
                    parseConf(line)
            except Exception, e:
                bugNum += 1
                print "line %d bug with e:%s" % (recorcNum, e)

    printResult()
    #outputResult()
    print "recorcNum:%d" % (recorcNum)
    print "bugNum:%d" % (bugNum)
