# -*- coding: utf-8 -*-
"""
1. Поменять PROFILE на необходимый.
2. Поменять два последних атрибута для объекта L. 
Если скачиваем посты, то должен быть включён последний пост; если скачиваем уже фото - то предпоследний.
3. Включить вызов двух последних функций (если скачиваем фото) и отключаем вызов (если скачиваем посты)
4. Если скачиваем посты - включаем вызов функции download_posts.
4.5 Если скачиваем фото, то download_posts комментируем, а owners_logins и owners_images раскомментируем. 
5. При скачивании фото ставим download_pictures=True. А если скачиваем посты, то этому же атрибуту ставим False.
"""

import instaloader
import os
import numpy as np

USER = "andrey1295"
PROFILE = "dogs_of_day"

L = instaloader.Instaloader(download_pictures=True, # для постов поменять на False
                            download_videos=False,
                            download_geotags=False,
                            download_video_thumbnails=False,
                            download_comments=False,
                            save_metadata=False,
                            post_metadata_txt_pattern='') # РАСкомментировать при скачивании фото
                            #post_metadata_txt_pattern='{caption}') # РАСкомментировать при скачивании никнеймов из постов


def download_posts():
    profile = instaloader.Profile.from_username(L.context, PROFILE)
    for post in profile.get_posts():
        L.download_post(post, PROFILE) # 'dogs' - сюда будут сохраниться .txt с постом-текстом


#download_posts()






def parse_pets_owners_logins(folderpath):
    """
    Пробегаю по всем папкам папок и ищу среди них логины в текстовых файлах, которые и буду парсить
    """

    owners_logins = np.empty(0)
    for dirpath, dirnames, filenames in os.walk(folderpath):
        for filename in filenames:
            filename = os.path.join(dirpath, filename)
            print(filename)
            if ('.txt' in filename) and ('UTC' in filename):
                with open(filename, 'r') as f:
                    try:
                        logins = f.read().split()
                        for login in logins:
                            if login.startswith('@'):
                                owners_logins = np.append(owners_logins, login)
                    except:
                        continue
    print(len(owners_logins))

    # Удаляем значок @
    owners_logins = [owner_login[1:] for owner_login in owners_logins]
    owners_logins = list(filter(lambda x: x != PROFILE, owners_logins))
    
    #owners_logins = [login[:-1] for login in owners_logins if login.endswith(':') or 
    #                                                          login.endswith(')') or 
    #                                                          login.endswith('.') or
    #                                                          login.endswith(',')]
    print(owners_logins)
    print('len: ', len(owners_logins))
    return owners_logins




def download_owners_images(owners_logins, num_of_pictures_per_profile=100):

    owner_num = 0
    for owner in owners_logins[0:]:
        if owner == PROFILE:
            continue
        owner_num += 1
        try:
            i = 0 # We calculate only first 100 photos from account to make parsing faster
            profile = instaloader.Profile.from_username(L.context, "{}".format(owner))
            for post in profile.get_posts():
                i += 1
                if i < num_of_pictures_per_profile:
                    L.download_post(post, '{}'.format(owner_num))
                else:
                    break
        except:
            continue
    #return None




owners_logins = parse_pets_owners_logins(r'C:\Users\User\Documents\Parser\{}'.format(PROFILE))
owners_images = download_owners_images(owners_logins)
