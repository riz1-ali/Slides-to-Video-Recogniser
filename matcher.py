import cv2 as cv
import glob
from os import listdir
import time
import numpy as np
import sys

def correlation_coefficient(patch1, patch2):
    product = np.mean((patch1 - patch1.mean()) * (patch2 - patch2.mean()))
    stds = patch1.std() * patch2.std()
    if stds == 0:
        return 0
    else:
        product /= stds
        return product

all_frames = []
frame_names = []
all_slides = []
slide_names = []
matched_slide = {}
slides_path = sys.argv[1]
frames_path = sys.argv[2]

if slides_path[-1] != '/':
    slides_path = slides_path + '/'
if frames_path[-1] != '/':
    frames_path = frames_path + '/'

for file in listdir(frames_path):
    if file == '.' or file == '..':
        continue
    img = cv.imread(frames_path + file)
    img = cv.resize(img,(512,512))
    all_frames.append(img)
    frame_names.append(file)

for file in listdir(slides_path):
    if file == '.' or file == '..':
        continue
    img = cv.imread(slides_path + file)
    img = cv.resize(img,(512,512))
    all_slides.append(img)
    slide_names.append(file)

orb = cv.ORB_create()
bfmatcher = cv.BFMatcher(cv.NORM_HAMMING, crossCheck=True)

for i in range(len(all_frames)):
    x=time.time()
    im1 = all_frames[i]
    ind=-1
    sums = []
    mini=1000000000000000000000000000000000000000000000000
    kp1, des1 = orb.detectAndCompute(im1,None)
    for j in range(len(all_slides)):
        im2 = all_slides[j]
        kp2, des2 = orb.detectAndCompute(im2,None)
        matches = bfmatcher.match(des1,des2)
        matches = sorted(matches, key = lambda x:x.distance)
        sumt=0
        for p in range(min(len(matches),30)):
            sumt+=matches[p].distance*matches[p].distance
        sums.append(sumt)

    lt = [i[0] for i in sorted(enumerate(sums), key=lambda x:x[1])]
    maxi = -1
    sumx = 0
    for p in range(min(5,len(lt))):
        im2 = all_slides[lt[p]]
        sumx = correlation_coefficient(im1,im2)
        if maxi < sumx:
            maxi = sumx
            ind = lt[p]

    matched_slide[frame_names[i]] = slide_names[ind]

frame_names.sort()

with open('output.txt','w') as file:
    for i in range(len(frame_names)):
        file.write(frame_names[i])
        file.write(' ')
        file.write(matched_slide[frame_names[i]])
        file.write('\n')
