n = int(input("enter a number : "))
bool = int(input("enter 1 or 0 : "))

if bool ==1:
    for i in range(1,n+1):
        print('*'*i)
elif bool == 0:
    i = n
    while i>0:
        print('*'*i)
        i -=1