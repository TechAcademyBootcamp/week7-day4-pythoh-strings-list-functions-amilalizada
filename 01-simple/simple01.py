
def power_func():
    count=5
    l=[]

    while count>0:
        numbers=int(input('reqem daxil edin:'))
        l.append(numbers)
        count-=1

    l2=[item**2 for item in l]
    return l2


print(power_func())

