import os

def findFiles():
    dirInput = input("Enter the directory name:")
    filesList = os.listdir(dirInput)
    #print(filesList)
    print("FileName"," # Lines", " # words")
    for fileName in filesList:
        readLineFromFile(dirInput, fileName)

def readLineFromFile(path,fileName):
    with open(path+"/"+fileName) as fileObj:
        lines = fileObj.readlines()
        #print("Number of Line in file ",fileName," ", len(lines))
        wordCounter = 0
        for line in lines:
            words = line.strip().split(" ")
            wordCounter = wordCounter+len(words)
        #print("Number of words in file ",fileName," ", wordCounter,"\n")
        print(fileName," ",len(lines),"\t\t",wordCounter)

findFiles()