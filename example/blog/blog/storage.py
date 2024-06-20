"""blog custom storage module."""

from django.core.files.storage import FileSystemStorage


class ImageCustomFileSystemStorage(FileSystemStorage):
    """
    Overrides save and url methods to add a custom path prefix to
    file URLs for your testing environment.
    """

    def save(self, name, content, max_length=None):
        """
        Overrides the save method. We'll leave the saving logic to the base
        FileSystemStorage class.
        """
        new_name = f"tests/custom/path/{name}"
        return super().save(
            name=new_name,
            content=content,
            max_length=max_length,
        )

    def url(self, name):
        """Overrides the URL generation for saved files."""
        return name


'''
# def image_url_handler(request):
#     """Return a unique image path_to/filename"""
#     img = request.FILES["upload"]
#     fpath = pathlib.Path(img.name)
#     new_name = "new_img_name"
#
#     return f"images/{new_name}{fpath.suffix}"
'''
