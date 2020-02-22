import datetime, os
from os import listdir

class FindFilesInDateRange:
    
    inputStartDate = datetime.datetime.strptime
    inputEndDate = datetime.datetime.strptime
    inputDirPath = ""
#     inputStartDate = datetime.datetime.strptime("02-02-2018", "%m-%d-%Y")
#     inputEndDate = datetime.datetime.strptime("06-06-2018", "%m-%d-%Y")
#     inputDirPath = "/Users/muthukumarangunasekaran/Documents/WS/Python1/directory/dateRangeFiles"
    
    def sorting(self,lst):
        splitup = lst.split("-")
        return splitup[2], splitup[0], splitup[1]
    
    def isValidDate(self, dateStr):
        try:
            datetime.datetime.strptime(dateStr, "%m-%d-%Y")
            return True
        except ValueError:
            return False
    
    def validateDate(self, dateStr):
        while not self.isValidDate(dateStr):
            print("Invalid date: "+dateStr)
            dt = input("Please enter valid date :")
            if self.isValidDate(dt):
                return datetime.datetime.strptime(dt, "%m-%d-%Y")
        return datetime.datetime.strptime(dateStr, "%m-%d-%Y")
        #return datetime.datetime.strptime(dateStr, "%m-%d-%Y")
#         if self.isValidDate(dateStr):
#             return datetime.datetime.strptime(dateStr, "%m-%d-%Y")
#         else:
#             print("Invalid date: "+dateStr)
#             self.validateDate(input("Please enter valid date :")
#             #return datetime.datetime.strptime(dateStr, "%m-%d-%Y")
                    
    def getInput(self):
        print(self.inputStartDate)
        self.inputStartDate = self.validateDate(input("Enter the start date in mm-dd-yyyy format :"))
        print(self.inputStartDate)
        #self.inputStartDate = datetime.datetime.strptime(stdt, "%m-%d-%Y")
        print(self.inputStartDate)
        self.inputEndDate = self.validateDate(input("Enter the end date in mm-dd-yyyy format :"))
#         self.inputStartDate = datetime.datetime.strptime(input("Enter the start date in mm-dd-yyyy format :"), "%m-%d-%Y")
#         self.inputEndDate = datetime.datetime.strptime(input("Enter the end date in mm-dd-yyyy format :"), "%m-%d-%Y")
        self.inputDirPath = input("Enter the directory path :")
        print(type(self.inputStartDate), self.inputStartDate)
        print(type(self.inputEndDate), self.inputEndDate)
        
    def getFilesInRange(self):
        resultList = []
        fileNames = [f for f in listdir(self.inputDirPath) if os.path.isfile(os.path.join(self.inputDirPath, f))]
        fileNames.sort(key=self.sorting)
        print("inputStartDate" ,self.inputStartDate)
        print("inputEndDate",self.inputEndDate)
        for fileName in fileNames:
           
            fileDate = datetime.datetime.strptime(fileName.split(".")[1], "%m-%d-%Y")
            if self.inputStartDate <= fileDate <= self.inputEndDate:
                resultList.append(fileName)
        print(resultList)
                
obj = FindFilesInDateRange() 
# val = obj.validateDate("12-35-2018") 
# print(val) 
# if not val is None:
#     print("Valid")            
obj.getInput()
obj.getFilesInRange()    
    
