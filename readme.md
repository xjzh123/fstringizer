# Fstringizer for python

This is a tool to convert python string concatenation expressions into f-string expressions.
这是一个把python的字符串拼接表达式转换成f-string表达式的工具。

However, this tool is just to help convert simple expressions. It is **NOT** made to generate such high-level code as shown in <https://docs.python.org/3/reference/lexical_analysis.html#formatted-string-literals>.
然而，这个工具只是转换简单的表达式。它**不是**用来生成<https://docs.python.org/zh-cn/3/reference/lexical_analysis.html#formatted-string-literals>里展示的那些高级代码的。

This tool can not convert f-string into string concatenation, or convert string concatenation into `str.format()`. It can **ONLY** convert string concatenation into f-string.
这个工具不能把f-string转换成字符串拼接，也不能把字符串拼接转换成`str.format()`。它**只能**把字符串拼接转换成f-string。

Let's check out examples:
让我们看看示例：

```python
>>> from fstringizer import *
>>> fstringize('i')
"f'{i}'"
>>> fstringize("date + time + ':' + nick + ' recorded to join ' + channel")
"f'{date}{time}:{nick} recorded to join {channel}'"
>>> fstringize(r"'\"A \'' + key + '\' is a \'so-called\' ' + d[key] + '\" -- ' + name")
'f\'"A \\\'{key}\\\' is a \\\'so-called\\\' {d[key]}" -- {name}\''
>>> print(fstringize(r"'\"A \'' + key + '\' is a \'so-called\' ' + d[key] + '\" -- ' + name"))
f'"A \'{key}\' is a \'so-called\' {d[key]}" -- {name}'
```

There is a demo program:
有一个演示程序：

```python
# fstringizer.py
...
def demo(exp):
    print(exp, fstringize(exp), '', sep='\n')
...
```

```python
# demo.py
from fstringizer import demo, fstringize

print(fstringize("'some text [' + time + '] some text ' + nick.str() + awa[0]"))
print()

demo('i')
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

```

```python
#test.py
# These expressions can not be written in string literals easily in python, so I put them in a file.

'some \' text \''

'\'some \' text'

' Var ' + key + ' is ' + d[key]
# f' Var {key} is {d[key]}'

'"A \'' + key + '\' is a \'so-called\' ' + d[key] + '" -- ' + name
# f'"A \'{key}\' is a \'so-called\' {d[key]}" -- {name}'
```

Run demo.py:
运行demo.py：

```python
f'some text [{time}] some text {nick.str()}{awa[0]}'

i
f'{i}'

date + time + ':' + nick + ' recorded to join ' + channel
f'{date}{time}:{nick} recorded to join {channel}'

'a' + time + 'b' + nick + 'awa'
f'a{time}b{nick}awa'

varName
f'{varName}'

'some text'
f'some text'

'some \' text \''
f"some ' text '"

'\'some \' text'
f"'some ' text"

' Var ' + key + ' is ' + d[key]
f' Var {key} is {d[key]}'

'"A \'' + key + '\' is a \'so-called\' ' + d[key] + '" -- ' + name
f'"A \'{key}\' is a \'so-called\' {d[key]}" -- {name}'
```
