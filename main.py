import smtplib
import datetime as dt
from random import choice

email = "samplyemail9@yahoo.com"
password = "zabpidkwdbuqwqtd"

now = dt.datetime.now()
day = now.weekday()

document = "quotes.txt"
with open(document, 'r') as doc:
    quotes = [line.strip() for line in doc]

quote = choice(quotes)

if day == 2:
    with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(from_addr=email,
                            to_addrs="samplgemail9@gmail.com",
                            msg=f"Subject:Wonderful Quote\n\n{quote}")

# print(quotes)
