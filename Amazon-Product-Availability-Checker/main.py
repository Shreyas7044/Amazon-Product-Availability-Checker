# Amazon Product Availability Checker

from lxml import html
import requests
from time import sleep
import time
import schedule
import smtplib

# Receiver email address
receiver_email_id = "EMAIL_ID_OF_USER"


def check(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'
    }

    page = requests.get(url, headers=headers)

    for i in range(20):
        sleep(3)

        doc = html.fromstring(page.content)
        XPATH_AVAILABILITY = '//div[@id ="availability"]//text()'
        raw_availability = doc.xpath(XPATH_AVAILABILITY)

        availability = ''.join(raw_availability).strip() if raw_availability else None
        return availability


def sendemail(ans, product):
    GMAIL_USERNAME = "YOUR_GMAIL_ID"
    GMAIL_PASSWORD = "YOUR_GMAIL_PASSWORD"

    recipient = receiver_email_id
    subject = f"{product} product availability"

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(GMAIL_USERNAME, GMAIL_PASSWORD)

    headers = "\r\n".join([
        "From: " + GMAIL_USERNAME,
        "To: " + recipient,
        "Subject: " + subject,
        "MIME-Version: 1.0",
        "Content-Type: text/html"
    ])

    message = headers + "\r\n\r\n" + ans
    s.sendmail(GMAIL_USERNAME, recipient, message)
    s.quit()


def ReadAsin():
    ASIN = "B077PWK5BT"   # Replace with your product ASIN
    url = "https://www.amazon.in/dp/" + ASIN

    print("Processing:", url)
    availability = check(url)
    print("Availability:", availability)

    valid_status = [
        'Only 1 left in stock.',
        'Only 2 left in stock.',
        'In stock.'
    ]

    if availability in valid_status:
        sendemail(availability, ASIN)


def job():
    print("Tracking product availability...")
    ReadAsin()


schedule.every(1).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
