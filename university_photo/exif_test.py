from university_photo.exif import *


def test_get_file_created_at():
    with open("media/test.jpg", "rb") as f:
        file = f.read()
    res = get_file_created_at(file)
    print(res)