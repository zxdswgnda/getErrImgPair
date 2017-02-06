# -*- coding: utf-8 -*-
import sys
import os
import shutil
import scipy.io as scio 
from common import *
from config import *
#path����setPath.py

#testMsg���errPair��Ϣ
testMsg=pathMsg(pathPath)
#midMsg���distance��Ϣ
midMsg=errPairIndex(resultPath,thre)

errDir=getErrPair(testMsg,midMsg)

#�������������ļ���
if not os.path.exists('..\\result\\sameErr'):
	os.mkdir('..\\result\sameErr')
if not os.path.exists('..\\result\\diffErr'):
	os.mkdir('..\\result\diffErr')

#ע���β��\\������ƴ��·��
diffRootPath='..\\result\diffErr\\'
sameRootPath='..\\result\sameErr\\'

i=0
#i���ڼ�¼cpoy�����ļ���
i=copyFile(imgPath,basicPath,diffRootPath,errDir['0'],i)
print('----------next copy prepare--------')
i=copyFile(imgPath,basicPath,sameRootPath,errDir['1'],i)
print('----------all---'+str(i)+'---files copy over--------')