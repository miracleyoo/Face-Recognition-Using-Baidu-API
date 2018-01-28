# coding: utf-8
import cv2
import os
import re
import sys
from PIL import Image
# 获取一个文件夹中命名中含有的唯一一个数字最大的文件名和这个数字的元组
def getNewestFileName(direc):
    fileNames=os.listdir(direc)
    maxNum=0
    p = re.compile(r'\d+')
    maxNum = 0
    for files in fileNames:
        if not files.startswith('.') == True and p.findall(files) != []:
            m = p.findall(files)
            num = int(m[-1])
            if int(num) > maxNum:
                maxNum = int(num)
    return maxNum

# 使用OpenCV拍张照片存在savePath里
def takePhotoWithCV(savePath):
    WINDOW_NAME = 'Take a photo of you!'
    cv2.startWindowThread()
    cap = cv2.VideoCapture(0)
    while (1):
        # get a frame
        ret, frame = cap.read()
        # show a frame

        cv2.imshow(WINDOW_NAME, frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.imwrite(savePath, frame)
            break
    cap.release()
    cv2.waitKey(1)
    cv2.destroyAllWindows()

# 使用OpenCV显示一张图片，图片路径为openPath
def showPhotoWithCV(openPath):
    cv2.startWindowThread()
    img = cv2.imread(openPath)
    cv2.imshow('Image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    for i in range(5):
        cv2.waitKey(1)

# 读取图片
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

# 批量制作缩略图
def make_thumbnail_for_image_in_dir(path,subdir='cropped',x=256,y=256):
    """This function will make a thumbnail for a series of pictures in a folder 
    path, and it will save the new generated images into path/subdir, with a resulotion
    of size(x,y)
    """
    size = (x,y)
    if path.endswith('/'):
        path=path[:-1]
    if os.path.exists(path+'/'+subdir) == False:
        os.mkdir(path+'/'+subdir)
    for infile in os.listdir(path):
        if not infile.startswith('.') and os.path.isfile(os.path.join(path, infile)):
            outfile = path+'/'+subdir+'/'+os.path.splitext(infile)[0]+'_thumbnail.jpg'
            try:
                im = Image.open(path+'/'+infile)
                im.thumbnail(size)
                im.save(outfile, "JPEG")
            except IOError:
                print("cannot create thumbnail for", infile)

# 批量剪裁文件夹中图片
def crop_images_in_dir(path,subdir='cropped',x1=0,y1=0,x2=256,y2=256):
    """This function will make a cropped image for a series of pictures in a folder 
    path, and it will save the new generated images into path/subdir.The region is 
    defined by a 4-tuple, where coordinates are (left, upper, right, lower). The 
    Python Imaging Library uses a coordinate system with (0, 0) in the upper left corner. 
    """
    if path.endswith('/'):
        path=path[:-1]
    if os.path.exists(path+'/'+subdir) == False:
        os.mkdir(path+'/'+subdir)
    classImageNames=os.listdir(path)
    for infile in classImageNames:
        if not infile.startswith('.') and os.path.isfile(os.path.join(path, infile)):
            outfile = path+'/'+subdir+'/'+os.path.splitext(infile)[0]+'_cropped.jpg'
    #         print outfile
            im=Image.open(path+'/'+infile)
            box = (x1, y1, x2, y2)
            region = im.crop(box)
            region.save(outfile)