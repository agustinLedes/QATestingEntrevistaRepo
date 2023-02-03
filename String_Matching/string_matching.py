def string_matching(text):
    stack = []
    for s in text:
        if s in ['(', '[']:
            stack.append(s)
        elif s in [')', ']']:
            pos = [')', ']'].index(s)
            if len(stack) > 0 and ['(', '['][pos] == stack[len(stack)-1]:
                stack.pop()
            else:
                return False

    if len(stack) == 0:
        return True
    else:
        return False


print(string_matching("(abc"))
print(string_matching(")abc)"))
print(string_matching("(a[b)c]d"))
print(string_matching("(a[b]c)"))
