#중첩 조건문
x = int(input('x 값을 입력하세요 : '))
y = int(input('y 값을 입력하세요 : '))
if x == y:
    print('x and y are equal')
else:
    if x < y:
        print('x is less than y')
    else:
        print('x is greater than y')
