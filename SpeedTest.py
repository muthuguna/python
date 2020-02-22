students = {}

def addStudent():
    nameInput = input("Enter the student name to add:")
    marksInput = input("Enter the student marks to add:")
    students[nameInput] = marksInput
    
def printStrudents():
    print(students)
    
def deleteStudent():
    nameInput = input("Enter the student name to delete:")
    students.pop(nameInput)
    
def printTotalInfo():
    print("Total number of students:",len(students))
    total = 0;
    for mark in students.values():
        total = total+int(mark)
    print("Total marks:",total)
    print("Average marks:",total/len(students))
while(1):
    optionInput = input("Enter the option 'a' to Add , 'p' to Print, 'd' to Delete and 'i' to Print Info:")
    
    if(optionInput == 'a'):
        addStudent()
    elif(optionInput == 'p'):
        printStrudents()
    elif(optionInput == 'd'):  
        deleteStudent()
    elif(optionInput == 'i'):    
        printTotalInfo()
    else:
        break
    
    
    