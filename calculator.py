def calculator(num1, num2, op):
    if op == '+':
        res = int(num1) + int(num2)
        print(res)
    elif op == '-':
        res = int(num1) - int(num2)
        print(res)
    elif op == '*':
        res = int(num1) * int(num2)
        print(res)
    elif op == '/':
        res = int(num1) / int(num2)
        print(res)
    else:
        print('Неизвестная операция')

request = input()
request_len = -(len(request))
i = 0
while i > request_len:
    if request[i] == ' ':
        num1i = i
    i -= 1
num1 = request[:num1i]
num2 = request[(num1i + 1):-2]
op = request[(-1)]

calculator(num1, num2, op)
