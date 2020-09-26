# File Handling means to perform the file operation
# Write operation: this operation is used to write information into the file. Before writing the information it first truncate the file
# Read operation:this operation is used to read information from file
# Append operation:the Append Operation is used to write information into the file, but it add iformation at the end position of the file
#How to open the file
#open():- open function is used to open the file, it takes two paramenter first one is filename, mode
#f= open(filename,mode) #it return the file object 
#write --> "w"
#read-->"r"
#append-->"a"
#f.close()

#WAP TO PERFORM WRITE OPERATION INTO THE FILE
# f=open("Employee.txt","w")
f=open("Employee.txt","a")
empId= input("Enter EmployeeId : ")
empName=input("Enter Employee Name : ")
empSalary=float (input("Enter Employee Salary : "))
f.write("Employee Id = "+empId+ "\n"+ "Employee Name = "+empName+"\n"+ "Salary = "+ str(empSalary)+"\n")
f.close()
print("The informtion is saved successfully")
