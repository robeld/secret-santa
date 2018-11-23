import csv
import random
#import smtplib

name_col = "Name?"
#email_col = "Email Address"
mailing_col = "Mailing Address?"


with open("responses.csv", mode="r") as file:
	reader = csv.DictReader(file)
	toAssign = list(reader)
	random.shuffle(toAssign)
	assigned = list(toAssign)
	assigned.append(assigned.pop(0))
	master = open("master-key.txt", "w+")
	for i, d in enumerate(toAssign):
		file_name = d[name_col] + ".txt"
		assignment = assigned[i]
		text = "Hello " + d[name_col] + "! This is an automatically generated secret santa message. You are assigned to " + assignment[name_col] + "!\nTheir mailing address is:\n" + assignment[mailing_col]
		f = open(file_name, 'w+')
		f.write(text)
		f.close()
		s = d[name_col] + " is buying a gift for " + assignment[name_col] + ".\n"
		master.write(s)
	master.close()