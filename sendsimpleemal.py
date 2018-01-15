#! /usr/bin/python
import smtplib
import string

HOST = "smtp.gmail.com"
SUBJECT = "TEST email from python"
TO ="nklongyi@qq.com"
FROM = "mangdinlongyi@gmail.com"
text = "python rules them all"
BODY = string.join((
	"From: %s " % FROM,
	"To: %s " % TO,
	"Subject: %s " % SUBJECT,
	"",
	text
	),"\r\n")
server = smtplib.SMTP()
server.connect(HOST,"25")
server.starttls();
server.login("mangdinlongyi@gmail.com","woainankai")
server.sendmail(FROM,[TO],BODY)
server.quit()