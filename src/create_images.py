import base64
from PIL import Image
from io import BytesIO


def create_images(face_image_base64, id_card_image_base64):
    try:
        face_image_decoded = base64.b64decode(face_image_base64)
        id_card_image_decoded = base64.b64decode(id_card_image_base64)

        face_image_bytes = Image.open(BytesIO(face_image_decoded))
        id_card_image_bytes = Image.open(BytesIO(id_card_image_decoded))

        face_image = face_image_bytes.convert("RGB")
        id_card_image = id_card_image_bytes.convert("RGB")

        face_image.save("images/face_image.png")
        id_card_image.save("images/id_card_image.png")
    except Exception:
        print("Error al crear las imágenes")
