from flask import Flask, request, Response
import time
import PIL.Image as Image
from img import baseimg
import base64
import io


app = Flask(__name__)

@app.route('/')
def index():
    return Response(open('./templates/ss.html').read(), mimetype="text/html")

# save the image as a picture
@app.route('/image', methods=['POST'])
def image():

    blob = request.files['image'].read()  # get the image
    blob2 = base64.b64encode(blob)
    print(blob2)
    #print(blob)
    f = ('%s.jpeg' % time.strftime("%Y%m%d-%H%M%S"))
    data = base64.b64decode(baseimg)
    #print(data)
    image_object = Image.open(io.BytesIO(blob))
    print(image_object)
    image_object.show()
    decodeit = open('hello_level.jpeg', 'wb')
    decodeit.write(base64.b64decode((blob2)))
    decodeit.close()
    print("images saved!!!!!!!")
    """image = blob[0][0]
    print("appple")
    print(image)

    # Decode the string
    binary_data = base64.b64decode(image)

    # Convert the bytes into a PIL image
    image = Image.open(io.BytesIO(binary_data))

    # Display the image"""
    #cv2.imshow('Aplle', image)

    """cap = cv2.VideoCapture(image_object)
    while True:
        _, frame = cap.read()
        cv2.imshow('Screen', frame)
        if cv2.waitKey(1) == 27:
            break
        cap.release()
        cv2.destroyAllWindows()"""
    """print(blob)
    blob.save('%s/%s' % (PATH_TO_TEST_IMAGES_DIR, "realTime.jpeg"))
    data = base64.b64decode(blob)
    print(data)"""
    return Response("%s saved" % f)



if __name__ == '__main__':
    #app.run(host='192.168.1.105', port=5000, debug=True)
    #app.run()
    from waitress import serve
    serve(app, host="0.0.0.0", port=5000)
