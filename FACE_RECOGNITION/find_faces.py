import face_recognition
image=face_recognition.load_image_file('/home/sahaaj/Desktop/VIT/git/Face-Detection/TEST/group_2.jpg')
face_locations=face_recognition.face_locations(image)
print(f'The number of people in this image are {len(face_locations)}')
