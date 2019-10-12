from PIL import Image
import face_recognition


image=face_recognition.load_image_file('/home/sahaaj/Desktop/VIT/git/Face-Detection/TEST/group_2.jpg')
image_faces=face_recognition.face_locations(image)

for a,b,x,y in image_faces:
    face_image=image[a:x,y:b]
    pil_image=Image.fromarray(face_image)
    pil_image.show();
    