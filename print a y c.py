a = ("감사합니다")
y = ("반갑습니다")
c = ("안녕하세요")
p = int(input("나이를 입력하세요 : "))
if p > 19:
    print(a)
elif 12 < p < 20:
    print(y)
elif 7 < p < 13:
    print(c)
else:
    print("요금 안내셔도 됩니다.")
