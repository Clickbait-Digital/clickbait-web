---
baslik: Web sitenizi yenilerken Google sıralamanızı nasıl korursunuz? 8 adımlık kontrol listesi
title: Site Yenilerken Google Sıralaması Nasıl Korunur? | Clickbait
description: Web sitenizi yenilerken Google sıralamanızı kaybetmemek için 8 adım: eski adreslerin listesi, 301 yönlendirmeler, içerik, yayın günü testleri ve takip.
ozet: Yeni bir site yıllar içinde kazanılan Google sıralamalarını birkaç gün içinde kaybettirebilir. Eski adresleri kaydetmekten 301 yönlendirmelere ve yayından sonraki takibe kadar, site yenilerken izlemeniz gereken 8 adımı topladık.
tarih: 2026-10-22
kume: web-tasarim
etiket: WEB TASARIM
kapak: 8 adımda güvenli geçiş
simge: kalkan
kisa_cevap: Web sitenizi yenilerken Google sıralamanızı korumak için eski sitenin ziyaretçi getiren sayfalarını kaydedin, tüm eski adreslerin listesini çıkarın, her eski adresi yeni karşılığıyla eşleştirin ve 301 kalıcı yönlendirme kurun. Sıralanan içerikleri koruyun, test ortamı ayarlarını temizleyin, yayın günü yönlendirmeleri test edip site haritasını gönderin ve sonraki haftalarda Search Console'u izleyin.
---
Yeni bir web sitesi çoğu zaman eskisinden daha hızlı ve daha güzeldir. Ama yenileme dikkatsiz yapılırsa, eski sitenin yıllar içinde Google'da kazandığı sıralamalar birkaç gün içinde kaybolabilir. Bunun en sık nedeni tasarım değil, **adresler**dir: Google'ın tanıdığı eski sayfalar artık açılmaz, ziyaretçiler hata sayfasına düşer ve Google bu sayfaların yerine neyin geldiğini bilemez.

Ekim 2026'da kendi sitemizi WordPress'ten daha hızlı, statik bir altyapıya taşırken aşağıdaki adımları izledik. Eski sitedeki hizmet, referans, iletişim ve KVKK sayfalarının her birini yeni karşılığına bağladık; örneğin eski /ankara-web-tasarim/ adresine gelen ziyaretçi artık otomatik olarak yeni [Ankara web tasarım](/web-tasarim/) sayfamıza gidiyor.

## 1. Eski sitenin mevcut durumunu kaydedin

Yenilemeye başlamadan önce eski sitenin neyi iyi yaptığını bilmeniz gerekir. Google Search Console'da **Performans** raporunu açın, son 12 ayı seçin ve **Sayfalar** ile **Sorgular** sekmelerini dışa aktarın. Böylece hangi sayfaların Google'dan ziyaretçi getirdiğini ve hangi aramalarda göründüğünüzü kayıt altına alırsınız. Search Console'daki **Bağlantılar** raporu da başka sitelerin en çok hangi sayfalarınıza bağlantı verdiğini gösterir. Bu sayfalar yenilemede en dikkatli taşınması gerekenlerdir.

## 2. Eski adreslerin tam listesini çıkarın

Eski sitenin site haritası (genellikle /sitemap.xml) iyi bir başlangıçtır ama her zaman eksiksiz değildir. Search Console'daki sayfa listesini ve bir tarama aracıyla bulduğunuz adresleri de ekleyin. Blog yazılarını, kategori sayfalarını, PDF dosyalarını ve görselleri unutmayın; başka siteler bunlara da bağlantı vermiş olabilir.

## 3. Her eski adresi yeni karşılığıyla eşleştirin

İki sütunlu bir tablo hazırlayın: solda eski adres, sağda yeni sitede ona en yakın sayfa. Hizmet sayfası hizmet sayfasına, yazı yazıya gitmelidir. Yeni sitede birebir karşılığı olmayan bir sayfa için konuya en yakın sayfayı seçin.

Kolay ama yanlış olan yol, bütün eski adresleri ana sayfaya yönlendirmektir. Google ilgisiz bir sayfaya yapılan bu tür yönlendirmeleri "bulunamadı" gibi değerlendirebilir ve eski sayfanın gücü yeni siteye taşınmaz.

## 4. 301 kalıcı yönlendirme kurun

Eşleştirme tablosundaki her satır için sunucuda **301 (kalıcı) yönlendirme** kurun. 301, Google'a "bu sayfa kalıcı olarak taşındı" der ve eski sayfanın sıralama sinyallerinin yeni adrese aktarılmasını sağlar. Geçici yönlendirme (302) ise Google'a taşınmanın kalıcı olmadığını söyler; kalıcı bir taşıma için 301 kullanın.

- Yönlendirmeler zincir oluşturmamalı: eski adres doğrudan son adrese gitmeli, araya başka adresler girmemeli.
- Sitenin http://, https://, www'li ve www'siz hâllerinden yalnızca biri açılmalı, diğerleri ona yönlenmeli.
- Google, yönlendirmeleri mümkün olduğunca uzun, en az bir yıl yerinde tutmayı önerir.
- Alan adınız da değişiyorsa, Search Console'daki **Adres değişikliği** aracını kullanarak Google'a ayrıca haber verin.

## 5. Sıralanan içerikleri ve başlıkları koruyun

Yeni tasarımda metinleri kısaltmak cazip gelebilir. Ama 1. adımda ziyaretçi getirdiğini gördüğünüz sayfaların içeriğini, sayfa başlığını (title), açıklamasını ve ana başlığını (H1) büyük ölçüde koruyun. Google o sayfayı içeriği yüzünden sıralıyordu; içerik kaybolursa sıralamanın da korunması zorlaşır. Geliştirmek istiyorsanız metni çıkarmak yerine eklemeyi tercih edin.

## 6. Yayından önce test ortamı ayarlarını temizleyin

Yeni site genellikle önce bir test adresinde hazırlanır ve orada Google'ın görmemesi için engellenir. Bu engellerin yayına taşınması en sık yaşanan ve en pahalı hatalardan biridir:

- robots.txt dosyasında siteyi tamamen kapatan "Disallow: /" satırı kalmamalı.
- Sayfalarda "noindex" etiketi kalmamalı.
- Kanonik etiketler test adresini değil, gerçek adresleri göstermeli.
- Site içindeki bağlantılar yönlendirmeye değil, doğrudan yeni adreslere gitmeli.

Bu kontrollerin ayrıntısını [teknik SEO kontrol listesi](/blog/teknik-seo-kontrol-listesi/) yazımızda bulabilirsiniz.

## 7. Yayın günü yönlendirmeleri test edin ve Google'a haber verin

Yeni site yayına girdiği gün eşleştirme tablosundaki adresleri tek tek açın: her biri tek adımda doğru sayfaya gitmeli. Ardından:

1. Yeni site haritasını Search Console'a gönderin.
2. En önemli sayfalar için Search Console'da **URL denetimi** yapıp "Dizine eklenmesini iste" deyin.
3. Bing Webmaster Tools kullanıyorsanız yeni sayfaları IndexNow ile bildirin.
4. Google İşletme Profili'nizdeki, sosyal medya hesaplarınızdaki ve rehber sitelerdeki web sitesi bağlantılarını kontrol edin.
5. Google Analytics ve dönüşüm ölçümünün yeni sitede çalıştığından emin olun.

## 8. Sonraki haftalarda Search Console'u izleyin

Yayından sonraki ilk haftalarda sıralamalarda bir miktar dalgalanma görmek normaldir; Google'ın yeni adresleri tarayıp değerlendirmesi zaman alır. Bu süreçte haftada bir Search Console'a bakın:

- **Sayfa sayısı** raporunda "Bulunamadı (404)" hatası veren eski adresler varsa eşleştirme tablosuna ekleyip yönlendirin.
- 1. adımda kaydettiğiniz önemli sayfaların ve aramaların yeni sitede nasıl gittiğini karşılaştırın.
- Birkaç hafta sonra hâlâ belirgin bir düşüş varsa yönlendirmeleri ve o sayfaların içeriğini yeniden kontrol edin.

## Kısaca

- Önce eski sitenin neyi iyi yaptığını kaydedin.
- Her eski adresi en yakın yeni karşılığına 301 ile yönlendirin, toptan ana sayfaya göndermeyin.
- Ziyaretçi getiren sayfaların içeriğini ve başlıklarını koruyun.
- Test ortamından kalan engelleri temizleyin.
- Yayın günü her yönlendirmeyi test edin, site haritasını gönderin.
- İlk haftalarda Search Console'u düzenli izleyin.

Web sitesi yaptırmadan önce sorulması gereken diğer konuları [Ankara'da web sitesi yaptırırken dikkat edilmesi gereken 10 şey](/blog/ankara-web-sitesi-yaptirirken-dikkat-edilmesi-gerekenler/) yazımızda topladık.

> Clickbait Dijital olarak site yenileme projelerine eski sitenin Search Console verilerini inceleyerek başlıyor, her eski adresi yeni karşılığına yönlendiriyor ve yayından sonraki haftalarda sonuçları izliyoruz. Ayrıntılar için [Ankara web tasarım](/web-tasarim/) sayfamıza, yayından sonraki Google çalışmaları için [SEO ajansı olarak neler yaptığımızı](/ankara-seo/) anlattığımız sayfaya bakabilirsiniz. Çayyolu'ndaki ofisimizde yüz yüze görüşebilir, Türkiye'nin her yerinden online çalışabiliriz.
