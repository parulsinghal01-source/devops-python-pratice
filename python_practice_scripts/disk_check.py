#!/usr/bin/python3
## Script to check disk usage and send an alert if usage is > 80%
import shutil
import smtplib
from email.mime.text import MIMEText

# Threshold (80%)
THRESHOLD = 80

def check_disk_usage(path="/"):
    total, used, free = shutil.disk_usage(path)
    
    usage_percent = (used / total) * 100
    return usage_percent

def send_alert(usage):
    print(f"ALERT! Disk usage is at {usage:.2f}%")

    # Optional: email alert (configure if needed)
    msg = MIMEText(f"Disk usage is high: {usage:.2f}%")
    msg["Subject"] = "Disk Usage Alert"
    msg["From"] = "alert@example.com"
    msg["To"] = "you@example.com"

    # Example SMTP (replace with real SMTP server)
    # with smtplib.SMTP("smtp.example.com", 587) as server:
    #     server.starttls()
    #     server.login("user", "password")
    #     server.send_message(msg)

def main():
    usage = check_disk_usage("/")
    print(f"Current disk usage: {usage:.2f}%")

    if usage > THRESHOLD:
        send_alert(usage)
    else:
        print("Disk usage is normal.")

if __name__ == "__main__":
    main()
