import smtplib
from unidecode import unidecode

def send_email(settings, subject, body):
    """
    Send an email using the settings provided.
    """
    address = settings['from']
    password = settings['password']
    server = settings['server']
    port = settings['port']
    to = settings['to']

    with smtplib.SMTP(server, port) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login(address, password)

        for email in to:
            msg = f'Subject: {subject}\n\n{body}'
            msg = unidecode(msg)
            smtp.sendmail(address, email, msg)

        print(f"Email - {subject} - sent to {to}", flush=True)
        smtp.quit()