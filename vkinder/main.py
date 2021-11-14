from random import randrange

from vkinder.api import Client
import re
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

# token = input('Token: ')

vk = vk_api.VkApi(token='5846ad33355da3ebe6d710908e8107598ae26c1c31dc58c02ebcea8670ee9c9ad33cb6b60994f5e25deaa')
longpoll = VkLongPoll(vk)


def write_msg(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message,  'random_id': randrange(10 ** 7),})


def send_person(user_id, person):
    write_msg(user_id, f'https://vk.com/id{person[0]}')
    for i in person[1]:
        vk.method('messages.send', {'user_id': user_id,
                                    'message': 'Ваше фото',
                                    'attachment': i,
                                    'random_id': randrange(10 ** 7), })


print('Запущено')
for event in longpoll.listen():

    dict_command = {'начать поиск': lambda: write_msg(event.user_id, "Укажите id для поиска в формате 'id359223119'"),
                    'помощь': lambda: write_msg(event.user_id, "Наберите помощь для списка команд"),
                    'следующий': lambda: send_person(event.user_id, client.send_person().__next__()),
                    }

    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            request = event.text.lower()
            if re.match('(id)([0-9]+)', request):
                client = Client(re.match('(id)([0-9]+)', request)[2])
                write_msg(event.user_id, 'Наберите следующий для поиска')
            else:
                dict_command.get(request, dict_command['помощь'])()




