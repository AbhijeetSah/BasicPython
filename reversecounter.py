#Reverse Counter WAP to print the number from 10 to 1
import time
count=10        #initilization
while count>0:      #condition
    print(count)    #code
    time.sleep(1000)
    count=count-1         #updateing the loop counter

stringcol="SOFTPRO"
for c in stringcol:
    print(c, end='')

#program to print the table of given number
num=int(input("Enter a number to print table"))
for i in range(1,11):
    print(n,"*",i,"=",(i*num))

#function in python
def sum(num1,num2):
    print (num1+num2)

#function call
sum(2,4)

#WAP TO FIND THE VOLUME OF CUBOID USING UDF
def volumeCuboid(length,breadth,height):
    return length*breadht*height

x=eval(input("Enter length of cubid: "))
y=eval(input("Enter breadth of cuboid: "))
z= eval(input("Enter height of cuboid:"))
voulume= volumeCuboid(x,y,z)
print("Volume of Cuboid=",voulume)

#Modules in python
#Module is the collection of function,classes,  and submodules that can be imported to any part of program
#every python code file is called module
#module name is same name as filename












