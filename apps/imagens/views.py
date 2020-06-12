import cv2
from django.http import HttpResponseServerError, StreamingHttpResponse
from django.shortcuts import render
from django.views.decorators import gzip

# Create your views here.



class VideoCamera(object):
    def __init__(self):
        # URL = 'apps/utils/video/WIN_20200611_22_01_47_Pro.mp4'
        URL = 'apps/utils/video/ezgif.com-gif-makerx4.mp4'
        # self.video = cv2.VideoCapture(0)
        self.video = cv2.VideoCapture(URL)
    def __del__(self):
        self.video.release()

    def get_frame(self):
        HAARCASCADE_FACE = 'apps/utils/haarcascade/haarcascade_frontalcatface.xml'
        ret,image = self.video.read()
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        face_cascade = cv2.CascadeClassifier(HAARCASCADE_FACE)
        faces = face_cascade.detectMultiScale(gray, 1.1, 0)
        for (x, y, w, h) in faces:
            # To draw a rectangle in a face
            cv2.rectangle(image, (x, y), (x + w, y + h), (255, 255, 0), 2)

        ret,jpeg = cv2.imencode('.jpg',image)
        return jpeg.tobytes()

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield(b'--frame\r\n'
        b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@gzip.gzip_page
def index(request):
    try:
        return StreamingHttpResponse(gen(VideoCamera()),content_type="multipart/x-mixed-replace;boundary=frame")
    except HttpResponseServerError as e:
        print("aborted")