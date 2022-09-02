import random
import string
print("Welcome to Random password generator")
def main(): 
    
    length=int(input("Enter the length of password you want: "))
    lowerdata=string.ascii_lowercase
    upperdata=string.ascii_uppercase
    digitsdata=string.digits
    symbolsdata=string.punctuation
    combine=lowerdata+upperdata+digitsdata+symbolsdata
    x=random.sample(combine,length)
    password="".join(x)
    print(password)
    main()
main() 