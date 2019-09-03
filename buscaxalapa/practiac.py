import smtplib 
from cred import user, password
from email.mime.text import MIMEText

def read(mensaje):
    return input(mensaje).strip()

def send(fromaddr, toaddrs, msg):
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(user, password)
        server.sendmail(fromaddr,toaddrs, str(msg))
        server.close()
        print("correoenviado")
    except Exception as e:
            print(e)

if  __name__ == '__main__':
    fromaddr = user
    toaddrs = read("to:").split()
    subject = read("Subject: ")
    leer = read("Message: ")
    msg =MIMEText(leer, _charset="UTF-8")
    send(fromaddr, toaddrs, msg) 