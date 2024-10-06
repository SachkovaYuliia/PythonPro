from message_senders import SMSService, EmailService, PushService, SMSAdapter, EmailAdapter, PushAdapter

def main():
    sms_service = SMSService()
    email_service = EmailService()
    push_service = PushService()

    sms_adapter = SMSAdapter(sms_service, "1234567890")
    email_adapter = EmailAdapter(email_service, "example@example.com")
    push_adapter = PushAdapter(push_service, "device_001")

    sms_adapter.send_message("Це SMS!")
    email_adapter.send_message("Це Email!")
    push_adapter.send_message("Це Push-повідомлення!")

if __name__ == "__main__":
    main()
