# Sistem Mimari Diyagramı Final

Aşağıdaki diyagram spagetti koddan kurtarılarak Tasarım Örüntüleri ile yeniden yazılan bildirim sisteminin son mimarisini göstermektedir.


```mermaid
classDiagram
    class NotificationFactory {
        +create_notification(type)
    }
    class NotificationInvoker {
        +add_command(cmd)
        +execute_commands()
    }
    class SendNotificationCommand {
        +execute()
    }
    class EventManager {
        +subscribe(event, listener)
        +notify(event, data)
    }
    
    NotificationFactory --> SendNotificationCommand : Kullanılacak bildirim servisini üretir
    NotificationInvoker o-- SendNotificationCommand : Komutları kuyrukta tutar
    SendNotificationCommand --> EventManager : İşlem bitince olay tetikler
    EventManager --> "Listeners (Log/Analytics)" : Dinleyicilere haber verir
```