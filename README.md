# Birthday_Wisher
Automated Birthday Wisher

I decided to use Python to create a automated way of wishing happy birthday.

Now ABW, which is going to send our family or friends a "Happy Birthday" email on their birthday automatically.

Modules: random, smtplib, datetime
Editor: vscode

Steps:
1. The first thing to do is to go into this birthdays.csv and update this with some birthdays. So I replaced all the data
2. Check if today's date matches a birthday in the birthday CSV.
3. if there is a match, so if this if statement is true, then pick a random letter out of letter_1, 2, 3, from our letter templates inside
   1. Use the replace() method to replace the name placeholder inside each of these letters right here with the actual name of the person whose birthday it is.
4. Send the letter which was generated in contents, and send it to that birthday person's email address.
   1. Create connection using smtplib
   2. Depending on the email provider pick the correct SMTP, Used "smtp.mail.yahoo.com"
   3. Login credentials(user, password)
   4. Send email(user, to_address, msg)
