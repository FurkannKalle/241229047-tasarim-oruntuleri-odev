from abc import ABC, abstractmethod

class Notification(ABC):
    @abstractmethod
    def send(self, message: str, target: str, attachment: str = None) -> bool:
        pass

class EmailNotification(Notification):
    def __init__(self):
        self.smtp_host = "smtp.mail.com"
        self.smtp_port = 587

    def send(self, message: str, target: str, attachment: str = None) -> bool:
        if "@" not in target:
            print(f"Gecersiz e-posta adresi: {target}")
            return False
        
        print(f"SMTP baglantisi kuruldu ({self.smtp_host}:{self.smtp_port})")
        print(f"[EMAIL] Kime: {target} | Mesaj: {message}")
        
        if attachment:
            print(f"[EMAIL] Eklenen dosya: {attachment}")
            
        return True

class SMSNotification(Notification):
    def __init__(self):
        self.api_key = "12345-ABCDE" 

    def send(self, message: str, target: str, attachment: str = None) -> bool:
        if len(message) > 160:
            print("SMS metni 160 karakteri gecemez.")
            return False
            
        if not str(target).startswith("+90"):
            print("Sadece yurt ici (+90) numaralara SMS gonderilebilir.")
            return False
        
        if attachment:
            print("SMS eklenti desteklemiyor, ek dosyalar yoksayildi.")
            
        print(f"[SMS] {target} numarasina iletildi. API Key: {self.api_key[:5]}***")
        return True

class PushNotification(Notification):
    def __init__(self):
        self.secret = "FIREBASE_SECRET_999"

    def send(self, message: str, target: str, attachment: str = None) -> bool:
        if not target:
            print("Cihaz token'i bulunamadi.")
            return False
        
        print(f"Cihaz: {target} | Bildirim gonderildi.")
        return True

class NotificationFactory:
    @staticmethod
    def get_sender(notif_type: str) -> Notification:
        providers = {
            "email": EmailNotification,
            "sms": SMSNotification,
            "push": PushNotification
        }
        
        sender_class = providers.get(notif_type.lower())
        if not sender_class:
            raise ValueError(f"Desteklenmeyen bildirim tipi: '{notif_type}'")
            
        return sender_class()

if __name__ == "__main__":
    factory = NotificationFactory()
    
    email = factory.get_sender("email")
    email.send("Faturaniz ektedir.", "musteri@sirket.com", attachment="fatura_mayis.pdf")
    print("-" * 40)
    
    sms = factory.get_sender("sms")
    sms.send("Kargonuz yola cikti.", "+905551234567", attachment="kargo_belgesi.png")
    print("-" * 40)
    
    email.send("Merhaba", "hatali-mail-adresi")