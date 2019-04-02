num1 = input('enter number 1')
num2 = input('Enter number 2')
def calc():
    print('1. add\n2.subtract\n3.mustiply\n4.divide')
    calculation = input()
    if int(calculation)==1:
        print(int(num1)+int(num2))
    elif int(calculation)==2:
        print(int(num1)-int(num2))
    elif int(calculation)==3:
        print(int(num1) * int(num2))
    elif int(calculation)==4:
        print(int(num1) / int(num2))
    else:
        print('enter valid input')
        calc()
calc()
