# Proje hafızası — Clickbait Dijital web sitesi

Bu dosya, projeye yeni başlayan bir Claude oturumunun önceki çalışmaları bilmesi için yazıldı.
Kullanıcıyla **Türkçe** konuş — son özet kutusu, sorular ve düğmeler dahil her şey Türkçe (kullanıcı 20.10.2026'da özellikle istedi). Kullanıcı MacBook kullanıyor; klavye kısayollarını Mac'e göre ver (⌘, ⌥).
Kullanıcı teknik değil: talimatları adım adım, "şuraya tıkla / şunu yaz" şeklinde ver.

## Şirket
- İşletme adı her yerde **Clickbait Dijital** (kullanıcı kararı, 19.10.2026; Google İşletme Profili de bu ad). "Digital" yazma. Sayfa başlıklarının sonunda kısa marka "| Clickbait" kalıyor.
  Resmî unvan: Clickbait Medya Limited Şirketi, Ankara. Alan adı: https://clickbait.com.tr
- Adres: Meksika Caddesi, Çayyolu / Ankara ("Çankaya", "Yenimahalle" deme; "Çayyolu" de).
- E-posta: info@clickbait.com.tr (Google Workspace).
- Instagram: https://www.instagram.com/clickbaitdijital/ · LinkedIn: https://www.linkedin.com/company/clickbait-digital-agency/
- Facebook paylaşılmak istenmiyor; YouTube kanalı yok.
- LinkedIn şirket sayfası (20.10.2026, Claude güncelledi): ad "Clickbait Dijital", adres Ümit Mah. Meksika Cad. No:56 D:21 Çayyolu, açıklama sitedeki hizmetlerle uyumlu, web https://clickbait.com.tr/. Adres (clickbait-digital-agency) değiştirilmedi. 22.10.2026: açıklama "tam kapsamlı reklam ve dijital ajans" olarak güncellendi, uzmanlık alanlarına Reklam Ajansı, TV Reklamı, Radyo Reklamı, Açık Hava Reklamı, Medya Planlama eklendi.
  Kuruluş yılı **2013** (kullanıcı onayladı, 20.10.2026); LinkedIn'de de 2013 ve açıklamada "2013'ten beri". Eski adres (Ahmet Taner Kışlalı Mah. 2873. Sk.) tumisyeri.com'da hâlâ duruyor (kullanıcı düzeltecek).
- Google İşletme Profili: https://share.google/u1DfuQgwwOlqnDbwp · Yorum bağlantısı: https://g.page/r/CVZVcZ6LobnvEBM/review
  21.10.2026: ilk 2 yorum geldi (Aslan Sineklik, Alican Nazik; 5,0), Claude cevapladı. Logo (C simgesi, mavi) ve kapak yüklendi; dosyalar `dev/duyuru/isletme-profili/` (repoda değil). 22.10.2026: açıklama "tam kapsamlı reklam ve dijital ajans" (TV, radyo, açık hava, medya planlama dahil) olarak güncellendi; birincil kategori Reklam Ajansı (ek: Web Sitesi Tasarımcısı, Medya Şirketi, Grafik Tasarımcı, Pazarlama Ajansı, İnternet Pazarlamacılığı Hizmeti; önceki "Web Sitesi Tasarımcısı birincil" bekleyen değişikliğin yerine), web sitesi https://clickbait.com.tr/ (www'siz) — üçü Google incelemesinde. Açılış tarihi profilde 9 Şubat 2023 (kuruluş 2013; kullanıcıya soruldu, dokunulmadı). Düzenleme: Google'da "Clickbait Dijital" araması (authuser=5) → Profili düzenle. Yönetim: business.google.com (info@ hesabı, authuser 5); logo/kapak yükleme penceresi doğrudan `https://www.google.com/local/business/12721594481278180870/promote/photos/logo` (ve `/cover`) adresinde açılınca dosya yüklenebiliyor.
- Rakamlar: 2013'ten beri (kuruluş yılı 2013), 10+ yıl, 300+ proje, 50+ marka, 7/24 destek.

## Hizmetler (bu sırayla; yapay zeka öne çıkarılıyor)
1. Yapay zeka danışmanlığı — /yapay-zeka-danismanligi/
2. Web tasarım — /web-tasarim/
3. Dijital pazarlama — /dijital-pazarlama/ (eski adı "Dijital medya")
4. Sosyal medya yönetimi — /sosyal-medya-yonetimi/
5. Kreatif hizmetler — /kreatif-hizmetler/
Sağlık turizmi hizmeti **kaldırıldı**, geri ekleme.
**SEO danışmanlığı** (rapor/yol haritası verip uygulamayı müşterinin ekibine bırakma) hizmeti **verilmiyor** (kullanıcı, 21.10.2026); SEO yalnızca aylık hizmet olarak anlatılır.

## Tasarım
Kullanıcının Google Stitch'te yaptırdığı tasarım esas alındı: gök mavisi degrade açılış, 3B yay kartlar, bento ızgara,
lime vurgu rengi `#D8F83C`, Plus Jakarta Sans (yerel font dosyaları `site/assets/fonts/`).
Statik HTML + derlenmiş Tailwind 3.4.17 (CDN değil) + sade JS (`site/assets/js/site.js`).
Görseller ve tasarım "her şey oturduktan sonra" tekrar ele alınacak.

## Yayın akışı (ÖNEMLİ)
- GitHub: `Clickbait-Digital/clickbait-web` (herkese açık repo). `site/` = sunucudaki `public_html`.
- Sunucu cPanel; terminal yok. Cron 5 dakikada bir `public_html/guncelle.php` çalıştırır,
  `site/SURUM` değiştiyse repodaki `site/` içeriğini indirip yazar.
- **Yayına almak için:** değişikliği yap → `site/SURUM` içindeki sayıyı 1 artır → `main`'e push. Kullanıcıdan dosya yükleme/silme isteme.
- Sunucudan dosya silmek için yolunu `site/SILINECEKLER` dosyasına yaz.
- Not (15.10.2026): Cron, söylenen 5 dakikadan seyrek çalışıyor gibi görünüyor (8+ dakikada almadı). Acil yayında kullanıcı izin verirse
  kullanıcının sohbete verdiği güncelleme bağlantısı çalıştırılır; anahtarı yine repoya yazma.
  Push'tan hemen sonra bağlantı GitHub önbelleği yüzünden 2–3 dakika eski sürümü görebilir ("Site güncel (sürüm N-1)"); ~45 sn arayla tekrar dene.
- Mobilde tüm sayfaların altında sabit "Hemen ara / WhatsApp'tan yaz" çubuğu var (`alt_bilgi()` içinde); tıklamalar `iletisim_tiklama` olayı.
- `guncelle.php` ve onun gizli anahtarı repoda YOK ve repoya asla yazılmamalı (repo herkese açık). Anahtar kullanıcıda.
- İletişim formu: `site/contact.php`, Gmail SMTP (smtp.gmail.com:465). Şifre sunucuda `/home/clickbait/clickbait-ayarlar.php`
  dosyasında; repoya veya sohbete şifre yazdırma. Hata olursa form "Hata kodu: …" gösterir.
- Formlar: ana sayfa formu (`#form`, site.js'teki eski kod), hizmet/Ankara sayfalarının altında `data-form="hizmet"` formu (`#teklif`),
  ücretsiz site analizi penceresi (`data-form="analiz"`, site.js oluşturur). contact.php `tur` (geri_arama/analiz), `kaynak` (sayfa) ve
  `site_adresi` alanlarını e-postaya yazar. Analiz penceresi: kullanıcı isteğiyle tüm cihazlarda sayfaya girişten 6 sn sonra açılır
  (çerez bandı açıksa karar verilince); kapatılırsa 7 gün, gönderilirse bir daha kendiliğinden açılmaz. Elle: `data-analiz` ya da adres sonuna `#analiz`.
- Yerel testte PHP yok (python http.server); form gönderimi 501 verir, başarı yolu fetch taklidiyle denenir.

## Üretici: `dev/sayfalar.py`
`python3 dev/sayfalar.py` şunları üretir: 5 hizmet sayfası (veri `HIZMETLER` listesinde), ortak alt bilgi
(index.html ve kvkk sayfasındaki ALT BİLGİ bölümüne yazılır), blog listesi, blog yazıları, ana sayfadaki BLOG bölümü,
hizmet sayfalarındaki "Konuyla ilgili yazılar", `sitemap.xml`. Üretilen dosyaları elle düzenleme; üreticiyi düzenle.
Yeni Tailwind sınıfı kullanıldıysa CSS'i derle (README'deki komut).
`site/index.html` bölümleri `BÖLÜM: X — BAŞLANGIÇ/BİTİŞ` yorumlarıyla işaretli.
Hizmet ve Ankara sayfalarının açılışında sağda hizmete özel çizim var: `dev/cizimler.py` (HTML + Tailwind arayüz görselleri, görsel dosya yok,
`aria-hidden`; rakam/sonuç uydurma). Yeni sayfa eklenirse `CIZIMLER` sözlüğüne çizimini ve `dev/sayfalar.py` → `TANIMLAR`'a "KISACA" tanımını ekle (kim/ne/nerede; yalnızca sayfada söylenenler). Kapsam kartlarının simgeleri `KART_SIMGE` (kart başlığı → simge); yeni kart başlığı eklersen buraya da ekle.
Ana sayfa hizmet kartlarındaki mini çizimler index.html'de elle yazılı. Yüzen kartlar: `.cizim-yuz` (dev/in.css).
Referans logo şeridi tek sıra, sürekli kayan (`<!-- KAYAN ŞERİT -->` … `<!-- /KAYAN ŞERİT -->`, logolar iki kez yazılı, `@keyframes kaydir` dev/in.css'te).
Üretici bu bloğu index.html'den alıp hizmet sayfalarına kopyalar; logo eklerken iki listeye de ekle (ikincisinde alt="").

## Ankara'ya özel sayfalar
- `dev/sayfalar.py` içindeki `ANKARA` listesi; hizmet sayfası şablonuyla üretilir, her biri bir ana hizmete bağlı (`ust`), ek olarak `metin` bölümleri var.
- Yayında: /ankara-seo/, /ankara-google-ads-ajansi/, /ankara-reklam-ajansi/, /ankara-instagram-reklam-ajansi/ (dijital pazarlama altında), /ankara-e-ticaret-sitesi/ (web tasarım altında).
- Ana sayfada hizmetlerin altında "ANKARA'YA ÖZEL HİZMETLER" bağlantıları (`<!-- ANKARA BAĞLANTILARI -->`, üretici yazar).
- Ana hizmet sayfalarının hedeflediği kelimelerle (Ankara web tasarım, Ankara sosyal medya yönetimi, Ankara dijital pazarlama ajansı) çakışan sayfa açma.
- Arama hacmi doğrulanmadı; kullanıcı Google Ads Anahtar Kelime Planlayıcısı'na erişebiliyor. **Clickbait tam kapsamlı reklam ajansı** (kullanıcı, 22.10.2026): TV reklam filmi (prodüksiyon) ve yayın planlama/satın alma, radyo reklamı, açık hava (billboard, raket, megalight: tasarım, yer kiralama, uygulama), medya planlama ve dijital; "tam kapsamlı bir ajans ne yapıyorsa yapabiliyoruz". /ankara-reklam-ajansi/ buna göre yeniden yazıldı. Eskiden "TV/radyo/açık hava yapmıyoruz" deniyordu, artık deme.

## Blog
- Yazılar `dev/blog/<adres>.md`. Ön bilgi alanları: baslik, title, description, ozet, tarih (YYYY-MM-DD), kume (hizmet adresi,
  ör. `web-tasarim`), etiket (ör. `WEB TASARIM`), isteğe bağlı guncelleme.
- Kapak: ön bilgide `kapak` (kapakta görünen kısa etiket, ör. `7 adımda başlangıç`) ve `simge` (`dev/cizimler.py` → `BLOG_SIMGE` adlarından biri); isteğe bağlı `rozet` (kapaktaki siyah rozet, varsayılan "Rehber"; araştırma yazısında "Araştırma").
  Kapak rengi kümeden gelir (`KAPAK_TEMA`). Yeni yazıdan sonra `python3 dev/kapaklar.py` çalıştır (1200x630 paylaşım görseli,
  `site/assets/img/blog/<adres>.jpg`; Chrome + sips), sonra `python3 dev/sayfalar.py` og:image'i bağlar.
- `kisa_cevap` (zorunlu sayılır): başlıktaki soruya 2–3 cümlelik, kendi başına anlaşılır cevap; yazının başında "KISA CEVAP" kutusu, JSON-LD `abstract` ve llms.txt'de kullanılır. Yazıdaki liste/başlıklarla birebir uyuşmalı.
- Markdown desteği: ##, ###, -, 1., >, **kalın**, [bağlantı](/adres/).
- İçerik planı ve durum: `dev/icerik-plani.md` (✅ yayında). Yayınlanan yazıyı orada ✅ yap.
- Kurallar: uydurma istatistik/fiyat yok; her yazı kendi hizmet sayfasına ve ilgili yazılara iç bağlantı verir;
  sonda Clickbait'i anlatan kısa bir `>` notu (Çayyolu ofisi + online çalışma). Haftada en az 1 yazı, kümeler dönüşümlü.
- Yayınlananlar: yapay zeka kullanım alanları, Ankara'da web sitesi yaptırırken 10 şey, Google Ads mi SEO mu, web sitesi fiyatları, Google İşletme Profili, yapay zeka danışmanlığı nedir ("ankara yapay zeka danışmanlığı" için hizmet sayfasını destekler), şirketinizde yapay zekaya nereden başlamalısınız (16.10.2026), kurumsal web sitesinde olması gereken 8 sayfa (17.10.2026), SEO firması seçerken sorulacak 10 soru (18.10.2026), SEO nedir, ne zaman sonuç verir? (19.10.2026), sosyal medya ajansı seçerken dikkat edilecek 9 şey (19.10.2026; ek Ankara yazıları listesi seo-plani.md'de), **Ankara işletme siteleri araştırması 2026** (20.10.2026; 101 site, Lighthouse mobil + kaynak kodu kontrolleri, isimsiz veri `site/assets/veri/ankara-isletme-siteleri-2026.csv`; bağlantı kazanmak için hazırlandı, duyurusu yapılacak: LinkedIn, yerel haber siteleri, SEO yazarları). Grafik/tablo sözdizimi: `::: grafik Başlık` / `- Etiket | 0–100 | metin` / `kaynak: …` / `:::` ve Markdown tablosu.
- Instagram reklamı nasıl verilir? Adım adım rehber (20.10.2026, → /ankara-instagram-reklam-ajansi/).
- Teknik SEO kontrol listesi ve GEO nedir? (21.10.2026, → /ankara-seo/). Web sitenizi yenilerken Google sıralamanızı korumak (22.10.2026, → /web-tasarim/).
- **/web-tasarim/ (22.10.2026):** "ankara web tasarım" 21.10'da ilk 50'nin dışındaydı. Sayfaya `projeler` alanı (müşteri sitesi ekran görüntüleri, `projeler_bolumu()`), 6 yeni metin bölümü, uzman kutusu, 3 SSS eklendi; 5 yazıdan "Ankara web tasarım" bağlantı metniyle bağlantı verildi. Canlı Lighthouse mobil 99. Etkisini 6–12 Kasım değerlendirmesinde ölç.
- SEO çalışma raporu (dışarıya gönderilebilir, Claude Docs): https://claude.ai/artifact/UY8Sm9Gw1C7p3cUm5H1QZ2 — güncellerken tarih çipini ve "Bir bakışta" tablosunu yenile.
- Sıradaki yazılar `dev/seo-plani.md` takviminde (hafta 5: "Aylık sosyal medya içerik planı nasıl hazırlanır?"). Search Console (20.10, veri 17.10'a kadar): /ankara-seo/ "ankara seo"da ~20–24. sırada, "yapay zeka danışmanlığı" ~11; bir sonraki iş /ankara-seo/'yu iç bağlantı ve içerikle güçlendirmek.

## SEO (kullanıcının en önemli önceliği)
- **Rakip analizi: `dev/rakip-analizi.md`** (19.10.2026; 11 Ankara aramasında sıramız, rakiplerin yaptıkları, öneriler). Değerlendirme haftalarında aynı aramalarla karşılaştır.
- **Plan ve kelime haritası: `dev/seo-plani.md`** (12 haftalık takvim, hangi sayfa hangi kelimeyi hedefler, kullanıcının site dışı işleri). Yeni sayfa/yazı açmadan önce kelime haritasına bak, çakışma yaratma; işi bitince planı güncelle.
- Hedef: önce Ankara aramaları, ikinci olarak uzaktan verilebilen hizmetlerde Türkiye geneli.
- Kurulu: JSON-LD (ProfessionalService `#isletme`, Service, FAQPage, BreadcrumbList, Blog/BlogPosting), canonical,
  site haritası, robots.txt, OG görseli, eski WordPress adreslerinden 301 yönlendirmeler (`site/.htaccess`), özel 404.
- Search Console doğrulandı, site haritası gönderildi. Yeni sayfadan sonra kullanıcıya "URL denetimi → Dizine eklenmeyi iste" hatırlat.
- **Bing ve yapay zeka araçları (20.10.2026):** Bing Webmaster Tools'a eklendi (kullanıcının Microsoft hesabı; Psychology Times da aynı hesapta; doğrulama ana sayfadaki `msvalidate.01` etiketi, silme).
  IndexNow anahtarı `site/<32 karakter>.txt`. **Yeni/değişen sayfayı yayınladıktan sonra** `python3 dev/indexnow.py <adres…>` (ya da `--hepsi`) çalıştır → Bing'e bildirir.
  `site/llms.txt` yapay zeka araçları için site özeti; `dev/sayfalar.py` (`llms_txt()`) her çalıştığında yeniden üretir. robots.txt tüm tarayıcılara açık (GPTBot, ClaudeBot, PerplexityBot dahil), kapatma.
  Yapay zeka testi soruları ve sonuç tablosu: `dev/yapay-zeka-testi.md` (ayda bir).
  Bing'deki "AI Performance" raporu yapay zeka cevaplarındaki görünürlüğü gösterir; değerlendirme haftalarında bak.
- Google Analytics `G-3GSS5F5FTT`, yalnızca çerez onayından sonra yüklenir (KVKK metninde 7. bölüm çerezler).
  Form başarılı gönderilince `generate_lead` olayı gider.
- 4–6 hafta sonra Search Console verisine bakılıp içerik planı güncellenecek.

## Test
Her değişiklikten sonra `site/` klasörünü `php -S` ile sunup Playwright (Chromium: `/opt/pw-browsers/chromium`)
ile 1440px ve 390px genişlikte kontrol et: konsol hatası yok, yatay taşma yok, sayfa başına tek H1, JSON-LD geçerli.

## Kullanıcıdan beklenenler
- **Psychology Times** (psychologytimes.com.tr, kullanıcının yönettiği WordPress sitesi; tagDiv Newspaper teması): alt bilgi şablonu "Footer – Urban Observer" (Cloud Templates, id 186), metinler base64(encodeURIComponent) ile saklanıyor. Yazar hesabı `sakiryavuz` (id 3); aynı adda iki hesap daha var (sakiryvz, sakir-yavuz), dokunulmadı. Yayın/kaydet düğmelerine gerçek tıklama ile basılıyor.
- Rehber kayıtları: **armut.com yapıldı**, **dijitalajanslar.com başvurusu yapıldı** (20.10.2026; onaylanınca listede görünüp görünmediğini kontrol et). Diğerleri (dijitalajanslar.com, Clutch vb.) kullanıcıya uzun geldi; ısrar etme, istenirse kopyala-yapıştır metin hazırla.
- Gerçek müşteri yorumu (metin, kişi, marka) — ana sayfada yer tutucu kart var.
- Proje görselleri: Active English, HUBEK, Psychology Times, Uslu Yapı, Form Çayyolu (otel, tam genişlik kart) ekran görüntüleri eklendi (`site/assets/img/projeler/`, tarayıcı çerçeveli kartlar).
  Rojin Nazik: Instagram profil kartı (SOSYAL MEDYA). German Dental, İstanbul Hair Center, Saye Emlak, EKM: kullanıcı bunların
  Meta & Google Ads hesaplarını yönetiyor, görsel yok → logo + "Google Ads · Meta Ads" kartı (REKLAM YÖNETİMİ); grafikte rakam yok, uydurma sonuç koyma.
  Bekleniyor: sitelerin adresleri (kartlara bağlantı için), gerçek reklam sonuçları (isteğe bağlı), German Dental logosunun yüksek çözünürlüklü hali.
- Referans markalara verilen hizmetler.
- Hizmet sayfalarındaki şu ifadelerin onayı: "hesaplar sizin adınıza", "fotoğraf/video çekimi", "ilk görüşme ücretsiz".
- Blog yazarı: **Şakir Yavuz** (kurucu, 2013; SEO'yu bizzat yürütüyor; yazılar onun deneyimine dayanıyor) — `dev/sayfalar.py` → `KURUCU`. Yazı başında ad, sonda "YAZAR" kutusu, JSON-LD Person.
  /ankara-seo/ sayfasında "SEO çalışmanızı kim yürütüyor?" bölümü (`UZMAN_METNI`). LinkedIn: https://www.linkedin.com/in/şakir-yavuz-2b62bb125/ (yazar kutusu, SEO sayfası, JSON-LD sameAs). Fotoğrafı var (21.10.2026): `site/assets/img/sakir-yavuz.jpg` ve kare `sakir-yavuz-kare.jpg` (uzman kutusu, yazar kutusu, JSON-LD Person `#sakir-yavuz`). Özgeçmişi kullanıcı onayıyla Claude yazdı: 2013'ten beri sağlık, eğitim, havacılık, inşaat, emlak, yayıncılık, konaklama; Active English, Psychology Times, Rojin Nazik SEO'su. Bunun dışında deneyim/eğitim/ödül yazma.
- **Yapay zeka ekibi:** 4 kişilik ekip (Şakir Yavuz dahil; isim/rol verilmedi, uydurma). Kurumsal yapay zeka eğitimi veriliyor (yüz yüze/online). Çalışılan araçlar logolarıyla /yapay-zeka-danismanligi/ sayfasında (`site/assets/img/araclar/`, Lobe Icons + Simple Icons). Fiyat yazılmıyor; çalışma modeli yazılabilir.
- **Gerçek SEO sonuçları:** info@clickbait.com.tr'de Search Console erişimi: active-languages.com, psychologytimes.com.tr, psikologrojinnazik.com, formcayyolu.com.tr. /ankara-seo/ "sonuclar" alanı 19.07–18.10.2026 verisiyle; ayda bir güncelle. Psychology Times için büyüme iddiası kurma (bkz. SEOmodi notu), yalnızca güncel rakamlar.
