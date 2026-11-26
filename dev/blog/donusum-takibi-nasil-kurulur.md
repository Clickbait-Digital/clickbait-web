---
baslik: Dönüşüm takibi kurmadan reklam vermeyin: Google Ads ve Meta için 6 adımlık kurulum
title: Dönüşüm Takibi Nasıl Kurulur? Google Ads ve Meta | Clickbait
description: Dönüşüm takibi nedir, neden reklamdan önce kurulmalı? Form, telefon ve WhatsApp tıklamalarını Google Ads, GA4 ve Meta'da ölçmek için 6 adım ve sık yapılan hatalar.
ozet: Reklam paneli size tıklama sayısını gösterir, ama hangi tıklamanın müşteriye dönüştüğünü söylemez. Dönüşüm takibi olmadan verilen reklam, bütçenin nereye gittiğini bilmeden harcanır. Form, telefon ve WhatsApp taleplerini ölçmek için 6 adımlık kurulumu anlattık.
tarih: 2026-11-26
kume: dijital-pazarlama
etiket: DİJİTAL PAZARLAMA
kapak: 6 adımda kurulum
simge: hedef
kisa_cevap: Dönüşüm takibi, reklama tıklayan kişinin sitenizde form doldurma, arama yapma, WhatsApp'tan yazma ya da satın alma gibi sizin için değerli bir işi yapıp yapmadığını ölçer. Kurmak için önce hangi işlerin dönüşüm sayılacağına karar verin, Google Analytics 4 ve Google etiketini kurun, form, telefon ve WhatsApp tıklamalarını etkinlik olarak tanımlayın, bunları Google Ads ve Meta'ya dönüşüm olarak bağlayın, çerez onayını doğru yapılandırın ve reklamı açmadan önce her dönüşümü test edin.
---
Bir işletme sahibi reklam panelini açtığında genellikle şu rakamları görür: gösterim, tıklama, tıklama başına maliyet. Bu rakamlar reklamın görüldüğünü ve tıklandığını söyler; ama asıl sorunun cevabını vermez: **Bu reklamdan kaç müşteri geldi?**

Dönüşüm takibi bu soruyu cevaplayan altyapıdır. Kurulmadan verilen reklamda hangi kelimenin, hangi kampanyanın ya da hangi görselin işe yaradığını bilemezsiniz; bütçeyi artırma ya da kesme kararlarını tahminle verirsiniz. Bu yazıda dönüşüm takibinin ne olduğunu, neden reklamdan önce kurulması gerektiğini ve 6 adımda nasıl kurulacağını anlattık.

## Dönüşüm nedir?

Dönüşüm, ziyaretçinin sitenizde sizin için değerli bir işi tamamlamasıdır. Bu iş işletmeden işletmeye değişir:

- **Form gönderimi:** Teklif, randevu ya da geri arama formu.
- **Telefon araması:** Sitedeki numaraya dokunarak arama ya da reklamdaki arama düğmesi.
- **WhatsApp mesajı:** "WhatsApp'tan yazın" düğmesine tıklama.
- **Satın alma:** E-ticaret sitesinde tamamlanan sipariş.
- **Diğer:** Katalog indirme, bülten kaydı, yol tarifi alma.

Reklamın amacı tıklama değil, bu işlerden biridir. Dönüşüm takibi de reklam paneline "bu tıklama bir talebe dönüştü" bilgisini geri gönderir.

## Neden reklamdan önce kurulmalı?

**Hangi harcamanın işe yaradığını görürsünüz.** İki kampanyanız aynı parayı harcıyor olabilir; biri on talep getirirken diğeri hiç getirmeyebilir. Dönüşüm verisi olmadan ikisi panelde aynı görünür.

**Otomatik teklif stratejileri doğru çalışır.** Google Ads ve Meta'nın "dönüşümleri en üst düzeye çıkar" gibi otomatik stratejileri, kimin talep bıraktığına bakarak öğrenir. Dönüşüm verisi yoksa ya da yanlışsa, sistem yanlış kişilere reklam göstermeyi öğrenir.

**Bütçe kararlarınız rakama dayanır.** [Google Ads bütçesi nasıl belirlenir?](/blog/google-ads-butcesi-nasil-belirlenir/) yazımızda anlattığımız hesabın temeli talep başına maliyettir. Bu rakamı ancak dönüşüm takibiyle öğrenebilirsiniz.

**Geriye dönük veri kurtarılamaz.** Takibi reklam başladıktan bir ay sonra kurarsanız, o ayın hangi talebinin hangi reklamdan geldiğini öğrenmenin yolu yoktur. Bu yüzden sıralama her zaman önce takip, sonra reklamdır.

## 1. Hangi işlerin dönüşüm sayılacağına karar verin

Kuruluma başlamadan önce bir kâğıda işletmeniz için değerli olan işleri yazın ve bunları ikiye ayırın:

- **Ana dönüşümler:** Doğrudan müşteri adayı getiren işler (form, arama, WhatsApp mesajı, satın alma). Reklam sistemlerinin optimize edeceği hedefler bunlardır.
- **Yardımcı dönüşümler:** Fikir veren ama tek başına müşteri anlamına gelmeyen işler (fiyat sayfasını görüntüleme, katalog indirme). Bunlar ölçülür ama otomatik teklif stratejilerinin hedefi yapılmaz.

En sık yapılan hata, "iletişim sayfasını görüntüleme" gibi zayıf işleri ana dönüşüm yapmaktır. Sistem bu durumda sayfaya bakıp çıkan kişileri bulmayı öğrenir.

## 2. Google Analytics 4 ve Google etiketini kurun

Google Analytics 4 (GA4), sitenizdeki ziyaretçi hareketlerini ölçen ücretsiz araçtır. Sitenize GA4'ün Google etiketini (gtag.js) doğrudan ya da Google Etiket Yöneticisi (Google Tag Manager) üzerinden eklersiniz. Etiket Yöneticisi, ileride yeni ölçümler eklerken her seferinde sitenin koduna dokunmadan çalışmanızı sağladığı için çoğu durumda daha pratiktir.

WordPress, Shopify, Ticimax ya da İdeasoft gibi altyapılarda GA4 bağlantısı çoğunlukla ayarlar menüsünden ya da bir eklentiyle yapılır. Altyapı seçiminin ölçüme etkisini [WooCommerce mi, hazır e-ticaret altyapısı mı?](/blog/woocommerce-mi-hazir-e-ticaret-altyapisi-mi/) yazımızda da ele aldık.

## 3. Form, telefon ve WhatsApp tıklamalarını etkinlik olarak tanımlayın

GA4 sayfa görüntülemelerini kendiliğinden ölçer, ama "form başarıyla gönderildi" ya da "telefon numarasına dokunuldu" bilgisini sizin tanımlamanız gerekir:

- **Form:** Etkinliği, form gerçekten başarıyla gönderildiğinde tetikleyin; "Gönder" düğmesine basılmasıyla değil. Boş ya da hatalı form da düğmeye basılarak gönderilmeye çalışılır. Başarı sonrası bir teşekkür sayfasına yönlendirme yapılıyorsa, bu sayfanın görüntülenmesi de kullanılabilir; ancak sayfanın arama motorlarından ya da doğrudan adresle açılmadığından emin olun.
- **Telefon:** `tel:` ile başlayan bağlantılara yapılan tıklamaları etkinlik olarak ölçün. Bu, aramanın gerçekleştiğini değil, aramanın başlatıldığını gösterir; raporlarken bu farkı akılda tutun.
- **WhatsApp:** `wa.me` ya da `api.whatsapp.com` bağlantılarına yapılan tıklamaları ayrı bir etkinlik olarak ölçün.

Ardından GA4'te bu etkinlikleri **önemli etkinlik** (key event) olarak işaretleyin. Kendi sitemizde de aynı yapıyı kullanıyoruz: başarılı form gönderimi `generate_lead`, telefon ve WhatsApp tıklamaları ayrı bir iletişim etkinliği olarak ölçülüyor.

## 4. Dönüşümleri Google Ads ve Meta'ya bağlayın

**Google Ads:** İki yol vardır. GA4 hesabınızı Google Ads'e bağlayıp önemli etkinlikleri dönüşüm olarak içe aktarabilir ya da Google Ads'in kendi dönüşüm etiketini kurabilirsiniz. Hangisini seçerseniz seçin, aynı işi iki kez saymamak için tek bir kaynağı ana dönüşüm yapın. Reklamdaki arama düğmesinden gelen aramalar için Google Ads'in arama dönüşümlerini de ayrıca açabilirsiniz.

Formda e-posta ya da telefon alıyorsanız **gelişmiş dönüşümler** (enhanced conversions) özelliğini de değerlendirin. Bu özellik, formdaki bilgiyi şifrelenmiş (hash'lenmiş) olarak Google'a göndererek eşleşmeyi iyileştirir. Kişisel veri işlendiği için aydınlatma metninizde ve çerez politikanızda karşılığı olmalıdır.

**Meta (Instagram ve Facebook reklamları):** Sitenize Meta pikselini kurun ve aynı dönüşümleri standart etkinliklerle (örneğin `Lead`, `Contact`, `Purchase`) tanımlayın. Altyapınız destekliyorsa, tarayıcı engellemelerinden daha az etkilenen Dönüşümler API'sini (Conversions API) de piksel ile birlikte kullanmak ölçümü güçlendirir. Instagram reklamı tarafını [Instagram reklamı nasıl verilir?](/blog/instagram-reklami-nasil-verilir/) yazımızda adım adım anlattık.

## 5. Çerez onayını doğru yapılandırın

Ölçüm etiketleri çerez kullanır ve Türkiye'de KVKK açısından analiz ve reklam çerezleri için genellikle ziyaretçinin açık rızası aranır. Bu yüzden sitenizde bir çerez onay bandı olmalı ve etiketler bu onaya göre çalışmalıdır. Bizim sitemizde de Google Analytics yalnızca ziyaretçi onay verdikten sonra yüklenir.

Bunun pratik bir sonucu var: Onay vermeyen ziyaretçilerin dönüşümleri ölçülmez ya da eksik ölçülür. Google'ın **onay modu** (Consent Mode) gibi araçlar bu boşluğun bir kısmını modellemeye çalışır. Raporlarınızdaki dönüşüm sayısının, telefonunuza ve e-postanıza gelen gerçek talep sayısından biraz düşük çıkması bu yüzden normaldir. Çerez metninizin içeriğini hukuk danışmanınızla birlikte netleştirin.

## 6. Reklamı açmadan önce test edin

Kurulum bittiğinde her dönüşümü kendiniz deneyin:

- Formu gerçek bir test talebiyle doldurun ve GA4'ün **gerçek zamanlı** raporunda etkinliği görün.
- Telefondan siteye girip numaraya ve WhatsApp düğmesine dokunun.
- Google'ın **Tag Assistant** aracıyla etiketlerin doğru sayfada ve doğru anda tetiklendiğini kontrol edin; Meta tarafında Etkinlik Yöneticisi'ndeki test aracını kullanın.
- Bir dönüşümün iki kez sayılmadığından emin olun (örneğin hem form etkinliği hem teşekkür sayfası ana dönüşüm olarak işaretlenmişse).

Reklam panelinde dönüşümlerin görünmesi birkaç saat sürebilir. Test sırasında sorun çıkmadıysa reklamı açabilirsiniz.

## Sık yapılan hatalar

- **Sayfa görüntülemeyi dönüşüm saymak:** Ana sayfa ya da iletişim sayfası görüntülemesi talep değildir.
- **Aynı işi iki kez saymak:** GA4'ten içe aktarılan dönüşümle Google Ads etiketinin aynı formu ayrı ayrı sayması.
- **Düğme tıklamasını form gönderimi saymak:** Hatalı ya da yarım kalan formlar da dönüşüm gibi görünür.
- **Kurup bir daha bakmamak:** Site yenilendiğinde, form değiştiğinde ya da tema güncellendiğinde etiketler sessizce bozulabilir. Site yenilerken dikkat edilecekleri [web sitenizi yenilerken Google sıralamanızı korumak](/blog/web-sitesi-yenilerken-google-siralamasini-korumak/) yazımızda anlattık; ölçüm etiketleri de bu kontrol listesinin parçası olmalı.
- **Talebin kalitesine bakmamak:** On form gelip hiçbiri müşteriye dönüşmüyorsa, sorun reklamda değil hedeflemede ya da teklifte olabilir. Hangi talebin satışa dönüştüğünü kendi kayıtlarınızda tutmak, reklam verisini anlamlı kılar.

## Özetle

- Önce hangi işlerin ana dönüşüm sayılacağına karar verin; zayıf işleri ana hedef yapmayın.
- GA4 ve Google etiketini kurun; form, telefon ve WhatsApp tıklamalarını önemli etkinlik olarak tanımlayın.
- Dönüşümleri Google Ads ve Meta'ya bağlayın; aynı işi iki kez saymayın.
- Çerez onayını doğru yapılandırın ve raporların gerçek talep sayısından biraz düşük çıkabileceğini bilin.
- Reklamı açmadan önce her dönüşümü kendiniz test edin.

Reklam mı, SEO mu kararını henüz vermediyseniz [Google Ads mi SEO mu?](/blog/google-ads-mi-seo-mu/) yazımız, dijital pazarlamaya küçük bir bütçeyle başlıyorsanız [küçük işletmeler için dijital pazarlama](/blog/kucuk-isletmeler-icin-dijital-pazarlama/) rehberimiz işinize yarar.

> Clickbait Dijital olarak reklam yönetimine dönüşüm takibiyle başlıyoruz: hangi işlerin ölçüleceğini sizinle birlikte belirliyor, GA4, Google Ads ve Meta ölçümünü kuruyor, reklamı açmadan önce her dönüşümü test ediyoruz. Mevcut bir reklam hesabını devraldığımızda da ilk kontrol ettiğimiz şey ölçümdür. Ayrıntılar için [Ankara Google Ads ajansı](/ankara-google-ads-ajansi/) sayfamıza bakabilirsiniz. Çayyolu'ndaki ofisimizde yüz yüze görüşebilir, Türkiye'nin her yerinden online çalışabiliriz.
