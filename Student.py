class Student:
    # name=""
    # rollNo=""
    # fee=0

    def setValues(self,rollNo,name,fee):
        self.name=name
        self.rollNo=rollNo
        self.fee=fee
    def display(self):
        print(" Roll No: ",self.rollNo,"\n Name :",self.name, "\n Fee :",self.fee )
    
s1=Student()
s1.setValues(1001,"abhijeet",10000)
s1.display()


