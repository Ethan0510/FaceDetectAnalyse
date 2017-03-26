"""
Using opencv get the faces in images.
Using Face++ get the similarity between two faces.
"""

from __future__ import print_function
import cv2
import numpy as np
import time
import requests
import os
import mimetypes

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
API_KEY = 'xxx'
API_SECRET = 'xxx'
BASE_URL = 'http://apicn.faceplusplus.com/v2'


def detect_face():　　　　
	"""
	using opencv detect faces.	Using opencv get the faces in images.
Using Face++ get the similarity between two faces.
"""
	"""
    cap = cv2.VideoCapture(0)
    next_capture_time = time.time()
    faces = []

    if not cap.isOpened():
        print("Capture Opening ERROR!")

    while 1:
        ret, img = cap.read()

        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        if next_capture_time < time.time():
            next_capture_time += 0.1
            faces = face_cascade.detectMultiScale(img_gray, 1.3, 5)
        if faces is not None:
            for x, y, w, h in faces:
                img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        
		cv2.imshow("face_detect", img)
        k = cv2.waitKey(1) & 0xFF
        if k == ord('s'):
            cv2.imwrite("image/face2.jpg", img)　　#save image when enter "s"
        if k == 27:
            break

    cap.release()
    cv2.destroyAllWindows()


def upload_img(file_dir, oneface=True):
	"""
	update faces to face++ and return faceID
	"""

    url = '%s/detection/detect?api_key=%s&api_secret=%s&attribute=none' % (BASE_URL, API_KEY, API_SECRET)
    if oneface:
        url += '&mode=oneface'
    files = {'img': (os.path.basename(file_dir), open(file_dir, 'rb'), mimetypes.guess_type(file_dir)[0])}
    r = requests.post(url, files=files)
    faces = r.json().get('face')
    if faces is None:
        print("No face")
    else:
        return faces[0]['face_id']


def compare(faceID1, faceID2):
	"""get similarity between two faces"""

    url = '%s/recognition/compare?api_key=%s&api_secret=%s&face_id1=%s&face_id2=%s' % (
    BASE_URL, API_KEY, API_SECRET, faceID1, faceID2)
    r = requests.get(url)
    return r.json()


if __name__ == "__main__":
    faceID1 = upload_img('image/lena.jpg')
    faceID2 = upload_img('image/17-1m.bmp')
    if faceID2 and faceID1:
        compare_json = compare(faceID1, faceID2)
        print(compare_json)
        if (compare_json['similarity'] > 90):　　# print "yes" when similarity > 90%,else "no"
            print("yes")
        else:
            print("no")
    else:
        print("Something wrong with the pictures!")
