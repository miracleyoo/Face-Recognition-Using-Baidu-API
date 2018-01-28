# coding: utf-8
from aip import AipFace
import cv2
import os
import json
"""
This file's purpose is to do some manipulation on users, such as groups, add users in batch.
"""

"""
Your APPID AK SK 
You can get them from https://ai.baidu.com
"""
APP_ID = 'xxx'
API_KEY = 'xxx'
SECRET_KEY = 'xxx'

client = AipFace(APP_ID, API_KEY, SECRET_KEY)

# 读取图片
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

croppedImageDir=[u"./imageGroups/SeedClass2015/cropped",
                 u"./imageGroups/Dormitory/cropped",
                 u"./imageGroups/Temp/cropped"]

groups=['Seed_Class_2015', 'Dormitory', 'Temp']
num=0
for memberImages in os.listdir(croppedImageDir[2]):
    if not memberImages.startswith('.') and os.path.isfile(os.path.join(croppedImageDir[2], memberImages)):
        memberName=memberImages.split('.')[0]
#         print memberName
        num += 1
        uid = 'DUid'+str(num)
        print memberName,"测试成员：",'uid:',uid
        user_info=memberName.encode('utf-8')+":测试成员"
        client.addUser(
            uid,
            user_info,
            groups[2],
            get_file_content((croppedImageDir[2]+'/'+memberImages))
            )
