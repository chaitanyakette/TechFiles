#input= aaaabbbccz
#output= 4a3b2c1z
s='aaaabbbccz'
c=1
previous=s[0]
output=''
i=1
while i < len(s):
    if s[i]==previous:
        c=c+1
     else:
        output=output+str(c)+previous
        previous=s[i]
        c=1
     i=i+1
print(output) 
                

