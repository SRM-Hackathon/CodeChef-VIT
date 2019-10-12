import face_recognition
from PIL import Image, ImageDraw

image_of_priyank=face_recognition.load_image_file('/home/sahaaj/Desktop/VIT/git/Face-Detection/images/Priyank.jpg')
priyank_face_encoding=face_recognition.face_encodings(image_of_priyank)[0]

image_of_sahaaj=face_recognition.load_image_file('/home/sahaaj/Desktop/VIT/git/Face-Detection/images/Sahaaj.jpg')
sahaaj_face_encoding=face_recognition.face_encodings(image_of_sahaaj)[0]

image_of_rajat=face_recognition.load_image_file('/home/sahaaj/Desktop/VIT/git/Face-Detection/images/Rajat.jpg')
rajat_face_encoding=face_recognition.face_encodings(image_of_rajat)[0]

image_of_dipto=face_recognition.load_image_file('/home/sahaaj/Desktop/VIT/git/Face-Detection/images/Dipto.jpg')
dipto_face_encoding=face_recognition.face_encodings(image_of_dipto)[0]

image_of_mehul=face_recognition.load_image_file('/home/sahaaj/Desktop/VIT/git/Face-Detection/images/Mehul.jpg')
mehul_face_encoding=face_recognition.face_encodings(image_of_mehul)[0]

# create an array of encoding and names
known_face_encodings=[priyank_face_encoding,sahaaj_face_encoding]
known_face_names=["Priyank","Sahaaj"]


#load test image to find faces in

test_image=face_recognition.load_image_file('/home/sahaaj/Desktop/VIT/git/Face-Detection/TEST/group_3.jpeg')

# find faces in test image

face_location=face_recognition.face_locations(test_image)
face_encodings=face_recognition.face_encodings(test_image,face_location)

# conver to pillow format
pil_image=Image.fromarray(test_image)

#create an ImageDraw instance
draw=ImageDraw.Draw(pil_image)


# loop through faces in the test_image
for (a,b,c,d) ,face_encodings in zip(face_location,face_encodings):
        matches=face_recognition.compare_faces(known_face_encodings,face_encodings)
        name="Unknown Person"
        
        if(True in matches):
            first_match_index=matches.index(True)
            name=known_face_names[first_match_index]
        
        # Draw the box
        draw.rectangle(((d,a),(b,c)),outline=(0,0,0))
        
        #Draw labels
        text_width, text_height=draw.textsize(name)
        draw.rectangle(((d,c-text_height-10),(b,c)),fill=(0,0,0),outline=(0,0,0))
        draw.text((d+6,c-text_height-5), name,fill=(255,255,255,255))
del draw

# plot image
pil_image.show()
            