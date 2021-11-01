import pytest
from tests.buhglater import app
from unittest.mock import patch

list_search = [('s', '2207 876234', '1'), ('p', '2207 876234', 'Василий Гупкин'),
               ('s', '10006', '2'), ('p', '10006', 'Аристарх Павлов')
               ]

list_del = [('2207 876234', "Документ удален!"), ('2207 876235', "Документ по введенному номеру не найден!")]

list_add = [('1', '2', '3', '4', "Данной полки не существует!"), ('1', '2', '3', '2', "Документ добавлен!")]


class TestBuhg:

    @pytest.mark.parametrize('a, b, c', list_search)
    def test_search(self, a, b, c):
        with patch('builtins.input', return_value=b):
            assert app.search(a) == c

    @pytest.mark.parametrize('a, b', list_del)
    def test_del(self, a, b):
        with patch('builtins.input', return_value=a):
            assert app.del_doc() == b

    @pytest.mark.parametrize('a, b, c, d, e', list_add)
    def test_add(self, a, b, c, d, e):
        with patch('tests.buhglater.app.inp_type_doc', return_value=a):
            with patch('tests.buhglater.app.inp_number_doc', return_value=b):
                with patch('tests.buhglater.app.inp_name_owner', return_value=c):
                    with patch('tests.buhglater.app.inp_number_locat', return_value=d):
                        assert app.add_doc() == e
