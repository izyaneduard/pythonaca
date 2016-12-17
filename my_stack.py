import random

class Stack:
    def __init__(self):
        self.arr = []

    def push(self, value):
        self.arr.append(value)

    def pop(self):
        if not self.arr:
            raise("Empty Stack")
        return self.arr.pop()

    def top(self):
        if not self.arr:
            raise("Empty Stack")
        return self.arr[-1]

    def is_empty(self):
        return not bool(self.arr)


def is_valid(inputString, parentheses):
    parentheses = dict(parentheses)
    print(parentheses)
    inp = inputString
    valid = True
    st = Stack()
    if not inp:
        return valid
    for par in inp:
        if par in parentheses:
            st.push(par)
        else:
            if st.is_empty():
                valid = False
                break
            else:
                if parentheses[st.top()] == par:
                  st.pop()
                elif par in parentheses.values():
                    valid = False
                    break
                else:
                    continue
            return valid and st.is_empty()


if __name__ == '__main__':
    assert (is_valid(inputString='() ({})()([])', parentheses=[('(', ')'), ('[', ']'), ('{', '}')]) == True)
    assert (is_valid(inputString='({} )<>>(())', parentheses=[('(', ')'), ('{', '}'), ('<', '>')]) == False)
    assert (is_valid(inputString='[ }]', parentheses=[('[', ']')]) == True)
