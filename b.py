def matchparen(str):
    str = list(str)
    stack = []
    for i, c in enumerate(str):
        if c == '(': # 左括号入栈
            stack.append(i)
        elif c == ')':
            if not stack: # 没有左括号匹配打?
                str[i] = '?'
            else:  
                str[i] = ' ' # 匹配打空格
                str[stack.pop()] = ' '
        else: # 其他字符打空格
            str[i] = ' '
    for i in stack: # 剩下打左括号打x
        str[i] = 'x'
    return ''.join(str)


while True:
    user_input = input()
    print(matchparen(user_input))
    