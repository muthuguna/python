import csv

class SendMessages:

    studentDictionary = {}
    
    # Assigning fileName to class object, so that filename will be available in object
    def __init__(self, fileName):
        self.fileName = fileName
 
    def getStudentInfo(self):
        with open(self.fileName) as fileObj:
            rows = csv.reader(fileObj, delimiter="\t")
            count = 0
            for row in rows:
                if count != 0:
                    self.studentDictionary[row[0]]= row[1:3]
                count = count+1
           
    def sendEmail(self):
        import smtplib
        toMailList = []
        for val in self.studentDictionary.values():
            toMailList.append(val[0])
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login("username", "password")
        server.sendmail("divpatel01.bhn@gmail.com",toMailList, "Happy Ugadi to all....")
        server.quit()
