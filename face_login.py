# coding: utf-8
from aip import AipFace
import miPhoto as mp
import json
import os
from enum import Enum, unique
"""
This file provide you with the function that you can enter your real name and take a photo,
then the system can determine whether you are the certain person you entered the name.
"""

# A look-up table. Left is the name of your mumber's name, 
# and the right is the number of each certain person
SCUid={
    'xxx':'SCUid1',
    'xxx':'SCUid2',
    'xxx':'SCUid3',
    'xxx':'SCUid4',
    'xxx':'SCUid5',
    'xxx':'SCUid6',
    'xxx':'SCUid7',
    'xxx':'SCUid8',
    'xxx':'SCUid9',
    'xxx':'SCUid10',
    'xxx':'SCUid11',
    'xxx':'SCUid12',
    'xxx':'SCUid13',
    'xxx':'SCUid14',
    'xxx':'SCUid15',
    'xxx':'SCUid16',
    'xxx':'SCUid17',
    'xxx':'SCUid18',
    'xxx':'SCUid19',
    'xxx':'SCUid20',
    'xxx':'SCUid21'}

"""
Your APPID AK SK 
You can get them from https://ai.baidu.com
"""
APP_ID = 'xxx'
API_KEY = 'xxx'
SECRET_KEY = 'xxx'

client = AipFace(APP_ID, API_KEY, SECRET_KEY)

cname = raw_input("Please input your Chinese name correctly:")
uid = SCUid[cname]

currentPath = os.getcwd()
imageSavePath = currentPath + '/imageBase'
if os.path.exists(imageSavePath) == False:
    os.mkdir("imageBase")
messageTargetPath=mp.getNewestFileName(imageSavePath)

# print messageTargetPath
nextFileName='/test('+str(int(messageTargetPath)+1)+').jpg'
imageSaveFullPath = imageSavePath + nextFileName

mp.takePhotoWithCV(imageSaveFullPath)
print 'Your photo was successfully taken!'

options = {
  'top_num': 1,
}

result=client.verifyUser(
                  uid,
                  'Seed_Class_2015',
                  mp.get_file_content(imageSaveFullPath),
                  options
                )
# print json.dumps(result, sort_keys=True, indent=4)
# print json.dumps(client.getUser(uid),indent=4,ensure_ascii=False)
if result['result']>= 80:
    print "认证成功！欢迎您，",client.getUser(uid)['result'][0]['user_info']
else:
    print "认证失败！"