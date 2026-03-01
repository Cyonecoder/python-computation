# Automated Exam Email Sender

A Python automation script that reads student exam results from a CSV file and sends personalized emails using Gmail SMTP over SSL.

One student is randomly selected to receive an additional presentation notification.

---

## Overview

This project demonstrates:

- CSV parsing using `csv.DictReader`
- Dynamic dictionary construction
- Keyword argument unpacking (`**kwargs`)
- Secure credential management using `.env`
- Email automation using `smtplib`
- Error handling with `try / except / else`
- Random selection logic

It is designed as a practical SMTP automation learning project.

---

## Project Structure

automating_email/
│
├── file_reading.py
├── exam.csv
├── .env
├── .env.example
├── .gitignore
└── README.md

---

## How It Works

1. The script reads student data from `exam.csv`.
2. It constructs a lookup dictionary where:
   - The key is the student email.
   - The value contains first name, last name, scores, and comments.
3. One random student is selected.
4. A personalized message is generated.
5. The message is sent securely using Gmail SMTP (SSL on port 465).
6. Success or failure is printed to the terminal.

---

## CSV Format

The `exam.csv` file must follow this exact column structure:

Email,Last name,First name,
Problem 1 score,Problem 1 comments,
Problem 2 score,Problem 2 comments,
Problem 3 score,Problem 3 comments

### Example Row

student@email.com ->,Bell,Ana,88,good job,75,needs work,90,clear and concise

⚠ Column order must match the script's `fieldnames` list.

---

## Gmail Configuration

This project uses Gmail SMTP over SSL.

### Requirements

1. Enable **2-Step Verification** on your Google account.
2. Generate a **Gmail App Password**.
3. Use the 16-character App Password (NOT your normal password).

---

## Environment Variables

Create a `.env` file in the project directory:

GMAIL_APP_USER=your_email@gmail.com

GMAIL_APP_PASSWORD=your_16_character_app_password

Example `.env.example`:

GMAIL_APP_USER=example@gmail.com

GMAIL_APP_PASSWORD=abcdefghijklmnop

The `.env` file is ignored via `.gitignore` for security.

---

## Installation

Install the required dependency:

pip install python-dotenv

Python 3.10+ recommended.

---

## Running the Script

From inside the project directory:

python file_reading.py

### Expected Output (Success)

Email sent successfully to student@email.com

---

## Example Email Content

Subject: Book assignment result

Dear Ana,

Your score for the book assignment is broken down below by question number.

88%: good job
75%: needs work
90%: clear and concise

You've been randomly chosen to present a summary of the book in the next class.

---

## Error Handling

The script handles:

- SMTP authentication errors
- SMTP connection errors
- Invalid recipient errors
- Unexpected runtime exceptions

Example error message:

Authentication failed. Check email or app password.

---

# ⚠⚠⚠ IMPORTANT AUTOMATION NOTICE ⚠⚠⚠

This script sends **real emails immediately upon execution**.

Before running:

- Verify `.env` credentials
- Double-check `exam.csv`
- Test with your own email first
- Confirm recipient addresses
- Ensure Gmail App Password is valid

There is NO dry-run mode.

Use responsibly.

---

## Security Best Practices

- Never commit `.env`
- Always use App Passwords
- Revoke credentials immediately if exposed
- Do not hardcode secrets in source code

---

## Technologies Used

- Python 3
- smtplib
- ssl
- csv
- random
- python-dotenv

---

## Possible Improvements

- Add HTML email support
- Add logging to file
- Add retry mechanism
- Add throttling (avoid Gmail rate limits)
- Add dry-run mode
- Add Docker support
- Add unit tests

---

## Author

Built as a practical SMTP automation and Python chill weekend project.
