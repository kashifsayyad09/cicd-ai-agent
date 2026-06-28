import os
import smtplib
import ssl
import traceback
import argparse

try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    print("Logging into Gmail...")
    server.login(EMAIL_USERNAME, EMAIL_PASSWORD)

    print("Sending email...")
    server.sendmail(
        EMAIL_USERNAME,
        EMAIL_TO,
        message.as_string()
    )

    print("✅ Email sent successfully!")

except Exception as e:
    print("❌ Email sending failed")
    print(str(e))
    traceback.print_exc()
    raise

finally:
    try:
        server.quit()
    except:
        pass
