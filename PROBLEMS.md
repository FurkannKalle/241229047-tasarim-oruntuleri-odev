# FAZ 0 Benim Bulduğum Sorunlar:
1. Açık Kapalı Prensibi Sorunu : Yeni bir bildirim ekleyeceğimiz zaman if-else yapılarının değiştirilmesi gerekli bunu yapmak hem performans açısından hem de koda müdahale açısından büyük zorluk içeriyor.
2. Tek Sorumluluk Prensibi Sorunu : send_notification birden çok işlem yapıyor bu sınıfa da müdahale etmek ve bir kodu değiştirmek çok zorlayacaktır düzgün bir yapıda her sınıf tek bir işlem gerçekleştirmesi gerekir.
3. Gereksiz Parametre Bağımlılık Sorunu : Yalnızca E-posta için gerekli olan attachment parametresi diğer türlerde de kullanılıyor bu da kodun gereksiz şekilde şişmesine ve performans kaybına neden oluyor.
4. Sabit Bağımlılıklar Sorunu : API bilgileri ve servis adresleri doğrudan sınıf içine gömüldüğü için yapı esnek değildir bu sebeple birim test yazımı zorlaşmaktadır.
5. Önemli Değerleri Değişkene Bağlamadan Direkt Kodun İçine Gömülmesi Sorunu: SMS uzunluğu için `160` gibi değerler birer konfigürasyon değişkeni olmak yerine kodun if bloklarının içine doğrudan gömülmüş Bunlarla ilgili bir değişiklik yapacağımız zaman direkt kodun içinden bulmak ve değiştirmek bizi zorlayacaktır.

# Ai Bulduğu Sorunlar Ve İkisinin Arasındaki Farklar

Ai Cevapları : 
Hardcoded Credentials — API key ve şifreler doğrudan kod içine gömülmüş, güvenlik riski oluşturuyor.
SRP İhlali — send_notification tek başına validasyon, yönlendirme ve gönderim yapıyor.
OCP İhlali — Yeni kanal eklemek için mevcut if/elif zincirine müdahale etmek gerekiyor.
Dağınık Validasyon — Her kanalın validasyonu gönderim mantığıyla iç içe geçmiş.
print ile Loglama — Log seviyesi yok, test edilmesi zor, çıktı yönlendirilemiyor.
Tutarsız Attachment Davranışı — SMS'te sessizce yoksayılıyor, Push'ta hiç ele alınmıyor.


Ai ile Benim Bulduğum Sorunlar Arasındaki Farklar: 
Hardcoded Credentials konusunda AI daha çok güvenlik riskleri ve olası zafiyetler üzerinde durmuş.
Önemli değerlerin değişkenlere atanmak yerine doğrudan kod içine gömülmesi sorununa AI hiç değinmemiş bu da aramızdaki farklardan biridir.
Print ile loglama sorununu ben fark etmemiştim, ancak AI bu detayı tespit etmiş bu da aramızdaki başka bir farktır.
Diğer kalan sorunlara ise ikimiz de değinmişiz yani bunlar ortak olarak tespit ettiğimiz problemlerdir.