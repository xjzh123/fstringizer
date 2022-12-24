# Fstringizer for python

This is a tool to convert python string concatenation expressions into f-string expressions.
这是一个把python的字符串拼接表达式转换成f-string表达式的工具。

However, this tool is just to help convert simple expressions. It is **NOT** made to generate such high-level code as shown in <https://docs.python.org/3/reference/lexical_analysis.html#formatted-string-literals>.
然而，这个工具只是转换简单的表达式。它**不是**用来生成<https://docs.python.org/zh-cn/3/reference/lexical_analysis.html#formatted-string-literals>里展示的那些高级代码的。

This tool can not convert f-string into string concatenation, or convert string concatenation into `str.format()`. It can **ONLY** convert string concatenation into f-string.
这个工具不能把f-string转换成字符串拼接，也不能把字符串拼接转换成`str.format()`。它**只能**把字符串拼接转换成f-string。

This tool may give strange outputs, but this should only happen when the input is not correct string concatenation expression.
如果你输入的都不是正确的字符串拼接表达式，这个工具的输出确实会很奇怪。否则，它的输出应该会是合法的f-string。

```cmd
> python fstringizer.py "a a" 
f'{aa}'
```

If you find any bug, please raise an simple issue. (Limited by my coding ability level,) I may decide whether to fix it based on how simple the input which causes a bug is. If you can pull request, I will appreciate it much.
如果你找到bug，请提个简单的issue。（因为我技术也很差）我可能会根据造成bug的输入有多简单来决定是否修复这个bug。如果你可以pull request，我就更感激了。

The original purpose of this tool is to help beginners who didn't know f-string and wrote many string concatenation to switch to f-string so that their code will become more readable.
这个工具的本意是帮助不知道f-string然后写了很多字符串拼接的新手把自己的代码改成用f-string的，这样代码就会更易读。

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

You can use fstringizer in 3 ways:
你可以用三个方式使用fstringizer：

1. import
   import

    ```python
    from fstringizer.py import fstringize
    print(fstringize(input()))
    ```

2. run and input
   直接运行然后输入

    ```cmd
    > python fstringizer.py
    Input your expression: '"A \'' + key + '\' is a \'so-called\' ' + d[key] + '" -- ' + name
    f'"A \'{key}\' is a \'so-called\' {d[key]}" -- {name}'
    ```

3. run with parameter
   带参数运行

    ```cmd
    > python fstringizer.py "'\"A \'' + key + '\' is a \'so-called\' ' + d[key] + '\" -- ' + name" 
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
            len(line.split('#')[0].replace(' ', '').replace('\t', '')) > 0,
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

That's all.
就这样。
