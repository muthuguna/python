"""
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

inpt = [8,1,2,3,4,5,6,7]
count = 0
for x in inpt:
    count = count+1
    if(count == 1):
        highest = x
        lowest = x 
        total = 0
    total = total + x
    if(x > highest):
        highest = x
    if(x < lowest):
        lowest = x
print("Average :", total/len(inpt))  
print("Highest :", highest)  
print("Lowest :", lowest)  
"""  


    