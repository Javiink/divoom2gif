import time, os
from apixoo import APIxoo, GalleryCategory, GalleryDimension


class Object(object):
    pass

# Divoom account
EMAIL = os.environ['EMAIL']
MD5_PASSWORD = os.environ['MD5_PASSWORD']

# Also accept password string with "password='password'"
api = APIxoo(EMAIL, md5_password=MD5_PASSWORD)
status = api.log_in()
if not status:
    print('Login error!')
else:
    """ files = api.get_category_files(
        GalleryCategory.RECOMMEND,
        dimension=GalleryDimension.W16H16,
        page=1,
        per_page=20,
    ) """

    animObj = Object()
    """Here you should place the animation ID, like maybe "group1/M00/87/87/eEwpPV9ZCeKEE3awAAAAAEajLp08050878" """
    animObj.file_id = ""

    pixel_bean = api.download(animObj)
    if pixel_bean:
        timestr = time.strftime("%Y%m%d-%H%M%S")
        pixel_bean.save_to_gif(f'gif/{timestr}.gif', scale=1)


    """ for info in files:
        print(info)
        pixel_bean = api.download(info)
        if pixel_bean:
            pixel_bean.save_to_gif(f'gif/{info.gallery_id}.gif', scale=5) """