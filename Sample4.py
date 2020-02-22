myDictionary ={}

def addItem():
    inptCity = input("Enter the City:")
    inptZip = input("Enter the Zip:")
    myDictionary[inptCity]=inptZip
    
def printItem():
    print(myDictionary);
    
def deleteItem():
    itemToDelete = input("Enter the City to delete:")
    myDictionary.pop(itemToDelete)
    
while(1):
    optionInput = input("Enter the option 'a' to Add, 'p' to Print, 'd' to Delete")
    if(optionInput == 'a'):
        addItem()
    elif(optionInput == 'p'):
        printItem()    
    elif(optionInput == 'd'):
        deleteItem()
    else:
        break
    