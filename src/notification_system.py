class NotificationManager:
    def __init__(self):
        self.email_host = "smtp.mail.com"
        self.email_port = 587
        self.sms_api_key = "12345-ABCDE"
        self.push_secret = "FIREBASE_SECRET_999"

    def send_notification(self, notif_type, message, target, attachment=None):
        print(
            f"Sistem logu: '{notif_type}' tipi için gönderim süreci başlatildi ")

        if notif_type == "Email":
            if "@" not in target:
                print("Hata: Gecersiz e-posta adresi formati \n")
                return False

            print(f"[{self.email_host}:{self.email_port}] adresine baglaniliyor")
            print(f"Email Gönderiliyor -> Alici: {target}\nİçerik: {message}")
            if attachment:
                print(f"Ek dosya eklendi: {attachment}")
            print("Durum: Basarili.\n")
            return True

        elif notif_type == "SMS":
            if len(message) > 160:
                print("Hata: SMS 160 karakterden uzun olamaz\n")
                return False
            if not str(target).startswith("+90"):
                print("Sadece Türkiye (+90) numaralarina SMS atilabilir!\n")
                return False

            print(
                f"API Key ({self.sms_api_key}) ile SMS servisine yetkilendirme yapiliyor ")
            print(f"SMS Gönderiliyor Tel: {target}\nİçerik: {message}")
            if attachment:
                print("Uyari SMSe ek dosya eklenemez eklenti yoksayildi")
            print("Durum: Basarili\n")
            return True

        elif notif_type == "Push":
            if not target:
                print("Hata Cihaz tokeni eksik\n")
                return False

            print(
                f"Firebase secret ({self.push_secret}) ile baglanti kuruluyor")
            print(f"Push Gönderiliyor  Cihaz: {target}\nİçerik: {message}")
            print("Durum: Başarili.\n")
            return True

        else:
            print(
                f"Kritik Hata: '{notif_type}' sistem tarafindan desteklenmiyor\n")
            return False


if __name__ == "__main__":
    manager = NotificationManager()

    manager.send_notification(
        "Email", "Faturaniz ektedir.", "musteri@sirket.com", attachment="fatura_pdf")
    manager.send_notification("SMS", "Kargonuz yola cikti.", "+905551234567")

    manager.send_notification("Email", "Merhaba", "hatali-mail-adresi")
    manager.send_notification(
        "SMS", "Kisa mesaj", "+12025550123", attachment="gizli_dosya.zip")
