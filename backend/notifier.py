import smtplib
from email.message import EmailMessage
from typing import Union, List
import config

class EmailNotifier:
    def __init__(self, sender_email: str, app_password: str):
        self.sender_email = sender_email
        self.app_password = app_password
        self.smtp_server = "smtp.gmail.com"
        self.smtp_port = 465

    def send_notification(
        self, 
        to_emails: Union[str, List[str]], 
        subject: str, 
        body: str
    ) -> bool:
        if isinstance(to_emails, str):
            to_emails = [to_emails]
            
        try:
            msg = EmailMessage()
            msg.set_content(body)
            msg['Subject'] = subject
            msg['From'] = self.sender_email
            msg['To'] = ', '.join(to_emails)
            
            with smtplib.SMTP_SSL(self.smtp_server, self.smtp_port) as server:
                server.login(self.sender_email, self.app_password)
                server.send_message(msg)
            return True
            
        except Exception as e:
            print(f"Failed to send email: {str(e)}")
            return False


if __name__ == "__main__":
    notifier = EmailNotifier(
        sender_email=config.EMAIL_SENDER,
        app_password=config.EMAIL_PASSWORD
    )
    
    # Send to single recipient
    # notifier.send_notification(
    #     "briannguyen013@gmail.com",
    #     "Test Notification",
    #     "This is a test message"
    # )
    
    # Send to multiple recipients
    notifier.send_notification(
        ["elewisdando@gmail.com", "briannguyen013@gmail.com"],
        "Group Notification",
        "This is a group message"
    )