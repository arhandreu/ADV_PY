import requests
import pytest
from datetime import datetime


def create_folder(folder_name, url, headers):
    return requests.put(url + "v1/disk/resources", headers=headers, params={'path': folder_name})


class TestYandex:
    name_folder = datetime.now().strftime("%Y-%m-%d_%H-%M")
    list_create = [(name_folder, 201), (name_folder, 409)]

    @classmethod
    def setup_class(cls):
        cls.token = 'AQAAAAA2H9_LAADLW-43ftNJPECCivb_MLCw-pk'
        cls.url = 'https://cloud-api.yandex.net:443/'
        cls.headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {cls.token}',
        }
        print('Начало теста')

    @pytest.mark.parametrize('folder_name, code', list_create)
    def test_create_folder(self, folder_name, code):
        assert create_folder(folder_name, self.url, self.headers).status_code == code

