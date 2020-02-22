numList = []

#Adding number to the list
def addNumber():
    inputAdd = input("Enter the number to add :")
    numList.append(inputAdd)

#Deleting number to the list
def deleteNumber():
    inputAdd = input("Enter the number to delete :")
    numList.remove(inputAdd)
    
#Print the list
def printNumber():
    print(numList)
    
#Print the info
def printInfo():
    total = 0
    for i in numList:
        total = total+int(i)
    avg = total/len(numList)
    print("Total : ", total)
    print("Average : ", avg)

while(1):
    inputOption = input("Enter the option 'a' to add, 'd' to Delete, 'p' to Print and 'i' to print statistics:")
    if(inputOption == 'a'):
        addNumber();
    elif(inputOption == 'd'):
        deleteNumber()
    elif(inputOption == 'p'):
        printNumber()
    elif(inputOption == 'i'):
        printInfo()
    else:
        break
        
    