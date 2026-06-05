##################### Extra Hard Starting Project ######################
import pandas as pd
import smtplib
import random
import datetime as dt


MY_EMAIL = "bobday32100days@gmail.com"
MY_PASSWORD = "xnry bleo ulww gpcu"

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
data = pd.read_csv("birthdays.csv")
today = dt.datetime.now()
month = today.month
day = today.day

data_to_wish= data[(data["month"] == month) & (data["day"] == day)]

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
if data_to_wish.shape[0] >= 1:

    for _,row in data_to_wish.iterrows():
        name = row["name"]
        mail = row["email"]

        random_letter_number = random.randint(1,3)
        with open(f"./letter_templates/letter_{random_letter_number}.txt") as file:
            text = file.read()
            text = text.replace("[NAME]", name)
            text = text.replace("Angela", "Valerian")
        # 4. Send the letter generated in step 3 to that person's email address.

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user = MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=mail,
                                msg = f"Subject: Happy Birthday!\n\n{text}")



