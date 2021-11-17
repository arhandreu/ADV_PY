import vk_api
import re
from vkinder.api import Client, vkuser
from vk_api.longpoll import VkEventType
from random import randrange


def init_client(user_id, req):
    try:
        client = Client(re.match('(id)([0-9]+)', req)[2])
        return client
    except vk_api.exceptions.ApiError:
        write_msg(user_id, 'Набран неверный id, поробуйте еще раз')


def change_data_client(user_id, client, longpoll, vk):
    while not client.data_client['bdate'] or int(client.data_client['bdate']) \
            not in range(1900, 2100) or not client.data_client['city'] or int(client.data_client['sex']) not in [1, 2]:
        write_msg(user_id, vk, "У Вас не хватает данных, либо Вы указали их неверно, давайте решим эту проблему!!")
        if not client.data_client['bdate'] or len(client.data_client['bdate']) != 4:
            write_msg(user_id, vk, "Введите год своего рождения")
            for event in longpoll.listen():
                if event.type == VkEventType.MESSAGE_NEW:
                    if event.to_me:
                        client.data_client['bdate'] = event.text
                        break
        elif client.data_client['bdate'].split('.') == 3:
            client.data_client['bdate'] = client.data_client['bdate'].rsplit('.', 1)[1]
        if not client.data_client['city']:
            write_msg(user_id, vk, "Введите город")
            for event in longpoll.listen():
                if event.type == VkEventType.MESSAGE_NEW:
                    if event.to_me:
                        city_title = event.text
                        try:
                            client.data_client['city'] = vkuser.method('database.getCities',
                                                                         {'country_id': vkuser.method('database.getCountries',
                                                                                                  {'code': 'RU'})['items'][0]['id'], 'q': city_title})['items'][0]
                        except IndexError:
                            pass
                        break
        if client.data_client['sex'] == 0 or not client.data_client['sex']:
            dict_sex = {'женщина': 2,
                        'мужчина': 1}
            write_msg(user_id, vk, "Напишите свой пол - мужчина/женщина")
            for event in longpoll.listen():
                if event.type == VkEventType.MESSAGE_NEW:
                    if event.to_me:
                        client.data_client['sex'] = dict_sex.get(event.text)
                        break
        if not client.data_client['relation']:
            pass


def write_msg(user_id, vk, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message,  'random_id': randrange(10 ** 7),})


def send_person_in_chat(user_id, event, client, vk):
    try:
        person = client.send_person().__next__()
        client.now_person = person[0]
        write_msg(user_id, vk, f'https://vk.com/id{client.now_person}')
        for i in person[1]:
            vk.method('messages.send', {'user_id': user_id,
                                        'attachment': i,
                                        'random_id': randrange(10 ** 7), })
    except NameError:
        write_msg(event.user_id, "Укажите id для поиска в формате 'id359223119'")
    except StopIteration:
        write_msg(event.user_id, "Закончились данные")