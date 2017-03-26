"""
Using OpenCV take photos
"""
import cv2
import time

timeformat = "%Y-%m-%d %H-%M-%S"

print '''
	enter "s" to save photo;
	enter "ESC" to exit.
	'''

cap=cv2.VideoCapture(0)
success,frame=cap.read()


while success:
	success,frame=cap.read()

	cv2.imshow("camera",frame)
	k=cv2.waitKey(1000/10) & 0xFF
	
	# enter "s" to save photo
	if k == ord("s"):
		photoname = time.strftime(timeformat)+".jpg"
		cv2.imwrite(photoname,frame)
		print "saved photo: "+photoname
	
	# enter "ESC" to exit
	if k == 27:
		break

cv2.destroyAllWindows()
