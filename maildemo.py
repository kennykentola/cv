import smtplib
server = smtplib.SMTP('smtp.gmail.com',587)

server.starttls()

server.login('peterkehindeademola@gmail.com','kehinde5')


server.sendmail('peterkehindeademola@gmail.com','peterkehindeademola9gmail.com','mail sent from python code')
print('mail sent')
