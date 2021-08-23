#str=input("please provide any of the string:")
#if ele in range len(str): #kindom king
#k=str[0]
#for ele in range(len(str)):

#print(str.replace(str[0],'@',5))

def change_char(str1):
  char = str1[0]
  str1 = str1.replace(char, '$')
  str1 = char + str1[1:]

  return str1

print(change_char('restart'))
