def f_string(exp): # 'a' + time + 'b' + nick + awa
    stack1 = []
    isInString = False
    lastI = 0
    for i in range(len(exp)):
        char = exp[i]
        if (char == "'" or i == len(exp)-1) and i != 0:
            if isInString:
                stack1.append(exp[lastI:i+1])
            else:
                stack1.append(exp[lastI+1:i])
            isInString = not isInString
            lastI = i
    
    # yield stack1 # ['a', "' + time + '", 'b', "' + nick + awa"]

    stack2 = []
    
    for i in range(len(stack1)):
        part = stack1[i]
        if i % 2 == 0:
            stack2.append(part)
        else:
            part = part.strip('\' +')
            part = part.replace(' ','')
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


...