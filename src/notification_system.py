from abc import ABC, abstractmethod


class Notification(ABC):
    @abstractmethod
    def send(self, message: str, target: str, attachment: str = None) -> bool:
        pass


class EmailNotification(Notification):
    def __init__(self):
        self.host = "smtp.mail.com"
        self.port = 587

    def send(self, message: str, target: str, attachment: str = None) -> bool:
        print(f"[{self.host}:{self.port}] baglanti kuruluyor")
        print(f"Email Alici: {target} | Icerik: {message}")
        return True


class SMSNotification(Notification):
    def send(self, message: str, target: str, attachment: str = None) -> bool:
        print(f"SMS Tel: {target} | Icerik: {message}")
        return True


class PushNotification(Notification):
    def send(self, message: str, target: str, attachment: str = None) -> bool:
        print(f"Push Cihaz: {target} | Icerik: {message}")
        return True


class WhatsAppClient:
    def push_message(self, text: str, contact_number: str):
        print(f"WA API {contact_number}: {text}")
        return "SUCCESS"


class WhatsAppAdapter(Notification):
    def __init__(self):
        self.api = WhatsAppClient()

    def send(self, message: str, target: str, attachment: str = None) -> bool:
        res = self.api.push_message(text=message, contact_number=target)
        return res == "SUCCESS"


class NotificationDecorator(Notification):
    def __init__(self, base_notif: Notification):
        self._base = base_notif

    def send(self, message: str, target: str, attachment: str = None) -> bool:
        return self._base.send(message, target, attachment)


class EncryptedNotification(NotificationDecorator):
    def send(self, message: str, target: str, attachment: str = None) -> bool:
        enc_msg = f"ENC[{message[::-1]}]"
        return super().send(enc_msg, target, attachment)


class LoggingNotification(NotificationDecorator):
    def send(self, message: str, target: str, attachment: str = None) -> bool:
        print(f"INFO: {target} icin gonderim basladi.")
        res = super().send(message, target, attachment) 
        print(f"gonderim bitti. sonuc={res}\n")
        return res


class NotificationFactory:
    @staticmethod
    def create_notification(notif_type: str) -> Notification:
        providers = {
            "Email": EmailNotification,
            "SMS": SMSNotification,
            "Push": PushNotification,
            "WhatsApp": WhatsAppAdapter
        }

        if notif_type not in providers:
            raise ValueError(f"Desteklenmeyen tip: {notif_type}")

        return providers[notif_type]()


if __name__ == "__main__":
    factory = NotificationFactory()

    wa = factory.create_notification("WhatsApp")
    wa.send("Siparis Alindi ", "+905551234567")

    print("-" * 40)

    sms = factory.create_notification("SMS")
    secure_sms = LoggingNotification(EncryptedNotification(sms)) 

    secure_sms.send("Gizli Doğrulama Kodu: 9876", "+905559998877")
