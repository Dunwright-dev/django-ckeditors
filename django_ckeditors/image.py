"""Image tools."""

import io
from pathlib import Path
from PIL import Image
# import pillow_avif  # noqa: F401
from django.core.exceptions import ValidationError
from django.core.files.images import ImageFile
from django.core.files.uploadedfile import UploadedFile
from django.db.models.fields.files import ImageFieldFile
from django.utils.translation import gettext_lazy as _
import logging

logger = logging.getLogger(__name__)


def image_formatter(
    image: UploadedFile = None,
    height: int = None,
    width: int = None,
    save_format: str = 'webp',
    quality: int = None,
) -> Image.Image:
    """Take an UploadedFile image and massage it to a suitable web format.

    Params
    ======

    :param image: `django.core.files.uploadedfile.InMemoryUploadedFile` object.
    :param save_format: str Options:
                                AVIF: convert image to .avif format.
                                WEBP: convert image to .webp format.
                                JPEG: convert image to .jpg format.
                                PNG: convert image to .png format.
    :param quality: int. Optional: 0 to 100 inclusive. Worst to Best quality.


    ###############################################

    NOT IMPLEMENTED

    :param height: int. Optional: Height in pixels.
    :param width: int. Optional: Width in pixels.

    ###############################################

    :raises ValidationError:  When user attempts to upload an unsupported file.
    :raises TypeError: When an internal error caused by developer mistake
                    passing incorrect types.

    :returns: UploadedFile


    See reference material here https://github.com/trader-biz/britstralian/issues/235

    """

    # if isinstance(image, ImageFieldFile):
    #     print(f"\n\nCONVERTING IMAGE NOT REQUIRED RETURNING {image}\n\n")
    #     return image

    save_format=save_format.lower()

    match image:
        case UploadedFile():
            uploaded_file_name = Path(image.__dict__["_name"])
            # supported_image_formats = [
            #     ".jpg",
            #     ".jpeg",
            #     ".jfif",
            #     ".pjpeg",
            #     ".pjp",
            #     ".avif",
            #     ".png",
            #     ".webp",
            # ]
            #
            # # Check the uploaded file type is supported.
            # # We use a validation error here so that feedback can be supplied to the user.
            # if (
            #     not uploaded_file_name.suffix.lower()
            #     in supported_image_formats
            # ):
            #     raise ValidationError(
            #         _(
            #             "The image format %(save_format)s you have uploaded is not supported. Please use one of %(supported)s"  # noqa: E501
            #         ),
            #         params={
            #             "save_format": uploaded_file_name.suffix,
            #             "supported": str(supported_image_formats)
            #             .replace("[", "")
            #             .replace("]", "")
            #             .replace("'", "")
            #             .replace(",", ""),
            #         },
            #     )

            img_size = int(image.__dict__["size"])
            file_extension = ""

            if img_size > 20_000_000:
                raise ValidationError(
                    _(
                        "The image size %(image_size)s Megabits you have uploaded is to large. The maximum image size is 20 Megabits."  # noqa: E501
                    ),
                    params={
                        "image_size": img_size / 1_000_000,
                    },
                )

            match save_format:
                # case None | "AVIF":
                #     save_format = "AVIF"
                #     # Determine a suitable quality for the image.
                #     # Determines the finished file size in bytes. Smaller is better.
                #     if 500_000 >= img_size:
                #         quality = 30
                #     if 500_000 <= img_size <= 1000_000:
                #         quality = 20
                #     if 1_000_001 <= img_size <= 2_000_000:
                #         quality = 10
                #     if 2_000_001 <= img_size <= 10_000_000:
                #         quality = 5
                #     if 10_000_001 <= img_size:
                #         quality = 3
                #     file_extension = ".avif"

                case 'webp' |  "jpeg" |  "png":
                    # Determine a suitable quality for the image.
                    # Determines the finished file size in bytes. Smaller is better.
                    if 500_000 >= img_size:
                        quality = 30
                    if 500_000 <= img_size <= 1000_000:
                        quality = 20
                    if 1_000_001 <= img_size <= 2_000_000:
                        quality = 10
                    if 2_000_001 <= img_size <= 10_000_000:
                        quality = 5
                    if 10_000_001 <= img_size:
                        quality = 3

                    file_extension = f'.{save_format}'
                # case "JPEG" | "jpeg":
                #     # Determine a suitable quality for the image.
                #     # Determines the finished file size in bytes. Smaller is better.
                #     if 500_000 >= img_size:
                #         quality = 30
                #     if 500_000 <= img_size <= 1000_000:
                #         quality = 20
                #     if 1_000_001 <= img_size <= 2_000_000:
                #         quality = 10
                #     if 2_000_001 <= img_size <= 10_000_000:
                #         quality = 5
                #     if 10_000_001 <= img_size:
                #         quality = 3
                #
                #     file_extension = f'.{save_format.lower()}'
                #
                # case "PNG" | "png":
                #     # Determine a suitable quality for the image.
                #     # Determines the finished file size in bytes. Smaller is better.
                #     if 500_000 >= img_size:
                #         quality = 30
                #     if 500_000 <= img_size <= 1000_000:
                #         quality = 20
                #     if 1_000_001 <= img_size <= 2_000_000:
                #         quality = 10
                #     if 2_000_001 <= img_size <= 10_000_000:
                #         quality = 5
                #     if 10_000_001 <= img_size:
                #         quality = 3
                #
                #     file_extension = ".png"

                case _:
                    raise TypeError(
                        f"Image save format must be of type WEBP, JPEG or PNG: {save_format} supplied",
                    )

        case _:
            raise TypeError(
                f"Image must be of type <class django.core.files.uploadedfile.UploadedFile>: {type(image)} supplied.",  # noqa: E501
            )

    # Create the new filename with correct extension to match the updated format
    file_name = Path(image.__dict__["_name"]).with_suffix(file_extension).name

    # Open the image as a pillow object to change format.
    formatted_image = Image.open(image)
    # Create an in memory buffer to save the image to.
    image_buffer = io.BytesIO()
    formatted_image.save(
        image_buffer,
        format=save_format,
        quality=quality,
        optimize=True,
    )

    updated_image = ImageFile(
        io.BytesIO(image_buffer.getvalue()),
        name=file_name,
    )

    # Close the buffer to free up memory.
    image_buffer.close()

    # Return a Django ImageFile with updated format.
    # return updated_image


    return formatted_image
