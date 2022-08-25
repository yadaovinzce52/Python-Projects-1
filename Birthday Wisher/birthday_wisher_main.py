##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name
# from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import smtplib
import datetime as dt
import pandas as pd
from random import randint

data = pd.read_csv('birthdays.csv')
birthdays = data.to_dict(orient='records')

now = dt.datetime.now()
year = now.year
month = now.month
day = now.day

for record in birthdays:
    record_year = record['year']
    record_month = record['month']
    record_day = record['day']
    if int(record_year) == year and int(record_month) == month and int(record_day) == day:
        my_email = 'pythondevtest52@gmail.com'
        password = 'rjcahicpfwgluzsx'
        recipient_name = record['name']
        recipient_email = record['email']
        template = randint(1, 3)
        with open(f'letter_templates/letter_{template}.txt', 'r') as file:
            contents = file.read()
            contents = contents.replace('[NAME]', recipient_name)
            contents = contents.replace('Angela', 'Vinzce')

        with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=recipient_email,
                msg=f'Subject:Happy Birthday!\n\n{contents}'
            )
