#DICTIONARY


# Dictionary is a Key-Value Pair Collection

dict={'abc':1000,10:123,1.5:'Hello','xyz':15,15.8:10,'m':'a','ab':'xyz'}
print(dict)

print(dict['abc'])

# print(dict[1]) It will Show Error Because there is no index postions in dictionary 

print(dict[1.5])

##b=dict.values
##c=dict.keys
##print("Values are:", b)
##print("Keys are:", c)

w={'abc':1000,'1000':[{'a':(1,2,6,9)}]}
print(w)

print(w['abc'])

print(w['1000'][0]['a'][1:3])

##w['1000'][0]['a'][1:3]=(123,100) #Show Error Because tuple can't change
##print(w)

q={'abc':1000,'1000':[{'a':[1,2,6,9]}]}
print("q=", q)

q['1000'][0]['a'][1:3]=[123,100]
print(q)


