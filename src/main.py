# -*- coding: utf-8 -*-
import sys
import os
import shutil
import scipy.io as scio 
from common import *
from config import *
#path都在setPath.py

#testMsg存放errPair信息
testMsg=pathMsg(pathPath)
#midMsg存放distance信息
midMsg=errPairIndex(resultPath,thre)

errDir=getErrPair(testMsg,midMsg)

#创建保存结果的文件夹
if not os.path.exists('..\\result\\sameErr'):
	os.mkdir('..\\result\sameErr')
if not os.path.exists('..\\result\\diffErr'):
	os.mkdir('..\\result\diffErr')

#注意结尾的\\，用于拼接路径
diffRootPath='..\\result\diffErr\\'
sameRootPath='..\\result\sameErr\\'

i=0
#i用于记录cpoy的总文件数
i=copyFile(imgPath,basicPath,diffRootPath,errDir['0'],i)
print('----------next copy prepare--------')
i=copyFile(imgPath,basicPath,sameRootPath,errDir['1'],i)
print('----------all---'+str(i)+'---files copy over--------')