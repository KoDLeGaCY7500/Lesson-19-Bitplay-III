def swap(a,b):
    a=a^b
    b=a^b
    a=a^b
    print("after swapping a======",a,"b=======>",b)

swap(4,8)

a=8
b=4

print("Before swapping===========>",a,b)
a=a+b
b=a-b
a=a-b

print("After swapping")
print(a,b)

def swap(a,b):
    a=(a&b)+(a|b)
    b=a+(~b)+1
    a=a+(~b)+1

    print("numbers after swapping",a,b)

swap(8,4)