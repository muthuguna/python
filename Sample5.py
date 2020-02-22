import os, threading, math

def loadFiles():
    #dirInput = input("Enter the directory name:")
    fileList = os.listdir(dirInput)
    #print(filesList)
    return fileList
   
def getFolderMetrics(fileList):
    for fileName in fileList:
        with open(dirInput+"/"+fileName) as fileObj:
            lines = fileObj.readlines()
            #print("Number of Line in file ",fileName," ", len(lines))
            wordCounter = 0
            for line in lines:
                words = line.strip().split(" ")
                wordCounter = wordCounter+len(words)
            #print("Number of words in file ",fileName," ", wordCounter,"\n")
        print(fileName+" "+str(len(lines))+" "+str(wordCounter)+" "+threading.currentThread().getName())
            
            
dirInput = "/Users/muthukumarangunasekaran/Documents/WS/Python1/directory/thread"
fileList = loadFiles() 
num_of_files = len(fileList)
num_of_threads = 5
files_per_thread = num_of_files/num_of_threads
extr = num_of_files%num_of_threads
start = 0
end = 0

for i in range(num_of_threads):
    if(i != 0):
        start = end
    end = start+math.floor(files_per_thread)
    if(extr > 0):
        end = end+1    
    extr = extr-1
    #print(str(start)+" "+str(end))
    threadName = "Thread"+str(i)
    thread=threading.Thread(name=threadName, target=getFolderMetrics, args =(fileList[start:end],))
    thread.start()