import random
import string
print("welcome to our random password generator")
length=int(input("enter the length of password you want: "))
lowerD=string.ascii_lowercase
upperD=string.ascii_uppercase
digitD=string.digits
symbolsD=string.punctuation
print(symbolsD)
combine=lowerD+upperD+digitD+symbolsD
x=random.sample(combine,length)
print(x)

