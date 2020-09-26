#word counter
sen = input("Enter a sentence: ")
words=sen.upper().split()
print(words)
print(type(words))
print("The No. of wordss in sentences:",len(words))


#Program to take full name as input and display the short name
#input = Abhijeet Kumar Sah
#output = A.K.Sah
name=input("Enter your full Name: ")
shortname= name.split()
for n in range(len(shortname)-1):
    print(shortname[n][0]+".", end="")
print(shortname[len(shortname)-1])


string1="ABCDEF is alphabet"
print(list(string1))