import json
import face_recognition


def facial_recognition(face_image, id_card_image):
    try:
        known_image = face_recognition.load_image_file(face_image)
        unknown_image = face_recognition.load_image_file(id_card_image)

        user_encoding = face_recognition.face_encodings(known_image)[0]
        unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

        results = face_recognition.compare_faces(
            [user_encoding], unknown_encoding)

        return {"response": json.dumps(bool(results[0]))}
    except Exception:
        return {"error": "Error al procesar las imágenes"}
