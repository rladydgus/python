data = 'From abc@ab.com Sat'
atpos=data.find('@')
sppos1=data.find(' ')
sppos2=data.find(' ',atpos)
host=data[sppos1+1:sppos2]
print(host)
