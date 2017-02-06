# -*- coding: utf-8 -*-
import scipy.io as scio 
from numpy import ndarray
import cPickle as pickle
import sys,os
import shutil

#将记录序号与图片对应关系的文件，读取成所需要的格式
#将同一人和非同一人的数据分开，以便之后将两类里的错误数据分开存放

def pathMsg(pathPath):

    #读取记录序号与图片对应关系的文件
    testList=scio.loadmat(pathPath)
    testMsg={'0':'value','1':'value'}

    #[0][0]是因为testList['pairlist_lfw']的格式，将数据提取成想要的形式
    #如果要将该程序封装，则要声明所需的数据格式，并附加上几个数据转换的教程和程序
    x=testList['pairlist_lfw'][0][0]

    #！！！！！此处数据处理受到很强的数据局限，应提前声明数据格式
    #pairlist_lfw的数据，x[0]里的数据对是同一个，故将其key设为1，x[1]为非同一人，故key为0
    testMsg[1]=ndarray.tolist(x[0])
    testMsg[0]=ndarray.tolist(x[1])
    
    return testMsg
	
#提取出错误图片对的index
#result.pkl里有两个key：label和distance
#在matlab里将mat转成pkl
#如果原本是pkl文件，先用py将pkl转成mat，再用matlab将所需数据转成pkl

def errPairIndex(resultPath,thre):
    
    #读取运行结果
    f=open(resultPath,'r+')
    result_dict=pickle.load(f)
    
    label=result_dict['label']
    distance=result_dict['distance']

    sameErrIndex=[]
    sameErrDistance=[]
    diffErrIndex=[]
    diffErrDistance=[]

    for index, item in enumerate(result_dict['distance']):
        if (label[index]==1)and(distance[index]<=thre):
            sameErrIndex=sameErrIndex+[index]
            sameErrDistance=sameErrDistance+[round(distance[index],2)]

        if (label[index]==0)and(distance[index]>=thre):
            diffErrIndex=diffErrIndex+[index-3000]
            diffErrDistance=diffErrDistance+[round(distance[index],2)]

    midMsg={'sameErrIndex':sameErrIndex,'sameErrDistance':sameErrDistance, \
           'diffErrIndex':diffErrIndex,'diffErrDistance':diffErrDistance}
    
    return midMsg
	
#提取出pair
def getErrPair(testMsg,midMsg):

    errDir={'0':{'distance':[],'errPair':[]},'1':{'distance':[],'errPair':[]}}

    for i in midMsg['diffErrIndex']:
        errDir['0']['errPair']= errDir['0']['errPair']+[testMsg[0][i]]
    #因为 errPair和distance在顺序上的对应关系，因此可以对distance直接赋值处理
    errDir['0']['distance']=midMsg['diffErrDistance']

    for i in midMsg['sameErrIndex']:
        errDir['1']['errPair']= errDir['1']['errPair']+[testMsg[1][i]]
    #因为 errPair和distance在顺序上的对应关系，因此可以对distance直接赋值处理    
    errDir['1']['distance']=errDir['1']['distance']+midMsg['sameErrDistance']
    
    return errDir
	
def copyFile(imgPath,basicPath,RootPath,errDir,i):
    j=0
    for index, item in enumerate(errDir['errPair']):  
        i=i+1
        j=j+1
        #基础路径处理
        tmp1=errDir['errPair'][index][0]
        tmp2=errDir['errPair'][index][1]

        fName=str(errDir['distance'][index])+'-'+imgPath[tmp1].split('\\',1)[0]+'-' \
        +imgPath[tmp2].split('\\',1)[0]

        path1=basicPath+imgPath[tmp1]
        path2=basicPath+imgPath[tmp2]

        fPath=RootPath+fName
        
        #创建每个errpair的文件夹
        if not os.path.exists(str(fPath)):
            os.mkdir(str(fPath))

        #复制图片
        shutil.copy(path1,fPath)
        print path1
        shutil.copy(path2,fPath)
        print path2
        print('---------------------'+str(j)+"---copy over")
		
    print('----------copy over with---'+str(j)+'---files--------')
    return i
