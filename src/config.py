# -*- coding: utf-8 -*-
#数据格式转化
import scipy.io as scio

#阈值，根据自己需求而设
thre=-141

#要注意pairlist_lfw.mat里路径的写法，/（linux下）和\（win下）不能混用，代码中的路径格式与mat中保持一致
#-----------------------------------------------------------------------------------------------------------
#result.pkl里存放的是测试结果
resultPath='..\data\\result.pkl'

#pairlist_lfw里存放被测试的图片对中，每张图片在imgPath.mat中的索引值
#通过索引值，在imgPath.mat中找到被测试图片的存放路劲
pathPath='..\data\pairlist_lfw.mat'

#-------------------------------------------------------------------------imgPath.mat里是n*1的char
#准备工作：
#在matlab里，在matlab里:
#1.用imgPath=char(imagelist_lfw['imagelist_lfw']),将里面的cell改成char，并保存成imgPath
#2.save imgPath.mat imgPath 保存成imgPath.mat
#然后在py中：
imgPath=scio.loadmat('..\data\imgPath.mat')['imgPath']
#-不建议采用的的方式---------------------------------------用imagelist_lfw得到imgPath,imagelist_lfw里是n*1的cell
#在Joint-Bayesian中，imgPath.mat里的数据=imagelist_lfw.mat
#但是imagelist_lfw.mat里的每个路径，都以cell的形式存放
#imagelist_lfw='..\data\imagelist_lfw.mat'

#这里的转化按情况自行修改
#得到的imgPath
#imgPath=str(scio.loadmat(imagelist_lfw)['imagelist_lfw'])

#这个方法的通用性不强，因为每个对象的索引是在scio.loadmat(imagelist_lfw)['imagelist_lfw'][i][0]上
#这样就必须在使用imgPath时，对其进行索引并再取[0],这样如果换了数据，数据形式上略微的差异，都会导致各种错误
#因此采用统一的数据输入，有利于复用
#如果非要用这种方式:
#将common.py里的copyFile方法中的imgPath[tmp1]和imgPath[tmp2]都替换成imgPath[tmp1][0]和imgPath[tmp2][0]

#-------------------------------------------------------------------------
#图片数据存放根路径，加上imgPath里的路径后，就形成了每个图片的路径
basicPath='..\data\lfw\\'
#注意结尾的\\，之后用于字符串拼接