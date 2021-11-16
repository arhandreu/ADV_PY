import vk_api
from pprint import pprint

vkuser = vk_api.VkApi(token='34cafda6f88390287a8e2f600dc44a44d406e6006cdf0b24246b3b974724be7b53497b864b7173c967498')


class Client:
    def __init__(self, client_id):
        self.client_id = client_id
        self.data_client = self.get_data_client()
        self.data_person = []
        self.now_person = None

    def get_data_client(self):
        fields = f'bdate, city, sex, relation'
        all_data_user = vkuser.method('users.get', {'user_ids': self.client_id, 'fields': fields})
        return {i: all_data_user[0].get(i) for i in fields.split(', ')}

    def search_person(self):
        if self.data_client['city']:
            city = self.data_client['city']['id']
        else:
            city = None
        return ([idp['id'] for idp in vkuser.method('users.search', {'birth_year': self.data_client['bdate'],
                                                                     'city': city,
                                                                     'sex': self.data_client['sex'],
                                                                     'relation': self.data_client['relation']
                                                                     })['items']])

    def send_person(self):
        for _ in self.data_person:
            try:
                id = self.data_person.pop()
                photo = [f'photo{id}_{idf}' for idf in self.get_photo_id(id)]
                yield id, photo
            except vk_api.exceptions.ApiError:
                pass

    def get_photo_id(self, id):
        all_photo = vkuser.method('photos.get', {'owner_id': id, 'album_id': 'profile', 'extended': 1})
        return [photo['id'] for photo in sorted(all_photo['items'], key=lambda photo: int(photo['likes']['count']) + (photo['comments']['count']))[:3]]

    # def change_data_client():


if __name__ == '__main__':
    user = Client(12345678)
    print(user.data_client)
    # user.search_person()
    # print(user.data_person)



