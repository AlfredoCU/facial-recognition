from os import remove


def delete_images(face_image, id_card_image):
    try:
        remove(face_image)
        remove(id_card_image)
    except Exception:
        print("Error al eliminar las imágenes")
