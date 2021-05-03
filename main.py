##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import datetime as dt
import random
import smtplib
import pandas as pd
from password import password

# check the spam in the destination account
# on google we have to check enable the less secure app
# the email account with i going to send emails
my_email = "davidraskovskypython@gmail.com"
email_password = password
# get the date
today = dt.datetime.now()
today_tuple = (today.month, today.day)
# get the birthday info from a file
birthday_df = pd.read_csv("birthdays.csv")
# with dictionary comprehension generate a dictionary from de dataframe
birthday_dictionary = {(data_row.month, data_row.day): data_row for (index, data_row) in birthday_df.iterrows()}
# check if today i have some birthday
if today_tuple in birthday_dictionary:
    birthday_person = birthday_dictionary[today_tuple]
    # i read a letter randomly for the birthday
    filepath = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    # reading the letter from the file
    with open(filepath) as letter_file:
        contents = letter_file.read()
        # replace the name of the destination person on the letter
        contents = contents.replace("[NAME]", birthday_person["name"])
        print(contents)
    # now i have to send the letter
    with smtplib.SMTP("smtp.gmail.com") as connection:
        # the starttls is the security method to connection with encyptions
        # make the connection more secure
        connection.starttls()
        # Establish the user to connection and password
        connection.login(user=my_email, password=password)
        # writing the email and sending
        connection.sendmail(from_addr=my_email,
                            to_addrs=birthday_person["email"],
                            msg=f"Subject:Happy Birthday\n\n{contents}"
                            )
