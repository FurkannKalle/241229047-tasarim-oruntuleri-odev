# 3. Faz Code Review

Ai ile tartışma sonucu ilerleme yönümüz:
Ai ile 30 dk'lık pair programming sürecinde ilk başta Strategy örüntüsünde karar kıldık daha sonra bunun uygun olmadığına karar vererek ileriki süreçlerde mimariyi daha ileri seviyeye taşıyarak Command ve Observer örüntülerini birleştirdik.Bildirim gönderme işlemleri nesneye dönüştürdük ve bir invoker içinde kuyruğa aldık Observer ile log ve Analitik servisleri oluşturduk.

Ai olmadan bu faz ne kadar sürerdi ? :
Ai kullanmasaydık bu faz en az 2-3 saatimi alırdı çünkü bu yapıyı sorunsuz kurgulamak zor bir işlem.

Ai beni nereden yanılttı ? :
Ai ilk etapta bildirim gönderim hızı açısından Strategy örünütüsünü önerdi fakat bildirimlerin bir kuyruğa alınarak işlenmesi daha doğru bir işlem olduğu için Command örüntüsünü uyguladık ve sistem daha sağlam bir zemine oturdu.



