# coding: utf-8
from aip import AipFace
import miPhoto as mp
import json
import os
"""
This is the file which can make you judge whether you are in a certain group.
You need to change the code in groups[i] to make the program know which group
you are in and also, you need to take a photo.
"""


"""
Your APPID AK SK 
You can get them from https://ai.baidu.com
"""
APP_ID = 'xxx'
API_KEY = 'xxx'
SECRET_KEY = 'xxx'

client = AipFace(APP_ID, API_KEY, SECRET_KEY)

currentPath = os.getcwd()
imageSavePath = currentPath + '/imageBase'
if not os.path.exists(imageSavePath):
    os.mkdir("imageBase")
messageTargetPath = mp.getNewestFileName(imageSavePath)

# print messageTargetPath
nextFileName = '/test(' + str(int(messageTargetPath) + 1) + ').jpg'
imageSaveFullPath = imageSavePath + nextFileName

mp.takePhotoWithCV(imageSaveFullPath)
print 'Your photo is successfully taken!'

options = {
    'top_num': 2,
}

groups = ['Seed_Class_2015', 'Dormitory', 'Temp']

result = client.identifyUser(
    groups[0],
    mp.get_file_content(imageSaveFullPath),
    options
)
print json.dumps(result, sort_keys=True, indent=4)
# print json.dumps(client.getUser(uid),indent=4,ensure_ascii=False)
if result['result'][0]['scores'][0] >= 80:
    print "认证成功！欢迎您，", result['result'][0]['user_info']
else:
    print "认证失败！"
