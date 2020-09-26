#class is the container of variable and method
#Program to demonstrate concept of class in python

class DemoClass:
    num1=123
    def sayHello(self):
        print("Hello world")
    
    def sayHell(self,name):
        print("Hello", name)
    
#Now we test the my class
#creation of object
#DemoClass().sayHello()     #anonymous object creation   
demoClass = DemoClass()     #Referentaial object
demoClass.sayHello()
n= input("enter your name:")
demoClass.sayHell(n)

