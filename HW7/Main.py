
class Stack:
    def __init__(self):
        self.__stack = []

    def __str__(self):
        return f'{self.__stack}'

    def isempty(self):
        return True if not self.__stack else False

    def push(self, *args):
        for arg in args:
            self.__stack.append(arg)

    def pop(self):
        return self.__stack.pop()

    def peek(self):
        return self.__stack[-1]

    def size(self):
        return len(self.__stack)


def balance(string: str = '(((([{}]))))'):
    stack = Stack()
    dict_bracket = {'}': '{',
                    ')': '(',
                    ']': '[',
                    }

    if len(string) % 2 != 0:
        return 'Несбалансированно'
    else:
        for bracket in string:
            if bracket in dict_bracket.values():
                stack.push(bracket)
            else:
                if dict_bracket.get(bracket, 'No found') == stack.pop():
                    pass
                else:
                    return 'Несбалансированно'
    if stack.isempty():
        return 'Сбалансированно'
    else:
        return 'Несбалансированно'


if __name__ == '__main__':
    print(balance('[[{()}]]'))
