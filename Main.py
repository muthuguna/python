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

   
    

    
    
