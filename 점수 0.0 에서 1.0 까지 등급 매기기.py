# 등급 매기기
while True:
    num = input('점수를 입력하세요 : ') 
    try:
        num = float(num) # 문자를 입력하게 되면 실수화 할 수 없으니까.. 에러발생
        if num>1 or num<0:
            print('0과 1 사이의 숫자를 입력해주세요')
        elif num>=0.9:
            print('A')
        elif num>=0.8:
            print('B')
        elif num>=0.7:
            print('C')
        elif num>=0.6:
            print('D')
        else:
            print('F')
    except:
        print('숫자를 입력해주세요')
