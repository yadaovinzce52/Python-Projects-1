import smtplib
import datetime as dt
from random import choice

now = dt.datetime.now()
day_of_week = now.weekday()
random_password = 'rjcahicpfwgluzsx'

if day_of_week == 0:
    with open('quotes.txt', 'r') as quotes:
        list_of_quotes = quotes.readlines()

    random_quote = choice(list_of_quotes)
    my_email = 'change to gmail'
    password = random_password

    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs='change to yahoo',
            msg=f'Subject:Motivational Quote!!\n\n{random_quote}'
        )

