import smtplib
import datetime as dt
import random
import pandas

message = ""
NOW = dt.datetime.now()
date = NOW.day
month = NOW.month
today_tuple = (month, date)
MY_EMAIL = ""  # your email
PASSWORD = ""  # your password
letter_number = random.randrange(1, 4)
data = pandas.read_csv("birthdays.csv")
data_dict = {
    (row.month, row.day): row for (index, row) in data.iterrows()
}
if today_tuple in data_dict:
    with open(f"letter_templates/letter_{letter_number}.txt") as letter_file:
        letter_list = letter_file.readlines()
        replaced = letter_list[0].replace("[NAME]", f"{data_dict[today_tuple].person}")
        letter_list[0] = replaced
    with open("birthday_wish.txt", mode="w") as birthday_msg:
        for i in range(len(letter_list)):
            birthday_msg.write(letter_list[i])
    with open("birthday_wish.txt") as birthday_message:
        birthday_msg_list = birthday_message.readlines()
        for i in range(len(birthday_msg_list)):
            message += birthday_msg_list[i]
        # print(message)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=data_dict[today_tuple].email,
                            msg=f"Subject: Happy Birthday!\n\n{message}")

