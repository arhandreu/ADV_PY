import json

url_wiki = 'https://en.wikipedia.org/wiki/'


class IteratorWiki():

    url_wiki = 'https://en.wikipedia.org/wiki/'

    def __init__(self, path_file='countries.json'):
        self.path = path_file
        self.list_countries = None

    def __iter__(self):
        self.create_list_countries()
        return self

    def __next__(self):
        country_name = self.list_countries.pop(0)
        if not self.list_countries:
            print('Запись завершена')
            raise StopIteration
        text = country_name[0] + ' - ' + self.url_wiki + country_name[1]
        self.write_in_files(text)

    def create_list_countries(self):
        with open(self.path, encoding='ascii') as countries:
            data = json.load(countries)
            self.list_countries = [[country['name']['official'], '_'.join(country['name']['official'].split())] for country in data]
            return self.list_countries

    def write_in_files(self, text, write_file= 'Iterator.txt'):
        with open(write_file, 'at', encoding='utf-8') as file:
            file.write(text + '\n')


if __name__ == '__main__':
    find_c = IteratorWiki()
    for item in find_c:
        item
