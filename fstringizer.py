def __extractStrings(exp):
    stack = []
    isInString = True if exp.startswith('"') or exp.startswith('\'') else False
    currentType = exp[0] if isInString else ''
    lastI = 0
    stringState = []
    isEscape = False
    for i in range(len(exp)):
        char = exp[i]

        if i >= 0 and isInString and exp[i-1] == '\\' and not isEscape:
            isEscape = True
        elif isEscape:
            isEscape = False

        if (char == "'" or char == '"' or i == len(exp)-1) and i != 0 and not isEscape:

            if i != len(exp)-1:
                if (isInString and currentType == char):
                    currentType = ''
                    stack.append(exp[lastI+1:i])
                elif not isInString:
                    currentType = char
                    stack.append(exp[lastI:i+1])
                else:
                    continue

            else:
                if isInString:
                    stack.append(exp[lastI+1:i])
                else:
                    currentType = char
                    stack.append(exp[lastI:i+1])

            stringState.append(isInString)
            isInString = not isInString
            lastI = i

    return stack, stringState


def fstringize(exp, *, debug=False):  # 'a' + time + 'b' + nick + awa

    stack1, stringState = __extractStrings(exp)

    if debug:
        print(stack1)
        print(stringState)

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
                stack2.append((p,))

    stack2 = list(filter(lambda part: part != ('',), stack2))

    if debug:
        print(stack2)

    fstring = ''

    for i in range(len(stack2)):
        part = stack2[i]
        if type(part) is str:
            fstring += part
        elif type(part) is tuple:
            fstring += '{' + part[0] + '}'

    return 'f'+repr(fstring).replace('\\\\', '')


def demo(exp):
    print(exp, fstringize(exp), '', sep='\n')

