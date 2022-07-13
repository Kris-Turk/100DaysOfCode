import datetime as dt
import pandas
import random
import smtplib
import logging
import azure.functions as func
import os

def main(mytimer: func.TimerRequest) -> None:
    utc_timestamp = dt.datetime.utcnow().replace(
        tzinfo=dt.timezone.utc).isoformat()

    if mytimer.past_due:
        logging.info('The timer is past due!')

from_email = os.environ["FROM_EMAIL"]
password = os.environ["PASSWORD"]

todays_day = dt.datetime.now().day
todays_month = dt.datetime.now().month


birthdays_file = "birthdays.csv"

birthdays_df = pandas.read_csv(birthdays_file)
birthdays_dict = birthdays_df.to_dict(orient='records')

for x in birthdays_dict:
    if x['day'] == todays_day and  x['month'] == todays_month:
        print(x)
        
        with open(f"letter_templates/letter_{random.randint(1,3)}.txt", "r") as letter:
            email = letter.readlines()
         
        email_string =' '.join(map(str,email))    
        email_string = email_string.replace('[NAME]', x['name'])
                
        with smtplib.SMTP("smtp.gmail.com", port=587) as conn:
            conn.starttls()
            conn.login(user=from_email,password=password)
            conn.sendmail(from_addr=from_email, 
                        to_addrs=x['email'], 
                        msg=f"Subject:Happy Birthday\n\n{email_string}")
