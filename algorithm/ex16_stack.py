class Stack:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        return self.stack.pop()

    def get_top(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            return None


def bracket_match(s):
    stack = Stack()

    for ch in s:
        if ch in {'(', '[', '{'}:
            stack.push(ch)
        else:
            match ch:
                case ')':
                    if stack.get_top() == '(':
                        stack.pop()
                    else:
                        print("String doesn't match, program exit")
                        exit(-1)
                case ']':
                    if stack.get_top() == '[':
                        stack.pop()
                    else:
                        print("String doesn't match, program exit")
                        exit(-1)
                case '}':
                    if stack.get_top() == '{':
                        stack.pop()
                    else:
                        print("String doesn't match, program exit")
                        exit(-1)

    if stack.get_top() is None:
        print("The string is match")
    else:
        print("The string is not match")


str1 = "{(abc)dad}"
str2 = "[ab]{cd(as[ab]aasf)ss;}"
bracket_match(str2)
