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