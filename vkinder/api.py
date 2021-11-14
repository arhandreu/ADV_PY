import vk_api
from pprint import pprint

vkuser = vk_api.VkApi(token='34cafda6f88390287a8e2f600dc44a44d406e6006cdf0b24246b3b974724be7b53497b864b7173c967498')


class Client:
    def __init__(self, user_id):
        self.user_id = user_id
        self.data_user = self.get_data_user()
        self.data_person = self.search_person()

    def get_data_user(self):
        fields = f'bdate, city, sex, relation'
        all_data_user = vkuser.method('users.get', {'user_ids': self.user_id, 'fields': fields})
        return {i: all_data_user[0].get(i) for i in fields.split(', ')}

    def search_person(self):
        return ([idp['id'] for idp in vkuser.method('users.search', {'bdate': self.data_user['bdate'],
                                              'city': self.data_user['city'],
                                              'sex': self.data_user['sex'],
                                              'relation': self.data_user['relation']
                                              })['items']])

    def change_data_user(self):
        for key, value in self.data_user.items():
            if not value:
                self.data_user[key] = 1

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


if __name__ == '__main__':
    user = Client(359223119)
    print(user.data_user)
    print(user.data_person)
