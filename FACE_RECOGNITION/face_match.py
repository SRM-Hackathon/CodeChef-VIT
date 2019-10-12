import face_recognition
image_of_priyank=face_recognition.load_image_file('/home/sahaaj/Desktop/VIT/git/Face-Detection/images/Priyank.jpg')
priyank_face_encoding=face_recognition.face_encodings(image_of_priyank)[0]

unknown_image=face_recognition.load_image_file('/home/sahaaj/Desktop/VIT/git/Face-Detection/TEST/test_3.jpg')
unknown_face_encoding=face_recognition.face_encodings(unknown_image)[0]

#compare faces
results=face_recognition.compare_faces([priyank_face_encoding],unknown_face_encoding)

if results[0]:
    print("This is Priyank\n")
else:
    print("This is not Priyank\n")