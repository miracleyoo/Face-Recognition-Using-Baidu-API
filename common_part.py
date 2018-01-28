# coding: utf-8
from aip import AipFace
import cv2
import os
import json
"""
A file which contain functions which can be used by other files all.
"""


"""
Your APPID AK SK 
You can get them from https://ai.baidu.com
"""
APP_ID = 'xxx'
API_KEY = 'xxx'
SECRET_KEY = 'xxx'

client = AipFace(APP_ID, API_KEY, SECRET_KEY)

# read the image
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()
