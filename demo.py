from fstringizer import demo

demo("'a' + time + 'b' + nick.str() + awa[0]")
demo("date + time + ':' + nick + ' recorded to join ' + channel")
demo("'a' + time + 'b' + nick + 'awa'")
demo("varName")
demo("'some text'")
with open('test.py', 'r', encoding='UTF-8') as fp:
    lines = fp.read().splitlines()
    noBlank = list(filter(
        lambda line:
            len(line.split('#')[0].replace(' ', '').replace('	', '')) > 0,
        lines
    ))
    for line in noBlank:
        demo(line)
