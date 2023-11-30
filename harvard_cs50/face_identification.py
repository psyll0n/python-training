from PIL import Image, ImageDraw
import face_recognition
import numpy as np

own_image = face_recognition.load_image_file("steve_carrel.jpg")
encoding = face_recognition.face_encodings(own_image)[0]

unknown_image = face_recognition.load_image_file("office_cast.jpg")

face_locations = face_recognition.face_locations(unknown_image)
face_encodings = face_recognition.face_encodings(unknown_image, face_locations)

pil_image = Image.fromarray(unknown_image)

draw = ImageDraw.Draw(pil_image)

for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
    matches = face_recognition.compare_faces([encoding], face_encoding)

    if True in matches:
        name = "Person Identified"

        draw.rectangle(((left, top), (right, bottom)), outline=(0, 255, 0))
        draw.text((left, top - 10), name, fill=(0, 255, 0), font=None)

    else:
        name = "Unknown"
        draw.rectangle(((left, top), (right, bottom)), outline=(255, 255, 0))
        draw.text((left, top - 10), name, fill=(255, 255, 0), font=None)


pil_image.show()
