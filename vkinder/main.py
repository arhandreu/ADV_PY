from random import randrange


import re
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vkinder.api import Client, vkuser

# token = input('Token: ')

vk = vk_api.VkApi(token='5846ad33355da3ebe6d710908e8107598ae26c1c31dc58c02ebcea8670ee9c9ad33cb6b60994f5e25deaa')
longpoll = VkLongPoll(vk)


def init_client(user_id, req):
    try:
        client = Client(re.match('(id)([0-9]+)', req)[2])
        return client
    except vk_api.exceptions.ApiError:
        write_msg(user_id, 'Набран неверный id, поробуйте еще раз')


def change_data_client(user_id):
    if not client.data_client['bdate'] or len(client.data_client['bdate'].split('.') != 3):
        write_msg(user_id, "Введите год своего рождения")
        for event in longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW:
                if event.to_me:
                    client.data_client['bdate'] = event.text
                    break
    else:
        client.data_client['bdate'] = client.data_client['bdate'].rsplit('.', 1)[1]
    if not client.data_client['city']:
        write_msg(user_id, "Наберите город")
        for event in longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW:
                if event.to_me:
                    city_title = event.text
                    client.data_client['city'] = vkuser.method('database.getCities',
                                                                 {'country_id': vkuser.method('database.getCountries',
                                                                                          {'code': 'RU'})['items'][0]['id'], 'q': city_title})['items'][0]
                    client.data_person = client.search_person()
                    break
    if client.data_client['sex'] == 0 or not client.data_client['sex']:
        dict_sex = {'женщина': 2,
                    'мужчина': 1}
        write_msg(user_id, "Напишите свой пол - мужчина/женщина")
        for event in longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW:
                if event.to_me:
                    client.data_client['sex'] = dict_sex.get(event.text)
                    break
    if not client.data_client['relation']:
        pass


def write_msg(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message,  'random_id': randrange(10 ** 7),})


def send_person_in_chat(user_id):
    try:
        person = client.send_person().__next__()
        client.now_person = person[0]
        write_msg(user_id, f'https://vk.com/id{client.now_person}')
        for i in person[1]:
            vk.method('messages.send', {'user_id': user_id,
                                        'attachment': i,
                                        'random_id': randrange(10 ** 7), })
    except NameError:
        write_msg(event.user_id, "Укажите id для поиска в формате 'id359223119'")
    except StopIteration:
        write_msg(event.user_id, "Закончились данные")


print('Запущено')
for event in longpoll.listen():

    dict_command = {'начать': lambda: write_msg(event.user_id, "Укажите id для поиска в формате 'id359223119'"),
                    'помощь': lambda: write_msg(event.user_id, "Наберите помощь для списка команд"),
                    'следующий': lambda: send_person_in_chat(event.user_id),
                    }

    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            request = event.text.lower()
            if re.match('(id)([0-9]+)', request):
                client = init_client(event.user_id, request)
                change_data_client(event.user_id)
                client.data_person = client.search_person()
                write_msg(event.user_id, "Наберите следующий для отображения ")
            else:
                dict_command.get(request, dict_command['помощь'])()




