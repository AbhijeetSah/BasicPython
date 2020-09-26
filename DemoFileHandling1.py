#WAP to read file

try:
    fileName= input("Enter File name to open : ")
    f=open(fileName, "r")
    contents= f.read()
    print(contents)

    f.close()
except FileNotFoundError:
    print("File Doesnot Exist")
