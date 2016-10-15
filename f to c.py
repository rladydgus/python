#화씨온도 -> 섭씨온도
inp = input('화씨 온도를 입력하세요 : ')
try:
    fahr = float(inp)
    cel = (fahr-32.0)*5.0/9.0
    print(cel)
except:
    print('Please enter the number')
