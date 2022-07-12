import math

from typing import Tuple
from django.db.models.fields.files import ImageFieldFile
from PIL import Image


def get_new_image_dimensions(
    original_dimensions: Tuple[int, int], new_width: int
) -> Tuple[int, int]:
    original_width, original_height = original_dimensions

    if original_width < new_width:
        return original_dimensions

    aspect_ratio = original_height / original_width

    new_height = round(new_width * aspect_ratio)

    return (new_width, new_height)


def resize_image(original_image: ImageFieldFile, width: int) -> Image:

    image = Image.open(original_image)

    new_size = get_new_image_dimensions(image.size, 1100)

    if new_size == image.size:
        return

    return image.resize(new_size, Image.ANTIALIAS)
