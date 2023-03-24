from flask import Flask, jsonify, request
from flask_cors import CORS

from src.create_images import create_images
from src.delete_images import delete_images
from src.facial_recognition import facial_recognition

app = Flask(__name__)
CORS(app)


@app.route('/user-recognition', methods=["POST"])
def user_recognition():
    try:
        face_image_base64 = request.json["faceImage"]
        id_card_image_base64 = request.json["idCardImage"]

        create_images(face_image_base64, id_card_image_base64)

        result = facial_recognition(
            "images/face_image.png", "images/id_card_image.png")

        delete_images("images/face_image.png", "images/id_card_image.png")

        return jsonify(result)
    except Exception:
        return jsonify({"error": "No se pudo procesar la petición"})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
