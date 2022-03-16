import smtplib
import datetime as dt
from random import choice
import pandas

email = "samplyemail9@yahoo.com"
password = "zabpidkwdbuqwqtd"

celebration = pandas.read_csv("birthdays.csv")

now = dt.datetime.now()
date = now.day
day = now.weekday()
month = now.month


l1 = "letter_templates/letter_1.txt"
l2 = "letter_templates/letter_2.txt"
l3 = "letter_templates/letter_3.txt"
letters = [l1, l2, l3]
r_letter = choice(letters)
with open(r_letter) as w:
    placeholder = w.read()

n = len(celebration)

for d in range(n-1):
    if celebration.day[d] == date:
        #print(date)
        new_letter = placeholder.replace("[NAME]", celebration.name[d])
        with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
            connection.starttls()
            connection.login(user=email, password=password)
            connection.sendmail(from_addr=email, to_addrs="samplgemail9@gmail.com",
                                msg=f"Subject:Happy Birthday\n\n{new_letter}")



#print(celebration.values[0])
#
# document = "quotes.txt"
# if day == 2:
#     with open(document, 'r') as doc:
#         quotes = doc.readlines()
#         quote = choice(quotes)
#     with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
#         connection.starttls()
#         connection.login(user=email, password=password)
#         connection.sendmail(from_addr=email,
#                             to_addrs="samplgemail9@gmail.com",
#                             msg=f"Subject:Wonderful Quote\n\n{quote}")

#print(month)
