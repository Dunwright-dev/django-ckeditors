"""Image tools."""

from __future__ import annotations

import logging
from bisect import bisect
from io import BytesIO
from pathlib import Path

from django.core.files.uploadedfile import UploadedFile
from PIL import Image, ImageSequence

logger = logging.getLogger(__name__)


def convert_image_to_webp(uploaded_file: UploadedFile) -> tuple[str, BytesIO]:
    """
    Converts an uploaded  validated image to WEBP format.

    Returns:
        A tuple containing the original filename with a .webp extension and
        the BytesIO stream of the converted image.
    """
    with uploaded_file.open("rb") as image_file:
        img = Image.open(image_file)

        # Handle multi-frame images (like GIFs or animated WebPs)
        if getattr(img, "is_animated", False):
            for i, frame in enumerate(ImageSequence.Iterator(img)):
                if getattr(frame, "mode", None) != "RGB":
                    img.seek(i)
                    img.paste(frame.convert("RGB"))

        # Handle single-frame images (like JPEG, PNG)
        elif getattr(img, "mode", None) != "RGB":
            img = img.convert("RGB")

        image_stream = BytesIO()
        quality = _determine_quality(uploaded_file.size)
        img.save(image_stream, format="WEBP", quality=quality, method=6)
        image_stream.seek(0)

        filename = Path(uploaded_file.name)
        webp_filename = filename.with_suffix(".webp")

        print(f"IMAGE NAME {filename}")
        print("SAVING IMAGE")
        with open(
            "/home/mark/projects/worktrees/django-ckeditors/issue-54/example/blog/tests/conv_img.webp",
            "wb",
        ) as f:
            f.write(image_stream.getvalue())

        return str(webp_filename), image_stream


def _determine_quality(image_size: int) -> int:
    """Determines the optimal WebP image quality level based on file size.

    This function uses a binary search algorithm (`bisect`) to efficiently
    find the appropriate quality level based on pre-defined file size thresholds.

    Args:
        image_size: The size of the original image in bytes.

    Returns:
        The recommended quality level for WebP compression (1-100). Lower
        values mean smaller file size but potentially lower visual quality.
    """

    # File size thresholds (in bytes) and corresponding quality levels
    thresholds = [500_000, 1_000_000, 2_000_000, 10_000_000]
    qualities = [30, 20, 10, 5, 3]  # 3 is the default for sizes over 10 MB

    # Find the index where image_size would be inserted to maintain sorted order
    index = bisect(thresholds, image_size)
    print(f"@@@@@@@  IMAGE QUALITY {qualities[index]} SIZE {image_size}")
    # Return the corresponding quality level
    return qualities[index]


"""
from django.core.files.uploadedfile import InMemoryUploadedFile
from io import BytesIO
from django_ckeditors.image import convert_image_to_webp as ci

with open('your_image.jpg', 'rb') as f:
    image_data = f.read()

image_stream = BytesIO(image_data)  # Create a BytesIO stream

uploaded_file = InMemoryUploadedFile(
    file=image_stream, 
    field_name='image_field',  # Optional: The name of the form field
    name='test_image.jpg',  # Filename
    content_type='image/jpeg',
    size=len(image_data),
    charset=None,
)
name, img = ci(uploaded_file)
"""
