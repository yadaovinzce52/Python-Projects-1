import smtplib

my_email = 'Change this to sender email'
password = 'Change this to app generated pw'

with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs='Change this to receiver email',
        msg='Subject:Hello\n\nThis is the body of the email'
    )

