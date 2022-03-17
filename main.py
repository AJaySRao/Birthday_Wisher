import smtplib
import datetime as dt
from random import randint
import pandas

email = "samplyemail9@yahoo.com"
password = "zabpidkwdbuqwqtd"

celebration = pandas.read_csv("birthdays.csv")

now = dt.datetime.now()
date = now.day
month = now.month

letter = f"letter_templates/letter_{randint(1,3)}.txt"

with open(letter) as w:
    placeholder = w.read()

for d in range(len(celebration)):
    if (celebration.month[d] == month) and celebration.day[d] == date:
        new_letter = placeholder.replace("[NAME]", celebration.name[d])
        address = celebration.email[d]

        with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
            connection.starttls()
            connection.login(user=email, password=password)
            connection.sendmail(from_addr=email, to_addrs=address,
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
