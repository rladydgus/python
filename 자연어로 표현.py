meal=int(input('음식값 입력 : '))
tax=0.0675
tip=0.15
total=meal*(1+tax)
total=total*(1+tip)
print(int(total))
    
