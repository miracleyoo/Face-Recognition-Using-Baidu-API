# coding: utf-8
from aip import AipFace
import miPhoto as mp
import os
import json
"""
This file is write to use the basic function of baidu ai. You can take a photo and upload it 
to let the baidu ai judge how old are you and how beautiful you are, together with your gender.
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
if os.path.exists(imageSavePath) == False:
    os.mkdir("imageBase")
messageTargetPath=mp.getNewestFileName(imageSavePath)
print messageTargetPath
nextFileName='/test('+str(int(messageTargetPath)+1)+').jpg'
imageSaveFullPath = imageSavePath + nextFileName

mp.takePhotoWithCV(imageSaveFullPath)
print 'Your photo is successfully taken!'


# 定义参数变量
options = {
    'max_face_num': 1,
    'face_fields': "age,beauty,expression,faceshape,gender",
}

# 调用人脸属性检测接口
result = client.detect(mp.get_file_content(imageSaveFullPath), options)

# print result
# print json.dumps(result, sort_keys=True, indent=4)
print 'It is seemingly that your age is :', result['result'][0]['age']
print 'Your beauty value is :', result['result'][0]['beauty'], ',and the full point is 100.'
print 'It seems like that you are a :', result['result'][0]['gender'], ',with a possibility of ',\
    result['result'][0]['gender_probability']

