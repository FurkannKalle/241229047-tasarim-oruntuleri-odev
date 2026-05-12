# 1.YARATIMSAL ÖRÜNTÜLER 
Factory Method Uygulandı.
Nerede: notification_system.py Dosyasında NotificationFactory classında kullanıldı.
Neden: Bildirim tipleri tek bir sınıf içerisindeydi ve if-else bloklarıyla karmaşık bir yapıyla kontrol ediliyordu.Hepsini farklı birimlere ayırmamız gerekliydi.
Ne Kazandık ? : Yeni bir bildirim tipi eklenmek istendiği zaman sadece yeni bir class açmamız yeterli,Ayrıca her classlar sadece kendine ait prensipler ile dolduruldu tek sorumluluk prensibine uygun bir yapı oluşturuldu.


### 1.Faz UML Diyagramları 

**Önceki Durum (Spagetti Kod - God Class):**
```mermaid
classDiagram
    class NotificationManager {
        +email_host: str
        +sms_api_key: str
        +push_secret: str
        +send_notification(notif_type, message, target, attachment) bool
    }
```

**Sonraki Durum (Factory Method Uygulanmış Hali):**
```mermaid
classDiagram
    class Notification {
        <<interface>>
        +send(message, target, attachment) bool
    }
    class EmailNotification {
        +host: str
        +port: int
        +send(message, target, attachment) bool
    }
    class SMSNotification {
        +api_key: str
        +send(message, target, attachment) bool
    }
    class PushNotification {
        +secret: str
        +send(message, target, attachment) bool
    }
    class NotificationFactory {
        +create_notification(notif_type: str) Notification
    }

    Notification <|-- EmailNotification
    Notification <|-- SMSNotification
    Notification <|-- PushNotification
    NotificationFactory ..> Notification : creates
```