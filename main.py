import os
from apixoo import APIxoo, GalleryCategory, GalleryDimension

# Divoom account
EMAIL = os.environ['EMAIL']
MD5_PASSWORD = os.environ['MD5_PASSWORD']
animations_per_page = int(os.environ['ANIMATIONS_PER_PAGE'])
pages_to_dl = int(os.environ['DOWNLOAD_PAGES'])

# Also accept password string with "password='password'"
api = APIxoo(EMAIL, md5_password=MD5_PASSWORD)
status = api.log_in()
if not status:
    print('Login error!')
else:
    iteration = 1

    while iteration <= pages_to_dl:            
        files = api.get_category_files(
            GalleryCategory.RECOMMEND,
            dimension=GalleryDimension.W16H16,
            page=iteration,
            per_page=animations_per_page,
        )

        for info in files:
            print(info)
            pixel_bean = api.download(info)
            if pixel_bean:
                pixel_bean.save_to_gif(f'gif/{info.gallery_id}.gif', scale=5)

        iteration += 1