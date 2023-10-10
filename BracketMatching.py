n = int(input())
str_n = input()
list_n = []

for char in str_n:
    if list_n and ((list_n[-1] == '(' and char == ')') or
                   (list_n[-1] == '[' and char == ']') or
                   (list_n[-1] == '{' and char == '}')):
        list_n.pop()
    else:
        list_n.append(char)

if len(list_n) == 0:
    print('Valid')
else:
    print('Invalid')
