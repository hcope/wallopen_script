from urllib2 import urlopen
from bs4 import BeautifulSoup
import smtplib
from email.MIMEMultipart import MIMEMultipart

wallPage = "http://scripts.mit.edu/~mitoc/wall/"
openWallPage = urlopen(wallPage).read()
html = BeautifulSoup(openWallPage, "html.parser")

openEntry = str(html.find_all(class_="entry open"))[1:-1]
currentStatus = str(html.find_all(class_="name "))[1:-1]

if currentStatus in openEntry:
  fromAddress = "wall-is-open@mit.edu"
  toAddress = "wall-is-open@mit.edu"
  message = MIMEMultipart()
  message['From'] = fromAddress
  message['To'] = toAddress
  message['Subject'] = "The wall is open! eom"
  text = message.as_string()
  server = smtplib.SMTP('outgoing.mit.edu',587)
  server.starttls()
  server.ehlo()
  server.login("MIT_Username", "Password")
  server.sendmail(fromAddress, toAddress, text)
