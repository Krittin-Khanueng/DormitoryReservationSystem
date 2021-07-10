""" Image Helper."""

# PIL
from PIL import Image, ExifTags

# IO
from io import BytesIO

# Django
from django.core.files.uploadedfile import InMemoryUploadedFile

# import
import sys
import time


class ImageHelper:
    """Image helper
    Rezise image that came from front-end
    """

    def compressImage(self, uploadedImage, width, height, quality):
        """read"""
        image = Image.open(uploadedImage)

        """ handle orientation"""
        try:
            orientation = None
            for orientation in ExifTags.TAGS.keys():
                if ExifTags.TAGS[orientation] == 'Orientation':
                    break

            exif = image._getexif()  # 6
            if exif[orientation] == 3:
                image = image.rotate(180, expand=True)
            elif exif[orientation] == 6:
                image = image.rotate(270, expand=True)
            elif exif[orientation] == 8:
                image = image.rotate(90, expand=True)

        except (AttributeError, KeyError, IndexError, TypeError):
            # cases: image don't have getexif
            pass

        """ get RGB IMAGE"""
        if image.mode != 'RGB':
            image = image.convert('RGB')

        """ rezise image """
        outputIoStream = BytesIO()
        image.thumbnail((width, height))
        time_stamp = int(round(time.time() * 1000))  # TIME
        image_name = "%s_%s%s" % (
            time_stamp, str(round(image.size[0])) + "x" + str(round(image.size[1])), ".jpg")  # filename image
        image.save(outputIoStream, format='JPEG', quality=quality)
        outputIoStream.seek(0)
        uploadedImage = InMemoryUploadedFile(outputIoStream, 'FileField', image_name, 'image/jpeg',
                                             sys.getsizeof(outputIoStream), None)
        return uploadedImage

# EX is user
# imagesave = ImageHelper()
# self.path = imagesave.compressImage(self.path, 1280, 1280, 70)
