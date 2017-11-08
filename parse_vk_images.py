"""
Данный скрипт принимает на вход логин и пароль ВК, а на выходе формирует .json
с фотографиями cо стены указанного пользователем сообщества ВК.
"""

import warnings
warnings.filterwarnings("ignore") 
import vk_requests
import vk
from auth import *
import json
import pandas as pd
import numpy as np


# Понаставить исключений на все случаи ошибок

def create_vk_groups_list():
    """Здесь тупо создаём пустой список"""
    all_vk_groups = np.empty(0)
    return all_vk_groups


def enter_the_vk_groups(all_vk_groups):
    """
    Здесь вбиваем id-ники от групп. Чтобы не было переинициализации списка (массива) при рекурсии,
    передаём его в качестве параметра от предыдущей функции
    """
    vk_group = input('\nEnter the group ID:\n')
    all_vk_groups = np.append(all_vk_groups, vk_group)
    answer = input('Is it all? Print 1 if that is all or 0 otherwise:\n')
    if answer == '1':
	return all_vk_groups
    else:
	return enter_the_vk_groups(all_vk_groups)


def isint(s):
"""Проверка на число"""
    try:
	int(s)
        return True
    except ValueError:
	return False


def request_photos(vk_group, login, password):
    session = vk.AuthSession(
    app_id=6169227, 
    user_login=login,
    user_password=password, 
    scope='photos'
    )
    api = vk.API(session)
    if isint(vk_group) is False:  # на случай, если страница вида vk.com/abcdef
	vk_group = api.groups.getById(group_ids=vk_group, fiels='id')
	vk_group = str(vk_group[0].get('gid'))
    photo_request = api.photos.get(owner_id='-'+vk_group, album_id='wall') # '-153967240, -67878782, zaokskypr' для сообществ. Для аккаунтов без "-".
    #print(photo_request) # посмотреть сформировавшийся файл
    return photo_request


def transform_to_df(photo_request):
    srcs = np.empty(0)
    owners = np.empty(0)
    for item in photo_request:
	srcs = np.append(srcs, item['src']) # src == photo
	owners = np.append(owners, int(abs(item['owner_id']))) # чтобы не ставилась "-" перед ID группы
    df = pd.DataFrame({
	'Groups': owners,
	'Photos': srcs
	})
    return df


def main():
    login = get_user_login()
    password = get_user_password()
    groups_list = create_vk_groups_list()
    vk_groups_input = enter_the_vk_groups(groups_list)
    for vk_group in vk_groups_input:	
        photo_request = request_photos(vk_group, login, password)
	df = transform_to_df(photo_request)


	


if __name__ == '__main__':
    main()



