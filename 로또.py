import random

a = random.sample(range(1, 46),7)
b = 0
c = 0

p1 = int(input('로또 숫자 : '))
p2 = int(input('로또 숫자 : '))
p3 = int(input('로또 숫자 : '))
p4 = int(input('로또 숫자 : '))
p5 = int(input('로또 숫자 : '))
p6 = int(input('로또 숫자 : '))

if p1 == a[0]:
    b = b+1
if p2 == a[1]:
    b = b+1
if p3 == a[2]:
    b = b+1
if p4 == a[3]:
    b = b+1
if p5 == a[4]:
    b = b+1
if p6 == a[5]:
    b = b+1
    
if b == 0 and c == 0 :
    print('0개 맞추셨습니다')
    
if b == 1 :
    print('1개 맞추셨습니다')

if b == 2 :
    print('2개 맞추셨습니다')

if b == 3 :
    print('3개 맞추셨습니다')

if b == 4 :
    print('4개 맞추셨습니다')

if b == 5 :
    print('5개 맞추셨습니다')

if b == 6 :
    print('6개 맞추셨습니다')
if p1 == a[0] or p2 == a[1] or p3 == a[2] or p4 == a[3] or p5 == a[4] or p6 == a[5]:
    print('보너스 당첨')

print(a[0],a[1],a[2],a[3],a[4],a[5])
print('보너스 :' , a[6])
