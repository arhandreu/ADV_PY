import re
import vk_api
from vkinder.functions import write_msg, send_person_in_chat, change_data_client, init_client
from vk_api.longpoll import VkLongPoll, VkEventType


# token = input('Token: ')

vk = vk_api.VkApi(token='5846ad33355da3ebe6d710908e8107598ae26c1c31dc58c02ebcea8670ee9c9ad33cb6b60994f5e25deaa')
longpoll = VkLongPoll(vk)


print('Запущено')
for event in longpoll.listen():

    dict_command = {'начать': lambda: write_msg(event.user_id, vk, "Укажите id для поиска в формате 'id359223119'"),
                    'помощь': lambda: write_msg(event.user_id, vk,  "Наберите помощь для списка команд"),
                    'следующий': lambda: send_person_in_chat(event.user_id, event, client, vk),
                    }

    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            request = event.text.lower()
            if re.match('(id)([0-9]+)', request):
                client = init_client(event.user_id, request)
                change_data_client(event.user_id, client, longpoll, vk)
                client.data_person = client.search_person()
                write_msg(event.user_id, vk, "Наберите следующий для отображения ")
            else:
                dict_command.get(request, dict_command['помощь'])()




