"""
using opencv to detect and show faces in image,
also list other classifiers
"""
import cv2
import numpy as np
import time

cap=cv2.VideoCapture(0)

success,frame=cap.read()
classifier=cv2.CascadeClassifier("haarcascades/haarcascade_frontalface_alt.xml")

# ***some classifiers in opencv***
# lbpcascades/lbpcascade_frontalface.xml
# haarcascades/haarcascade_eye.xml
# haarcascades/haarcascade_eye_tree_eyeglasses.xml
# haarcascades/haarcascade_frontalface_alt.xml
# haarcascades/haarcascade_frontalface_alt_tree.xml
# haarcascades/haarcascade_frontalface_alt2.xml
# haarcascades/haarcascade_frontalface_default.xml
# haarcascades/haarcascade_fullbody.xml
# haarcascades/haarcascade_lefteye_2splits.xml
# haarcascades/haarcascade_lowerbody.xml
# haarcascades/haarcascade_mcs_eyepair_big.xml
# haarcascades/haarcascade_mcs_eyepair_small.xml
# haarcascades/haarcascade_mcs_lusing opencv to detect and show faces in image,
also list other classifierseftear.xml
# haarcascades/haarcascade_mcs_lefteye.xml
# haarcascades/haarcascade_mcs_mouth.xml
# haarcascades/haarcascade_mcs_nose.xml
# haarcascades/haarcascade_mcs_rightear.xml
# haarcascades/haarcascade_mcs_righteye.xml
# haarcascades/haarcascade_mcs_upperbody.xml
# haarcascades/haarcascade_profileface.xml
# haarcascades/haarcascade_righteye_2splits.xml
# haarcascades/haarcascade_upperbody.xml

starttime=0

while success:
	success,frame=cap.read()
	size=frame.shape[:2]
	image=np.zeros(size,dtype=np.float16)
	image=cv2.cvtColor(frame,cv2.cv.CV_BGR2GRAY)
	cv2.equalizeHist(image,image)
	divisor=8
	h,w=size
	minSize=(w/divisor,h/divisor)
	faceRects=classifier.detectMultiScale(image,1.1,3,cv2.CASCADE_SCALE_IMAGE,minSize)
	
	if len(faceRects)>0:
		for faceRect in faceRects:
			x,y,w,h=faceRect
			cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
	'''
	#create a window for each face
			face=frame[y:y+h,x:x+w]
			n=np.where(faceRects==faceRect)
			win_name="face "+str(n[0][0]+1)
			cv2.imshow(win_name,face)
	else:
		cv2.destroyWindow(win_name)
	'''
	cv2.imshow("Faces",frame)
	k=cv2.waitKey(10) & 0xFF
	if k == 27:
		break
cv2.destroyAllWindows()
