documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}


def help():
    print('p – people – Введите номер документа и получите имя человека, которому он принадлежит;',
          's – shelf – Введите номер документа и получите номер полки, на которой он находится;',
          'l– list – Вывод списка всех документов в формате passport "2207 876234" "Василий Гупкин";',
          'a – add – Добавление нового документа в каталог и в перечень полок, с вводом его номера, типа, имя владельца и номера полки, на котором он будет храниться;',
          'd – delete – Удаление документа из каталога и перечня полок по его номеру;',
          'm – move – Перенос документа на введенную полку;', 'as – add shelf – Добавление полки;',
          'stop - завершение работы программы.', sep='\n')


def all_docs():
    all_doc = list()
    for value in directories.values():
        all_doc += value
    return all_doc


def search(search_key):
    number_doc = input('Введите номер документа: ')
    if number_doc in all_docs():
        if search_key == "p":
            for document in documents:
                if number_doc == document['number']:
                    return document['name']
        elif search_key == "s":
            for key, value in directories.items():
                if number_doc in value:
                    return key
    else:
        print("Документ по введенному номеру не найден!")


def print_all_doc():
    for document in documents:
        print(f'{document["type"]} "{document["number"]}" "{document["name"]}"')


def inp_type_doc():
    return input('Тип документа: ')


def inp_number_doc():
    return input('Номер документа: ')


def inp_name_owner():
    return input("Имя владельца: ")


def inp_number_locat():
    return input("Номер полки: ")


def add_doc():
    type_doc = inp_type_doc()
    number_doc = inp_number_doc()
    name_owner = inp_name_owner()
    number_locat = inp_number_locat()
    if number_locat in directories.keys():
        directories[number_locat].append(number_doc)
        documents.append({"type": type_doc, "number": number_doc, "name": name_owner})
        return "Документ добавлен!"
    else:
        return "Данной полки не существует!"


def del_doc():
    number_doc = input('Введите номер документа: ')
    if number_doc in all_docs():
        for document in documents:
            if document["number"] == number_doc:
                documents.remove(document)
                for value in directories.values():
                    if number_doc in value:
                        value.remove(number_doc)
        return "Документ удален!"
    else:
        return "Документ по введенному номеру не найден!"


def move_doc():
    number_doc = input('Введите номер документа: ')
    if number_doc in all_docs():
        number_locat = input('Введите номер полки: ')
        if number_locat in directories.keys():
            for key, value in directories.items():
                if number_doc in value:
                    value.remove(number_doc)
                    directories[number_locat].append(number_doc)
            print("Документ перенесен!")
        else:
            print("Такой полки не существует!")
    else:
        print("Документ по введенному номеру не найден!")


def add_locate():
    number = input("Введите номер полки: ")
    if number in directories.keys():
        print("Данная полка уже есть!")
    else:
        directories[number] = list()
        print("Полка добавлена!")


if __name__ == '__main__':

    command = input('Введите команду(help - справка): ')

    while True:
        if command == 'help':
            help()
        elif command == 'p':
            print(search(command))
        elif command == 's':
            print(search(command))
        elif command == 'l':
            print_all_doc()
        elif command == 'a':
            print(add_doc())
        elif command == 'd':
            print(del_doc())
        elif command == 'm':
            move_doc()
        elif command == 'as':
            add_locate()
        elif command == 'stop':
            break
        else:
            print('Неверная команда, ознакомьтесь со списком доступных команд - help')

        command = input('Введите команду(help - справка): ')