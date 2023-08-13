import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def mailtoclient(email,name):
   sender_email = "freelanceuniverse2@gmail.com"
   receiver_email = email
   password = "hxdsvuvkzpyjipge"

   message = MIMEMultipart("alternative")
   message["Subject"] = "Thanks for showing interest in our services we'll contact you soon"
   message["From"] = sender_email
   message["To"] = receiver_email


   text = """Hello {},
We're thrilled you reached out to Freelance Universe! Your interest in our services is greatly appreciated.
We're already reviewing your inquiry and will be in touch soon . 
Your projects are important to us, and we're committed to providing top-notch assistance.
If you have immediate questions, feel free to reply. We're here to make your freelancing experience exceptional.

Best regards,

Tanmay Arora
Freelance Universe
""".format(name)


   part1 = MIMEText(text, "plain")

   message.attach(part1)

   context = ssl.create_default_context()
   with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
       server.login(sender_email, password)
       server.sendmail(
           sender_email, receiver_email, message.as_string()
       )

def mailtoourself(email,name,contact,subject):
   sender_email = "examplemsit@gmail.com"
   receiver_email = "freelanceuniverse2@gmail.com"
   password = "smwtujbcmobbmbda"

   message = MIMEMultipart("alternative")
   message["Subject"] = "New client Alert"
   message["From"] = sender_email
   message["To"] = receiver_email


   text = """
   client request
   name :{}
   email:{}
   contact:{}
   subject:{}
""".format(name,email,contact,subject)


   part1 = MIMEText(text, "plain")

   message.attach(part1)

   context = ssl.create_default_context()
   with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
       server.login(sender_email, password)
       server.sendmail(
           sender_email, receiver_email, message.as_string()
       )
