import csv
import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time

def read_participants(file_path):
    """Reads participants from a CSV file."""
    participants = []
    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            participants.append({'name': row[0], 'email': row[1]})
    return participants

def assign_secret_santa(participants):
    """Randomly assigns Secret Santa pairs."""
    names = [p['name'] for p in participants]
    santa_pairs = {}
    while True:
        shuffled = names[:]
        random.shuffle(shuffled)
        if all(shuffled[i] != names[i] for i in range(len(names))):
            for i, participant in enumerate(participants):
                santa_pairs[participant['name']] = shuffled[i]
            break
    return santa_pairs

def send_emails(santa_pairs, participants, smtp_server, smtp_port, sender_email, sender_password):
    """Sends emails to participants with their Secret Santa assignments."""
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)

        for participant in participants:
            santa = participant['name']
            recipient = santa_pairs[santa]

            msg = MIMEMultipart()
            msg['From'] = sender_email
            msg['To'] = participant['email']
            msg['Subject'] = "Your Secret Santa Assignment!🌲🎅"

            # Clean and simple email body
            body = f"""
            <html>
                <body>
                    <p>Hello {santa},</p>
                    <p>You have been chosen as the Secret Santa for <b>{recipient}</b>!</p>
                    <p>Please keep this a surprise and prepare a thoughtful gift for them.</p>
                    <p><b>Location:</b> Example Office<br>
                    <b>Date:</b> 27/12/2024<br>
                    <b>Amount to spend:</b> 10K USD</p>
                    <p>Best regards,<br>
                    Secret Santa</p>
                </body>
            </html>
            """

            msg.attach(MIMEText(body, 'html'))

            server.sendmail(sender_email, participant['email'], msg.as_string())
            print(f"Email sent to {participant['email']}")
            time.sleep(2)  # Add a delay to avoid rate limiting

        server.quit()
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    file_path = "path/for/your/csv_file" # replace this 

    # SMTP server configuration
    smtp_server = "smtp.example.com" # change this to your smpt server
    smtp_port = 587 # change this
    sender_email = "example@emali.com" # write your email address 
    sender_password = "password" # write your emali password

    participants = read_participants(file_path)
    santa_pairs = assign_secret_santa(participants)

    print("Secret Santa Pairings:")
    for santa, recipient in santa_pairs.items():
        print(f"{santa} → {recipient}")

    # Send emails
    send_emails(santa_pairs, participants, smtp_server, smtp_port, sender_email, sender_password)

    print("Emails sent successfully!")
