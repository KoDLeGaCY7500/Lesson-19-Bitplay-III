# def swap(a,b):
#     a=a^b
#     b=a^b
#     a=a^b
#     print("after swapping a======",a,"b=======>",b)

# swap(4,8)

# a=8
# b=4

# print("Before swapping===========>",a,b)
# a=a+b
# b=a-b
# a=a-b

# print("After swapping")
# print(a,b)

# def swap(a,b):
#     a=(a&b)+(a|b)
#     b=a+(~b)+1
#     a=a+(~b)+1

#     print("numbers after swapping",a,b)

# swap(8,4)

def divide(dividend,divisor):
    sign=(-1 if((dividend<0)^(divisor<0))else 1);
    dividend=abs(dividend);
    divisor=abs(divisor);

    quotientno=0
    tempno=0
    for i in range(31,-1,-1):
        if (tempno+(divisor<<i) <= dividend):
            tempno+=divisor<<i
            quotientno|=1 <<i
    if sign == -1:
       quotientno=-quotientno
    return quotientno

a=int(input("Enter a for a/b: "))
b=int(input("Enter b for b/a: "))
print("Result of",a,"/",b,"is",divide(a,b))