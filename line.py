fout=open('mbox.txt','r')
count=0
for line in fout:
    print(line)
    count=count+1
print('Line count : ',count)
