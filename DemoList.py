#List is a collection which storess multiple value of different types
#import string

list1=[] #blank list
list2 = [1,2,3,4,5] # list of numbers
list3=["suraj", "saurav"] # list of strings
mix = [1,2,3,4, "Ajay", "vijay", "sanjay"]  # list of number and string


print (list2)
print(list3)
print(list3[1])
print("Maximum no. =", max(list2))
print("Minumum no. =", min(list2))
print("Length of list=", len(list2))
print("sum of number in list=", sum(list2))
print("Average of number in list =", sum(list2)/len(list2))





listFrineds=["suraj", "saroj", "saurav", "ajay", "abhijeet"]

list2.append(6)
print(list2)
list2.insert(2,10)
print(list2)
list2.remove(3)
print("After removing 3 from list", list2)


print(listFrineds)
print("List of Friend")
for n in listFrineds:
    print(n)
print("")



listFrineds.sort()
print("Names In ascending order")
for n in listFrineds:
    print(n)
print("")
listFrineds.reverse() # reverse the element after sort
print("Names in descending order")
for n in listFrineds:
    print(n)



#Createing list with user input

n= int(input("How many number do you wanat to input"))
#using blank list now
print("Enter", n ,"numbers")

for i in range(n):
    num= int(input())
    list1.append(num)
    #or list1.insert(i,num)


print("")
print("number in list")
for i in list1:
    print(i)






