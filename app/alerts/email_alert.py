import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage


def send_alert(image_path):

    sender = "godofwar77001@gmail.com"

    password = "svvjgqkywymovivd"

    receiver = "godofwar77001@gmail.com"

    msg = MIMEMultipart()

    msg["Subject"] = "AI Surveillance Alert"
    msg["From"] = sender
    msg["To"] = receiver

    body = "Intrusion detected. Evidence attached."

    msg.attach(
        MIMEText(body)
    )

    with open(
        image_path,
        "rb"
    ) as f:

        img = MIMEImage(
            f.read()
        )

        msg.attach(img)

    server = smtplib.SMTP(
        "smtp.gmail.com",
        587
    )

    server.starttls()

    try:

        server.login(
            sender,
            password
    )

    except Exception as e:

        print(
            "EMAIL LOGIN FAILED:",
            e
        )

        return

    server.sendmail(
        sender,
        receiver,
        msg.as_string()
    )

    server.quit()

    print("EMAIL SENT")