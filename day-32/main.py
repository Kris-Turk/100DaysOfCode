import datetime as dt
import random
import smtplib

now = dt.datetime.now()

if now.weekday() == 1:
    with open("quotes.txt","r") as quotes:
        tuesday_quote = random.choice(quotes.readlines())
        print(tuesday_quote)
    
    email = "turk.kris@gmail.com"
    password = "naiehyhevjdmplva"
           
    with smtplib.SMTP("smtp.gmail.com", port=587) as conn:
        conn.starttls()
        conn.login(user=email,password=password)
        conn.sendmail(from_addr=email, 
                    to_addrs="kris.turk@gitch.solutions", 
                    msg=f"Subject:Tuesday Quote\n\n{tuesday_quote}")
        