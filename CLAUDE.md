# Proje hafızası — Clickbait Dijital web sitesi

Bu dosya, projeye yeni başlayan bir Claude oturumunun önceki çalışmaları bilmesi için yazıldı.
Kullanıcıyla **Türkçe** konuş. Kullanıcı MacBook kullanıyor; klavye kısayollarını Mac'e göre ver (⌘, ⌥).
Kullanıcı teknik değil: talimatları adım adım, "şuraya tıkla / şunu yaz" şeklinde ver.

## Şirket
- İşletme adı her yerde **Clickbait Dijital** (kullanıcı kararı, 19.10.2026; Google İşletme Profili de bu ad). "Digital" yazma. Sayfa başlıklarının sonunda kısa marka "| Clickbait" kalıyor.
  Resmî unvan: Clickbait Medya Limited Şirketi, Ankara. Alan adı: https://clickbait.com.tr
- Adres: Meksika Caddesi, Çayyolu / Ankara ("Çankaya", "Yenimahalle" deme; "Çayyolu" de).
- E-posta: info@clickbait.com.tr (Google Workspace).
- Instagram: https://www.instagram.com/clickbaitdijital/ · LinkedIn: https://www.linkedin.com/company/clickbait-digital-agency/
- Facebook paylaşılmak istenmiyor; YouTube kanalı yok.
- Google İşletme Profili: https://share.google/u1DfuQgwwOlqnDbwp · Yorum bağlantısı: https://g.page/r/CVZVcZ6LobnvEBM/review
- Rakamlar: 10+ yıl, 300+ proje, 50+ marka, 7/24 destek.

## Hizmetler (bu sırayla; yapay zeka öne çıkarılıyor)
1. Yapay zeka danışmanlığı — /yapay-zeka-danismanligi/
2. Web tasarım — /web-tasarim/
3. Dijital pazarlama — /dijital-pazarlama/ (eski adı "Dijital medya")
4. Sosyal medya yönetimi — /sosyal-medya-yonetimi/
5. Kreatif hizmetler — /kreatif-hizmetler/
Sağlık turizmi hizmeti **kaldırıldı**, geri ekleme.

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
`aria-hidden`; rakam/sonuç uydurma). Yeni sayfa eklenirse `CIZIMLER` sözlüğüne çizimini ekle. Kapsam kartlarının simgeleri `KART_SIMGE` (kart başlığı → simge); yeni kart başlığı eklersen buraya da ekle.
Ana sayfa hizmet kartlarındaki mini çizimler index.html'de elle yazılı. Yüzen kartlar: `.cizim-yuz` (dev/in.css).
Referans logo şeridi tek sıra, sürekli kayan (`<!-- KAYAN ŞERİT -->` … `<!-- /KAYAN ŞERİT -->`, logolar iki kez yazılı, `@keyframes kaydir` dev/in.css'te).
Üretici bu bloğu index.html'den alıp hizmet sayfalarına kopyalar; logo eklerken iki listeye de ekle (ikincisinde alt="").

## Ankara'ya özel sayfalar
- `dev/sayfalar.py` içindeki `ANKARA` listesi; hizmet sayfası şablonuyla üretilir, her biri bir ana hizmete bağlı (`ust`), ek olarak `metin` bölümleri var.
- Yayında: /ankara-seo/, /ankara-google-ads-ajansi/, /ankara-reklam-ajansi/, /ankara-instagram-reklam-ajansi/ (dijital pazarlama altında), /ankara-e-ticaret-sitesi/ (web tasarım altında).
- Ana sayfada hizmetlerin altında "ANKARA'YA ÖZEL HİZMETLER" bağlantıları (`<!-- ANKARA BAĞLANTILARI -->`, üretici yazar).
- Ana hizmet sayfalarının hedeflediği kelimelerle (Ankara web tasarım, Ankara sosyal medya yönetimi, Ankara dijital pazarlama ajansı) çakışan sayfa açma.
- Arama hacmi doğrulanmadı; kullanıcı Google Ads Anahtar Kelime Planlayıcısı'na erişebiliyor. Reklam ajansı sayfası TV/radyo/açık hava yapmadığımızı söyler (kullanıcı onayladı).

## Blog
- Yazılar `dev/blog/<adres>.md`. Ön bilgi alanları: baslik, title, description, ozet, tarih (YYYY-MM-DD), kume (hizmet adresi,
  ör. `web-tasarim`), etiket (ör. `WEB TASARIM`), isteğe bağlı guncelleme.
- Kapak: ön bilgide `kapak` (kapakta görünen kısa etiket, ör. `7 adımda başlangıç`) ve `simge` (`dev/cizimler.py` → `BLOG_SIMGE` adlarından biri).
  Kapak rengi kümeden gelir (`KAPAK_TEMA`). Yeni yazıdan sonra `python3 dev/kapaklar.py` çalıştır (1200x630 paylaşım görseli,
  `site/assets/img/blog/<adres>.jpg`; Chrome + sips), sonra `python3 dev/sayfalar.py` og:image'i bağlar.
- Markdown desteği: ##, ###, -, 1., >, **kalın**, [bağlantı](/adres/).
- İçerik planı ve durum: `dev/icerik-plani.md` (✅ yayında). Yayınlanan yazıyı orada ✅ yap.
- Kurallar: uydurma istatistik/fiyat yok; her yazı kendi hizmet sayfasına ve ilgili yazılara iç bağlantı verir;
  sonda Clickbait'i anlatan kısa bir `>` notu (Çayyolu ofisi + online çalışma). Haftada en az 1 yazı, kümeler dönüşümlü.
- Yayınlananlar: yapay zeka kullanım alanları, Ankara'da web sitesi yaptırırken 10 şey, Google Ads mi SEO mu, web sitesi fiyatları, Google İşletme Profili, yapay zeka danışmanlığı nedir ("ankara yapay zeka danışmanlığı" için hizmet sayfasını destekler), şirketinizde yapay zekaya nereden başlamalısınız (16.10.2026), kurumsal web sitesinde olması gereken 8 sayfa (17.10.2026), SEO firması seçerken sorulacak 10 soru (18.10.2026), SEO nedir, ne zaman sonuç verir? (19.10.2026), sosyal medya ajansı seçerken dikkat edilecek 9 şey (19.10.2026; ek Ankara yazıları listesi seo-plani.md'de).
- Sıradaki yazılar `dev/seo-plani.md` takviminde (hafta 4: "Instagram reklamı nasıl verilir? Adım adım rehber" → /ankara-instagram-reklam-ajansi/).

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
  Bing'deki "AI Performance" raporu yapay zeka cevaplarındaki görünürlüğü gösterir; değerlendirme haftalarında bak.
- Google Analytics `G-3GSS5F5FTT`, yalnızca çerez onayından sonra yüklenir (KVKK metninde 7. bölüm çerezler).
  Form başarılı gönderilince `generate_lead` olayı gider.
- 4–6 hafta sonra Search Console verisine bakılıp içerik planı güncellenecek.

## Test
Her değişiklikten sonra `site/` klasörünü `php -S` ile sunup Playwright (Chromium: `/opt/pw-browsers/chromium`)
ile 1440px ve 390px genişlikte kontrol et: konsol hatası yok, yatay taşma yok, sayfa başına tek H1, JSON-LD geçerli.

## Kullanıcıdan beklenenler
- Gerçek müşteri yorumu (metin, kişi, marka) — ana sayfada yer tutucu kart var.
- Proje görselleri: Active English, HUBEK, Psychology Times, Uslu Yapı, Form Çayyolu (otel, tam genişlik kart) ekran görüntüleri eklendi (`site/assets/img/projeler/`, tarayıcı çerçeveli kartlar).
  Rojin Nazik: Instagram profil kartı (SOSYAL MEDYA). German Dental, İstanbul Hair Center, Saye Emlak, EKM: kullanıcı bunların
  Meta & Google Ads hesaplarını yönetiyor, görsel yok → logo + "Google Ads · Meta Ads" kartı (REKLAM YÖNETİMİ); grafikte rakam yok, uydurma sonuç koyma.
  Bekleniyor: sitelerin adresleri (kartlara bağlantı için), gerçek reklam sonuçları (isteğe bağlı), German Dental logosunun yüksek çözünürlüklü hali.
- Referans markalara verilen hizmetler.
- Hizmet sayfalarındaki şu ifadelerin onayı: "hesaplar sizin adınıza", "fotoğraf/video çekimi", "ilk görüşme ücretsiz".
- Blog yazarı olarak gösterilecek kişi (ad, kısa biyografi, fotoğraf) — şu an "Clickbait ekibi".
