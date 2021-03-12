import os, subprocess
import smtplib, ssl

def main():
    hostname = subprocess.run("hostname -I")
    hostname = hostname.stdout[:14]
    if get_old() != hostname:
        update(hostname)

def get_old():
    old = ""
    try:
        with open("old.txt", "r") as file:
            old = file.readline()
    except FileNotFoundError:
        os.system("echo \"Error reading file\" >> err.txt")
        exit()
    return old

def update(hostname):
    with open("old.txt", "w") as file:
        file.write(hostname)
    email(hostname)

def email(message):
    port = 465
    smtp_server = "smtp.gmail.com"
    sender = "Sample email"
    password = "Sample password"
    receiver = "Sample email"
    context = ssl.create_default_context()
    full_message = "ALERT: Server IP address has changed to: " + message
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender, password)
        server.sendmail(sender, receiver, full_message)