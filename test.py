# These expressions can not be written in string literals easily in python, so I put them in a file.

'some \' text \''

'\'some \' text'

' Var ' + key + ' is ' + d[key]
# f' Var {key} is {d[key]}'

'"A \'' + key + '\' is a \'so-called\' ' + d[key] + '" -- ' + name
# f'"A \'{key}\' is a \'so-called\' {d[key]}" -- {name}'
