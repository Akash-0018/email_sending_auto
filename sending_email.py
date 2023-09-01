# sending email using python

pip smdplib

import smtplib as s

ob = s.SMTP('smtp.gmail.com',587)  # server port defining gmail's port is 587

ob.ehlo() 
ob.starttls()

ob.login('uamrsunny@gmail.com','password')
subject = "test python"

body="I love python"

message = "subject:{}\n\n{}.format(subject,body)" # curli braces-dot-formatting function is used coz if user input or not input it works in both cases

listadd = ['fsjhf@hfkj.com','fksjd@fh.com']

ob.sendmail('sender mail address', listadd, message) # or u can give directly in place of listdd and message variables..

print("mail is sent")

ob.quit