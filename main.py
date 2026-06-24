# To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.


from datetime import datetime
import pandas
import random
import smtplib
import os

# import os and use it to get the Github repository secrets
MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")

date = dt.datetime.now()
df = pd.read_csv("birthdays.csv")


day_exists = df[(df["month"] == date.month) & (df["day"] == date.day)].any().any()
if day_exists:
    curr = df[(df["month"] == date.month) & (df["day"] == date.day)]
    new_list = curr.values.tolist()

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        for mail_info in new_list:
            letter_num = random.randint(1, 3)
            with open(f"letter_templates/letter_{letter_num}.txt") as file:
                letter = file.read()
            letter = letter.replace("[NAME]", mail_info[0])
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=mail_info[1], msg =f"Subject:Happy Birthday!\n\n{letter}")
