import smtplib, ssl
import json

sender_address = "gabriele.falace@gmail.com"
password = input("insert password:  ")
msg_subject = "HELL NO, SUCH A SUBJECT"
msg_text = "Hi {}, \n this message is sent via my python script. \n I hope you enjoy that :)"
message = "Subject: {} \n\n {}".format(msg_subject, msg_text)
server = smtplib.SMTP_SSL(host="smtp.gmail.com", port=465, context=ssl.create_default_context())
server.login(sender_address, password)
for recipient in json.loads(open("/Users/gabrielefalace/kita.json").read()): 
  server.sendmail(sender_address, recipient["email"], message.format(recipient["name"]))
server.quit()
