import instaloader
import os
import numpy as np

USER = "andrey1295"
PROFILE = "cats_of_instagram"

L = instaloader.Instaloader(download_pictures=True, # для постов поменять на False
                            download_videos=False,
                            download_geotags=False,
                            download_video_thumbnails=False,
                            download_comments=False,
                            save_metadata=False,
                            post_metadata_txt_pattern='')



def download_posts():
    profile = instaloader.Profile.from_username(L.context, PROFILE)
    for post in profile.get_posts():
        L.download_post(post, 'From') # 'From' - навазние папки с описанием постов

#download_posts()

def parse_pets_owners_logins(folderpath):
    """
    Пробегаю по всем папкам папок и ищу среди них логины в текстовых файлах, которые и буду парсить
    """
    owners_logins = np.empty(0)
    for dirpath, dirnames, filenames in os.walk(folderpath):
        for filename in filenames:
            filename = os.path.join(dirpath, filename)
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
    owners_logins = [login[:-1] for login in owners_logins if login.endswith(':') or login.endswith(')') or login.endswith('.')]
    return owners_logins


def download_owners_images(owners_logins, num_of_pictures_per_profile=100):

    owner_num = 742
    for owner in owners_logins[742:]:
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
    return None




owners_logins = parse_pets_owners_logins('/Users/user/Desktop/parser/From')
owners_images = download_owners_images(owners_logins)




