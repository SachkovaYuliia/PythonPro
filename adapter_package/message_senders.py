class MessageSender:
    def send_message(self, message: str):
        pass

class SMSService:
    def send_sms(self, phone_number: str, message: str):
        print(f"Відправлено SMS на {phone_number}: {message}")

class EmailService:
    def send_email(self, email_address: str, message: str):
        print(f"Відправлено Email на {email_address}: {message}")

class PushService:
    def send_push(self, device_id: str, message: str):
        print(f"Відправлено Push-повідомлення на {device_id}: {message}")


class SMSAdapter(MessageSender):
    def __init__(self, sms_service: SMSService, phone_number: str):
        self.sms_service = sms_service
        self.phone_number = phone_number

    def send_message(self, message: str):
        self.sms_service.send_sms(self.phone_number, message)

class EmailAdapter(MessageSender):
    def __init__(self, email_service: EmailService, email_address: str):
        self.email_service = email_service
        self.email_address = email_address

    def send_message(self, message: str):
        self.email_service.send_email(self.email_address, message)

class PushAdapter(MessageSender):
    def __init__(self, push_service: PushService, device_id: str):
        self.push_service = push_service
        self.device_id = device_id

    def send_message(self, message: str):
        self.push_service.send_push(self.device_id, message)
