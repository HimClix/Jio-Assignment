from secrets import choice
from funtions import *
while True:
 print("What do you want?")
 print("1 Addition")
 print("2 Substraction")
 print("3 Multiplication")
 print("4 Division")
 print("Enter Q or q to exit")

 choice = input("Enter your choice : ")

 if choice == 'Q' or choice == 'q':
    break

 num1 = float(input("Enter number 1 : "))
 num2 = float(input("Enter number 2 : "))

 if choice == '1':
   Addition(num1,num2)
 elif choice == '2':
   Substraction(num1,num2) 
 elif choice == '3':
   Multiplication(num1,num2)
 elif choice == '4':
   Division(num1,num2)
 else: 
    print("Invalid Choice") 
    print("\n")          