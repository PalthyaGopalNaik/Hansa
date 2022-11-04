array = ['hello','world','hello python','python hello', 'java', 'hello java', 'print me', 'things','thinker','eat','hell']
exp = input()
if exp[0] == '*' and exp[-1] == "*":
    exp = exp[1:len(exp)-1]
    for  i in array:
        if exp in i:
            print(i)
elif exp[0] == "*" and exp[-1] != "*":
    exp = exp[1:]
    for i in array:
        if i.endswith(exp):
            print(i)
elif exp[0] != "*" and exp[-1] == "*":
    exp = exp[:len(exp)-1]
    for i in array:
        if i.startswith(exp):
            print(i)
else:
    for i in array:
        if exp == i:
            print(i)
