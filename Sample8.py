from SendMessage import SendMessages

obj = SendMessages("/Users/muthukumarangunasekaran/Documents/WS/Python1/StudentsInfo.csv")                
obj.getStudentInfo()
obj.sendEmail()
print(obj.studentDictionary)