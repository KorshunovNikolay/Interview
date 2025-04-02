class Stack:

    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()

    def peek(self):
        if self.size() > 0:
            return self.stack[-1]

    def size(self):
        return len(self.stack)


def is_balance(brackets):
    s = Stack()
    open_brackets = '([{'
    close_brackets = ')]}'
    for bracket in brackets:
        if bracket in open_brackets:
            s.push(bracket)
        elif s.size()> 0 and open_brackets.find(s.peek()) == close_brackets.find(bracket):
            s.pop()
        else:
            print('Несбалансированно')
            break
    else:
        print('Сбалансированно' if s.is_empty() else 'Несбалансированно')


brackets = ['(((([{}]))))', '[([])((([[[]]])))]{()}', '{{[()]}}', '}{}', '{{[(])]}}', '[[{())}]]']
for item in brackets:
    is_balance(item)






