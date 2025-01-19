print("Hello World!")

a = "hello"
print(type(a))

b = "Hello World"
print(b[3]) #With this operation we can see third character of the sentence. Result: l

c = "Kairbek Abulkhair"
print(len(c)) #with this operation we can see how many letters and spaces there are in the sentence. Result: 19.

h = "5"
p = "3"
print (h+p) #Result will be 53  Because program will be consider the 5 and 3 same as the string. 

lol = "Hello World"
print(lol[3:7]) #Result will be: characters from position 3 to position 7 (not included). Result is: l0,

pop = "Hello World"
print(pop[:5]) #The first 4 elements. Result: Hello

kai = "Kairbek Abulkhair"
print(kai.upper()) #All elements in capital letters

sps = "Kairbek Abulkhair"
print(sps.lower()) #All elements in lowercase

sub = "PP1, PP2, Linear algerba"
print(sub.split()) #Result: ['PP1,', 'PP2,', 'Discrete', 'structures'] Using split we can create a list. If any spaces between words it will be new word in list.

#Second information: The strip() method removes any whitespace from the beginning or the end:

str = " Kairbek Abulkhair "
print (str.strip()) #Result: this operation removes spaces in the sentences. Spaces that located at the beginning and at the end. 

top = "Hello"
pot = ", PP2!"
result = top + " " + pot
print(result) #Concatenate. Result is: Hello, PP2!