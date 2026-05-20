from abc import ABC, abstractmethod
from typing import Callable, Dict, List


class Notification(ABC):
    @abstractmethod
    def send(self, message: str, target: str, attachment: str = None) -> bool:
        pass


class EmailNotification(Notification):
    def __init__(self):
        self.host = "smtp.mail.com"
        self.port = 587

    def send(self, message: str, target: str, attachment: str = None) -> bool:
        print(f"[{self.host}:{self.port}] Baglanti kuruldu")
        print(f"Email -> {target} | Mesaj: {message}")
        return True


class SMSNotification(Notification):
    def send(self, message: str, target: str, attachment: str = None) -> bool:
        print(f"SMS -> {target} | Mesaj: {message}")
        return True


class PushNotification(Notification):
    def send(self, message: str, target: str, attachment: str = None) -> bool:
        print(f"Push -> {target} | Mesaj: {message}")
        return True


class WhatsAppClient:
    def push_message(self, text: str, contact_number: str):
        print(f"WhatsApp {contact_number}: {text}")
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


class NotificationFactory:
    def __init__(self):
        self._providers: Dict[str, Callable[[], Notification]] = {}

    def register_provider(self, notif_type: str, provider: Callable[[], Notification]):
        self._providers[notif_type] = provider

    def create_notification(self, notif_type: str) -> Notification:
        if notif_type not in self._providers:
            raise ValueError(f"Desteklenmeyen tip: {notif_type}")
        return self._providers[notif_type]()


class EventManager:
    def __init__(self):
        self._listeners: Dict[str, List[Callable]] = {}

    def subscribe(self, event_type: str, listener: Callable):
        if event_type not in self._listeners:
            self._listeners[event_type] = []
        self._listeners[event_type].append(listener)

    def notify(self, event_type: str, data: dict):
        for listener in self._listeners.get(event_type, []):
            listener(data)


def audit_logger_listener(data: dict):
    print(f"[KAYIT] Islem: {data['event']} | Hedef: {data['target']} | Sonuc: {data['status']}")


def analytics_listener(data: dict):
    print("[ISTATISTIK] Yeni bildirim islemi tamamlandi")


class Command(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass


class SendNotificationCommand(Command):
    def __init__(self, notification: Notification, message: str, target: str, event_manager: EventManager):
        self.notification = notification
        self.message = message
        self.target = target
        self.event_manager = event_manager

    def execute(self) -> None:
        try:
            result = self.notification.send(self.message, self.target)
            self.event_manager.notify(
                "notification_sent",
                {
                    "event": "send",
                    "target": self.target,
                    "status": result
                }
            )
        except Exception as e:
            self.event_manager.notify(
                "notification_failed",
                {
                    "event": "send",
                    "target": self.target,
                    "status": "Error",
                    "error": str(e)
                }
            )


class NotificationInvoker:
    def __init__(self):
        self._commands: List[Command] = []

    def add_command(self, command: Command):
        self._commands.append(command)

    def execute_commands(self):
        for command in self._commands:
            command.execute()
        self._commands.clear()


if __name__ == "__main__":
    event_manager = EventManager()

    event_manager.subscribe("notification_sent", audit_logger_listener)
    event_manager.subscribe("notification_sent", analytics_listener)

    factory = NotificationFactory()

    factory.register_provider("Email", EmailNotification)
    factory.register_provider("SMS", SMSNotification)
    factory.register_provider("WhatsApp", WhatsAppAdapter)

    wa_notif = factory.create_notification("WhatsApp")
    sms_notif = EncryptedNotification(factory.create_notification("SMS"))

    invoker = NotificationInvoker()

    cmd1 = SendNotificationCommand(
        wa_notif,
        "Siparis Alindi",
        "+905551234567",
        event_manager
    )

    cmd2 = SendNotificationCommand(
        sms_notif,
        "Gizli Kod: 9876",
        "+905559998877",
        event_manager
    )

    invoker.add_command(cmd1)
    invoker.add_command(cmd2)

    print("--- Bildirimler Gonderiliyor ---\n")

    invoker.execute_commands()