import os

class GroupFilesByContent:
    
    def groupFiles(self):
        dic = {}
        inputDirPath = input("Enter the directory path :")
        #inputDirPath = "/Users/muthukumarangunasekaran/Documents/WS/Python1/directory/rootDir"
        for root,dir,files in os.walk(inputDirPath):
            for file in files:
                dic[os.path.join(root, file)] = open(os.path.join(root, file)).read()
        result = {}
        for key, value in sorted(dic.items()):
            result.setdefault(value, []).append(key)
            #print(result.values())
        for item in result.values():
            print(item)
        
obj = GroupFilesByContent()
obj.groupFiles()