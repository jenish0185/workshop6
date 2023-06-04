ele=[]
a=int(input('Enter the numbers of elements in the list:'))
for i in range(1,a+1):
    b=int(input('enter a number:'))
    if b>100:
        ele.append('over')
    else:
        ele.append(b)
print(ele)