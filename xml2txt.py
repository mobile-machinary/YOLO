import os
import random

trainval_percent = 0.5
train_percent = 0.5
xmlfilepath = 'data/xml'
txtsavepath = 'data/main'
total_xml = os.listdir(xmlfilepath)

#将全部的xml文件随机分为trainval和train两份
num=len(total_xml)
list=range(num)
tv=int(num*trainval_percent)
tr=int(tv*train_percent)
trainval= random.sample(list,tv)
train=random.sample(trainval,tr)

#将生成的数据分别写入trainval.txt, test.txt, train.txt, val.txt四个文件中
ftrainval = open(txtsavepath+'/trainval.txt', 'w')
ftest = open(txtsavepath+'/test.txt', 'w')
ftrain = open(txtsavepath+'/train.txt', 'w')
fval = open(txtsavepath+'/val.txt', 'w')

for i  in list:
    name=total_xml[i][:-4]+'\n'
    if i in trainval:
        ftrainval.write(name)
        if i in train:
            ftrain.write(name)
        else:
            fval.write(name)
    else:
        ftest.write(name)

ftrainval.close()
ftrain.close()
fval.close()
ftest .close()