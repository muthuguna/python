# Find greatest number of 3 given numbers
A = 10
B = 11
C = 12
result = A
if A >= B and A >= B:
    result = A
elif B >= A and B >= C:
    result = B
else:
    result = C
    
print(result)

# Fibonacci series
count = 15
p1=1
p2=0
 
if count > 0:
    for i in range(count):
        p3=p1+p2
        p1=p2
        p2=p3
        print(p2)

#Find highest, lowest and average on series of input number
count = 0
while(1):
    inputNumber = input("Enter number:")
    if(count == 0):
        highest = inputNumber
        lowest = inputNumber
        average = inputNumber
    if(inputNumber == 99):
        print("Exiting...")
        break
    if(inputNumber > highest):
        highest = inputNumber
    if(inputNumber < lowest):
        lowest = inputNumber
    count = count+1 
    if(count > 1):
        average = (((average * (count-1))+ inputNumber)/count)
    print('Highest :',highest)
    print('Lowest :',lowest)
    print('Average :',average)


# slogan = "\"Strength is life\"\n\t -Swamy Vivekananda"
# print(slogan)

#Print pyramid string
counttryName = "America"

for i in range(0, len(counttryName)):
    print(counttryName[0:(i+1)])

   
    

    
    

# Find highest, lowest and average for the series of given number
count = 0
while(1):
    inputNumber = input("Enter the number:")
    if(inputNumber == 99):
        print("Exiting.....")
        break
    else:
        if(count == 0):
            highestNum = inputNumber
            lowestNum = inputNumber
            average = inputNumber
        if(inputNumber > highestNum):
            highestNum = inputNumber
        if(inputNumber < lowestNum):
            lowestNum = inputNumber
        count = count+1
        if(count > 1):
            count
            average = ((average*(count-1))+inputNumber)/count
        print(highestNum)
        print(lowestNum)
        print(average)    

  
#Append user input to the list
students = []
while(1):
    inputStudent = input("Enter the student :")
    if(inputStudent == "Done"):
        print("Exiting...")
        break
    else:
        students.append(inputStudent)
 
students.insert(0, "Mr")  
#print(students.pop()) 
del students[0:1]
students.sort(key=None, reverse=False)
for name in students:
    print(name)


maxArraySize = 7
students = []
while(1):
    addItem = input("Enter item to add :")
    if(addItem == "Done"):
        print("Exiting...")
        break
    if(len(students) > maxArraySize):
        print(students)
        removeItem = input("Enter item to remove from the above list:")
        students.remove(removeItem)
    else:
        students.append(addItem)
print(students)

# Find series of input number odd or even
numList = [1,2,3,4,5,6,7]    
for x in numList:
    if(x%2 == 0):
        print("Even :",x)
    else:
        print("Odd :",x)
 
# Find prime number from series of input numbers 
numList = [1,2,3,4,5,6,7,8,9,10,17,19,34]              
for x in numList:
    if x>1:
        flag = 1   
        for y in range(2,x):
            if(x%y == 0):
                flag = 0
                break
        if(flag == 1):
            print(x)        

# Add key value pair to dictionary
myDictionary = {"Muthu":["Honda","Toyota"], "Divesh":"Nissan", "Kumar": ["Ford", "Honda"]}

for name in myDictionary.keys():
    print(name, myDictionary[name])
    
while(1):
    addKey = input("Enter key to add :")
    if(addKey == "Done"):
        print("Exiting...")
        break
    addValue = input("Enter value to add :")
    myDictionary[addKey]=addValue
print(myDictionary)            