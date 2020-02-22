"""
File1.txt
Little Rock:72201
Sacramento:94203
Denver:80201
Hartford:06101
Dover:19901
Washington:20001
Miami:33124
Atlanta:30301
Honolulu:96801
Montpelier:83254

#File2.txt
Hartford:Conneticut
Dover:Deleware
Washington:District of Columbia
Miami:Florida
Atlanta:Georgia
Honolulu:Hawaii
Montpelier:Idaho
Huntsville:Alabama
Anchorage:Alaska
Phoenix:Arizona

#Result File
Hartford:06101:Conneticut
Dover:19901:Deleware
Washington:20001:District of Columbia
Miami:33124:Florida
Atlanta:30301:Georgia
Honolulu:96801:Hawaii
Montpelier:83254:Idaho
"""

# Merging files content
with open("File1.txt") as file1Obj:
    file1Lines = file1Obj.readlines()
    
with open("File2.txt") as file2Obj:
    file2Lines = file2Obj.readlines()
    
resultFile = open("File3.txt", "w")

for lineFile1 in file1Lines:
    cityFile1, zipFile1 = lineFile1.split(":",1)
    for lineFile2 in file2Lines:
        cityFile2, stateFile2 = lineFile2.split(":",1)
        if(cityFile1 == cityFile2):
            resultFile.write(cityFile1.strip()+":"+zipFile1.strip()+":"+stateFile2.strip()+"\n")
            
file1Obj.close()
file2Obj.close()
resultFile.close()
    
    