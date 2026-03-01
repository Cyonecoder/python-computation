import csv
import os
import smtplib
import random
import ssl
from dotenv import load_dotenv

load_dotenv()

lookup = {}
fieldnames = [
    "Email",
    "Last name",
    "First name",
    "Problem 1 score",
    "Problem 1 comments",
    "Problem 2 score",
    "Problem 2 comments",
    "Problem 3 score",
    "Problem 3 comments",
]
APP_USER_MAIL = os.getenv("GMAIL_APP_USER")
APP_PASSWORD = os.getenv("GMAIL_APP_PASSWORD")


def main():

    reader = file_open_read("exam.csv")
    # for line in file_open_read():
    #     print(line)

    for key, value in lookup.items():
        value_cleaned = clean_keys(value)

        smtpsend(
            email=key,
            **value_cleaned,
        )


def smtpsend(email, **kwargs):
    from_addr = APP_USER_MAIL
    extra_message = ""
    if kwargs.get("selected"):
        extra_message = "\nYou've been randomly chosen to present a summary of the book in the next class. Looking forward to it!"

    else:
        """"""
    msg = f"""Dear {kwargs.get('first_name')} ,Your score for the book assignment is broken down below by question number.\n\n
    {kwargs.get('socres')[0]}%: {kwargs.get('comments')[0]}\n
    {kwargs.get('socres')[1]}%: {kwargs.get('comments')[1]}\n
    {kwargs.get('socres')[2]}%: {kwargs.get('comments')[2]}\n
    {extra_message}
    """

    context = ssl.create_default_context()
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", port=465, context=context) as server:
            server.login(APP_USER_MAIL, APP_PASSWORD)
            # server.set_debuglevel(1)
            server.sendmail(from_addr, email, msg)
    except smtplib.SMTPAuthenticationError:
        print("Authentication failed. Check email or app password.")

    except smtplib.SMTPConnectError:
        print("Could not connect to SMTP server.")

    except smtplib.SMTPRecipientsRefused:
        print("Recipient address refused.")

    except Exception as e:
        print(f"Unexpected error: {e}")

    else:
        print(f"Email sent successfully to {email}")


def file_open_read(filename):
    with open(filename, newline="") as file:
        rows = csv.DictReader(file, fieldnames=fieldnames)
        for row in rows:
            lookup[row["Email"]] = {
                "First name": row["First name"],
                "Last name": row["Last name"],
                "socres": [
                    row["Problem 1 score"],
                    row["Problem 2 score"],
                    row["Problem 3 score"],
                ],
                "comments": [
                    row["Problem 1 comments"],
                    row["Problem 2 comments"],
                    row["Problem 3 comments"],
                ],
            }
        selected_email = random.choice(list(lookup.keys()))
        lookup[selected_email]["selected"] = True
        return lookup


def clean_keys(d):
    return {key.replace(" ", "_").lower(): value for key, value in d.items()}


if __name__ == "__main__":
    main()
