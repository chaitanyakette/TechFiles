# printing the odd index, even index characters seperately
str='kingdom king' # kndmkn igo ig
i=0
while i< len(str):
    print(str[i], end='\n')
    i=i+2
    #print (even)  
i=1
while i< len(str):
    print(str[i], end=' ')
    i=i+2              


# Slicing method for theabove program

str= 'kingdomking'
print("Even index char's:",str[::2]) # str[starts:end:step]
print("odd index char's:",str[1::2])


# Printing any file data in the console
#print(open('Tuple.py').read())

#WAP to generate 6 digit otp using function random library and randint function
from random import randint
for i in range(10):
    print(randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9),sep ='')

#WAP to test integral type hexaadecimal (allowed a, b, c, d, e, f) must be (0X, Ox) digits(0 to 9)
a=0Xface
print(type(a))
print(id(a))
print(a)


#WAP to test integral type octadecimal  must be (0o, OO) digits(0 to 7)
a=0o1234
print(type(a))
print(id(a))
print(a)


#WAP to test integral type Binary  must be (0b, OB) digits(0 & 1)
a=0B1010
print(type(a))
print(id(a))
print(a)

# WAP to test complex data type    format = 10(real part)+20j(imaginary part)
a=45+65J
b=0b111+36J
""" a=45.05+65J == yes
    a=0b1111+65J == Yes
    a=0xface+35j == Yes
    a=0o123456+24J== Yes
    a=45+0B1111J  == NO No 
"""

print(type(a))
print(id(a))
print(a)
print(b)
print(a.real)
print(a.imag)
print(a+b, a-b, a/b, a*b)
print(True+True)  # O/p  2
print(True*False)  # o/p    0
