
class Stack:
    def __init__(self):
        self.stack = []

    def __str__(self):
        return f'{self.stack}'

    def isempty(self):
        return True if not self.stack else False

    def push(self, *args):
        for arg in args:
            self.stack.append(arg)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)


def balance(string: str = '(((([{}]))))'):
    stack = Stack()
    dict_bracket = {'}': '{',
                    ')': '(',
                    ']': '[',
                    }
    list_bracket = list(string)

    if len(list_bracket) % 2 != 0:
        return 'Несбалансированно'
    else:
        for bracket in list_bracket:
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
