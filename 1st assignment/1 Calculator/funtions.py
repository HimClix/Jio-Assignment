from unittest import result


def Addition(num1,num2):
    result = num1 + num2
    print("{0} + {1} = {2}".format(num1,num2,result))

def Substraction(num1,num2):
    result = num1 - num2
    print("{0} - {1} = {2}".format(num1,num2,result))

def Multiplication(num1,num2):
    result = num1 * num2
    print("{0} * {1} = {2}".format(num1,num2,result))

def Division(num1,num2):
    if num2 == 0.0:
       print("cant do division oeration")
    else:
       result = num1/num2   
    print("{0} / {1} = {2}".format(num1,num2,result))
