import psutil
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# ===== CONFIGURATION =====
SENDER_EMAIL = "sender@gmail.com"
APP_PASSWORD = "abcd efgh ijkl mnop"  # Use Gmail App Password
# Enable 2-Step Verification
# Go to:
# 👉 https://myaccount.google.com/apppasswords
# Generate App Password

RECEIVER_EMAIL = "reciver@gmail.com"

def send_email_alert(current_cpu, cpu_threshold):
    subject = "🚨 CPU Usage Alert!"
    
    body = f"""
    Warning!

    Current CPU Usage: {current_cpu}%
    Threshold Set: {cpu_threshold}%

    CPU usage has exceeded the defined threshold.
    Please check the system immediately.
    """

    message = MIMEMultipart()
    message["From"] = SENDER_EMAIL
    message["To"] = RECEIVER_EMAIL
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(SENDER_EMAIL, APP_PASSWORD)
        server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, message.as_string())
        server.quit()
        print("✅ Email alert sent successfully!")
    except Exception as e:
        print("❌ Failed to send email:", e)


def check_cpu_threshold():
    cpu_threshold = float(input("Enter the CPU usage threshold (in percentage): "))
    
    current_cpu = psutil.cpu_percent(interval=1)

    if current_cpu > cpu_threshold:
        print(f"CPU usage is {current_cpu}%, which exceeds the threshold of {cpu_threshold}%. Sending email alert...")
        send_email_alert(current_cpu, cpu_threshold)
    else:
        print(f"CPU usage is {current_cpu}%, which is within the threshold.")


if __name__ == "__main__":
    check_cpu_threshold()