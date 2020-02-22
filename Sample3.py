"""
myDictionary= {}

def add():
    nameValue = input("Enter name to add:")
    movieValue = input("Enter movie to add:")
    myDictionary[nameValue] = movieValue
    
def printItems():
    print(myDictionary) 
    
def deleteItem():
    nameValue = input("Enter name to delete:")
    del myDictionary[nameValue]
while(1):
    option = input("Enter option 'a' (Add), 'p' (Print), 'd' (Delete :")
    if option == 'a':
        add()
    elif option == 'p':
        printItems()
    elif option == 'd':
        deleteItem()
    else:
        break
"""
#Go to this link and select Turn On
#https://www.google.com/settings/security/lesssecureapps
import smtplib, getpass

server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
userName = input("Enter userName:")
pwd = getpass.getpass("Enter Password:")
server.login(userName, pwd)
server.sendmail("From Email id", "To Email id", "Test mail")
server.quit()
#Go to this link and select Turn Off