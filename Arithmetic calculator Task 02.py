#Arithmetic operation
a=float(input("Enter a number 1: "))
b=float(input("Enter a number 2: "))
c=input("Enter a operation sign: ")

if c=='+':
    print(f'Addition of two number : {a+b}')
elif c=='-':
    print(f'Subraction of two number : {a-b}')
elif c=='*':
    print(f'Multiplication of two number : {a*b}')
elif c=='/' and b!=0:
    print(f'Division of two number : {a/b}')
else :
    print("Enter a Arithmetic operation")

