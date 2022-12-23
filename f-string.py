def f_string(exp):  # 'a' + time + 'b' + nick + awa
    stack1 = []
    isInString = True if exp.startswith('"') or exp.startswith('\'') else False
    currentType = exp[0] if isInString else ''
    lastI = 0
    stringState = []
    for i in range(len(exp)):
        char = exp[i]

        #print(isInString, char)
        if (char == "'" or char == '"' or i == len(exp)-1) and i != 0:

            if i != len(exp)-1:
                if (isInString and currentType == char):
                    currentType = ''
                    stack1.append(exp[lastI+1:i])
                elif not isInString:
                    currentType = char
                    stack1.append(exp[lastI:i+1])
                else:
                    continue

            else:
                if isInString:
                    stack1.append(exp[lastI+1:i])
                else:
                    currentType = char
                    stack1.append(exp[lastI:i+1])

            stringState.append(isInString)
            isInString = not isInString
            lastI = i

    # print(stack1)
    # print(stringState)

    # yield stack1 # ['a', "' + time + '", 'b', "' + nick + awa"]

    stack2 = []

    for i in range(len(stack1)):
        part = stack1[i]
        if stringState[i]:
            stack2.append(part)
        else:
            part = part.strip('\'\" +')
            part = part.replace(' ', '')
            parts = part.split('+')
            for p in parts:
                stack2.append(tuple([p]))

    # yield stack2 # ['a',('time'),'b',('nick')]

    fstring = "f'"

    for i in range(len(stack2)):
        part = stack2[i]
        if type(part) is str:
            fstring += part
        elif type(part) is tuple:
            fstring += '{' + part[0] + '}'

    fstring += "'"

    return fstring


print(f_string("'a' + time + 'b' + nick + awa"))  # f'a{time}b{nick}{awa}'
print(f_string("a + time + 'b' + nick + awa"))
print(f_string("'a' + time + 'b' + nick + 'awa'"))  # f'a{time}b{nick}awa'
print(f_string("'a\"a\"' + time + \"b\" + nick + awa")) # f'a"a"{time}b{nick}{awa}'
