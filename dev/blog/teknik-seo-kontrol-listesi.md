---
baslik: Teknik SEO kontrol listesi: 12 madde ve e-ticaret siteleri için ek kontroller
title: Teknik SEO Kontrol Listesi: 12 Madde ve E-ticaret | Clickbait
description: Teknik SEO kontrol listesi: dizine eklenmeden hıza, yönlendirmelerden yapılandırılmış veriye 12 madde ve e-ticaret siteleri için ek kontroller.
ozet: İçerik ne kadar iyi olursa olsun, Google sitenizi düzgün tarayıp anlayamıyorsa sıralama gelmez. Sitenizde kendi başınıza kontrol edebileceğiniz 12 teknik SEO maddesini, nereye bakacağınızla birlikte topladık.
tarih: 2026-10-21
guncelleme: 2026-10-27
kume: dijital-pazarlama
etiket: DİJİTAL PAZARLAMA
kapak: 12 maddelik kontrol
simge: kalkan
kisa_cevap: Teknik SEO, Google'ın sitenizi sorunsuz tarayıp dizine eklemesi ve doğru anlaması için yapılan altyapı çalışmalarıdır. Temel kontroller şunlardır: sayfaların dizinde olması, site haritası ve robots.txt, HTTPS, mobil uyum, sayfa hızı, kanonik adresler, yönlendirmeler, kırık bağlantılar, başlık ve açıklamalar, tek H1, yapılandırılmış veri ve iç bağlantılar. E-ticaret sitelerinde bunlara ek olarak filtre ve sıralama adresleri, stokta olmayan ürünler, ürün yapılandırılmış verisi, kategori sayfalaması ve kopya ürün açıklamaları kontrol edilmelidir.
---
Bir sitenin Google'da üst sıralara çıkması için iyi içerik gerekir, ama tek başına yetmez. Google önce sitenizi **taramalı**, sonra **dizine eklemeli** ve en sonunda ne anlattığını **anlamalı**. Bu üç adımdan birinde sorun varsa en iyi yazılmış sayfa bile görünmez. **Teknik SEO**, bu adımların sorunsuz işlemesi için yapılan altyapı çalışmalarının adıdır.

Ekim 2026'da Ankara'daki 101 işletme sitesini incelediğimiz [araştırmamızda](/blog/ankara-isletme-siteleri-arastirmasi-2026/) sitelerin %26'sında ana başlık (H1) yoktu, %42'sinde işletme bilgisini Google'a anlatan yapılandırılmış veri bulunmuyordu ve %87'sinde sayfanın ana içeriği telefonda 4 saniyeden geç yükleniyordu. Bunların hepsi teknik SEO konusu ve çoğu kolayca düzeltilebilir.

Aşağıdaki 12 maddeyi kendi sitenizde kontrol edebilirsiniz; e-ticaret siteniz varsa yazının sonundaki ek kontrollere de bakın. Çoğu için ücretsiz olan **Google Search Console** ve **PageSpeed Insights** yeterli.

## 1. Sayfalarınız Google'ın dizininde mi?

Google'da görünmeyen bir sayfa hiçbir aramada sıralanamaz. Search Console'da **Sayfa sayısı** (dizine ekleme) raporu, hangi sayfaların dizinde olduğunu ve olmayanların nedenini gösterir. Tek bir sayfayı kontrol etmek için üstteki arama kutusuna adresini yazıp **URL denetimi** yapabilirsiniz. Yeni ya da değişen önemli sayfalar için buradan "Dizine eklenmesini iste" diyebilirsiniz.

## 2. Site haritası ve robots.txt doğru mu?

- **Site haritası (sitemap.xml):** Sitenizdeki önemli sayfaların listesidir. Search Console'a gönderilmiş olmalı ve yalnızca gerçekten var olan, dizine eklenmesini istediğiniz sayfaları içermelidir.
- **robots.txt:** Arama motorlarına hangi bölümleri taramamaları gerektiğini söyler. Yanlış bir satır bütün sitenin taranmasını engelleyebilir. Özellikle site yenilendikten sonra test ortamından kalan "Disallow: /" satırı en sık görülen hatalardan biridir.

## 3. Site HTTPS ile açılıyor mu?

Adres çubuğunda kilit simgesi görünmeli ve sitenin http:// ile başlayan hali otomatik olarak https:// adresine yönlenmelidir. Aynı şekilde www'li ve www'siz adreslerden biri tercih edilmeli, diğeri ona yönlendirilmelidir. Aksi hâlde Google aynı sayfanın birden fazla kopyasını görebilir.

## 4. Mobilde düzgün görünüyor mu?

Google siteleri öncelikle mobil sürümleriyle değerlendirir. Sitenizi kendi telefonunuzdan açın: yazılar okunuyor mu, düğmelere rahat dokunulabiliyor mu, sayfa yana kayıyor mu? Sayfanın kodunda mobil uyumluluk etiketi (viewport) bulunmalıdır.

## 5. Sayfalar telefonda hızlı açılıyor mu?

PageSpeed Insights'a sitenizin adresini yazın ve **Mobil** sekmesine bakın. Google'ın "Önemli Web Verileri" için iyi kabul ettiği sınırlar şunlardır:

- **LCP** (ana içeriğin yüklenme süresi): 2,5 saniye ve altı
- **INP** (dokunmalara tepki süresi): 200 milisaniye ve altı
- **CLS** (sayfa yüklenirken kayma): 0,1 ve altı

Yavaşlığın en yaygın nedeni sıkıştırılmamış büyük görsellerdir. Fotoğrafları küçültmek, WebP gibi modern biçimlere çevirmek ve kullanılmayan eklentileri kaldırmak çoğu zaman büyük fark yaratır.

## 6. Her sayfanın kanonik adresi doğru mu?

Aynı içerik birden fazla adresten açılabiliyorsa (filtreler, takip parametreleri, sayfa sonunda / olup olmaması gibi), sayfanın kodundaki **kanonik etiket** Google'a hangi adresin asıl olduğunu söyler. Her sayfanın kanonik adresi kendisini göstermeli, yanlışlıkla ana sayfayı ya da başka bir sayfayı göstermemelidir.

## 7. Eski adresler yeni sayfalara yönleniyor mu?

Site yenilendiğinde ya da sayfa adresleri değiştiğinde, eski adreslerin yenilerine **301 yönlendirmesiyle** bağlanması gerekir. Aksi hâlde eski adreslerin kazandığı sıralamalar ve başka sitelerden gelen bağlantılar kaybolur, ziyaretçiler hata sayfasına düşer. Search Console'daki "Bulunamadı (404)" listesi bu sorunu yakalamak için iyi bir başlangıçtır.

## 8. Kırık bağlantı var mı?

Sitenizin içinde artık var olmayan sayfalara giden bağlantılar hem ziyaretçiyi hem Google'ı çıkmaza sokar. Önemli sayfalarınızdaki bağlantılara tıklayarak ya da ücretsiz bir tarama aracıyla bunları bulup düzeltin. Olmayan bir adrese girildiğinde site gerçek bir "404" yanıtı vermeli, ana sayfaya ya da boş bir sayfaya göndermemelidir.

## 9. Her sayfanın başlığı ve açıklaması var mı?

Google'da sitenizin adı olarak görünen **sayfa başlığı** (title) ve altındaki iki satırlık **açıklama**, tıklanıp tıklanmayacağınızı belirler. Her sayfanın kendine özgü bir başlığı olmalı; başlık yaklaşık 60, açıklama yaklaşık 155 karakteri geçmemeli, aksi hâlde sonu kesilebilir. Aynı başlığı taşıyan birden fazla sayfa, Google'ın hangisini göstereceğini şaşırmasına yol açar.

## 10. Her sayfada tek bir ana başlık (H1) var mı?

H1, sayfanın konusunu söyleyen ana başlıktır. Her sayfada bir tane olmalı ve sayfanın hedeflediği aramayla uyumlu olmalıdır. Ara başlıklar (H2, H3) ise içeriği bölümlere ayırır; hem okuyucunun hem Google'ın sayfayı anlamasını kolaylaştırır.

## 11. Yapılandırılmış veri ekli mi?

Yapılandırılmış veri, işletmenizin adını, adresini, telefonunu, çalışma saatlerini, hizmetlerini ve sık sorulan sorularınızı Google'a düzenli bir biçimde anlatan koddur. Google'ın **Zengin Sonuç Testi** aracıyla sayfanızdaki yapılandırılmış veriyi kontrol edebilirsiniz. Yapay zeka araçlarının da işletmenizi doğru tanımasına yardımcı olur; bu konuyu [GEO nedir?](/blog/geo-nedir-yapay-zeka-aramalarinda-gorunmek/) yazımızda anlattık.

## 12. Önemli sayfalarınıza site içinden bağlantı veriliyor mu?

Google bir sayfanın ne kadar önemli olduğunu, sitenizin geri kalanının ona ne kadar ve hangi kelimelerle bağlandığına bakarak anlar. Hizmet sayfalarınıza yalnızca menüden değil, ilgili yazılarınızın metninden de bağlantı verin ve bağlantı metninde "buraya tıklayın" yerine sayfanın konusunu yazın (örneğin "[Ankara web tasarım](/web-tasarim/)").

## E-ticaret siteleri için ek teknik SEO kontrolleri

E-ticaret siteleri yukarıdaki 12 maddenin hepsine ihtiyaç duyar, ama yüzlerce ürün, filtre ve kategori sayfası yüzünden birkaç sorun bu sitelerde çok daha sık görülür. Hazır e-ticaret platformlarında da WooCommerce gibi altyapılarda da bu ayarların bir kısmı varsayılan olarak gelir; yine de kontrol etmeden doğru olduğunu varsaymayın.

### Filtre ve sıralama adresleri

Renk, beden, fiyat aralığı ya da "en ucuz önce" gibi her filtre seçimi çoğu zaman yeni bir adres üretir. Bu adreslerin hepsi taranır ve dizine eklenirse Google aynı ürün listesinin binlerce kopyasını görür; asıl kategori sayfanız güç kaybeder. Filtreli adreslerin kanonik etiketi ana kategori sayfasını göstermeli, aramada değeri olmayan kombinasyonlar dizine eklenmemelidir. Bir adresi hem robots.txt ile engelleyip hem de "noindex" etiketiyle işaretlemeyin: Google engellenen sayfayı tarayamadığı için "noindex" etiketini hiç göremez.

### Stokta olmayan ve kaldırılan ürünler

Ürün geçici olarak tükendiyse sayfayı silmeyin; "stokta yok" bilgisiyle yayında kalsın ve benzer ürünlere bağlantı versin. Ürün kalıcı olarak satıştan kalktıysa adresi en yakın ürüne ya da kategorisine 301 ile yönlendirin. Karşılığı olmayan ürünlerde sayfanın gerçek bir 404 yanıtı vermesi, ana sayfaya yönlendirilmesinden daha doğrudur.

### Ürün yapılandırılmış verisi

Ürün sayfalarında ürün adı, görseli, fiyatı, para birimi ve stok durumu yapılandırılmış veriyle (Product ve Offer) Google'a anlatılmalıdır. Böylece Google arama sonuçlarında fiyatı ve stok durumunu gösterebilir. Sayfadaki fiyat ile yapılandırılmış verideki fiyat her zaman aynı olmalı; yorum ve puan bilgisi yalnızca gerçek müşteri yorumlarından gelmelidir. Zengin Sonuç Testi ve Search Console'daki ürün raporları hataları gösterir.

### Kategori sayfalarında sayfalama

Çok ürünlü kategoriler genellikle birkaç sayfaya bölünür. Her sayfanın kendi adresi olmalı ve kanonik etiketi kendisini göstermelidir; 2. ve sonraki sayfaların kanonik adresini 1. sayfaya vermek, oradaki ürünlerin Google tarafından bulunmasını zorlaştırır. Sonsuz kaydırma kullanılıyorsa ürünlere tıklanabilir sayfa bağlantılarıyla da ulaşılabilmelidir.

### Kopya ürün açıklamaları

Üreticinin ürün açıklamasını olduğu gibi kullanan yüzlerce site, Google'ın gözünde aynı metni yayınlar. En çok satan ve en çok aranan ürünlerden başlayarak kendi açıklamalarınızı yazın: ürünün kime uygun olduğu, ölçüleri, kullanım ve teslimat bilgisi gibi müşterinin gerçekten sorduğu bilgilerle. Renk ve beden gibi seçenekler ayrı adreslerde ise kanonik etiketleri tutarlı olmalıdır.

### Ürün görselleri ve site içi arama

Ürün sayfaları görsel ağırlıklı olduğu için hızın en çok bozulduğu yer burasıdır. Görselleri gösterildikleri boyuta göre küçültün, WebP gibi modern biçimlere çevirin ve ilk görünen ürün görseli dışındakileri gecikmeli yükleyin. Görsellerin alt metninde ürünün adı yazsın. Sitenizin kendi arama kutusunun sonuç sayfaları ise dizine eklenmemelidir; bu sayfalar sonsuz sayıda düşük değerli adres üretir.

E-ticaret sitesi kurmayı ya da mevcut mağazanızı yenilemeyi düşünüyorsanız bu kontrolleri baştan planladığımız [e-ticaret sitesi](/ankara-e-ticaret-sitesi/) hizmetimize bakabilirsiniz.

## Kontrol listesi

- Önemli sayfalar Search Console'da dizinde
- Site haritası gönderilmiş, robots.txt engellemiyor
- HTTPS ve tek bir adres sürümü (www'li ya da www'siz)
- Telefonda düzgün görünüyor
- Mobil hızda LCP 2,5 saniyenin altında
- Kanonik adresler doğru
- Eski adresler 301 ile yönleniyor
- Kırık bağlantı yok, olmayan sayfa gerçek 404 veriyor
- Her sayfanın kendine özgü başlığı ve açıklaması var
- Her sayfada tek H1
- Yapılandırılmış veri hatasız
- Hizmet sayfalarına metin içinden bağlantı veriliyor

E-ticaret siteleri için ek olarak:

- Filtre ve sıralama adresleri ana kategoriye kanonik veriyor
- Tükenen ürünler yayında, kaldırılan ürünler 301 ile yönleniyor
- Ürün sayfalarında fiyat ve stok bilgisi yapılandırılmış veride
- Kategori sayfalarının her biri kendi kanonik adresinde
- Çok satan ürünlerin açıklamaları özgün
- Ürün görselleri küçültülmüş, site içi arama sayfaları dizinde değil

Teknik SEO bir kez yapılıp bırakılan bir iş değildir; site güncellendikçe yeni sorunlar ortaya çıkabilir. SEO'nun genel olarak nasıl işlediğini ve ne zaman sonuç verdiğini [SEO nedir, ne zaman sonuç verir?](/blog/seo-nedir-ne-zaman-sonuc-verir/) yazımızda anlattık.

> Clickbait Dijital olarak SEO çalışmalarımıza her zaman bu teknik denetimle başlıyoruz: sorunları öncelik sırasına koyuyor, düzeltiyor ve sonuçları Search Console verileriyle izliyoruz. Ayrıntılar için [SEO hizmeti](/ankara-seo/) sayfamıza bakabilirsiniz. Çayyolu'ndaki ofisimizde yüz yüze görüşebilir, Türkiye'nin her yerinden online çalışabiliriz.
