from flask import Flask, request, Response, render_template
import time
import PIL.Image as Image
from img import baseimg
import base64
import io
import cv2
import joblib


app = Flask(__name__)

face_detector = cv2.CascadeClassifier('static/haarcascade_frontalface_default.xml')

def extract_faces(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face_points = face_detector.detectMultiScale(gray, 1.3, 5)
    return face_points

def identify_face(facearray):
    model = joblib.load('static/face_recognition_model.pkl')
    return model.predict(facearray)

@app.route('/')
def index():
    #return Response(open('./templates/ss.html').read(), mimetype="text/html")
    return render_template('ss.html')

# save the image as a picture
@app.route('/image', methods=['GET', 'POST'])
def image():

    blob = request.files['image'].read()  # get the image
    blob2 = base64.b64encode(blob)
    print(blob2)
    image_object = Image.open(io.BytesIO(blob))
    print(image_object)
    #image_object.show()
    decodeit = open('hello_level.jpeg', 'wb')
    decodeit.write(base64.b64decode((blob2)))
    decodeit.close()
    frame = cv2.imread('hello_level.jpeg')
    #print(frame)
    (x, y, w, h) = extract_faces(frame)[0]
    #cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 20), 2)
    face = cv2.resize(frame[y:y + h, x:x + w], (50, 50))
    image.identified_person = identify_face(face.reshape(1, -1))[0]
    #if request.method == 'POST':
    #identified_person = "Apple"
    print("images saved!!!!!!!")
    print(image.identified_person[:-2])

    #return render_template('ss.html', identified_person=identified_person)
    return "Success"

@app.route('/ass', methods=['GET', 'POST'])
def print_name():
    try:
        akk = image.identified_person[:-2]
    except Exception as e:
        akk = "Abhishek"
    print(akk)

    return render_template('ss.html', akk=akk)

if __name__ == '__main__':
    #app.run(host='192.168.1.101', port=5000, debug=True)
    #app.run(debug=True)
    from waitress import serve
    serve(app, host="0.0.0.0", port=5000)
