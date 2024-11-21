# ROLL NO: BSE - 192
opt=int(input('''please select your option in number:
1.calculator
2.area of circle
3.temperature
4.even and odd
5.for factorial
'''))
if opt==1:
    num1=int(input('input a number: '))
    num2=int(input('input a number: '))
    oprator=input('''enter an operation:
    multiplication(*)
    division(/)
    addition(+)
    subtraction(-)
    ''')

    if oprator=='*':
        ans=num1*num2
        print(f" Multiplication :{ans}")
    elif oprator=='/':
        ans=num1/num2
        print(f" division :{ans}")
    elif oprator=='+':
        ans=num1+num2
        print(f" Addition :{ans}")
    elif oprator=='-':
        ans=num1-num2
        print(f" subtraction :{ans}")
elif opt== 2:
    radius=int(input('enter radius: '))
    ans =3.142*radius**2
    print(f"Area of Circle is :{ans}")
elif opt== 3:
    tem1=int(input('temperature in fahrenheit: '))
    tem2=(tem1-32)*5/9
    print(f'{tem2}C in celsius')
elif opt== 4:
    num=int(input('enter a number: '))
    if num%2 == 0:
        print(f'{num}is even')
    else:
        print(f'{num}is odd')
elif opt==5:
    num=int(input('enter a number: '))
    fac=1
    for i in range(1,num+1):
       fac*=i
    print(f"{fac} factorial of {num}")