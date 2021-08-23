# string based examples 
str = "Python programming"
ele = "String Examples"
print(type(str),"",str[0],"",str[-5],"",len(str),"", min(str),"",max(str),"",str[6:15])

# format method using example
print("{0} is an integer and {2} is an float type" .format(10,'char',30.55,0.5))
print(str+" ",ele,"",str*2, "",min(str))
print(min(ele))  # this command is not working

# member ship operator in,  not in for checking the sequencce in the given string
print('p' in str,"", 'z' in str, "", 'j' not in ele,"",'tr' in ele,"",)

#Iteraations in string
for k in str:
    print (k, end='')

for l in range (len(str)):
    print (str[l], end='')

# Built in Methods ***************IMP***********    40 + Methods
mthd = "built in meTHOD eXAMples"
#print("\n",mthd.capitalize())
print("\n", mthd.capitalize(),"", mthd.center(30,'*'),"",mthd.count('e',3,len(mthd)),"",mthd.swapcase(),"",mthd.upper())
print("\n","",mthd.encode(),"",mthd.endswith('es',7,len(mthd)),"",mthd.find('m',2,len(mthd)),"",mthd.startswith('i',6,len(mthd)),"",mthd.strip())
""" isspace -- Onlyspace returns true, isdigit--only  digits, isalpha--only alphabets, islower-checks all letters in
string for lower, isupper--checks in string for uppercase letters

"""
print("\n","",)

# Reverse of string using slicing example
print (mthd[::-1]) 

# Reversed of string using Reverse funtction
rmthd=reversed(mthd) 
for ch in rmthd:
    print (ch, end='')

                                  # Reverse the string using join Operator
p = input("Enter some string here: ")
q= reversed(p)
output=''.join(q)
print (output)   

                                     # Reverse the string using normal code
p=input("Enter the input value here :") # kingdom king
i = len(p)-1 #6
output =''
while i>=0:
    output = output + p[i]
    i=i-1
print(output)


         #write a program to reverse the order of words ex: chaitanya  is from nuzvid o/p : nuzvid from is chaitanya

str=input('Enter the string to convert the reverse of the string words:') #welcome to the python
p=str.split()
print(p[::-1])
output=' '.join(p)
print (output)


         #write a program to reverse the content of the words      ex: tothe new    o/p : ehtot wen
str=input('Enter the string to reverse the content of the each word: ')  #tothe new  
q=str.split()
l=[]
for s in q:
    l.append(s[::-1])
    output=' '.join(l)
    print(output)  
