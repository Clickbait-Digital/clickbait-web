#!/usr/bin/env python3
"""Clickbait — hizmet sayfası üreticisi.

Hizmet sayfalarını (site/<adres>/index.html), ortak alt bilgiyi ve site haritasını üretir.
Metinleri değiştirmek için aşağıdaki HIZMETLER listesini düzenleyip çalıştırın:

    python3 dev/sayfalar.py
"""
import json, os, re, datetime, html, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cizimler import cizim, kart_simgesi, blog_kapagi   # açılış bölümündeki hizmete özel çizimler

KOK = os.path.join(os.path.dirname(__file__), '..', 'site')
ALAN = 'https://clickbait.com.tr'
BUGUN = datetime.date.today().isoformat()

INSTAGRAM = 'https://www.instagram.com/clickbaitdijital/'
LINKEDIN = 'https://www.linkedin.com/company/clickbait-digital-agency/'
HARITA = 'https://share.google/u1DfuQgwwOlqnDbwp'   # Google İşletme Profili
YORUM = 'https://g.page/r/CVZVcZ6LobnvEBM/review'   # Google yorum bağlantısı
TEL_GORUNEN, TEL_LINK, WHATSAPP = '0507 923 85 75', 'tel:+905079238575', 'https://wa.me/905079238575'

# ---------------------------------------------------------------- İçerik
HIZMETLER = [
  {
    'adres': 'yapay-zeka-danismanligi', 'kisa': 'Yapay zeka danışmanlığı', 'renk': 'lime',
    'title': 'Ankara Yapay Zeka Danışmanlığı ve Eğitimi | Clickbait',
    'description': 'Ankara’da yapay zeka danışmanlığı ve kurumsal yapay zeka eğitimi: doğru araçları iş akışınıza kuruyor, ekibinizi eğitiyoruz. Türkiye geneline online.',
    'h1': 'Ankara’da yapay zeka danışmanlığı: işinize gerçekten zaman kazandıran kurulumlar',
    'giris': 'Yapay zekayı denemek kolay, işin içine yerleştirmek zor. 4 kişilik yapay zeka ekibimizle ekibinizin her hafta tekrar eden işlerini birlikte buluyor, doğru aracı seçip iş akışınıza bağlıyor ve kurumsal eğitimlerle ekibinizi kullanımına alıştırıyoruz. Ankara’daki işletmelerle yüz yüze, Türkiye’nin her yerinden işletmelerle online çalışıyoruz.',
    'kartlar': [
      ('İhtiyaç analizi', 'Hangi işlerin otomatikleşebileceğini, hangilerinin insanda kalması gerektiğini birlikte çıkarıyoruz.'),
      ('Raporlama ve otomasyon', 'Haftalık raporlar, veri derleme, e-posta ve doküman hazırlığı gibi tekrar eden işleri otomatikleştiriyoruz.'),
      ('İçerik ve görsel üretimi', 'Sosyal medya, blog ve reklam metinleri için markanızın diline uygun yapay zeka iş akışları kuruyoruz.'),
      ('Müşteri iletişimi', 'Sık sorulan sorulara ilk yanıtı veren, gerektiğinde ekibinize aktaran asistanlar tasarlıyoruz.'),
      ('Kurumsal yapay zeka eğitimi', 'Ekiplerinize kendi işleri üzerinden uygulamalı eğitim veriyoruz: doğru komut yazma, sonuçları kontrol etme ve araçları güvenle kullanma.'),
      ('Veri güvenliği ve KVKK', 'Hangi verinin hangi araçla paylaşılabileceğini belirleyen kullanım kuralları hazırlıyoruz.'),
    ],
    'adimlar': [
      ('Keşif görüşmesi', 'Ekibinizin bir haftasını konuşuyoruz: hangi işler tekrar ediyor, nerede vakit kaybediliyor.'),
      ('Pilot uygulama', 'Tek bir işle başlıyor, kazandırdığı zamanı ölçüyoruz.'),
      ('Yaygınlaştırma', 'İşe yarayan kurulumu diğer süreçlere ve ekiplere taşıyoruz.'),
      ('Eğitim ve takip', 'Ekibinizi eğitiyor, ilk haftalarda kullanımı birlikte takip ediyoruz.'),
    ],
    'sss': [
      ('AI danışmanlığı ile yapay zeka danışmanlığı aynı şey mi?', 'Evet. “AI” İngilizce “artificial intelligence” yani yapay zeka kelimesinin kısaltmasıdır; AI danışmanlığı, yapay zeka danışmanlığıyla aynı hizmeti anlatır. Bir işletmenin ChatGPT, Claude, Gemini gibi yapay zeka araçlarını hangi işlerde ve hangi kurallarla kullanacağını belirleyip bu kullanımı kurmayı ve ekibi eğitmeyi kapsar.'),
      ('Yapay zeka danışmanlığı hangi işletmeler için uygun?', 'Raporlama, teklif hazırlama, içerik üretimi ya da müşteri yazışmaları gibi her hafta tekrar eden işleri olan her ölçekte işletme için uygundur. Küçük ekiplerde kazanılan zaman çoğu zaman daha belirgin olur.'),
      ('Teknik bir ekibimiz olması gerekiyor mu?', 'Hayır. Kurulumu biz yapıyoruz, ekibinize günlük kullanımı öğretiyoruz. Yazılım ekibiniz varsa onlarla birlikte de çalışabiliriz.'),
      ('Verilerimiz güvende olur mu?', 'Kurulumdan önce hangi verinin hangi araçla paylaşılabileceğini birlikte belirliyoruz. Kişisel ve gizli verileri KVKK’ya uygun şekilde ayıran kullanım kuralları hazırlıyoruz.'),
      ('Ankara dışındaki işletmelere de hizmet veriyor musunuz?', 'Evet. Görüşmeleri, kurulumu ve eğitimleri online yürütebiliyoruz. Ankara’daki işletmelerle Çayyolu’ndaki ofisimizde de buluşuyoruz.'),
      ('İlk görüşme nasıl ilerliyor?', 'Ekibinizin iş akışını dinliyoruz ve görüşmenin sonunda yapay zekayla başlanabilecek ilk işi öneriyoruz.'),
      ('Kurumsal yapay zeka eğitimi veriyor musunuz?', 'Evet. Şirketlere ve ekiplere yüz yüze ya da online, uygulamalı yapay zeka eğitimleri veriyoruz. Eğitimi ekibinizin kendi işleri üzerinden kurguluyor, veri güvenliği ve KVKK kurallarını da eğitimin parçası yapıyoruz.'),
      ('Hangi yapay zeka araçlarıyla çalışıyorsunuz?', 'ChatGPT, Claude, Gemini, Microsoft Copilot ve Perplexity gibi dil modelleriyle, Midjourney gibi görsel araçlarla ve n8n, Make, Zapier gibi otomasyon araçlarıyla çalışıyoruz. Tek bir araca bağlı değiliz; işinize ve veri güvenliği ihtiyacınıza uygun olanı seçiyoruz.'),
      ('Bir yapay zeka projesi ne kadar sürer?', 'İşin kapsamına göre değişir. Tek bir işle başlayan pilot uygulamanın takvimini keşif görüşmesinden sonra netleştiriyor, sonuç alındıkça diğer işlere geçiyoruz.'),
      ('Fiyat neye göre belirleniyor?', 'Kaç iş akışının kurulacağı, kaç kişinin eğitileceği, eğitimin yüz yüze mi online mı olacağı ve kullanılacak araçların lisansları fiyatı belirler. Keşif görüşmesinden sonra kalem kalem teklif hazırlıyoruz.'),
    ],
    'metin': [
      ('Ankara’da yapay zeka danışmanlığında neler teslim ediyoruz?', 'Çalışmanın sonunda elinizde somut çıktılar olur: hangi işlerin yapay zekayla hızlanabileceğini öncelik sırasıyla gösteren bir ihtiyaç analizi, hangi verinin hangi araçla paylaşılabileceğini belirleyen ve KVKK’yı gözeten kullanım kuralları, ilk iş için kurulmuş ve denenmiş bir pilot uygulama, ekibinizin günlük kullanımı için kısa kılavuzlar ve ilk haftalarda birlikte takip. Pilotun kazandırdığı zamanı ölçüyor, işe yarayan kurulumu diğer süreçlere taşıyoruz.'),
      ('Kurumsal yapay zeka eğitimi', 'Şirketlere ve ekiplere yüz yüze ya da online yapay zeka eğitimleri veriyoruz. Eğitimler genel bir sunum değil, ekibinizin kendi işleri üzerinden ilerleyen uygulamalı çalışmalardır: doğru komut yazma, sonuçları kontrol etme, belgeyle ve veriyle çalışma, hangi işte hangi aracın uygun olduğu ve veri güvenliği. Eğitimden sonra ekibinizin elinde kendi işlerine göre hazırlanmış örnekler ve kullanım kuralları kalır. Nereden başlayacağınızı [şirketinizde yapay zekaya nereden başlamalısınız?](/blog/sirketinizde-yapay-zekaya-nereden-baslamalisiniz/) yazımızda adım adım anlattık.'),
      ('Kimler için uygun, kimler için değil?', 'Raporlama, teklif hazırlama, müşteri yazışmaları ya da içerik üretimi gibi her hafta tekrar eden işleri olan ve ekibinin zamanını daha değerli işlere ayırmak isteyen işletmeler için uygundur. Tek tıkla her şeyi çözecek hazır bir ürün arıyorsanız ya da süreçlerinizi değiştirmeye hiç zaman ayıramayacaksanız henüz doğru zaman olmayabilir; yapay zeka, ekibin onu kullanmayı öğrendiği ölçüde fayda sağlar. Hangi işlerde zaman kazandırdığını [işletmeler için yapay zekanın 8 kullanım alanı](/blog/isletmeler-icin-yapay-zeka-kullanim-alanlari/) yazımızda topladık.'),
      ('Örnek kullanım senaryoları', 'Aşağıdakiler temsili örneklerdir; her işletmede kurulum farklıdır. **Haftalık rapor:** satış ya da reklam verileri her pazartesi otomatik derlenir, yapay zeka özetini yazar, yönetici yalnızca kontrol eder. **Teklif hazırlama:** müşteri talebi ve fiyat listesinden ilk teklif taslağı hazırlanır, ekip düzeltip gönderir. **Müşteri soruları:** sık sorulan sorulara ilk yanıtı veren, cevabı bilmediğinde ekibe aktaran bir asistan kurulur. **İçerik akışı:** aylık konu planından sosyal medya ve blog taslakları markanızın diliyle hazırlanır, onaydan sonra yayınlanır. Bu kurulumlarda ChatGPT, Claude ya da Gemini gibi dil modellerini n8n, Make ya da Zapier gibi otomasyon araçlarıyla birlikte kullanıyoruz.'),
    ],
    'araclar': [('ChatGPT', 'chatgpt'), ('Claude', 'claude'), ('Gemini', 'gemini'), ('Microsoft Copilot', 'copilot'), ('Perplexity', 'perplexity'), ('Grok', 'grok'), ('DeepSeek', 'deepseek'), ('Mistral', 'mistral'), ('Midjourney', 'midjourney'), ('n8n', 'n8n'), ('Make', 'make'), ('Zapier', 'zapier')],
  },
  {
    'adres': 'web-tasarim', 'kisa': 'Web tasarım', 'renk': 'sky', 'guncelleme': '2026-10-22',
    'title': 'Ankara Web Tasarım | Web Sitesi Yaptırma | Clickbait',
    'description': 'Ankara web tasarım: mobil uyumlu, hızlı ve Google’a hazır kurumsal web siteleri; hosting ve bakım dahil. Türkiye geneline online hizmet.',
    'h1': 'Ankara web tasarım: hızlı, mobil uyumlu ve Google’da bulunabilir siteler',
    'giris': '2013’ten beri Ankara’dan kurumsal web siteleri ve e-ticaret mağazaları tasarlıyoruz. Tasarım, geliştirme, hosting ve bakımı tek ekipte yürütüyoruz; Türkiye’nin her yerinden müşterilerimizle online da çalışıyoruz.',
    'kartlar': [
      ('Kurumsal web sitesi', 'Markanızı anlatan, ziyaretçiyi aramaya ya da teklif istemeye yönlendiren siteler.'),
      ('E-ticaret ve WooCommerce', 'Ürün, stok, kargo ve ödeme altyapısıyla satışa hazır mağazalar.'),
      ('UI/UX tasarım', 'Önce kullanıcının yolunu çiziyor, sonra her ekranı o yola göre tasarlıyoruz.'),
      ('Özel ikon ve illüstrasyon', 'Hazır görseller yerine markanıza özel çizimler.'),
      ('Hosting ve bakım', 'Sunucu, SSL sertifikası, yedekleme ve güncellemeleri biz takip ediyoruz.'),
      ('Performans ve güvenlik denetimi', 'Mevcut sitenizin hızını, güvenliğini ve kullanılabilirliğini ölçüp raporluyoruz.'),
    ],
    'adimlar': [
      ('Keşif görüşmesi', 'Hedeflerinizi, hedef kitlenizi ve rakiplerinizi konuşuyoruz.'),
      ('Site haritası ve tasarım', 'Sayfa yapısını çıkarıyor, tasarımları onayınıza sunuyoruz.'),
      ('Geliştirme ve içerik', 'Siteyi kodluyor, içerikleri yerleştiriyor, arama motorlarına hazırlıyoruz.'),
      ('Yayın ve destek', 'Siteyi yayına alıyor, sonrasında bakım ve güncellemeleri sürdürüyoruz.'),
    ],
    'metin': [
      ('Bir web tasarım firması olarak nasıl çalışıyoruz?', 'Clickbait Dijital, 2013’ten beri Ankara’da web tasarım firması olarak kurumsal web siteleri ve e-ticaret mağazaları hazırlıyor. Sayfa planından tasarıma, geliştirmeden hosting ve bakıma kadar tüm süreci aynı ekipte yürütüyoruz; böylece işin her aşamasında tek bir muhatapla çalışırsınız.'),
      ('Ankara’da web tasarım firması seçerken nelere bakmalı?', 'Ankara’da web tasarım hizmeti veren çok sayıda firma var ve teklifler arasında büyük farklar olabilir. Bir firma seçerken yayındaki referans sitelerine telefonunuzdan bakın, teklifte neyin dahil olduğunu kontrol edin ve alan adı ile hosting hesaplarının sizin adınıza açılacağından emin olun. Ayrıntılı kontrol listesini [Ankara’da web sitesi yaptırırken dikkat edilmesi gereken 10 şey](/blog/ankara-web-sitesi-yaptirirken-dikkat-edilmesi-gerekenler/) yazımızda, maliyeti belirleyen kalemleri [web sitesi fiyatlarını neler belirler?](/blog/web-sitesi-fiyatlarini-neler-belirler/) yazımızda bulabilirsiniz.'),
      ('Teslim ettiğimiz her sitede neler var?', 'Hangi sektörde olursa olsun yayına aldığımız her sitede şu temel işler yapılmış olur: telefonda, tablette ve bilgisayarda düzgün görünen bir tasarım; sıkıştırılmış görseller ve hızlı açılan sayfalar; her sayfa için ayrı başlık, açıklama ve tek bir ana başlık (H1); site haritası, Search Console kaydı ve işletme bilgilerinizi Google’a anlatan yapılandırılmış veri; tek dokunuşla arama ve WhatsApp bağlantıları; form, arama ve WhatsApp tıklamalarını ölçen Google Analytics kurulumu; KVKK aydınlatma metni ve çerez onayı. Yani siteniz yayına girdiği gün Google’da bulunmaya hazır olur; SEO çalışmasına sıfırdan değil, sağlam bir temelden başlanır.'),
      ('Hız neden bu kadar önemli?', 'Ziyaretçilerin çoğu sitenize telefondan girer ve sayfa geç açılırsa beklemeden geri döner; Google da sayfa deneyimini sıralamada dikkate alır. Ekim 2026’da Ankara’da 101 işletme sitesini incelediğimizde sitelerin yalnızca %9’u Google’ın mobil hız testinde 90 ve üzeri puan aldı, %87’sinde sayfanın ana içeriği telefonda 4 saniyeden geç yükleniyordu. Kendi sitemizi de aynı ölçütlerle hazırladık: bu sayfa mobil testte 90’ın üzerinde puan alıyor. Bulguların tamamı [Ankara İşletme Siteleri Araştırması 2026](/blog/ankara-isletme-siteleri-arastirmasi-2026/) sayfasında.'),
      ('Kurumsal web sitesi mi, e-ticaret sitesi mi?', 'Ürünlerinizi internetten satmayacaksanız ihtiyacınız olan çoğu zaman bir kurumsal web sitesidir: ne yaptığınızı anlatan, güven veren ve ziyaretçiyi aramaya ya da teklif istemeye yönlendiren sayfalar. Hangi sayfaların olması gerektiğini [kurumsal web sitesinde olması gereken 8 sayfa](/blog/kurumsal-web-sitesinde-olmasi-gereken-sayfalar/) yazımızda anlattık. Online satış yapacaksanız ödeme, kargo ve stok altyapısıyla birlikte planlanan bir mağaza gerekir; bunun için [Ankara e-ticaret sitesi](/ankara-e-ticaret-sitesi/) sayfamıza bakabilirsiniz.'),
      ('Sitenizi yenilerken Google sıralamanızı korumak', 'Eski bir siteyi yenilerken en sık yapılan hata, eski sayfa adreslerini unutmaktır: Google’ın tanıdığı adresler bir anda hata vermeye başlar ve yıllar içinde kazanılan sıralamalar kaybolur. Yenileme projelerine eski sitenin hangi sayfalarının Google’dan ziyaretçi getirdiğini çıkararak başlıyor, her eski adresi yeni karşılığına kalıcı (301) yönlendirmeyle bağlıyor ve yayından sonraki haftalarda Search Console’u izliyoruz. Kendi sitemizi Ekim 2026’da WordPress’ten yeni altyapısına taşırken de aynı yöntemi uyguladık. Adım adım kontrol listesini [web sitenizi yenilerken Google sıralamanızı korumak](/blog/web-sitesi-yenilerken-google-siralamasini-korumak/) yazımızda topladık.'),
      ('Hangi sektörler için web sitesi tasarladık?', 'Eğitim (dil kursu, havacılık akademisi), yayıncılık, inşaat, otel ve konaklama sektörlerinden markalar için web siteleri hazırladık; bazılarını aşağıda görebilirsiniz. Her sektörde ziyaretçinin aradığı farklıdır: bir otelde odalar ve rezervasyon, bir inşaat firmasında tamamlanan projeler, bir eğitim kurumunda programlar ve kayıt bilgisi öne çıkar. Sayfa planını bu yüzden sektörünüzde müşterilerin gerçekte ne aradığına göre kuruyoruz.'),
      ('Ankara’da nerede çalışıyoruz?', 'Ofisimiz Çayyolu’nda: Ümit Mah. Meksika Cad. No:56/21, Çayyolu, Ankara ([haritada aç](https://share.google/u1DfuQgwwOlqnDbwp)). Çayyolu, Ümitköy ve çevresindeki işletmelerle ofisimizde yüz yüze görüşüyor, Ankara’nın diğer ilçelerinden ve Türkiye genelinden müşterilerimizle süreci online yürütüyoruz. Siteniz yayına girdikten sonra Google’da üst sıralara çıkmak için [SEO çalışmasını](/ankara-seo/) da aynı ekipte sürdürebiliriz.'),
    ],
    'ilgili': ['ankara-web-sitesi-yaptirirken-dikkat-edilmesi-gerekenler', 'web-sitesi-yenilerken-google-siralamasini-korumak', 'kurumsal-web-sitesinde-olmasi-gereken-sayfalar', 'web-sitesi-fiyatlarini-neler-belirler', 'ankara-isletme-siteleri-arastirmasi-2026'],
    'projeler': [
      ('Active English', 'Dil eğitimi · Ankara', 'active-english', 'https://active-languages.com/', 1400, 684),
      ('HUBEK Flight Academy', 'Havacılık eğitimi', 'hubek-flight-academy', '', 1400, 684),
      ('Psychology Times Türkiye', 'Yayıncılık', 'psychology-times-turkiye', 'https://psychologytimes.com.tr/', 1400, 684),
      ('Uslu Yapı', 'İnşaat', 'uslu-yapi', '', 1400, 684),
      ('Form Çayyolu', 'Otel ve konaklama · Ankara', 'form-cayyolu', 'https://formcayyolu.com.tr/', 1600, 611),
    ],
    'sss': [
      ('Ankara’daki web tasarım firmaları arasında nasıl seçim yapmalıyım?', 'Yayındaki referans sitelerine telefonunuzdan bakın, teklifte tasarım, içerik, hosting ve bakımın dahil olup olmadığını kalem kalem isteyin ve alan adı ile hosting hesaplarının kimin adına açılacağını sorun. Fiyatı düşük ama kapsamı dar bir teklif sonunda daha pahalıya gelebilir.'),
      ('Ankara dışındaki firmalarla da çalışıyor musunuz?', 'Evet. Görüşmeleri online yapıyor, süreci uzaktan yürütüyoruz. Ankara’daki müşterilerimizle Çayyolu’ndaki ofisimizde de buluşuyoruz.'),
      ('Bir web sitesi ne kadar sürede hazır olur?', 'Sayfa sayısına, özel özelliklere ve içeriklerin hazır olmasına göre değişir. Keşif görüşmesinden sonra size net bir takvim veriyoruz.'),
      ('Web sitesi fiyatı neye göre belirleniyor?', 'Sayfa sayısı, özel tasarım ihtiyacı, e-ticaret gibi ek özellikler ve içerik üretimi fiyatı belirler. İhtiyacınızı dinledikten sonra kalem kalem teklif hazırlıyoruz.'),
      ('Siteyi kendimiz güncelleyebilir miyiz?', 'İsterseniz yönetim paneli kuruyor ve ekibinize kullanımını gösteriyoruz. Güncellemeleri bizim yapmamızı da tercih edebilirsiniz.'),
      ('Mevcut sitemizi yenileyebilir misiniz?', 'Evet. Önce mevcut sitenin hızını, arama motoru durumunu ve içeriklerini inceliyoruz. Google’daki sıralamanızı korumak için eski adresleri yeni sayfalara yönlendiriyoruz.'),
      ('Siteler SEO’ya uygun teslim ediliyor mu?', 'Evet. Her sayfanın başlığı, açıklaması ve ana başlığı ayrı yazılır; site haritası, Search Console kaydı ve yapılandırılmış veri kurulur, görseller sıkıştırılır. Bu temel her sitede yapılır; düzenli içerik ve sıralama takibi isteyenlere aylık SEO hizmeti de veriyoruz.'),
      ('Web sitesi hangi altyapıyla yapılıyor?', 'İhtiyaca göre seçiyoruz. İçeriği sık güncellenecek sitelerde ekibinizin kullanabileceği bir yönetim paneli kuruyoruz; online satış yapacak mağazalarda WooCommerce gibi e-ticaret altyapıları kullanıyoruz. Seçimi teklif aşamasında gerekçesiyle birlikte paylaşıyoruz.'),
      ('Siteden gelen talepleri ölçebilecek miyiz?', 'Evet. Form gönderimlerini, telefon ve WhatsApp tıklamalarını Google Analytics’te ayrı ayrı ölçecek şekilde kuruyoruz. Böylece sitenin kaç talep getirdiğini ve reklamlarınızın etkisini görebilirsiniz.'),
    ],
  },
  {
    'adres': 'dijital-pazarlama', 'kisa': 'Dijital pazarlama', 'renk': 'blue', 'guncelleme': '2026-10-27',
    'title': 'Ankara Dijital Pazarlama Ajansı | Reklam ve SEO | Clickbait',
    'description': 'Ankara’da dijital pazarlama: Google Ads ve Meta reklam yönetimi, SEO ve medya planlama. Bütçenizi doğru kanala koyuyor, sonuçları her ay raporluyoruz.',
    'h1': 'Ankara dijital pazarlama: reklam bütçeniz doğru kanalda, sonuçlar ölçülebilir',
    'giris': 'Google ve Meta reklamlarınızı kuruyor, yönetiyor ve her ay raporluyoruz. Google’da organik olarak bulunmanız için SEO çalışmasını da aynı ekipte yürütüyoruz. Ankara’yı ya da Türkiye genelini hedefleyen kampanyalar hazırlıyoruz.',
    'kartlar': [
      ('Google Ads yönetimi', 'Arama, görüntülü reklam ve YouTube kampanyaları; anahtar kelime ve dönüşüm takibi.'),
      ('Meta reklamları', 'Instagram ve Facebook’ta hedef kitle, kreatif ve bütçe yönetimi.'),
      ('SEO', 'Teknik SEO, içerik planı ve yerel SEO ile Google’da organik görünürlük.'),
      ('Dijital medya planlama', 'Hangi kanala ne kadar bütçe ayrılacağını hedeflerinize göre planlıyoruz.'),
      ('Dönüşüm takibi', 'Form, arama ve WhatsApp dönüşümlerini ölçerek reklamın gerçek getirisini gösteriyoruz.'),
      ('Raporlama', 'Her ay sade bir raporla neyin işe yaradığını ve sonraki adımı paylaşıyoruz.'),
    ],
    'adimlar': [
      ('Hedef ve bütçe', 'Ne satmak, kime ulaşmak istediğinizi ve bütçenizi netleştiriyoruz.'),
      ('Kurulum', 'Hesapları, dönüşüm takibini ve ilk kampanyaları kuruyoruz.'),
      ('Optimizasyon', 'Sonuçlara göre hedeflemeyi, metinleri ve bütçe dağılımını iyileştiriyoruz.'),
      ('Raporlama', 'Her ay sonuçları ve bir sonraki ayın planını paylaşıyoruz.'),
    ],
    'metin': [
      ('Ankara dijital pazarlama ajansı olarak nereden başlıyoruz?', 'Reklam açmadan önce iki şeye bakıyoruz: müşterilerinizin sizi nasıl aradığı ve sitenizin gelen ziyaretçiyi talebe çevirip çeviremediği. Telefonda hızlı açılmayan, arama ve WhatsApp düğmesi olmayan ya da form gönderimlerini ölçmeyen bir siteye reklam bütçesi harcamak, kovaya delik açıkken su doldurmaya benzer. Bu yüzden ilk iş olarak sitenizi ve ölçüm altyapısını kontrol ediyor, eksikleri gideriyor, ardından hedefinize uygun kanalları seçiyoruz. Küçük bir işletme olarak dijital pazarlamaya nereden başlayacağınızı adım adım [küçük işletmeler için dijital pazarlama rehberimizde](/blog/kucuk-isletmeler-icin-dijital-pazarlama/) anlattık.'),
      ('Hangi kanal hangi işletmeye uygun?', 'Müşterileriniz hizmetinizi Google’da arıyorsa (tesisatçı, muhasebeci, dil kursu, web tasarım gibi) önce aramaları karşılamak gerekir: Google Ads hemen görünmenizi sağlar, SEO ise aynı aramalarda reklam ödemeden bulunmanızı sağlayan uzun vadeli çalışmadır. İkisinin farkını [Google Ads mi SEO mu?](/blog/google-ads-mi-seo-mu/) yazımızda anlattık; organik tarafı [aylık SEO hizmetimizle](/ankara-seo/) yürütüyoruz. Ürününüz ya da hizmetiniz görsel olarak ilgi çekiyorsa ve henüz aranmıyorsa (yeni bir konut projesi, bir restoran, bir moda markası) Instagram ve Facebook reklamları daha uygundur; ayrıntılar [Ankara Instagram reklam ajansı](/ankara-instagram-reklam-ajansi/) sayfamızda. Geniş bir kitleye kısa sürede ulaşmak gereken kampanyalarda dijitali [TV, radyo ve açık hava reklamlarıyla](/ankara-reklam-ajansi/) tek bir medya planında birleştiriyoruz.'),
      ('Reklam bütçesini nasıl planlıyoruz?', 'Bütçeyi baştan tüm kanallara dağıtmak yerine hedefe en yakın kanalla başlamayı öneriyoruz. İlk haftalarda hangi aramaların, hangi kitlelerin ve hangi reklam metinlerinin talep getirdiğini ölçüyor, getirmeyenleri kapatıyor ve bütçeyi işe yarayan tarafa kaydırıyoruz. Bir kanal düzenli olarak talep getirmeye başladığında ikinci kanalı ekliyoruz. Böylece bütçe tahmine göre değil, ölçülen sonuca göre büyür. Google reklamlarında bu süreci [Ankara Google Ads ajansı](/ankara-google-ads-ajansi/) sayfamızda ayrıntılı anlattık.'),
      ('Sonuçları nasıl ölçüyoruz?', 'Tıklama ve gösterim sayısı tek başına bir şey söylemez; bizim için asıl ölçü, reklamın getirdiği talep ve bir talebin size kaça mal olduğudur. Bu yüzden her projede form gönderimlerini, telefon ve WhatsApp tıklamalarını Google Analytics’te ayrı ayrı ölçecek şekilde kuruyor, reklam hesaplarına dönüşüm olarak bağlıyoruz. Aylık raporda harcamayı, gelen talepleri, talep başına maliyeti, en iyi çalışan aramaları ve reklamları, bir sonraki ayın planıyla birlikte sade bir dille paylaşıyoruz.'),
      ('Hangi markaların dijital pazarlamasını yürütüyoruz?', 'Rast Grup’un Ankara’daki konut projelerinin (Avend Fera, Avend Doku, Avend Voven, Palais Bozbük ve Magna Epic) dijital pazarlamasını yürütüyoruz. Saye Emlak, EKM, German Dental ve İstanbul Hair Center’ın Google ve Meta reklam hesaplarını yönetiyoruz. Sağlık, eğitim, havacılık, inşaat, emlak, yayıncılık ve konaklama sektörlerinden markalarla çalıştık. Her sektörde müşterinin karar verme süresi ve kullandığı kanal farklı olduğu için planı sektörünüze göre kuruyoruz.'),
    ],
    'ilgili': ['kucuk-isletmeler-icin-dijital-pazarlama', 'google-ads-mi-seo-mu', 'instagram-reklami-nasil-verilir', 'acik-hava-reklami-rehberi', 'seo-nedir-ne-zaman-sonuc-verir'],
    'sss': [
      ('Küçük bir işletme dijital pazarlamaya nereden başlamalı?', 'Önce web sitenizin telefonda hızlı açıldığından ve gelen talepleri (form, telefon, WhatsApp) ölçtüğünden emin olun. Ardından tek bir kanalla başlayın: müşterileriniz sizi Google’da arıyorsa Google Ads ve SEO, aramıyorsa Instagram reklamları. Sonuçları ölçüp işe yarayan kanalı büyütün.'),
      ('Google reklamı mı, Instagram reklamı mı vermeliyim?', 'Hizmetiniz Google’da aranıyorsa Google reklamları talebi doğrudan yakalar. Ürününüz görsel olarak ilgi çekiyorsa ya da henüz aranmıyorsa Instagram reklamları sizi yeni kişilere tanıtır. Çoğu işletme için doğru cevap, birinden başlayıp ölçtükten sonra diğerini eklemektir.'),
      ('Reklam bütçesi ne kadar olmalı?', 'Sektörünüze, hedef bölgenize ve hedeflerinize göre değişir. Küçük bir test bütçesiyle başlayıp sonuçlara göre artırmayı öneriyoruz.'),
      ('SEO sonuçları ne zaman görülür?', 'SEO uzun vadeli bir çalışmadır; ilk iyileşmeler genellikle birkaç ay içinde görülmeye başlar. Süreyi rekabet ve sitenizin mevcut durumu belirler.'),
      ('Reklamları sadece Ankara’yı hedefleyecek şekilde ayarlayabilir misiniz?', 'Evet. Reklamları il, ilçe ya da belirli bir mesafe içindeki kullanıcılarla sınırlayabiliyoruz. Türkiye geneline açılan kampanyalar da hazırlıyoruz.'),
      ('Reklam hesapları kimin adına açılıyor?', 'Hesapların sizin adınıza açılmasını ve sahipliğin sizde kalmasını öneriyoruz; biz yönetici olarak erişiyoruz.'),
      ('Raporları ne sıklıkla paylaşıyorsunuz?', 'Her ay rapor paylaşıyoruz; kampanya dönemlerinde ihtiyaca göre daha sık özetler de hazırlıyoruz.'),
    ],
  },
  {
    'adres': 'sosyal-medya-yonetimi', 'kisa': 'Sosyal medya yönetimi', 'renk': 'dark',
    'title': 'Ankara Sosyal Medya Ajansı ve Yönetimi | Clickbait',
    'description': 'Ankara sosyal medya ajansı: aylık içerik planı, post, story ve reels tasarımı, paylaşım takvimi ve raporlama. Instagram ve LinkedIn’de markanızın sesi oluyoruz.',
    'h1': 'Ankara sosyal medya ajansı: planlı, tutarlı ve markanıza ait içerikler',
    'giris': 'Her ay hedeflerinize göre bir içerik planı hazırlıyor, tasarımları üretiyor, paylaşımları takvime göre yayınlıyor ve ay sonunda sonuçları raporluyoruz. Ankara’daki markalarla yüz yüze, Türkiye genelindeki markalarla online çalışıyoruz.',
    'kartlar': [
      ('Aylık içerik planı', 'Hedeflerinize ve önemli günlere göre bir ayın paylaşımlarını önceden planlıyoruz.'),
      ('Post, story ve reels', 'Markanızın kimliğine uygun tasarımlar ve kısa videolar üretiyoruz.'),
      ('Metin yazımı', 'Paylaşım metinlerini ve başlıkları markanızın diliyle yazıyoruz.'),
      ('Paylaşım takvimi', 'İçerikleri takipçilerinizin en aktif olduğu saatlere göre yayınlıyoruz.'),
      ('Fotoğraf ve video çekimi', 'İçerikler için ihtiyaç duyulan çekimleri planlıyor ve gerçekleştiriyoruz.'),
      ('Aylık raporlama', 'Erişim, etkileşim ve takipçi değişimini sade bir raporla paylaşıyoruz.'),
    ],
    'adimlar': [
      ('Marka ve hedef', 'Markanızın dilini, hedef kitlenizi ve rakiplerinizi inceliyoruz.'),
      ('Aylık plan', 'İçerik planını ve tasarımları onayınıza sunuyoruz.'),
      ('Yayın', 'Onaylanan içerikleri takvime göre yayınlıyoruz.'),
      ('Rapor ve iyileştirme', 'Ay sonunda sonuçları paylaşıp bir sonraki ayın planını güncelliyoruz.'),
    ],
    'metin': [
      ('Ankara’da sosyal medya yönetimini nasıl yürütüyoruz?', 'Her ay markanızın o ayki hedefini belirleyerek başlıyoruz: bilinirlik mi, etkileşim mi, yoksa mesaj ve randevu gibi talepler mi? Ardından önemli tarihleri ve kampanyalarınızı takvime işliyor, 3–5 içerik başlığı belirliyor ve ayın paylaşımlarını tarih, format ve konuya göre bir takvimde topluyoruz. Metinler ve tasarımlar ay başlamadan hazırlanıp tek seferde onayınıza sunuluyor; onaylanan içerikler takvime göre yayınlanıyor. Bu süreci örnek bir takvimle [aylık sosyal medya içerik planı nasıl hazırlanır?](/blog/aylik-sosyal-medya-icerik-plani/) yazımızda anlattık.'),
      ('Ay sonunda neyi raporluyoruz?', 'Takipçi sayısından çok işe yarayan ölçülere bakıyoruz: içeriklerin kaç kişiye ulaştığı, kaç kez kaydedilip paylaşıldığı, profil ziyaretleri ve sosyal medyadan gelen mesaj ve talepler. En iyi sonuç veren konu ve formatları bir sonraki ayın planında artırıyor, işe yaramayanları azaltıyoruz. İçeriklerinizi daha fazla kişiye ulaştırmak isterseniz sponsorlu paylaşımları [Ankara Instagram reklam ajansı](/ankara-instagram-reklam-ajansi/) hizmetimizle aynı plana ekliyoruz.'),
    ],
    'sss': [
      ('Hangi platformlarda hizmet veriyorsunuz?', 'Ağırlıklı olarak Instagram ve LinkedIn’de çalışıyoruz. Markanıza uygunsa diğer platformlar için de plan hazırlıyoruz.'),
      ('İçerikleri yayından önce görebilir miyiz?', 'Evet. Aylık plan ve tasarımlar onayınıza sunulur, yalnızca onaylanan içerikler yayınlanır.'),
      ('Ayda kaç paylaşım yapılıyor?', 'Paylaşım sayısı hedeflerinize ve seçtiğiniz pakete göre belirlenir; teklifte net sayıyı yazıyoruz.'),
      ('Sponsorlu reklamlar dahil mi?', 'Sponsorlu paylaşımları dijital pazarlama hizmetimiz kapsamında yönetiyoruz. İki hizmeti birlikte alabilirsiniz.'),
      ('Ankara’daki sosyal medya ajansları arasında nasıl seçim yapmalıyım?', 'Ajansın yönettiği gerçek hesaplara bakın; aylık plan ve onay süreci olup olmadığını, kapsamın ve paylaşım sayılarının yazılı olduğunu, mesaj ve yorumlara kimin cevap vereceğini ve hesapların sizin adınıza kalacağını kontrol edin. Ayrıntılı listeyi blogumuzdaki “Sosyal medya ajansı seçerken dikkat edilmesi gereken 9 şey” yazısında topladık.'),
      ('Ankara dışındaki markalarla çalışıyor musunuz?', 'Evet. Planlama, onay ve raporlama süreçlerini online yürütüyoruz.'),
    ],
  },
  {
    'adres': 'kreatif-hizmetler', 'kisa': 'Kreatif hizmetler', 'renk': 'lime',
    'title': 'Ankara Logo Tasarım ve Kurumsal Kimlik | Clickbait',
    'description': 'Ankara logo tasarım ve kurumsal kimlik: logo, renk, yazı tipi, şablon ve basılı işlerle markanız her yerde aynı dili konuşsun. Türkiye geneline online.',
    'h1': 'Ankara logo tasarım ve kurumsal kimlik: markanız her yerde aynı dili konuşsun',
    'giris': 'Logodan kartvizite, sosyal medya şablonundan sunum dosyasına kadar markanızın tüm görsel dilini tek elden tasarlıyoruz. Ankara’daki ofisimizde ya da online çalışabiliriz.',
    'kartlar': [
      ('Logo tasarımı', 'Markanızın karakterini taşıyan, her boyutta okunabilir logolar.'),
      ('Kurumsal kimlik kılavuzu', 'Renk, yazı tipi ve kullanım kurallarını tek dosyada topluyoruz.'),
      ('Kartvizit ve basılı işler', 'Kartvizit, antetli kâğıt, broşür ve afiş tasarımları.'),
      ('Sosyal medya şablonları', 'Ekibinizin kolayca kullanabileceği, markaya uygun şablonlar.'),
      ('Özel ikon ve illüstrasyon', 'Web siteniz ve sunumlarınız için markanıza özel çizimler.'),
      ('Sunum ve katalog', 'Satış sunumları ve ürün katalogları için düzenli, okunaklı tasarımlar.'),
    ],
    'adimlar': [
      ('Tanışma', 'Markanızın hikâyesini, hedef kitlesini ve rakiplerini konuşuyoruz.'),
      ('Yön belirleme', 'Farklı tasarım yönlerini sunuyor, birlikte birini seçiyoruz.'),
      ('Geliştirme', 'Seçilen yönü logodan uygulamalara kadar geliştiriyoruz.'),
      ('Teslim', 'Tüm dosyaları ve kullanım kılavuzunu teslim ediyoruz.'),
    ],
    'sss': [
      ('Logo tasarım süreci nasıl ilerliyor?', 'Önce markanızı tanıyoruz, ardından farklı tasarım yönleri sunuyoruz. Seçtiğiniz yönü birlikte geliştirip son hâline getiriyoruz.'),
      ('Teslimde hangi dosyaları alıyoruz?', 'Logonun vektörel dosyalarını (SVG, PDF) ve web için PNG dosyalarını, renk kodları ve kullanım kurallarıyla birlikte teslim ediyoruz.'),
      ('Mevcut logomuzu yenileyebilir misiniz?', 'Evet. Markanızın tanınırlığını kaybetmeden, mevcut logonuzu bugünün kullanımlarına uygun hâle getirebiliyoruz.'),
      ('Sadece sosyal medya şablonu yaptırabilir miyiz?', 'Evet. Mevcut kimliğinize uygun şablonları ayrı bir iş olarak da hazırlıyoruz.'),
      ('Ankara dışından çalışabilir miyiz?', 'Evet. Tüm süreci online görüşmeler ve paylaşılan dosyalar üzerinden yürütebiliyoruz.'),
    ],
  },
]

# ---------------------------------------------------------------- Ankara'ya özel sayfalar
# Yüksek hacimli "Ankara + hizmet" aramaları için. Ana hizmet sayfalarıyla aynı kelimeyi hedeflemezler
# (çakışma olmasın diye); her biri bir ana hizmetin altındadır ('ust'). Alanlar HIZMETLER ile aynı, ek olarak:
# 'metin' = sayfaya özgü açıklayıcı bölümler (başlık, paragraf; [bağlantı](/adres/) ve **kalın** kullanılabilir).
ANKARA = [
  {
    'adres': 'ankara-seo', 'kisa': 'Ankara SEO', 'ust': 'dijital-pazarlama', 'renk': 'blue',
    'title': 'Ankara SEO Ajansı | Aylık SEO Hizmeti | Clickbait', 'guncelleme': '2026-10-21',
    'description': 'Ankara SEO hizmeti: teknik SEO, yerel SEO, Google İşletme Profili ve içerikle sitenizi Google’da öne çıkarmak için çalışıyoruz. Her ay şeffaf rapor.',
    'h1': 'Ankara SEO: Google’da sizi arayan müşteriler sizi bulsun',
    'giris': 'Sitenizin teknik altyapısını düzeltiyor, müşterilerinizin Ankara’da ve Türkiye genelinde gerçekten aradığı kelimelere göre içerik planlıyor, Google İşletme Profilinizi güçlendiriyoruz. Her ay neyin değiştiğini sade bir raporla paylaşıyoruz.',
    'kapsam': 'Ankara SEO ajansı olarak neler yapıyoruz?',
    'kartlar': [
      ('Teknik SEO', 'Site hızı, mobil uyum, dizine eklenme hataları, site haritası ve yönlendirmeleri düzeltiyoruz.'),
      ('Anahtar kelime araştırması', 'Müşterilerinizin Google’da gerçekte ne aradığını verilerle çıkarıyor, öncelik sırasına koyuyoruz.'),
      ('Yerel SEO', 'Google İşletme Profili, müşteri yorumları ve tutarlı adres bilgileriyle harita sonuçlarında görünmenizi sağlıyoruz.'),
      ('Sayfa içi SEO', 'Başlık, açıklama, ara başlık, iç bağlantı ve yapılandırılmış veriyi her sayfa için düzenliyoruz.'),
      ('İçerik planı', 'Hizmet sayfalarınızı destekleyen, müşterilerinizin sorularını cevaplayan yazılar planlıyor ve yazıyoruz.'),
      ('Aylık rapor', 'Search Console ve Analytics verileriyle hangi aramalarda yükseldiğinizi gösteriyoruz.'),
    ],
    'adimlar': [
      ('SEO denetimi', 'Sitenizin teknik durumunu, içeriklerini ve rakiplerinizi inceliyoruz.'),
      ('Strateji', 'Hedef kelimeleri ve hangi sayfanın hangi kelimeyle sıralanacağını belirliyoruz.'),
      ('Uygulama', 'Teknik düzeltmeleri yapıyor, sayfaları ve içerikleri hazırlıyoruz.'),
      ('Ölçüm ve iyileştirme', 'Sıralamaları izliyor, yükselmeye yakın sayfaları güçlendiriyoruz.'),
    ],
    'metin': [
      ('Ankara’da SEO neden ayrı bir çalışma ister?', 'Birisi “Ankara diş kliniği” ya da “Çayyolu emlak ofisi” diye aradığında Google sonuçları arayanın konumuna göre sıralar. Bu yüzden Ankara’da hizmet veren bir işletme için SEO yalnızca web sitesinden ibaret değildir: Google İşletme Profili, müşteri yorumları, adres ve telefon bilgilerinin her yerde aynı olması da sıralamayı etkiler. Çalışmaya bu yerel sinyallerle başlıyor, ardından Türkiye genelinde aranan kelimelere geçiyoruz. Profilinizi nasıl güçlendireceğinizi [Google İşletme Profili rehberimizde](/blog/google-isletme-profili-ile-yerel-aramalarda-one-cikmak/) anlattık.'),
      ('Ankara’daki işletme sitelerinde en sık gördüğümüz eksikler', 'Ekim 2026’da Ankara’da 18 sektörden 101 işletme sitesini aynı yöntemle inceledik. Sitelerin yalnızca %9’u Google’ın mobil hız testinde 90 ve üzeri puan aldı; %87’sinde sayfanın ana içeriği telefonda 4 saniyeden geç yükleniyor. Ana sayfaların %26’sında konuyu söyleyen ana başlık (H1) yok, %10’unda Google’da görünen açıklama yazılmamış, %42’sinde işletme bilgisini Google’a bildiren yapılandırılmış veri bulunmuyor. Bu eksiklerin çoğu büyük bir yenileme gerektirmeden düzeltilebilir; SEO çalışmamıza da genellikle bunlarla başlıyoruz. Tüm bulgular ve yöntem [Ankara İşletme Siteleri Araştırması 2026](/blog/ankara-isletme-siteleri-arastirmasi-2026/) sayfasında.'),
      ('SEO mu, Google Ads mi?', 'Google Ads ile reklam verdiğiniz sürece üst sıralarda görünürsünüz; bütçe bittiğinde görünürlük de durur. SEO ise organik sonuçlarda kalıcı bir yer edinmek için yapılan çalışmadır: sonuç vermesi zaman alır ama tıklama başına ödeme yapmazsınız. Çoğu işletmeye ikisini birlikte yürütmeyi, reklamdan gelen verilerle SEO önceliklerini belirlemeyi öneriyoruz. Farkları [Google Ads mi SEO mu?](/blog/google-ads-mi-seo-mu/) yazımızda karşılaştırdık; reklam tarafı için [Ankara Google Ads ajansı](/ankara-google-ads-ajansi/) sayfamıza bakabilirsiniz.'),
      ('SEO hizmeti fiyatını neler belirler?', 'SEO hizmetinin fiyatını birkaç şey belirler: sitenizin teknik durumu ve ne kadar düzeltme gerektiği, hedeflediğiniz kelimelerin sayısı ve rekabeti, her ay ne kadar yeni içerik üretileceği, Google İşletme Profili ve yorum yönetiminin işe dahil olup olmadığı, sitenizin altyapısı ve düzenlemeleri kimin yapacağı. Bu yüzden herkese aynı paketi sunmak yerine önce sitenizi inceliyor, ardından her ay neler yapılacağını kalem kalem yazan bir teklif hazırlıyoruz. Teklifleri karşılaştırırken nelere bakmanız gerektiğini [SEO firması seçerken sorulacak 10 soru](/blog/seo-firmasi-secerken-sorulacak-sorular/) yazımızda topladık.'),
      ('Çalışma modelimiz: aylık SEO hizmeti', 'SEO’yu tek seferlik bir iş olarak değil, aylık bir hizmet olarak yürütüyoruz. İlk ay sitenizin teknik denetimini yapıyor, düzeltilmesi gerekenleri öncelik sırasına koyuyor ve hangi sayfanın hangi aramayla sıralanacağını gösteren bir kelime haritası çıkarıyoruz. Sonraki aylarda teknik düzeltmeleri uyguluyor, sayfa içi düzenlemeleri yapıyor, yeni içerikleri planlayıp yazıyor ve Google İşletme Profilinizi güncel tutuyoruz. Her ayın sonunda Search Console verileriyle hazırlanmış sade bir rapor paylaşıyor, bir sonraki ayın planını birlikte konuşuyoruz.'),
      ('Yapay zeka aramalarında görünürlük (GEO)', 'Müşterileriniz artık yalnızca Google’da arama yapmıyor; ChatGPT, Gemini, Perplexity ve Google’ın yapay zeka özetlerine de soru soruyor. Bu araçların işletmenizi doğru tanıması ve önermesi için SEO çalışmasına yapay zeka görünürlüğünü de ekliyoruz: işletme bilgilerinizi yapılandırılmış veriyle tanımlıyor, sayfalarınıza alıntılanabilir kısa tanımlar ve sık sorulan sorular ekliyor, yapay zeka araçları için site özeti (llms.txt) hazırlıyor ve Bing Webmaster Tools’un yapay zeka raporuyla görünürlüğü izliyoruz. Ayrıntıları [GEO nedir?](/blog/geo-nedir-yapay-zeka-aramalarinda-gorunmek/) yazımızda anlattık; yapay zekayı işinizde kullanmak için [Ankara yapay zeka danışmanlığı](/yapay-zeka-danismanligi/) sayfamıza bakabilirsiniz.'),
      ('Hangi sektörlerde çalıştık?', 'Sağlık (diş ve saç ekimi klinikleri, psikologlar), eğitim (dil kursları, havacılık akademisi), inşaat ve emlak, yayıncılık, konaklama ve kamu kurumlarından markalarla çalıştık. Her sektörün arama davranışı farklıdır: bir psikolog için semt adıyla yapılan aramalar, bir dil kursu için “ankara ingilizce kursu fiyatları” gibi fiyat aramaları öne çıkar. Bu yüzden çalışmaya sektörünüzde müşterilerin gerçekte ne aradığını çıkararak başlıyoruz. Teknik tarafta nelere baktığımızı [teknik SEO kontrol listesi](/blog/teknik-seo-kontrol-listesi/) yazımızda topladık.'),
      ('Ankara’da nerede çalışıyoruz?', 'Ofisimiz Çayyolu’nda: Ümit Mah. Meksika Cad. No:56/21, Çayyolu, Ankara ([haritada aç](https://share.google/u1DfuQgwwOlqnDbwp)). Çayyolu, Ümitköy ve çevresindeki işletmelerle ofisimizde yüz yüze görüşüyor, Ankara’nın diğer ilçelerinden ve Türkiye genelinden müşterilerimizle online çalışıyoruz.'),
      ('Neyi söz veriyoruz, neyi vermiyoruz?', 'Sıralamayı Google kendi algoritmasıyla belirler; “bir ayda ilk sıra” gibi sözler veren bir ajansa temkinli yaklaşmanızı öneririz. Bizim sözümüz yaptığımız her işi açıkça raporlamak, Google’ın kurallarına uygun çalışmak ve sonuçları Search Console verileriyle ölçmektir. Sitenizi yeniliyorsanız sıralamanızı kaybetmemek için eski adresleri yeni sayfalara yönlendirmeyi de bu sürece dahil ediyoruz.'),
    ],
    'sss': [
      ('SEO ne kadar sürede sonuç verir?', 'İlk iyileşmeler genellikle birkaç ay içinde görülmeye başlar. Rekabetin yüksek olduğu kelimelerde bu süre uzar. Sitenizin mevcut durumuna bakıp size gerçekçi bir takvim veriyoruz.'),
      ('SEO fiyatları neye göre belirlenir?', 'Sitenizin teknik durumu, hedeflediğiniz kelimelerin sayısı ve rekabeti, ne kadar içerik üretileceği fiyatı belirler. Denetimden sonra kalem kalem teklif hazırlıyoruz.'),
      ('Sitemizi siz yapmadınız, yine de SEO yapabilir misiniz?', 'Evet. Önce mevcut sitenin altyapısını inceliyoruz. Düzeltilmesi gereken teknik sorunları raporluyor, sitenizi yapan ekiple ya da doğrudan biz düzenliyoruz.'),
      ('Yerel SEO nedir?', 'İşletmenizin “Ankara” ya da “yakınımdaki” gibi konum içeren aramalarda ve Google Haritalar’da görünmesi için yapılan çalışmadır. Google İşletme Profili, müşteri yorumları ve tutarlı iletişim bilgileri bu çalışmanın temelidir.'),
      ('Ankara’da SEO uzmanı mı, SEO ajansı mı?', 'Clickbait Dijital’de SEO çalışmalarını ajansın kurucusu Şakir Yavuz bizzat yürütüyor. Böylece bir SEO uzmanıyla doğrudan çalışırken tasarım, içerik ve reklam ihtiyaçlarınız için ajans ekibinden de destek alırsınız.'),
      ('Ankara’daki SEO ajansları arasında nasıl seçim yapmalıyım?', 'Sitenizi inceleyip somut tespitlerle gelen, ilk ayların iş planını yazılı veren, sıra garantisi vermeyen ve hesapları sizin adınıza açan bir ajans seçin. Görüşmede sorulacak soruları blogumuzdaki “SEO firması seçerken sorulacak 10 soru” yazısında topladık.'),
      ('ChatGPT ve Gemini gibi yapay zeka araçlarında görünmek için ne yapıyorsunuz?', 'İşletme bilgilerinizi yapılandırılmış veriyle tanımlıyor, sayfalarınıza kısa ve alıntılanabilir tanımlar ekliyor, yapay zeka araçları için site özeti (llms.txt) hazırlıyor ve görünürlüğü Bing Webmaster Tools’un yapay zeka raporuyla izliyoruz.'),
      ('Aylık raporda neler oluyor?', 'Hangi aramalarda göründüğünüz, sıralama değişimleri, siteye gelen ziyaretçi ve talep sayısı ile o ay yaptığımız işler. Bir sonraki ayın planını da rapora ekliyoruz.'),
    ],
    'ilgili': ['seo-nedir-ne-zaman-sonuc-verir', 'teknik-seo-kontrol-listesi', 'geo-nedir-yapay-zeka-aramalarinda-gorunmek', 'seo-firmasi-secerken-sorulacak-sorular', 'ankara-isletme-siteleri-arastirmasi-2026'],
    'sonuclar': {
      'donem': '19 Temmuz – 18 Ekim 2026 (son 3 ay)',
      'siteler': [
        {'ad': 'Active English', 'tur': 'Dil kursu · Ankara', 'adres': 'https://active-languages.com/', 'tiklama': '6.500', 'gosterim': '620.000', 'konum': '8,1',
         'not': 'Adında “Ankara” geçen 524 farklı aramada görünüyor.', 'ornek': [('ankara ingilizce kursu fiyatları', '2,7'), ('ankara dil kursları fiyatları', '2,8'), ('ankara ispanyolca kursu', '5,4')]},
        {'ad': 'Psychology Times', 'tur': 'Psikoloji yayını · Türkiye geneli', 'adres': 'https://psychologytimes.com.tr/', 'tiklama': '21.500', 'gosterim': '805.000', 'konum': '9,1',
         'not': '1.000’den fazla farklı aramada görünüyor.', 'ornek': [('psychology times', '1,3'), ('pembe fil deneyi', '1,9'), ('psikolog feyzanur gündüz', '5,1')]},
        {'ad': 'Rojin Nazik', 'tur': 'Psikolog · Ankara', 'adres': 'https://www.psikologrojinnazik.com/', 'tiklama': '440', 'gosterim': '33.100', 'konum': '15,3',
         'not': 'Yerel bir psikolog sitesi; marka ve bilgi aramalarında üst sıralarda.', 'ornek': [('psikolog teşhis koyar mı', '2,1'), ('rojin nazik', '4,2'), ('yaşamkent psikolog', '12,9')]},
      ],
    },
  },
  {
    'adres': 'ankara-google-ads-ajansi', 'kisa': 'Ankara Google Ads ajansı', 'ust': 'dijital-pazarlama', 'renk': 'blue',
    'title': 'Ankara Google Ads Ajansı | Reklam Yönetimi | Clickbait',
    'description': 'Ankara Google Ads ajansı: arama, YouTube ve Performance Max kampanyalarınızı kuruyor, dönüşüm takibiyle ölçüyor ve her ay raporluyoruz.',
    'h1': 'Ankara Google Ads ajansı: reklam bütçeniz müşteri getiren aramalara gitsin',
    'giris': 'Google reklamlarınızı sıfırdan kuruyor ya da mevcut hesabınızı devralıyoruz. Doğru kelimeleri seçiyor, alakasız tıklamaları eliyor, form, telefon ve WhatsApp taleplerini ölçüyoruz. Her ay harcanan bütçenin neye dönüştüğünü açıkça raporluyoruz.',
    'kapsam': 'Google Ads yönetimimizde neler var?',
    'kartlar': [
      ('Arama ağı kampanyaları', 'Hizmetinizi arayan kişilere, aradıkları anda Google’ın en üstünde görünürsünüz.'),
      ('Performance Max ve Alışveriş', 'E-ticaret siteleri için ürünlerinizi Google’ın tüm kanallarında gösteren kampanyalar.'),
      ('YouTube ve görüntülü reklam', 'Markanızı hedef kitlenize video ve görsellerle tanıtan kampanyalar.'),
      ('Kelime ve negatif kelime yönetimi', 'Bütçeyi boşa harcatan alakasız aramaları düzenli olarak eliyoruz.'),
      ('Dönüşüm takibi', 'Form, telefon araması ve WhatsApp taleplerini ölçerek hangi reklamın müşteri getirdiğini gösteriyoruz.'),
      ('Konum ve saat hedefleme', 'Reklamları Ankara’ya, belirli ilçelere ya da ofisinize belirli bir mesafeye ve çalışma saatlerinize göre sınırlıyoruz.'),
    ],
    'adimlar': [
      ('Hedef ve bütçe', 'Hangi hizmeti, kime, hangi bütçeyle duyurmak istediğinizi netleştiriyoruz.'),
      ('Kurulum', 'Hesabı, dönüşüm takibini ve ilk kampanyaları kuruyoruz.'),
      ('Optimizasyon', 'İlk haftalardan itibaren kelimeleri, metinleri ve teklifleri iyileştiriyoruz.'),
      ('Raporlama', 'Her ay harcamayı, gelen talepleri ve sonraki ayın planını paylaşıyoruz.'),
    ],
    'metin': [
      ('Ankara’yı hedefleyen bir kampanya nasıl kurulur?', 'Google Ads’te konum ayarı sanıldığından önemlidir. Varsayılan ayar, reklamınızı Ankara’da bulunan kişilerin yanında “Ankara ile ilgilenen” başka şehirlerdeki kişilere de gösterebilir. Yerel hizmet veren bir işletmede bu ayarı yalnızca Ankara’da bulunan kişilerle sınırlıyor; gerekirse belirli ilçelere ya da ofisinize belirli bir mesafeye daraltıyoruz. Reklamları çalışma saatlerinize göre planlayıp telefonu açamayacağınız saatlerde bütçe harcanmasını önlüyoruz.'),
      ('Bütçe ne kadar olmalı?', 'Tek bir doğru rakam yoktur; sektörünüzdeki rekabet, hedef bölgenin büyüklüğü ve bir müşterinin size kazandırdığı tutar belirler. Küçük bir test bütçesiyle başlayıp hangi kelimelerin gerçekten talep getirdiğini görmeyi, sonra bütçeyi bu kelimelere yoğunlaştırmayı öneriyoruz. Hedef müşteri sayınızdan geriye doğru bütçe hesabını örnek bir tabloyla [Google Ads bütçesi nasıl belirlenir?](/blog/google-ads-butcesi-nasil-belirlenir/) yazımızda anlattık; reklamla mı SEO ile mi başlamanız gerektiğini [Google Ads mi SEO mu?](/blog/google-ads-mi-seo-mu/) yazımızda ele aldık.'),
      ('Reklam hesabı kimin adına açılır?', 'Hesabın sizin adınıza açılmasını ve sahipliğin sizde kalmasını öneriyoruz; biz yönetici olarak erişiyoruz. Böylece birlikte çalışmayı bıraksanız bile geçmiş veriler ve kampanyalar sizde kalır. Organik görünürlük için reklamla birlikte [SEO çalışması](/ankara-seo/) da yürütebiliriz.'),
    ],
    'sss': [
      ('Mevcut Google Ads hesabımızı devralabilir misiniz?', 'Evet. Önce hesabı inceleyip boşa giden harcamaları ve eksik dönüşüm takibini raporluyoruz, ardından iyileştirmeye başlıyoruz.'),
      ('Reklamlar ne zaman yayına girer?', 'Hesap ve dönüşüm takibi kurulup reklamlar Google’ın onayından geçtikten sonra yayına girer. Kurulum takvimini ilk görüşmede netleştiriyoruz.'),
      ('Sadece Ankara’daki kişilere reklam gösterebilir miyiz?', 'Evet. Reklamları il, ilçe ya da belirli bir mesafeyle sınırlayabiliyoruz. Türkiye geneline açılan kampanyalar da hazırlıyoruz.'),
      ('Reklam bütçesi ile ajans ücreti ayrı mı?', 'Evet. Reklam bütçesi doğrudan Google’a ödenir; yönetim ücretimizi teklifte ayrıca belirtiyoruz.'),
      ('Instagram reklamlarını da yönetiyor musunuz?', 'Evet. Meta (Instagram ve Facebook) reklamlarını da aynı ekipte yönetiyor, iki kanalın sonuçlarını tek raporda karşılaştırıyoruz.'),
    ],
  },
  {
    'adres': 'ankara-reklam-ajansi', 'kisa': 'Ankara reklam ajansı', 'ust': 'dijital-pazarlama', 'renk': 'dark', 'guncelleme': '2026-10-22',
    'title': 'Ankara Reklam Ajansı | TV, Açık Hava ve Dijital | Clickbait',
    'description': 'Ankara reklam ajansı: kampanya fikri, TV reklam filmi, radyo, açık hava, medya planlama ve Google, Instagram reklamları tek ekipte. 2013’ten beri.',
    'h1': 'Ankara reklam ajansı: TV’den açık havaya, radyodan dijitale tek ekip',
    'giris': 'Kampanya fikrinden reklam filmine, billboarddan Google ve Instagram reklamlarına kadar tam kapsamlı reklam hizmeti veriyoruz. Hangi mecrada ne kadar görüneceğinizi tek bir medya planında topluyor, üretimi ve yayını aynı ekipte yürütüyoruz. 2013’ten beri Çayyolu’ndaki ofisimizden Ankara’daki markalarla çalışıyoruz.',
    'kapsam': 'Reklam ajansı olarak neler yapıyoruz?',
    'kartlar': [
      ('Kampanya fikri ve strateji', 'Markanızın mesajını, hedef kitlesini ve kampanyanın ana fikrini birlikte belirliyoruz.'),
      ('TV reklam filmi', 'Senaryodan çekime ve kurguya kadar reklam filminin prodüksiyonunu yönetiyoruz.'),
      ('Medya planlama ve satın alma', 'TV, radyo, açık hava ve dijitalde hangi kanalda ne zaman görüneceğinizi planlıyor, yayın alanlarını satın alıyoruz.'),
      ('Radyo reklamı', 'Radyo spotunu hazırlıyor, kanal ve saat planını yapıyoruz.'),
      ('Açık hava reklamı', 'Billboard, raket ve megalight gibi alanların tasarımını, yer kiralamasını ve uygulamasını üstleniyoruz.'),
      ('Google reklamları', 'Arama, YouTube ve görüntülü reklam kampanyalarını kuruyor ve yönetiyoruz.'),
      ('Instagram ve Facebook reklamları', 'Hedef kitle, kreatif ve bütçe yönetimiyle Meta reklamları.'),
      ('Reklam kreatifleri', 'Afiş, ilan, sosyal medya görseli, kısa video ve reklam metinlerini üretiyoruz.'),
      ('Ölçüm ve raporlama', 'Dijital kanallardan gelen talepleri ölçüyor, kampanyanın sonuçlarını raporluyoruz.'),
    ],
    'adimlar': [
      ('Tanışma', 'Markanızı, hedef kitlenizi, rakiplerinizi ve bütçenizi konuşuyoruz.'),
      ('Fikir ve medya planı', 'Kampanya fikrini ve hangi mecrada, ne zaman, ne kadar bütçeyle görüneceğinizi planlıyoruz.'),
      ('Üretim ve yayın', 'Filmi, spotu, açık hava ve dijital tasarımları hazırlıyor, onayınızdan sonra yayına alıyoruz.'),
      ('Ölçüm', 'Sonuçları izliyor, işe yarayan mecraya daha fazla bütçe ayırıyoruz.'),
    ],
    'metin': [
      ('Tam kapsamlı reklam ajansı olarak hangi mecralarda çalışıyoruz?', 'Televizyon, radyo, açık hava, basılı ilan ve dijital mecraların hepsinde çalışıyoruz. Bir kampanyada hangi mecranın kullanılacağına bütçenize ve hedefinize göre birlikte karar veriyoruz: geniş bir kitlede bilinirlik kazanmak için TV ve açık hava, belirli bir kitleye ulaşıp sonucu ölçmek için Google ve Instagram reklamları öne çıkar. Hepsini tek bir medya planında topladığımız için mecralar birbirinin tekrarı değil, devamı olur.'),
      ('TV reklamı: filmden yayın planına', 'TV reklamında iş iki parçadan oluşur: filmin kendisi ve yayın planı. Senaryo, çekim ve kurgu aşamalarını yönetiyor, filmi markanızın diliyle hazırlıyoruz. Yayın tarafında hedef kitlenizin izlediği kanalları ve kuşakları seçiyor, yayın alanlarını sizin adınıza satın alıyoruz. Aynı filmin kısa sürümlerini YouTube ve sosyal medya reklamlarında da kullanarak bütçenizden daha fazla verim alıyoruz.'),
      ('Radyo ve açık hava reklamı', 'Radyoda kısa ve akılda kalan bir spot hazırlıyor, dinleyici profilinize uygun kanal ve saatleri planlıyoruz. Açık havada billboard, raket ve megalight gibi alanlar için tasarımı hazırlıyor, Ankara’da hedef kitlenizin en çok geçtiği noktalarda yer kiralıyor ve uygulamayı takip ediyoruz. Açık hava tasarımlarında mesajı birkaç saniyede okunacak kadar kısa tutuyoruz. Türleri, yer seçimini ve ölçümü [açık hava reklamı rehberimizde](/blog/acik-hava-reklami-rehberi/) anlattık.'),
      ('Geleneksel mecralar ve dijital birlikte nasıl çalışır?', 'Bir kişi reklamınızı televizyonda ya da bir billboardda gördükten sonra çoğu zaman markanızı Google’da arar ya da Instagram hesabınıza bakar. Bu yüzden geleneksel kampanyaları dijitalle birlikte planlıyoruz: o aramaları Google reklamları ve [SEO](/ankara-seo/) ile karşılıyor, kampanya döneminde sosyal medya ve web sitesini aynı mesaja hazırlıyoruz. Dijital tarafı [Ankara Google Ads ajansı](/ankara-google-ads-ajansi/) ve [Ankara Instagram reklam ajansı](/ankara-instagram-reklam-ajansi/) sayfalarımızda ayrıntılı anlattık.'),
      ('Neden tek ekip?', 'Reklam filmini bir ajans, billboard tasarımını başka bir tasarımcı, dijital reklamları ve web sitesini üçüncü bir firma yaptığında mesajlar birbirini tutmaz ve sorun çıktığında kimin sorumlu olduğu belirsizleşir. Kampanya fikri, prodüksiyon, medya planı, [web sitesi](/web-tasarim/) ve [sosyal medya](/sosyal-medya-yonetimi/) aynı ekipte olduğunda kampanya tek bir plandan çıkar.'),
      ('Ankara’da nerede çalışıyoruz?', 'Ofisimiz Çayyolu’nda: Ümit Mah. Meksika Cad. No:56/21, Çayyolu, Ankara ([haritada aç](https://share.google/u1DfuQgwwOlqnDbwp)). Ankara’daki markalarla ofisimizde yüz yüze çalışıyor, Türkiye genelindeki markalarla planlama ve onay süreçlerini online yürütüyoruz.'),
    ],
    'sss': [
      ('Televizyon, radyo ve açık hava reklamı yapıyor musunuz?', 'Evet. TV reklam filminin prodüksiyonunu ve yayın planlamasını, radyo spotunu ve yayın planını, billboard, raket ve megalight gibi açık hava alanlarının tasarımını, yer kiralamasını ve uygulamasını üstleniyoruz. Dijital reklamları da aynı medya planının parçası olarak yönetiyoruz.'),
      ('Reklam filmini siz mi hazırlıyorsunuz?', 'Evet. Senaryodan çekime ve kurguya kadar prodüksiyon sürecini biz yönetiyoruz; film yayından önce onayınıza sunuluyor.'),
      ('Sadece dijital reklamla başlayabilir miyiz?', 'Evet. Bütçeniz ve hedefiniz dijitalle başlamaya uygunsa Google ve Instagram reklamlarıyla başlıyor, sonuçlara göre diğer mecraları ekliyoruz.'),
      ('Reklam bütçesi ile ajans ücreti ayrı mı?', 'Evet. Yayın ve yer kiralama bedelleri ile ajans hizmet ücretini teklifte ayrı kalemler olarak yazıyoruz.'),
      ('Sonuçları nasıl görüyoruz?', 'Dijital kanallarda harcamayı ve gelen talepleri ölçüp raporluyoruz. TV, radyo ve açık hava kampanyalarında yayın ve uygulama bilgilerini ve kampanya döneminde markanızın aranma ve dijital etkileşimindeki değişimi raporluyoruz.'),
      ('Ankara dışındaki markalarla çalışıyor musunuz?', 'Evet. Planlama, onay ve raporlama süreçlerini online yürütüyoruz; Ankara’daki müşterilerimizle Çayyolu’ndaki ofisimizde de buluşuyoruz.'),
    ],
    'ilgili': ['acik-hava-reklami-rehberi', 'google-ads-mi-seo-mu', 'instagram-reklami-nasil-verilir', 'google-isletme-profili-ile-yerel-aramalarda-one-cikmak'],
  },
  {
    'adres': 'ankara-e-ticaret-sitesi', 'kisa': 'Ankara e-ticaret sitesi', 'ust': 'web-tasarim', 'renk': 'sky',
    'title': 'Ankara E-Ticaret Sitesi Kurulumu | Online Mağaza | Clickbait',
    'description': 'Ankara’da e-ticaret sitesi kurulumu: mobil uyumlu mağaza tasarımı, ödeme ve kargo bağlantıları, SEO altyapısı ve reklam ölçümüyle satış yapan mağazalar.',
    'h1': 'Ankara e-ticaret sitesi: satışa hazır, yönetmesi kolay bir online mağaza',
    'giris': 'İşinize uygun altyapıyı seçiyor, mağazanızı tasarlıyor, ödeme ve kargo bağlantılarını kuruyor, ürünlerinizi Google’da bulunur hâle getiriyoruz. Açılıştan sonra reklam ve ölçümle satışların artmasına da yardımcı oluyoruz.',
    'kapsam': 'E-ticaret sitesi kurulumunda neler var?',
    'kartlar': [
      ('Mağaza tasarımı', 'Mobilde hızlı açılan, ürünü öne çıkaran ve satın almayı kolaylaştıran bir tasarım.'),
      ('Ürün ve stok yönetimi', 'Ürünleri, varyantları ve stokları ekibinizin kolayca yöneteceği bir panel.'),
      ('Ödeme altyapısı', 'Kullandığınız ödeme kuruluşu ya da bankanın sanal POS bağlantısını kuruyoruz.'),
      ('Kargo bağlantısı', 'Sipariş ve kargo takibini anlaşmalı kargo firmanızla birlikte çalışacak şekilde kuruyoruz.'),
      ('E-ticaret SEO’su', 'Kategori ve ürün sayfalarını Google’da bulunacak şekilde yapılandırıyoruz.'),
      ('Reklam ve ölçüm', 'Google Alışveriş ve Meta katalog reklamları için ürün akışı ve satış takibi.'),
    ],
    'adimlar': [
      ('İhtiyaç analizi', 'Ürün sayınızı, satış kanallarınızı ve büyüme planınızı konuşuyoruz.'),
      ('Altyapı ve tasarım', 'Size uygun altyapıyı seçiyor, mağaza tasarımını onayınıza sunuyoruz.'),
      ('Kurulum ve entegrasyon', 'Ürünleri, ödeme ve kargo bağlantılarını kuruyor, test siparişleriyle deniyoruz.'),
      ('Yayın ve büyüme', 'Mağazayı açıyor, reklam ve SEO ile ziyaretçi getirmeye başlıyoruz.'),
    ],
    'metin': [
      ('Hangi altyapıyı seçmeli?', 'İki temel yol var. Aylık ücretli hazır e-ticaret altyapıları hızlı açılır, bakımı altyapı firmasındadır; buna karşılık tasarım ve özellikler o altyapının sunduklarıyla sınırlıdır. WooCommerce gibi açık kaynak altyapılar daha esnektir ve site tamamen sizindir; buna karşılık sunucu, güncelleme ve güvenlik bakımı gerekir. Ürün sayınıza, bütçenize ve ekibinizin teknik imkânlarına göre birlikte karar veriyoruz.'),
      ('Açmadan önce hazır olması gerekenler', 'Ürün fotoğrafları ve açıklamaları, fiyat ve stok bilgileri, bir ödeme kuruluşu ya da banka ile sanal POS anlaşması ve bir kargo anlaşması. Yasal metinler (mesafeli satış sözleşmesi, ön bilgilendirme formu, iade koşulları, KVKK aydınlatma metni) de gereklidir; bunları hukuk danışmanınızla hazırlamanızı öneriyoruz, biz siteye yerleştiriyoruz. Genel olarak dikkat edilecekleri [Ankara’da web sitesi yaptırırken dikkat edilmesi gereken 10 şey](/blog/ankara-web-sitesi-yaptirirken-dikkat-edilmesi-gerekenler/) yazımızda topladık.'),
      ('Açıldıktan sonra satış nasıl gelir?', 'Yeni bir mağazaya ziyaretçi kendiliğinden gelmez. İlk aylarda Google Alışveriş ve Instagram reklamlarıyla satış başlatıyor, aynı anda kategori sayfaları ve blog içerikleriyle organik trafiği büyütüyoruz. Reklam tarafını [Ankara Google Ads ajansı](/ankara-google-ads-ajansi/), organik tarafı [Ankara SEO](/ankara-seo/) sayfalarımızda anlattık. Maliyeti etkileyen kalemler için [web sitesi fiyatlarını neler belirler?](/blog/web-sitesi-fiyatlarini-neler-belirler/) yazımıza bakabilirsiniz.'),
    ],
    'sss': [
      ('E-ticaret sitesi ne kadar sürede açılır?', 'Ürün sayısına, seçilen altyapıya ve içeriklerin hazır olmasına göre değişir. İhtiyaç analizinden sonra size net bir takvim veriyoruz.'),
      ('Ürünleri kendimiz ekleyebilir miyiz?', 'Evet. Yönetim panelini kuruyor ve ekibinize ürün ekleme, sipariş ve stok takibini gösteriyoruz.'),
      ('Pazaryerlerinde de satış yapıyoruz, site gerekli mi?', 'Pazaryerleri hızlı satış sağlar ama müşteri ve marka pazaryerine aittir. Kendi siteniz markanızı büyütmenizi, müşterilerinize doğrudan ulaşmanızı ve komisyon ödememenizi sağlar. Çoğu marka ikisini birlikte yürütür.'),
      ('Mevcut e-ticaret sitemizi yenileyebilir misiniz?', 'Evet. Ürünleri, müşteri verilerini ve Google’daki sıralamanızı koruyarak yeni altyapıya taşıyabiliyoruz.'),
      ('Siteyi açtıktan sonra destek veriyor musunuz?', 'Evet. Bakım, güncelleme ve teknik destek hizmeti sunuyor; isterseniz reklam ve SEO çalışmasını da sürdürüyoruz.'),
    ],
  },
  {
    'adres': 'ankara-instagram-reklam-ajansi', 'kisa': 'Ankara Instagram reklam ajansı', 'ust': 'dijital-pazarlama', 'renk': 'dark',
    'title': 'Ankara Instagram Reklam Ajansı | Meta Reklamları | Clickbait',
    'description': 'Ankara Instagram reklam ajansı: Instagram ve Facebook reklamlarınızı kitle, kreatif ve bütçe yönetimiyle kuruyor, talepleri ölçüp her ay raporluyoruz.',
    'h1': 'Ankara Instagram reklam ajansı: doğru kişiye, doğru görselle, ölçülebilir sonuçla',
    'giris': 'Instagram ve Facebook reklamlarınızı tek ekipte planlıyor, tasarlıyor ve yönetiyoruz. Reklamı kime göstereceğinizi, ne söyleyeceğinizi ve bütçenin nasıl harcanacağını birlikte belirliyor; gelen mesaj, form ve aramaları ölçüyoruz.',
    'kapsam': 'Instagram reklam yönetimimizde neler var?',
    'kartlar': [
      ('Hedef kitle kurgusu', 'Konum, yaş, ilgi alanı ve mevcut müşteri listelerinize benzer kitlelerle reklamı doğru kişiye gösteriyoruz.'),
      ('Reklam kreatifleri', 'Instagram’ın akış, story ve reels alanlarına uygun görsel, video ve metinler üretiyoruz.'),
      ('Mesaj ve form kampanyaları', 'WhatsApp’a, Instagram DM’e ya da form doldurmaya yönlendiren kampanyalar kuruyoruz.'),
      ('Yeniden pazarlama', 'Sitenizi ziyaret eden ya da profilinizle etkileşime geçen kişilere tekrar ulaşıyoruz.'),
      ('Ölçüm kurulumu', 'Meta pikseli ve dönüşüm takibiyle reklamdan gelen talepleri ölçüyoruz.'),
      ('Aylık rapor', 'Harcanan bütçeyi, gelen talepleri ve bir sonraki ayın planını sade bir raporla paylaşıyoruz.'),
    ],
    'adimlar': [
      ('Hedef ve kitle', 'Neyi, kime, hangi bütçeyle duyurmak istediğinizi netleştiriyoruz.'),
      ('Kreatif ve kurulum', 'Görselleri ve metinleri hazırlıyor, kampanyaları ve ölçümü kuruyoruz.'),
      ('Test ve iyileştirme', 'Farklı görsel ve kitleleri deniyor, iyi sonuç vereni büyütüyoruz.'),
      ('Raporlama', 'Her ay sonuçları ve sonraki adımları paylaşıyoruz.'),
    ],
    'metin': [
      ('Instagram reklamı kimler için uygun?', 'Google’da sizi arayan müşteriler zaten bir ihtiyacı fark etmiş kişilerdir. Instagram ise henüz aramaya başlamamış kişilere ulaşmanın yoludur: ürününüz ya da hizmetiniz görsel olarak anlatılabiliyorsa, belirli bir yaş grubuna ya da bölgeye hitap ediyorsa ve yeni müşterilerin sizi tanıması gerekiyorsa Instagram reklamları güçlü bir kanaldır. Restoran ve kafeler, güzellik ve sağlık işletmeleri, eğitim kurumları, emlak ve e-ticaret markaları bu kanaldan sıkça faydalanır.'),
      ('Ankara’daki kişilere nasıl ulaşılır?', 'Meta reklamlarında konumu il, ilçe ya da belirli bir noktanın çevresindeki mesafe olarak seçebiliyoruz. Ofisinize ya da mağazanıza gelebilecek kişilere ulaşmak için bu alanı daraltıyor, online satış yapan markalarda Türkiye geneline açıyoruz. Reklamı gören kişinin WhatsApp’tan ya da Instagram mesajından tek dokunuşla size yazabilmesi, yerel işletmelerde en çok talep getiren kurgulardan biridir.'),
      ('Takipçi mi, müşteri mi?', 'Takipçi sayısı ya da beğeni, tek başına işinizi büyütmez. Kampanyaları başından itibaren mesaj, form ya da satış gibi ölçülebilir bir hedefe göre kuruyor ve sonuçları bu hedefe göre raporluyoruz. Arama tarafında görünür olmak için [Ankara Google Ads ajansı](/ankara-google-ads-ajansi/), düzenli içerik için [sosyal medya yönetimi](/sosyal-medya-yonetimi/) sayfalarımıza bakabilirsiniz.'),
    ],
    'sss': [
      ('Instagram reklam bütçesi ne kadar olmalı?', 'Hedef bölgenize, sektörünüze ve hedefinize göre değişir. Küçük bir test bütçesiyle başlayıp sonuç veren görsel ve kitleye bütçeyi aktarmayı öneriyoruz.'),
      ('Reklam bütçesi ile ajans ücreti ayrı mı?', 'Evet. Reklam bütçesi doğrudan Meta’ya ödenir; yönetim ücretimizi teklifte ayrıca belirtiyoruz.'),
      ('Reklam görsellerini siz mi hazırlıyorsunuz?', 'Evet. Görselleri, kısa videoları ve metinleri ekibimiz hazırlıyor; tüm içerikler yayından önce onayınıza sunuluyor.'),
      ('Reklam hesabı kimin adına açılıyor?', 'Reklam hesabının ve iş hesabının sizin adınıza olmasını, bizim yönetici olarak erişmemizi öneriyoruz. Böylece veriler ve kampanyalar sizde kalır.'),
      ('Facebook’ta da reklam çıkıyor mu?', 'Evet. Instagram ve Facebook reklamları aynı panelden yönetilir; hangi alanda görüneceğini sonuçlara göre birlikte belirliyoruz.'),
    ],
  },
]

# ---------------------------------------------------------------- Parçalar
# Kurucu / SEO'yu yürüten kişi ve blog yazarı. Yalnızca kullanıcının verdiği bilgiler (20.10.2026): kurucu, 2013, SEO'yu bizzat yürütüyor, yazılar onun deneyimine dayanıyor.
# Sektöre özel sayfalar: Ankara sayfalarıyla aynı şablon, ama Türkiye geneli hedeflenir ('sektor': True).
# Yalnızca gerçek referansı olan sektörler; doktor/avukat sayfalarında reklam yasağına uygun dil (bkz. seo-plani.md).
SEKTORLER = [
  {
    'adres': 'insaat-firmalari-icin-reklam-ajansi', 'kisa': 'İnşaat ve konut projeleri', 'ust': 'dijital-pazarlama', 'renk': 'dark', 'sektor': True,
    'guncelleme': '2026-10-29',
    'title': 'İnşaat Firmaları İçin Reklam Ajansı | Clickbait',
    'description': 'İnşaat firmaları ve konut projeleri için reklam: lansman, Google ve Instagram reklamları, açık hava, proje web sitesi ve satış ofisine gelen talebin ölçümü.',
    'h1': 'İnşaat firmaları için reklam ajansı: konut projenizi doğru alıcıya duyurun',
    'giris': 'Rast Grup’un Ankara’daki villa ve konut projelerinin dijital pazarlamasını yürütüyoruz. Proje lansmanından satış ofisine gelen ziyarete kadar reklamı, proje web sitesini ve ölçümü tek ekipte planlıyor; Türkiye’nin her yerindeki inşaat firmalarıyla çalışıyoruz.',
    'kapsam': 'İnşaat firmaları için neler yapıyoruz?',
    'kartlar': [
      ('Proje lansman kampanyası', 'Ön satış ve lansman döneminde projeyi Google, Instagram, açık hava ve gerektiğinde TV ve radyoda tek bir plan içinde duyuruyoruz.'),
      ('Google reklamları', 'Bölgede konut, villa ya da daire arayanları ve projenizin adını arayanları arama sonuçlarında yakalıyoruz.'),
      ('Instagram ve Facebook reklamları', 'Projenin bulunduğu bölgeye ve hedef kitleye göre görsel ve videolu reklamlar hazırlıyor, siteyi ziyaret edenlere yeniden ulaşıyoruz.'),
      ('Proje web sitesi', 'Daire tipleri, kat planları, konum, sosyal alanlar ve satış ofisi bilgisiyle telefonda hızlı açılan, talep toplayan proje siteleri.'),
      ('Açık hava ve saha', 'Satış ofisine giden yollarda billboard, raket ve megalight; şantiye panoları ve yönlendirmeler.'),
      ('Talep ve satış ölçümü', 'Form, telefon, WhatsApp ve satış ofisi randevularını kaynağına göre ölçüyor, hangi reklamın satışa yaklaştırdığını raporluyoruz.'),
    ],
    'adimlar': [
      ('Proje ve alıcı', 'Projenin konumunu, daire tiplerini, fiyat aralığını ve kimin alacağını birlikte netleştiriyoruz.'),
      ('Lansman planı', 'Web sitesini, görselleri, ölçümü ve kanal planını lansmandan önce hazırlıyoruz.'),
      ('Kampanya', 'Reklamları yayına alıyor, talepleri her hafta izleyip bütçeyi işe yarayan kanala kaydırıyoruz.'),
      ('Satış dönemine göre güncelleme', 'Ön satıştan teslime kadar mesajı ve kanalları projenin aşamasına göre değiştiriyoruz.'),
    ],
    'metin': [
      ('İnşaat firmalarının reklamı neden farklıdır?', 'Konut, çoğu insanın hayatında verdiği en büyük satın alma kararıdır. Alıcı bir projeyi haftalarca, bazen aylarca araştırır; siteye birkaç kez döner, kat planlarını inceler, ailesiyle konuşur ve satış ofisini ziyaret etmeden karar vermez. Bu yüzden inşaat sektöründe reklamın amacı tek tıklamayla satış değil, doğru kişiyi satış ofisine ya da bir görüşmeye getirmektir. Kampanyayı da tıklama sayısına göre değil, gelen randevu ve görüşme taleplerine göre yönetiyoruz.'),
      ('Konut projesi lansmanını nasıl planlıyoruz?', 'Lansmandan önce proje web sitesini, görselleri ve talep ölçümünü hazır hâle getiriyoruz; reklam başladığında gelen ilginin kaybolmaması için bu sıra önemlidir. Lansman döneminde projeyi Google’da arayanları yakalıyor, Instagram ve Facebook’ta hedef bölgedeki kitleye tanıtıyor, satış ofisine giden yollarda açık hava reklamlarıyla görünür kılıyoruz. Siteyi ziyaret edip talep bırakmayan kişilere yeniden ulaşan reklamlar, uzun karar sürecinde projenin akılda kalmasını sağlar. Açık hava tarafını [açık hava reklamı rehberimizde](/blog/acik-hava-reklami-rehberi/), TV ve radyoyu da içeren kampanyaları [Ankara reklam ajansı](/ankara-reklam-ajansi/) sayfamızda anlattık.'),
      ('Proje web sitesinde neler olmalı?', 'Alıcının aklındaki ilk sorular nettir: Nerede, hangi daire tipleri var, kat planı nasıl, ne zaman teslim, satış ofisine nasıl gidilir? İyi bir proje sitesi bu soruları ilk ekranlarda cevaplar: daire tipleri ve kat planları, konum ve ulaşım, sosyal alanlar, teslim tarihi, satış ofisi adresi ve tek dokunuşla arama, WhatsApp ve randevu. Sitenin telefonda hızlı açılması da şarttır, çünkü reklamdan gelen ziyaretçilerin çoğu telefondadır. Proje sitelerini bu ihtiyaçlara göre [web tasarım](/web-tasarim/) ekibimizle hazırlıyoruz.'),
      ('Hangi talep satışa dönüşüyor?', 'Her talebi kaynağıyla birlikte ölçüyoruz: Google reklamından gelen arama, Instagram’dan gelen mesaj, siteden gelen randevu formu. Satış ekibinizin “bizi nereden duydunuz?” sorusuna verilen cevapları da bu tabloya ekliyoruz. Aylık raporda harcamayı, gelen talepleri, talep başına maliyeti ve satış ofisine gelen ziyaretleri birlikte gösteriyoruz; böylece bütçe tahmine göre değil, satışa en çok yaklaştıran kanala göre büyür. Bütçeyi hedeften geriye doğru nasıl hesapladığımızı [Google Ads bütçesi nasıl belirlenir?](/blog/google-ads-butcesi-nasil-belirlenir/) yazımızda anlattık.'),
      ('Hangi inşaat ve emlak markalarıyla çalışıyoruz?', 'Rast Grup’un Ankara’daki konut ve villa projelerinin (Avend Fera, Avend Doku, Avend Voven, Palais Bozbük ve Magna Epic) dijital pazarlamasını yürütüyoruz. Uslu Yapı’nın web sitesini hazırladık ve Aden İncek projesinde birlikte çalıştık. Saye Emlak’ın Google ve Meta reklam hesaplarını yönetiyoruz. Ankara’daki projelerde satış ofisini ve bölgeyi yerinde tanıyarak, Türkiye’nin diğer şehirlerindeki projelerde süreci online yürüterek çalışıyoruz.'),
    ],
    'ilgili': ['acik-hava-reklami-rehberi', 'google-ads-butcesi-nasil-belirlenir', 'instagram-reklami-nasil-verilir', 'kucuk-isletmeler-icin-dijital-pazarlama'],
    'sss': [
      ('Konut projesi reklamına ne zaman başlanmalı?', 'Ön satış başlamadan önce. Proje web sitesi, görseller ve talep ölçümü lansmandan önce hazır olmalı; reklam başladığında gelen ilgi böylece kaybolmaz ve ilk haftalardan itibaren hangi kanalın işe yaradığı görülür.'),
      ('Hangi kanal daha çok satış getirir?', 'Projeye, bölgeye ve alıcı kitlesine göre değişir. Google reklamları projeyi zaten arayanları yakalar, Instagram ve Facebook projeyi henüz tanımayanlara duyurur, açık hava ise satış ofisinin çevresinde görünürlük sağlar. Hangisinin satışa daha çok yaklaştırdığını her talebi kaynağıyla ölçerek görüyor, bütçeyi buna göre kaydırıyoruz.'),
      ('Reklam bütçesi nasıl belirlenir?', 'Hedeflediğiniz satış ve satış ofisi ziyareti sayısından geriye doğru: kaç ziyaretten bir satış çıktığı, kaç talepten bir ziyaret geldiği ve bölgedeki tıklama maliyeti hesaba katılır. Küçük bir test döneminden sonra bütçeyi gerçek rakamlara göre güncelliyoruz.'),
      ('Proje web sitesini de siz mi hazırlıyorsunuz?', 'Evet. Daire tipleri, kat planları, konum ve satış ofisi bilgisiyle, telefonda hızlı açılan ve talep toplayan proje sitelerini reklamlarla birlikte planlıyoruz. Mevcut bir siteniz varsa önce onu inceliyoruz.'),
      ('Ankara dışındaki projelerle çalışıyor musunuz?', 'Evet. Planlama, onay ve raporlama süreçlerini online yürütüyoruz. Ankara’daki projelerde satış ofisinizde yüz yüze de çalışıyoruz.'),
    ],
  },
  {
    'adres': 'doktorlar-icin-seo', 'kisa': 'Doktorlar ve klinikler', 'ust': 'dijital-pazarlama', 'renk': 'blue', 'sektor': True,
    'guncelleme': '2026-10-30',
    'title': 'Doktorlar İçin SEO | Klinik ve Hekim Sitesi | Clickbait',
    'description': 'Doktorlar ve klinikler için SEO: sağlık tanıtım kurallarına uygun, reklam dili kullanmayan bilgilendirici içerik, hızlı web sitesi ve aylık rapor.',
    'h1': 'Doktorlar ve klinikler için SEO: kurallara uygun, hastanın sorusunu cevaplayan bir site',
    'giris': 'Hekimler ve sağlık kuruluşları için reklam yolları sınırlı; hastalar ise hekimini, tedavisini ve muayenehanesini Google’da araştırıyor. Web sitenizi ve içeriklerinizi reklam dili kullanmadan, doğru ve bilgilendirici bir dille hazırlıyor, Google’da bulunmanız için teknik SEO’yu aynı ekipte yürütüyoruz.',
    'kapsam': 'Doktorlar ve klinikler için neler yapıyoruz?',
    'kartlar': [
      ('Hekim ve klinik web sitesi', 'Uzmanlık alanlarınızı, eğitim ve deneyiminizi, muayenehane adresini ve randevu bilgisini anlatan, telefonda hızlı açılan siteler.'),
      ('Bilgilendirici sağlık içerikleri', 'Hastalarınızın sık sorduğu sorulara, tıbbi bilgileri sizin onayınızdan geçen, sade ve doğru bilgilendirme yazıları.'),
      ('Teknik SEO', 'Hız, mobil uyum, dizine eklenme ve yapılandırılmış veriyle sitenizin Google tarafından doğru anlaşılması.'),
      ('Kurallara uygunluk kontrolü', 'Her metni yayından önce tanıtım kuralları açısından gözden geçiriyor; fiyat, kampanya, hasta teşekkürü ve abartılı ifadeler kullanmıyoruz.'),
      ('KVKK ve hasta mahremiyeti', 'Randevu ve iletişim formları için KVKK aydınlatma metni, çerez onayı ve güvenli bağlantı.'),
      ('Aylık rapor', 'Search Console verileriyle sitenizin hangi aramalarda göründüğünü ve nasıl ilerlediğini her ay sade bir dille paylaşıyoruz.'),
    ],
    'adimlar': [
      ('Site ve içerik denetimi', 'Mevcut sitenizi teknik açıdan ve içerik dili açısından inceliyoruz.'),
      ('Plan', 'Hastalarınızın aradığı konuları ve hangi sayfanın hangi soruyu cevaplayacağını birlikte belirliyoruz.'),
      ('Uygulama ve yazılar', 'Teknik düzeltmeleri yapıyor, içerik taslaklarını hazırlayıp onayınıza sunuyoruz.'),
      ('Ölçüm ve rapor', 'Sıralamaları izliyor, her ay neyin değiştiğini raporluyoruz.'),
    ],
    'metin': [
      ('Doktorlar için SEO neden önemli?', 'Sağlık Bakanlığı’nın tanıtım ve bilgilendirme kuralları, hekimlerin ve sağlık kuruluşlarının açık ya da gizli reklam yapmasını yasaklıyor; sosyal medyada reklam, fiyat ve kampanya duyurusu, hasta teşekkürlerinin tanıtım amacıyla kullanılması da bu kapsamda. Öte yandan hastalar bir hekime gitmeden önce şikâyetini, tedavi seçeneklerini ve hekimin uzmanlığını Google’da araştırıyor. Bu yüzden doğru ve bilgilendirici bir web sitesiyle Google’da bulunmak, sağlık alanında en sağlam görünürlük yoludur. Önemli olan, sitedeki içeriğin tanıtım değil bilgilendirme diliyle yazılmasıdır.'),
      ('Sağlık sitelerinde nelere dikkat ediyoruz?', 'Sitede fiyat, indirim ve kampanya bilgisi kullanmıyoruz. Hasta teşekkürlerini ve memnuniyet yorumlarını tanıtım amacıyla yayınlamıyoruz. “En iyi”, “garantili”, “kesin sonuç” gibi abartılı ya da yanıltıcı ifadeler yazmıyoruz. Önce-sonra görsellerini kuralların koşullarını karşılamadan kullanmıyoruz. Sitede yalnızca hekimin gerçek uzmanlık alanlarını anlatıyor, tıbbi bilgileri hekimin onayı olmadan yayınlamıyoruz. Hukuki danışmanlık vermiyoruz; tereddüt olan konularda tabip odanızın ve hukuk danışmanınızın görüşünü esas alıyoruz.'),
      ('Hastalar Google’da ne arıyor?', 'Hastaların aramaları genellikle üç türdür: bir şikâyet ya da hastalık hakkında bilgi (“diş eti çekilmesi neden olur?”), tedavi süreci hakkında sorular (“implant tedavisi kaç seans sürer?”) ve semt ile uzmanlık adıyla yapılan aramalar (“çayyolu diş hekimi”). İyi bir hekim sitesi bu üçünü de karşılar: uzmanlık alanlarını ve hekimi tanıtan sayfalar, hastaların sık sorduğu sorulara verilen doğru cevaplar, adres, ulaşım, çalışma saatleri ve tek dokunuşla arama. Bir sitede hangi sayfaların bulunması gerektiğini [kurumsal web sitesinde olması gereken 8 sayfa](/blog/kurumsal-web-sitesinde-olmasi-gereken-sayfalar/) yazımızda anlattık.'),
      ('Google sağlık sitelerine neden daha sıkı bakar?', 'Google, sağlık gibi insanların hayatını doğrudan etkileyen konulardaki sayfalarda içeriğin kim tarafından yazıldığına ve ne kadar güvenilir olduğuna özellikle dikkat eder. Bu yüzden sağlık sitelerinde yazıların hekimin adıyla ve uzmanlığıyla yayınlanması, güncelleme tarihinin görünmesi, bilgilerin doğru ve sade olması sıralamayı da etkiler. Sitenizdeki her yazıyı bu ölçütlere göre hazırlıyor, teknik tarafta da [teknik SEO kontrol listemizdeki](/blog/teknik-seo-kontrol-listesi/) maddeleri uyguluyoruz. SEO’nun nasıl çalıştığını ve ne zaman sonuç verdiğini [SEO nedir, ne zaman sonuç verir?](/blog/seo-nedir-ne-zaman-sonuc-verir/) yazımızda anlattık.'),
      ('Sağlık alanında kimlerle çalıştık?', 'Diş ve saç ekimi klinikleri ile psikologlarla çalıştık: German Dental ve İstanbul Hair Center ile çalışıyor, Psikolog Rojin Nazik’in SEO çalışmasını yürütüyoruz; Çayyolu Psikolog ve Psikolog Duygu Sarıkaya’nın web sitelerini hazırladık. Ankara’da 29 psikolog ve terapi merkezi sitesini incelediğimiz araştırmanın bulgularını [Ankara İşletme Siteleri Araştırması 2026](/blog/ankara-isletme-siteleri-arastirmasi-2026/) sayfasında paylaştık. SEO çalışmasını [aylık SEO hizmetimiz](/ankara-seo/) olarak, siteyi [web tasarım](/web-tasarim/) ekibimizle hazırlıyoruz.'),
    ],
    'ilgili': ['seo-nedir-ne-zaman-sonuc-verir', 'teknik-seo-kontrol-listesi', 'kurumsal-web-sitesinde-olmasi-gereken-sayfalar', 'ankara-isletme-siteleri-arastirmasi-2026'],
    'sss': [
      ('Doktorlar SEO çalışması yaptırabilir mi?', 'Kurallar reklamı sınırlar; doğru ve objektif bilgilendirmeyi değil. Bu yüzden SEO çalışmasını reklam değil bilgilendirme diliyle yürütüyor, içeriklerin kurallara uygunluğunu yayından önce sizinle birlikte kontrol ediyoruz.'),
      ('Sitede fiyat ve kampanya bilgisi verebilir miyim?', 'Sağlık hizmetlerinde fiyat ve kampanya duyurusu tanıtım kurallarıyla sınırlandığı için hekim ve klinik sitelerinde fiyat ve kampanya bilgisi kullanmıyoruz.'),
      ('Hasta yorumlarını sitede kullanabilir miyim?', 'Hasta teşekkürlerinin ve memnuniyet paylaşımlarının tanıtım amacıyla kullanılması yasaklandığı için sitede hasta yorumlarına yer vermiyoruz.'),
      ('Sağlık yazılarını kim yazıyor?', 'Taslakları biz hazırlıyoruz; tıbbi bilgiler sizin onayınızdan geçmeden yayınlanmıyor. Yazılar sizin adınız ve uzmanlığınızla yayınlanıyor.'),
      ('SEO sonuçları ne zaman görülür?', 'SEO uzun vadeli bir çalışmadır; ilk iyileşmeler genellikle birkaç ay içinde görülür. Süreyi bölgenizdeki rekabet, uzmanlık alanınız ve sitenizin mevcut durumu belirler. Sıra garantisi vermiyoruz.'),
      ('Ankara dışındaki hekimlerle çalışıyor musunuz?', 'Evet. Planlama, içerik onayı ve raporlamayı online yürütüyoruz. Ankara’daki hekimlerle muayenehanelerinde ya da Çayyolu’ndaki ofisimizde yüz yüze de görüşüyoruz.'),
    ],
  },
  {
    'adres': 'psikologlar-icin-web-sitesi', 'kisa': 'Psikologlar', 'ust': 'web-tasarim', 'renk': 'lime', 'sektor': True,
    'guncelleme': '2026-10-31',
    'title': 'Psikologlar İçin Web Sitesi ve SEO | Clickbait',
    'description': 'Psikologlar ve terapi merkezleri için web sitesi ve SEO: danışan mahremiyetine ve sağlık tanıtım kurallarına uygun, telefonda hızlı açılan, bilgilendirici siteler.',
    'h1': 'Psikologlar için web sitesi ve SEO: güven veren, danışanın sorusunu cevaplayan bir site',
    'giris': 'Danışanlar bir psikoloğa ulaşmadan önce çoğu zaman Google’da hem yaşadıkları sorunu hem de semtlerindeki psikoloğu araştırıyor. Psikologlar ve terapi merkezleri için reklam dili kullanmayan, danışan mahremiyetini koruyan, telefonda hızlı açılan siteler hazırlıyor ve bu sitelerin Google’da bulunması için SEO çalışmasını aynı ekipte yürütüyoruz.',
    'kapsam': 'Psikologlar için neler yapıyoruz?',
    'kartlar': [
      ('Psikolog web sitesi', 'Çalışma alanlarınızı, eğitiminizi, görüşme biçimlerinizi (yüz yüze ya da online), adresinizi ve ulaşım bilgisini sade bir dille anlatan siteler.'),
      ('Bilgilendirici yazılar', 'Danışanların sık sorduğu sorulara, bilgileri sizin onayınızdan geçen, doğru ve anlaşılır yazılar.'),
      ('Teknik SEO', 'Hız, mobil uyum, dizine eklenme ve yapılandırılmış veriyle sitenizin Google tarafından doğru anlaşılması.'),
      ('Danışan mahremiyeti ve KVKK', 'Formlarda gereğinden fazla bilgi istemiyor; KVKK aydınlatma metni, çerez onayı ve güvenli bağlantıyı kuruyoruz.'),
      ('Kurallara uygunluk kontrolü', 'Her metni yayından önce sağlık tanıtım kuralları açısından gözden geçiriyor; danışan yorumu, kampanya ve abartılı ifade kullanmıyoruz.'),
      ('Aylık rapor', 'Search Console verileriyle sitenizin hangi aramalarda göründüğünü ve nasıl ilerlediğini her ay sade bir dille paylaşıyoruz.'),
    ],
    'adimlar': [
      ('Tanışma ve denetim', 'Çalışma alanlarınızı konuşuyor, varsa mevcut sitenizi teknik ve içerik açısından inceliyoruz.'),
      ('Site ve içerik planı', 'Danışanlarınızın aradığı konuları ve hangi sayfanın hangi soruyu cevaplayacağını birlikte belirliyoruz.'),
      ('Tasarım ve yazılar', 'Siteyi hazırlıyor, metin taslaklarını onayınıza sunuyor, onaydan sonra yayına alıyoruz.'),
      ('Ölçüm ve rapor', 'Google’daki görünürlüğü izliyor, her ay neyin değiştiğini raporluyoruz.'),
    ],
    'metin': [
      ('Danışanlar psikoloğunu nasıl arıyor?', 'Danışanların aramaları genellikle üç türdür: yaşadıkları durum hakkında bilgi (“kaygı bozukluğu nasıl geçer?”), terapi süreci hakkında sorular (“psikolog teşhis koyar mı?”, “online terapi işe yarar mı?”) ve semt adıyla yapılan aramalar (“çayyolu psikolog”). İyi bir psikolog sitesi bu üçünü de karşılar: sizi ve çalışma alanlarınızı tanıtan sayfalar, sık sorulan sorulara doğru ve sade cevaplar, adres, ulaşım, görüşme biçimleri ve tek dokunuşla arama. Bir sitede hangi sayfaların bulunması gerektiğini [kurumsal web sitesinde olması gereken 8 sayfa](/blog/kurumsal-web-sitesinde-olmasi-gereken-sayfalar/) yazımızda anlattık.'),
      ('Psikolog sitesinde güveni ne sağlar?', 'Terapiye başlamak kolay bir karar değildir; danışan siteye girdiğinde karşısındaki kişiyi tanımak ister. Bu yüzden gerçek bir fotoğraf, eğitim ve uzmanlık bilgisi, hangi konularda ve hangi yaklaşımla çalıştığınız, görüşmenin nasıl ilerlediği ve gizlilik ilkesi sitenin en önemli parçalarıdır. Sakin bir tasarım, okunaklı yazılar ve telefonda hızlı açılan sayfalar da güvenin parçasıdır. Görüşme biçimlerini (yüz yüze, online, çift ya da aile görüşmesi) ayrı ayrı anlatmak, danışanın aklındaki soruları ilk ziyarette cevaplar.'),
      ('Psikolog sitelerinde nelere dikkat ediyoruz?', 'Psikologlar ve klinik psikologlar sağlık meslek mensubu olduğu için Sağlık Bakanlığı’nın tanıtım ve bilgilendirme kurallarına tabidir. Bu yüzden sitede danışan yorumlarına ve teşekkürlerine yer vermiyor, kampanya ve indirim duyurusu yapmıyor, “en iyi”, “kesin çözüm” gibi abartılı ifadeler kullanmıyoruz. Yalnızca gerçek eğitim ve çalışma alanlarınızı anlatıyor, bilgilendirici yazıları sizin onayınız olmadan yayınlamıyoruz. Hukuki danışmanlık vermiyoruz; tereddüt olan konularda meslek derneğinizin ve hukuk danışmanınızın görüşünü esas alıyoruz.'),
      ('Danışan mahremiyeti sitede nasıl korunur?', 'Sağlık verileri KVKK’da özel nitelikli kişisel veri sayılır. Bu yüzden iletişim ve randevu formlarında yalnızca size ulaşmak için gereken bilgileri (ad, telefon, uygun saat) istiyor, yaşanan sorunun ayrıntısını formda sormuyoruz. Formların yanında KVKK aydınlatma metni, sitede çerez onayı ve güvenli bağlantı (SSL) bulunuyor; ziyaret istatistikleri yalnızca onay verilirse toplanıyor. Ankara’daki 29 psikolog ve terapi merkezi sitesini incelediğimiz araştırmada ana sayfasında KVKK metnine atıf bulunan sitelerin oranı yalnızca %28’di.'),
      ('Psikolog siteleri ne kadar hızlı?', 'Aynı araştırmada Ankara’daki psikolog ve terapi merkezi sitelerinin ortanca hız puanı 60, ana içeriğin telefonda ortanca açılma süresi 12,3 saniyeydi; Google’ın iyi kabul ettiği süre 2,5 saniye. Sitelerin %93’ünde tıklanabilir telefon, %76’sında WhatsApp bağlantısı vardı; yani iletişim tarafı güçlü, hız ve mahremiyet tarafı zayıf. Ölçümün ayrıntılarını [Ankara İşletme Siteleri Araştırması 2026](/blog/ankara-isletme-siteleri-arastirmasi-2026/) sayfasında paylaştık; teknik tarafta [teknik SEO kontrol listemizdeki](/blog/teknik-seo-kontrol-listesi/) maddeleri uyguluyoruz.'),
      ('Hangi psikologlarla çalışıyoruz?', 'Psikolog Rojin Nazik’in SEO çalışmasını yürütüyoruz: sitesi 19 Temmuz–18 Ekim 2026 arasında Google’da 33.100 kez göründü, 440 tıklama aldı ve “psikolog teşhis koyar mı” aramasında ortalama 2,1. sırada. Çayyolu Psikolog ve Psikolog Duygu Sarıkaya’nın web sitelerini hazırladık; psikoloji yayını Psychology Times’ın sitesini ve SEO çalışmasını da biz yürütüyoruz. Siteyi [web tasarım](/web-tasarim/) ekibimizle hazırlıyor, SEO’yu [aylık SEO hizmetimiz](/ankara-seo/) olarak sürdürüyoruz. SEO’nun ne zaman sonuç verdiğini [SEO nedir, ne zaman sonuç verir?](/blog/seo-nedir-ne-zaman-sonuc-verir/) yazımızda anlattık.'),
    ],
    'ilgili': ['ankara-isletme-siteleri-arastirmasi-2026', 'seo-nedir-ne-zaman-sonuc-verir', 'kurumsal-web-sitesinde-olmasi-gereken-sayfalar', 'teknik-seo-kontrol-listesi'],
    'sss': [
      ('Psikologlar web sitesi ve SEO çalışması yaptırabilir mi?', 'Sağlık tanıtım kuralları reklamı sınırlar; doğru ve objektif bilgilendirmeyi değil. Bu yüzden siteyi ve yazıları reklam değil bilgilendirme diliyle hazırlıyor, metinlerin kurallara uygunluğunu yayından önce sizinle birlikte kontrol ediyoruz.'),
      ('Sitede danışan yorumlarına yer verebilir miyim?', 'Sağlık hizmetlerinde teşekkür ve memnuniyet paylaşımlarının tanıtım amacıyla kullanılması kurallarla sınırlandığı için psikolog sitelerinde danışan yorumlarına yer vermiyoruz.'),
      ('Seans ücretini sitede yazabilir miyim?', 'Kampanya ve indirim duyurusu yapmıyoruz. Ücret bilgisinin nasıl paylaşılacağı konusunda meslek derneğinizin ve hukuk danışmanınızın görüşünü esas alıyoruz; sitede ücret yerine görüşmenin nasıl ilerlediğini anlatmayı öneriyoruz.'),
      ('Online görüşme yapıyorum, site Türkiye genelinde görünür mü?', 'Online görüşmeleri ayrı bir sayfada anlatıyor, bu sayfayı Türkiye genelindeki aramalar için, semt sayfalarını ise yerel aramalar için hazırlıyoruz.'),
      ('SEO sonuçları ne zaman görülür?', 'SEO uzun vadeli bir çalışmadır; ilk iyileşmeler genellikle birkaç ay içinde görülür. Süreyi bölgenizdeki rekabet, çalışma alanlarınız ve sitenizin mevcut durumu belirler. Sıra garantisi vermiyoruz.'),
      ('Ankara dışındaki psikologlarla çalışıyor musunuz?', 'Evet. Planlama, metin onayı ve raporlamayı online yürütüyoruz. Ankara’daki psikologlarla Çayyolu’ndaki ofisimizde ya da kendi ofislerinde yüz yüze de görüşüyoruz.'),
    ],
  },
  {
    'adres': 'egitim-kurumlari-icin-dijital-pazarlama', 'kisa': 'Eğitim kurumları ve dil kursları', 'ust': 'dijital-pazarlama', 'renk': 'sky', 'sektor': True,
    'guncelleme': '2026-10-31',
    'title': 'Eğitim Kurumları ve Dil Kursları İçin Dijital Pazarlama | Clickbait',
    'description': 'Dil kursları ve eğitim kurumları için dijital pazarlama: kayıt dönemine göre Google ve Instagram reklamları, program sayfaları, SEO ve kayıt talebinin ölçümü.',
    'h1': 'Eğitim kurumları ve dil kursları için dijital pazarlama: kayıt döneminde doğru öğrenciye ulaşın',
    'giris': 'Active English’in web sitesini hazırladık ve SEO çalışmasını yürütüyoruz; site Google’da adında “Ankara” geçen yüzlerce aramada görünüyor. Dil kursları, eğitim kurumları ve akademiler için kayıt dönemine göre reklam, program sayfaları, SEO ve kayıt talebinin ölçümünü tek ekipte planlıyor; Türkiye genelinde online çalışıyoruz.',
    'kapsam': 'Eğitim kurumları için neler yapıyoruz?',
    'kartlar': [
      ('Kayıt dönemi kampanyaları', 'Eylül, ocak ve yaz dönemi gibi kayıt zamanlarına göre reklam takvimini önceden planlıyor, bütçeyi talebin arttığı haftalarda yoğunlaştırıyoruz.'),
      ('Google reklamları', 'Kurs, program ve sınav hazırlığı arayanları arama sonuçlarında yakalıyor, alakasız aramaları eliyoruz.'),
      ('Instagram ve Facebook reklamları', 'Öğrenciye, veliye ya da çalışanlara göre ayrı mesajlar ve görsellerle kurumunuzu henüz aramaya başlamamış kişilere tanıtıyoruz.'),
      ('Program ve kurs sayfaları', 'Her program için seviye, süre, ders saatleri, şube ve kayıt bilgisini anlatan, telefonda hızlı açılan sayfalar.'),
      ('SEO', 'Kurs ve program aramalarında, semt ve şehir adıyla yapılan aramalarda reklam ödemeden bulunmanız için içerik ve teknik çalışma.'),
      ('Talep ve kayıt ölçümü', 'Form, telefon, WhatsApp ve seviye testi taleplerini programa ve kaynağa göre ölçüyor, hangi reklamın kayda dönüştüğünü raporluyoruz.'),
    ],
    'adimlar': [
      ('Programlar ve öğrenci', 'Hangi programın kime (öğrenci, veli, çalışan, şirket) satıldığını ve kayıt dönemlerini birlikte çıkarıyoruz.'),
      ('Sayfa ve ölçüm hazırlığı', 'Program sayfalarını, talep formlarını ve ölçümü reklam başlamadan hazırlıyoruz.'),
      ('Kayıt dönemi kampanyası', 'Reklamları yayına alıyor, talepleri her hafta izleyip bütçeyi kayıt getiren programa kaydırıyoruz.'),
      ('Dönem sonu değerlendirme', 'Dönem bitince hangi kanalın ve hangi programın kayıt getirdiğini raporluyor, bir sonraki dönemi buna göre planlıyoruz.'),
    ],
    'metin': [
      ('Eğitim kurumlarının dijital pazarlaması neden farklıdır?', 'Eğitimde talep yıl boyunca eşit dağılmaz: okulların açıldığı eylül, ikinci dönemin başladığı ocak ve şubat, yaz kursları ve sınav takvimleri kayıtların yoğunlaştığı zamanlardır. Kayıt kararı da çoğu zaman tek kişinin değildir; öğrenci, veli ya da çalışanın şirketi birlikte karar verir. Bu yüzden reklam takvimini kayıt dönemlerinden geriye doğru planlıyor, sayfaları ve ölçümü talebin başlamasından önce hazır hâle getiriyoruz. Bütçeyi de tıklamaya göre değil, gelen seviye testi, deneme dersi ve kayıt görüşmesi taleplerine göre yönetiyoruz.'),
      ('Dil kursu arayanlar Google’da ne arıyor?', 'Dil kursu aramaları genellikle üç türdür: şehir ya da semt adıyla kurs araması (“ankara ingilizce kursu”), fiyat araması (“ankara dil kursları fiyatları”) ve belirli bir dil ya da program araması (“ispanyolca kursu”, “ielts hazırlık”). Active English’in sitesi 19 Temmuz–18 Ekim 2026 arasında Google’da adında “Ankara” geçen 524 farklı aramada göründü; “ankara ingilizce kursu fiyatları” aramasında ortalama 2,7., “ankara dil kursları fiyatları” aramasında 2,8. sırada. Bunu her dil ve program için ayrı, ayrıntılı sayfalar hazırlayarak ve sık sorulan sorulara açık cevaplar vererek sağlıyoruz.'),
      ('Kurs reklamında hangi kanal ne işe yarar?', 'Google reklamları kursu zaten arayan kişileri yakalar; kayıt döneminde en hızlı talep getiren kanal genellikle budur. Instagram ve Facebook reklamları ise henüz aramaya başlamamış öğrencilere ve velilere kurumunuzu tanıtır; ders ortamını, öğretmenleri ve öğrenci etkinliklerini gösteren videolar burada işe yarar. SEO ise aynı aramalarda reklam ödemeden bulunmanızı sağlayan uzun vadeli çalışmadır. İkisinin farkını [Google Ads mi SEO mu?](/blog/google-ads-mi-seo-mu/) yazımızda, Instagram reklamının kurulumunu [Instagram reklamı nasıl verilir?](/blog/instagram-reklami-nasil-verilir/) rehberimizde anlattık.'),
      ('Eğitim reklamlarında nelere dikkat ediyoruz?', 'Eğitim reklamları Ticaret Bakanlığı’nın yanıltıcı reklam kurallarına tabidir. Bu yüzden “garantili başarı”, “3 ayda akıcı İngilizce” gibi kanıtlanamayan vaatler, gerçek olmayan indirimler ve kontenjan baskısı kullanmıyoruz. Sınav başarısı ya da öğrenci sayısı gibi rakamları yalnızca kurumun belgeleyebildiği hâliyle yazıyoruz. Öğrenci fotoğraflarını ve görüşlerini izin alınmadan, 18 yaşından küçük öğrencilerinkini velinin onayı olmadan kullanmıyoruz; formlar için KVKK aydınlatma metni ve çerez onayını kuruyoruz.'),
      ('Kayıt talebini nasıl ölçüyoruz?', 'Her talebi programla ve kaynağıyla birlikte ölçüyoruz: Google reklamından gelen seviye testi başvurusu, Instagram’dan gelen mesaj, siteden gelen arama. Kayıt ekibinizin “bizi nereden duydunuz?” sorusuna verilen cevapları da bu tabloya ekliyoruz. Dönem sonunda harcamayı, gelen talepleri ve kayda dönen talepleri program program gösteriyoruz; böylece bir sonraki dönemin bütçesi tahmine değil, gerçek kayıtlara göre planlanır. Bütçenin hedeften geriye doğru nasıl hesaplandığını [Google Ads bütçesi nasıl belirlenir?](/blog/google-ads-butcesi-nasil-belirlenir/) yazımızda anlattık.'),
      ('Hangi eğitim kurumlarıyla çalışıyoruz?', 'Active English’in web sitesini hazırladık ve SEO çalışmasını yürütüyoruz; HUBEK Flight Academy’nin web sitesini hazırladık. Dil kurslarından havacılık eğitimine kadar eğitim kurumlarının program sayfalarını, reklamlarını ve SEO’sunu aynı ekipte planlıyoruz. Ankara’daki kurumlarla yüz yüze, Türkiye’nin diğer şehirlerindeki kurumlarla online çalışıyoruz. SEO tarafını [aylık SEO hizmetimiz](/ankara-seo/), reklam tarafını [Google Ads yönetimimiz](/ankara-google-ads-ajansi/) olarak yürütüyoruz.'),
    ],
    'ilgili': ['google-ads-mi-seo-mu', 'instagram-reklami-nasil-verilir', 'google-ads-butcesi-nasil-belirlenir', 'kucuk-isletmeler-icin-dijital-pazarlama'],
    'sss': [
      ('Kayıt dönemi reklamlarına ne zaman başlanmalı?', 'Kayıtların yoğunlaştığı haftalardan birkaç hafta önce. Program sayfaları, formlar ve ölçüm önceden hazır olmalı; reklam başladığında gelen ilgi böylece kaybolmaz ve ilk haftalardan itibaren hangi kanalın işe yaradığı görülür.'),
      ('Dil kursu için Google mı Instagram mı daha etkili?', 'İkisi farklı işler yapar. Google reklamları kursu zaten arayanları yakalar, Instagram ise kurumunuzu henüz aramaya başlamamış öğrencilere ve velilere tanıtır. Hangisinin daha çok kayıt getirdiğini her talebi kaynağıyla ölçerek görüyor, bütçeyi buna göre kaydırıyoruz.'),
      ('Kurs fiyatlarını sitede yazmalı mıyım?', 'Kurs fiyatı en çok aranan konulardan biridir ve fiyat bilgisi veren sayfalar bu aramalarda öne çıkabilir. Fiyatın sitede nasıl gösterileceğine siz karar veriyorsunuz; yazılan fiyatın güncel ve kampanya koşullarının açık olmasına dikkat ediyoruz.'),
      ('Reklamlarda öğrenci fotoğrafı kullanabilir miyiz?', 'Yalnızca öğrencinin, 18 yaşından küçükse velisinin izni alınmış fotoğraf ve videoları kullanıyoruz. İzin yoksa ders ortamını ve öğretmenleri gösteren görseller hazırlıyoruz.'),
      ('Ankara dışındaki eğitim kurumlarıyla çalışıyor musunuz?', 'Evet. Planlama, onay ve raporlamayı online yürütüyoruz. Ankara’daki kurumlarla Çayyolu’ndaki ofisimizde ya da kurumunuzda yüz yüze de çalışıyoruz.'),
    ],
  },
]

KURUCU = {
  'ad': 'Şakir Yavuz', 'bas_harf': 'ŞY', 'unvan': 'Kurucu, Clickbait Dijital',
  'foto': '/assets/img/sakir-yavuz.jpg', 'foto_kare': '/assets/img/sakir-yavuz-kare.jpg',
  'linkedin': 'https://www.linkedin.com/in/%C5%9Fakir-yavuz-2b62bb125/',
  'yazar_notu': 'Şakir Yavuz, Clickbait Dijital’in kurucusudur. Ajansı 2013’te Ankara’da kurdu ve SEO çalışmalarını bizzat yürütüyor. Blogdaki yazılar, Ankara’daki işletmelerle yaptığı çalışmalardan edindiği deneyime dayanıyor.',
}

# Sayfa başındaki "KISACA" kutusu: yapay zeka araçlarının ve Google'ın alıntılayabileceği, kendi başına anlaşılır tanım.
# Kural: kim (Clickbait Dijital), ne, nerede, nasıl; yalnızca sayfada zaten söylenen bilgiler, rakam/sonuç yok. llms.txt de bunu kullanır.
TANIMLAR = {
  'yapay-zeka-danismanligi': 'Yapay zeka danışmanlığı (AI danışmanlığı), bir işletmenin yapay zekayı hangi işlerde, hangi araçlarla ve hangi kurallarla kullanacağını belirleyip bu kullanımı hayata geçiren hizmettir. Clickbait Dijital, Ankara Çayyolu’ndaki ofisinden 4 kişilik yapay zeka ekibiyle işletmelerin tekrar eden işlerini inceler, uygun araçları kurar, kullanım kurallarını yazar ve kurumsal yapay zeka eğitimleri verir. Ankara’daki işletmelerle yüz yüze, Türkiye’nin her yerinden işletmelerle online çalışır.',
  'web-tasarim': 'Clickbait Dijital, Ankara’da 2013’ten beri kurumsal web siteleri ve e-ticaret mağazaları tasarlayan bir dijital ajanstır. Tasarım, geliştirme, hosting ve bakım tek ekipte yürütülür; siteler mobil uyumlu, hızlı ve Google’da bulunabilir şekilde hazırlanır. Ankara’daki işletmelerle Çayyolu’ndaki ofiste, Türkiye genelindeki işletmelerle online çalışılır.',
  'dijital-pazarlama': 'Dijital pazarlama; Google Ads, Instagram ve Facebook (Meta) reklamları, SEO ve dijital medya planlamasıyla bir işletmenin internette müşteriye ulaşmasını sağlayan çalışmaların tamamıdır. Clickbait Dijital, Ankara’daki ve Türkiye genelindeki işletmeler için reklam hesaplarını kurar ve yönetir, SEO çalışmasını aynı ekipte yürütür ve sonuçları her ay raporlar.',
  'sosyal-medya-yonetimi': 'Sosyal medya yönetimi; bir markanın hesaplarında aylık içerik planının hazırlanması, tasarımların ve metinlerin üretilmesi, paylaşımların takvime göre yayınlanması ve sonuçların raporlanmasıdır. Clickbait Dijital, Ankara’da markaların sosyal medya hesaplarını ağırlıklı olarak Instagram ve LinkedIn’de yönetir; her ayın planı ve tasarımları yayından önce müşteri onayına sunulur.',
  'kreatif-hizmetler': 'Kreatif hizmetler; logo, kurumsal kimlik, sosyal medya şablonları, kartvizit, katalog ve sunum gibi bir markanın görsel dilini oluşturan tasarım işleridir. Clickbait Dijital, Ankara Çayyolu’ndaki ofisinde markaların logo ve kurumsal kimliğini tasarlar ve bu kimliğin tüm kullanım alanları için uygulamalarını hazırlar.',
  'ankara-seo': 'Ankara SEO, Ankara’da hizmet veren bir işletmenin web sitesinin Google’da Ankara ve bölge adıyla yapılan aramalarda üst sıralarda görünmesi için yapılan çalışmalardır: teknik düzeltmeler, anahtar kelime araştırması, sayfa içi düzenlemeler, içerik ve Google İşletme Profili. Clickbait Dijital, Çayyolu’ndaki ofisinden Ankara’daki işletmelere SEO hizmeti verir, ilerlemeyi her ay Search Console verileriyle raporlar ve sıra garantisi vermez.',
  'ankara-google-ads-ajansi': 'Google Ads ajansı, işletmelerin Google arama, YouTube ve görüntülü reklam kampanyalarını kurup yöneten ajanstır. Clickbait Dijital, Ankara’daki işletmeler için doğru kelimeleri seçer, alakasız tıklamaları eler, telefon, form ve WhatsApp taleplerini ölçer ve harcanan bütçenin neye dönüştüğünü her ay raporlar.',
  'ankara-reklam-ajansi': 'Clickbait Dijital, Ankara Çayyolu’nda 2013’ten beri hizmet veren tam kapsamlı bir reklam ajansıdır. Kampanya fikri ve strateji, TV reklam filmi ve yayın planlaması, radyo reklamı, açık hava reklamı (billboard, raket, megalight), medya planlama ile Google ve Instagram reklamları aynı ekipte planlanır ve yürütülür.',
  'ankara-e-ticaret-sitesi': 'Clickbait Dijital, Ankara’daki işletmeler için e-ticaret siteleri kurar: işe uygun altyapının seçimi, mağaza tasarımı, ödeme ve kargo bağlantıları, ürün ve kategori sayfalarının Google için hazırlanması ve açılıştan sonra reklam ve ölçüm. Ankara’daki işletmelerle yüz yüze, Türkiye genelinde online çalışır.',
  'insaat-firmalari-icin-reklam-ajansi': 'İnşaat firmaları için reklam ajansı hizmeti; konut ve villa projelerinin lansman kampanyasını, Google ve Instagram reklamlarını, açık hava reklamlarını, proje web sitesini ve satış ofisine gelen talebin ölçümünü kapsar. Clickbait Dijital, Ankara’daki konut projelerinin dijital pazarlamasını yürütür; Türkiye genelindeki inşaat firmalarıyla online çalışır.',
  'doktorlar-icin-seo': 'Doktorlar için SEO; hekimlerin ve kliniklerin web sitelerinin, hastaların Google’da yaptığı aramalarda doğru ve bilgilendirici içerikle bulunması için yapılan teknik ve içerik çalışmasıdır. Clickbait Dijital, sağlık sitelerini Sağlık Bakanlığı’nın tanıtım ve bilgilendirme kurallarına uygun, reklam dili kullanmadan hazırlar; Ankara’daki hekimlerle yüz yüze, Türkiye genelinde online çalışır.',
  'psikologlar-icin-web-sitesi': 'Psikologlar için web sitesi ve SEO; psikologların ve terapi merkezlerinin, danışanların Google’da yaptığı aramalarda güven veren ve bilgilendirici bir siteyle bulunması için yapılan tasarım, teknik ve içerik çalışmasıdır. Clickbait Dijital, psikolog sitelerini danışan mahremiyetine ve sağlık tanıtım kurallarına uygun, reklam dili kullanmadan hazırlar; Ankara’daki psikologlarla yüz yüze, Türkiye genelinde online çalışır.',
  'egitim-kurumlari-icin-dijital-pazarlama': 'Eğitim kurumları için dijital pazarlama; dil kurslarının, eğitim kurumlarının ve akademilerin kayıt dönemlerine göre planlanan Google ve Instagram reklamlarını, program sayfalarını, SEO çalışmasını ve kayıt talebinin ölçümünü kapsar. Clickbait Dijital, Ankara’daki eğitim kurumlarıyla yüz yüze, Türkiye genelinde online çalışır.',
  'ankara-instagram-reklam-ajansi': 'Instagram reklam ajansı, markaların Instagram ve Facebook’taki sponsorlu reklamlarını hedef kitle, kreatif ve bütçe yönetimiyle planlayıp yöneten ajanstır. Clickbait Dijital, Ankara’daki işletmeler için Meta reklamlarını kurar, reklamdan gelen mesaj, form ve aramaları ölçer ve sonuçları her ay raporlar.',
}

def e(s): return html.escape(s, quote=True)
def buyuk(s): return s.replace('i', 'İ').upper()   # Türkçe büyük harf

IKON_IG = '<svg class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1" fill="currentColor" stroke="none"/></svg>'
IKON_LI = '<svg class="w-5 h-5" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M4.98 3.5a2.5 2.5 0 11-.01 5 2.5 2.5 0 01.01-5zM3 9h4v12H3zM9 9h3.8v1.7h.05c.53-1 1.83-2.05 3.77-2.05 4.03 0 4.78 2.65 4.78 6.1V21h-4v-5.4c0-1.3-.02-2.95-1.8-2.95-1.8 0-2.08 1.4-2.08 2.86V21H9z"/></svg>'

IKON_TEL = '<svg class="w-[18px] h-[18px]" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M22 16.92v3a2 2 0 01-2.18 2 19.8 19.8 0 01-8.63-3.07 19.5 19.5 0 01-6-6A19.8 19.8 0 012.12 4.18 2 2 0 014.11 2h3a2 2 0 012 1.72c.13.96.36 1.9.7 2.81a2 2 0 01-.45 2.11L8.09 9.91a16 16 0 006 6l1.27-1.27a2 2 0 012.11-.45c.91.34 1.85.57 2.81.7A2 2 0 0122 16.92z"/></svg>'
IKON_WA = '<svg class="w-5 h-5" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M17.47 14.38c-.3-.15-1.75-.86-2.02-.96-.27-.1-.47-.15-.67.15-.2.3-.77.96-.94 1.16-.17.2-.35.22-.64.07-.3-.15-1.26-.46-2.39-1.47-.88-.79-1.48-1.76-1.65-2.06-.17-.3-.02-.46.13-.6.13-.14.3-.35.45-.52.15-.17.2-.3.3-.5.1-.2.05-.37-.02-.52-.08-.15-.67-1.62-.92-2.22-.24-.58-.49-.5-.67-.51h-.57c-.2 0-.52.07-.79.37-.27.3-1.04 1.02-1.04 2.48 0 1.46 1.07 2.88 1.21 3.08.15.2 2.1 3.2 5.08 4.49.71.31 1.26.49 1.7.63.71.22 1.36.19 1.87.12.57-.09 1.75-.72 2-1.41.25-.69.25-1.29.17-1.41-.07-.13-.27-.2-.57-.35zM12.05 21.5h-.01a9.4 9.4 0 01-4.8-1.32l-.34-.2-3.57.94.95-3.48-.22-.36a9.4 9.4 0 01-1.44-5.02c0-5.2 4.23-9.43 9.44-9.43 2.52 0 4.89.98 6.67 2.77a9.37 9.37 0 012.76 6.67c0 5.2-4.23 9.43-9.44 9.43zm8.03-17.47A11.3 11.3 0 0012.05.7C5.79.7.7 5.8.7 12.05c0 2 .52 3.95 1.52 5.67L.6 23.3l5.71-1.5a11.3 11.3 0 005.43 1.38h.01c6.26 0 11.35-5.09 11.35-11.35 0-3.03-1.18-5.88-3.32-8.02z"/></svg>'
WA_METIN = 'Merhaba%20Clickbait%2C%20web%20sitenizden%20yaz%C4%B1yorum.'

def alt_bilgi():
    hiz = ''.join(f'<li><a class="hover:text-slate-900" href="/{h["adres"]}/">{e(h["kisa"])}</a></li>' for h in HIZMETLER)
    return f'''<!-- ▼▼▼▼▼ BÖLÜM: ALT BİLGİ — BAŞLANGIÇ ▼▼▼▼▼ -->
<footer class="bg-white border-t border-slate-200 pt-12 pb-[calc(7rem+env(safe-area-inset-bottom,0px))] md:pb-[calc(2.5rem+env(safe-area-inset-bottom,0px))]">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="grid gap-10 md:grid-cols-12 text-sm text-slate-600">
      <div class="md:col-span-4">
        <a href="/" aria-label="Clickbait, ana sayfa"><img src="/assets/img/logo-siyah.svg" alt="Clickbait" width="103" height="24" class="h-6 w-auto"></a>
        <p class="mt-4 max-w-xs leading-relaxed">Ankara merkezli dijital ajans. Yapay zeka danışmanlığı, web tasarım, dijital pazarlama ve sosyal medya.</p>
        <div class="mt-5 flex gap-2">
          <a href="{INSTAGRAM}" target="_blank" rel="noopener" aria-label="Instagram: @clickbaitdijital" class="w-10 h-10 rounded-full bg-slate-100 hover:bg-[#D8F83C] text-slate-800 flex items-center justify-center transition-colors">{IKON_IG}</a>
          <a href="{LINKEDIN}" target="_blank" rel="noopener" aria-label="LinkedIn: Clickbait Digital Agency" class="w-10 h-10 rounded-full bg-slate-100 hover:bg-[#D8F83C] text-slate-800 flex items-center justify-center transition-colors">{IKON_LI}</a>
        </div>
      </div>
      <nav class="md:col-span-3" aria-label="Hizmetler">
        <p class="text-xs font-bold tracking-widest text-slate-900">HİZMETLER</p>
        <ul class="mt-4 grid gap-2.5">{hiz}</ul>
      </nav>
      <nav class="md:col-span-2" aria-label="Kurumsal">
        <p class="text-xs font-bold tracking-widest text-slate-900">KURUMSAL</p>
        <ul class="mt-4 grid gap-2.5"><li><a class="hover:text-slate-900" href="/#projeler">Projeler</a></li><li><a class="hover:text-slate-900" href="/#hakkimizda">Hakkımızda</a></li><li><a class="hover:text-slate-900" href="/blog/">Blog</a></li><li><a class="hover:text-slate-900" href="/kvkk/">KVKK</a></li></ul>
      </nav>
      <div class="md:col-span-3">
        <p class="text-xs font-bold tracking-widest text-slate-900">İLETİŞİM</p>
        <ul class="mt-4 grid gap-2.5"><li><a class="hover:text-slate-900" href="{TEL_LINK}">{TEL_GORUNEN}</a></li><li><a class="hover:text-slate-900" href="mailto:info@clickbait.com.tr">info@clickbait.com.tr</a></li><li><a class="hover:text-slate-900" href="{HARITA}" target="_blank" rel="noopener">Ümit Mah. Meksika Cad. No:56/21<br>Çayyolu, Ankara</a></li><li><a class="inline-flex items-center gap-1.5 font-semibold text-slate-900 hover:underline" href="{HARITA}" target="_blank" rel="noopener">Haritada aç <span aria-hidden="true">↗</span></a></li><li><a class="inline-flex items-center gap-1.5 font-semibold text-slate-900 hover:underline" href="{YORUM}" target="_blank" rel="noopener">Google’da bizi değerlendirin <span aria-hidden="true">★</span></a></li><li><a class="inline-flex items-center gap-1.5 rounded-full bg-[#D8F83C] px-3 py-1.5 text-xs font-bold text-black hover:bg-[#c7e92e]" href="#analiz" data-analiz>Ücretsiz site analizi <span aria-hidden="true">↗</span></a></li></ul>
      </div>
    </div>
    <nav aria-label="Ankara hizmetleri" class="mt-10 flex flex-wrap items-center gap-x-4 gap-y-2 text-xs text-slate-600"><span class="font-bold tracking-widest text-slate-900">ANKARA</span>{''.join(f'<a class="hover:text-slate-900" href="/{x["adres"]}/">{e(x["kisa"])}</a>' for x in ANKARA)}</nav>
    <nav aria-label="Sektörlere özel hizmetler" class="mt-3 flex flex-wrap items-center gap-x-4 gap-y-2 text-xs text-slate-600"><span class="font-bold tracking-widest text-slate-900">SEKTÖRLER</span>{''.join(f'<a class="hover:text-slate-900" href="/{x["adres"]}/">{e(x["kisa"])}</a>' for x in SEKTORLER)}</nav>
    <div class="mt-6 pt-6 border-t border-slate-100 text-xs text-slate-500">© 2013–{datetime.date.today().year} Clickbait Medya Limited Şirketi, Ankara. Tüm hakları saklıdır.</div>
  </div>
</footer>
<!-- Mobil hızlı iletişim çubuğu (yalnızca telefonda görünür) -->
<nav aria-label="Hızlı iletişim" class="md:hidden fixed inset-x-0 bottom-0 z-40 px-3 pt-2 pb-[calc(0.75rem+env(safe-area-inset-bottom,0px))] bg-gradient-to-t from-white via-white/90 to-transparent">
  <div class="grid grid-cols-2 gap-2">
    <a href="{TEL_LINK}" data-iletisim="telefon" class="flex items-center gap-2 rounded-full bg-[#111315] text-white pl-2 pr-3 py-2 shadow-lg shadow-black/20 active:scale-[0.97] transition-transform">
      <span class="shrink-0 w-8 h-8 min-[380px]:w-9 min-[380px]:h-9 rounded-full bg-white/10 flex items-center justify-center">{IKON_TEL}</span>
      <span class="min-w-0 leading-tight whitespace-nowrap"><span class="block text-xs min-[360px]:text-[13px] min-[380px]:text-sm font-bold">Hemen ara</span><span class="block text-[11px] text-white/70">{TEL_GORUNEN}</span></span>
    </a>
    <a href="{WHATSAPP}?text={WA_METIN}" target="_blank" rel="noopener" data-iletisim="whatsapp" class="flex items-center gap-2 rounded-full bg-[#D8F83C] text-black pl-2 pr-3 py-2 shadow-lg shadow-black/20 active:scale-[0.97] transition-transform">
      <span class="shrink-0 w-8 h-8 min-[380px]:w-9 min-[380px]:h-9 rounded-full bg-black/10 flex items-center justify-center">{IKON_WA}</span>
      <span class="min-w-0 leading-tight whitespace-nowrap"><span class="block text-xs min-[360px]:text-[13px] min-[380px]:text-sm font-bold">WhatsApp’tan yaz</span><span class="block text-[11px] text-black/60">Hemen yanıtlıyoruz</span></span>
    </a>
  </div>
</nav>
<!-- ▲▲▲▲▲ BÖLÜM: ALT BİLGİ — BİTİŞ ▲▲▲▲▲ -->'''

# Üst menüdeki Hizmetler açılır listesinde her hizmetin altındaki kısa açıklama
MENU_ACIKLAMA = {
  'yapay-zeka-danismanligi': 'Doğru araçlar, kullanım kuralları ve ekip eğitimi',
  'web-tasarim': 'Kurumsal web sitesi ve e-ticaret',
  'dijital-pazarlama': 'Google Ads, Meta reklamları ve SEO',
  'sosyal-medya-yonetimi': 'İçerik planı, tasarım ve raporlama',
  'kreatif-hizmetler': 'Logo ve kurumsal kimlik',
}

def menu(ana=False):
    # ana=True: ana sayfadaki kopya (bölüm bağlantıları sayfa içi, logo sayfa başına gider)
    k = '' if ana else '/'
    linkler = [(f'{k}#projeler', 'Projeler'), (f'{k}#hakkimizda', 'Hakkımızda'), ('/blog/', 'Blog'), (f'{k}#iletisim', 'İletişim')]
    ust = ''.join(f'\n        <a class="hover:text-white transition-colors" href="{u}">{buyuk(a)}</a>' for u, a in linkler)
    mob = ''.join(f'\n        <a class="px-4 py-3.5 rounded-2xl text-lg font-bold text-slate-900 hover:bg-slate-100" href="{u}">{a}</a>' for u, a in linkler)
    # Hizmetler açılır listesi: masaüstünde üzerine gelince/odaklanınca açılır, mobilde menünün içinde alt liste
    acilir_hiz = ''.join(f'<a class="block rounded-2xl px-4 py-3 hover:bg-slate-50" href="/{h["adres"]}/"><span class="block text-sm font-bold text-slate-900">{e(h["kisa"])}</span><span class="mt-0.5 block text-xs font-medium text-slate-500">{e(MENU_ACIKLAMA[h["adres"]])}</span></a>' for h in HIZMETLER)
    mob_hiz = ''.join(f'<a class="px-4 py-2.5 rounded-xl text-base font-semibold text-slate-700 hover:bg-slate-100" href="/{h["adres"]}/">{e(h["kisa"])}</a>' for h in HIZMETLER)
    return f'''  <!-- ▼▼▼▼▼ BÖLÜM: MENÜ — BAŞLANGIÇ ▼▼▼▼▼ -->
  <header class="relative z-40 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="flex items-center justify-between h-14 gap-4">
      <a aria-label="Clickbait, {'sayfa başı' if ana else 'ana sayfa'}" class="flex items-center group" href="{'#top' if ana else '/'}">
        <img src="/assets/img/logo-beyaz.svg" alt="Clickbait" width="137" height="32" class="h-7 sm:h-8 w-auto drop-shadow-sm transition-transform group-hover:scale-105">
      </a>
      <nav aria-label="Ana menü" class="hidden md:flex items-center gap-8 lg:gap-9 text-xs font-semibold tracking-wider text-white/90">
        <div class="relative group">
          <a class="inline-flex items-center gap-1 hover:text-white transition-colors" href="{k}#hizmetler">HİZMETLER<svg class="w-3 h-3 transition-transform group-hover:rotate-180 group-focus-within:rotate-180" viewBox="0 0 12 12" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M2.5 4.5 6 8l3.5-3.5"/></svg></a>
          <div class="absolute left-0 top-full pt-3 hidden group-hover:block group-focus-within:block">
            <div class="w-80 grid rounded-3xl bg-white p-2 tracking-normal shadow-2xl">{acilir_hiz}</div>
          </div>
        </div>{ust}
      </nav>
      <div class="flex items-center gap-2">
        <a class="hidden sm:inline-flex items-center justify-center px-5 py-2.5 rounded-full text-xs font-bold tracking-wider text-black bg-[#D8F83C] hover:bg-[#c9eb2f] transition-all shadow-md shadow-black/5 hover:scale-[1.03]" href="{k}#iletisim">TEKLİF ALIN</a>
        <button id="menuBtn" class="md:hidden inline-flex items-center px-4 py-2.5 rounded-full text-xs font-bold tracking-wider text-white bg-black/25 backdrop-blur-md border border-white/25" aria-expanded="false" aria-controls="mobileMenu">MENÜ</button>
      </div>
    </div>
    <div id="mobileMenu" hidden class="md:hidden fixed left-4 right-4 top-[calc(4.25rem+env(safe-area-inset-top,0px))] max-h-[calc(100dvh-10rem-env(safe-area-inset-top,0px)-env(safe-area-inset-bottom,0px))] overflow-y-auto overscroll-contain bg-white rounded-3xl shadow-2xl p-3">
      <nav aria-label="Mobil menü" class="grid">
        <a class="px-4 py-3.5 rounded-2xl text-lg font-bold text-slate-900 hover:bg-slate-100" href="{k}#hizmetler">Hizmetler</a>
        <div class="grid pl-3 pb-2">{mob_hiz}</div>{mob}
        <a class="mt-2 text-center px-5 py-3.5 rounded-full text-sm font-bold tracking-wider text-black bg-[#D8F83C]" href="{k}#iletisim">TEKLİF ALIN</a>
      </nav>
    </div>
  </header>
  <!-- ▲▲▲▲▲ BÖLÜM: MENÜ — BİTİŞ ▲▲▲▲▲ -->'''

def bas(baslik, aciklama, adres, ekler='', gorsel='/assets/img/og-clickbait.jpg'):
    return f'''<!DOCTYPE html>
<html lang="tr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{e(baslik)}</title>
<meta name="description" content="{e(aciklama)}">
<link rel="canonical" href="{ALAN}{adres}">
<meta property="og:type" content="website">
<meta property="og:locale" content="tr_TR">
<meta property="og:site_name" content="Clickbait Dijital">
<meta property="og:url" content="{ALAN}{adres}">
<meta property="og:title" content="{e(baslik)}">
<meta property="og:description" content="{e(aciklama)}">
<meta property="og:image" content="{ALAN}{gorsel}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#0866c9">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="icon" href="/favicon-32.png" type="image/png" sizes="32x32">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="preload" href="/assets/fonts/plus-jakarta-sans-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/assets/fonts/plus-jakarta-sans-latin-ext.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/assets/css/tailwind.css">
<link rel="stylesheet" href="/assets/css/site.css">
{ekler}</head>
<body>
'''

KART_RENK = {
  'lime': ('bg-[#D8F83C]', 'text-slate-900', 'text-slate-800', 'bg-black/10'),
  'sky':  ('bg-gradient-to-br from-sky-500 to-sky-700', 'text-white', 'text-white', 'bg-white/15'),
  'blue': ('bg-[#0284c7]', 'text-white', 'text-white', 'bg-white/15'),
  'dark': ('bg-[#111315]', 'text-white', 'text-slate-300', 'bg-white/10'),
}

def referans_seridi():
    s = open(os.path.join(KOK, 'index.html'), encoding='utf-8').read()
    m = re.search(r'<!-- KAYAN ŞERİT.*?<!-- /KAYAN ŞERİT -->', s, re.S)
    return m.group(0).replace('src="assets/', 'src="/assets/') if m else ''

UZMAN_METNI = {
  'ankara-seo': ('Ankara SEO uzmanı ile doğrudan çalışın',
                 'Ankara SEO çalışmalarımızı Clickbait Dijital’in kurucusu Şakir Yavuz bizzat yürütüyor. Şakir Yavuz ajansı 2013’te Ankara’da kurdu; o günden bu yana sağlık, eğitim, havacılık, inşaat, emlak, yayıncılık ve konaklama sektörlerinden markaların web sitelerini, reklamlarını ve SEO çalışmalarını yönetiyor. Active English, Psychology Times ve Rojin Nazik gibi sitelerin SEO süreçlerini yürütüyor. Sitenizin incelenmesinden hedef aramaların belirlenmesine ve aylık raporlara kadar süreci kendisi yönettiği için bir SEO uzmanıyla doğrudan çalışırsınız; tasarım, içerik ve reklam ihtiyaçlarınız için ajans ekibi de yanınızdadır.'),
  'web-tasarim': ('Web projenizi kim yönetiyor?',
                 'Web projelerimizi Clickbait Dijital’in kurucusu Şakir Yavuz yönetiyor. Şakir Yavuz ajansı 2013’te Ankara’da kurdu; o günden bu yana sağlık, eğitim, havacılık, inşaat, emlak, yayıncılık ve konaklama sektörlerinden markaların web sitelerini, reklamlarını ve SEO çalışmalarını yönetiyor. Sayfa planından yayına ve Google’a hazırlanmaya kadar süreci aynı kişi takip ettiği için sitenizin tasarımı ile Google’daki görünürlüğü baştan birlikte düşünülür.'),
  'dijital-pazarlama': ('Reklamlarınızı kim yönetiyor?',
                 'Dijital pazarlama çalışmalarımızı Clickbait Dijital’in kurucusu Şakir Yavuz yönetiyor. Şakir Yavuz ajansı 2013’te Ankara’da kurdu; o günden bu yana sağlık, eğitim, havacılık, inşaat, emlak, yayıncılık ve konaklama sektörlerinden markaların web sitelerini, reklamlarını ve SEO çalışmalarını yönetiyor. Reklam hesaplarınızı, SEO çalışmanızı ve web sitenizi aynı ekip takip ettiği için bir kanalda öğrenilen (hangi arama talep getiriyor, hangi mesaj işe yarıyor) diğer kanallarda da hemen kullanılır.'),
  'yapay-zeka-danismanligi': ('Yapay zeka çalışmalarınızı kim yürütüyor?',
                 'Yapay zeka projelerimizi kurucumuz Şakir Yavuz’la birlikte 4 kişilik bir ekip yürütüyor. İhtiyaç analizinden araç seçimine, kurulumdan kurumsal eğitimlere kadar sürecin her adımında aynı ekip yanınızda olur. Analiz, kurulum ve eğitim birbirini bilerek ilerlediği için ekibinize anlatılanla kurulan sistem aynı dili konuşur.'),
}

def uzman_bolumu(h):
    """Bazı hizmet sayfalarında işi yürüten kişiyi tanıtan kart (UZMAN_METNI)."""
    if h['adres'] not in UZMAN_METNI: return ''
    baslik, metin = UZMAN_METNI[h['adres']]
    return f'''
<!-- ▼▼▼▼▼ BÖLÜM: UZMAN — BAŞLANGIÇ ▼▼▼▼▼ -->
<section class="pb-20 md:pb-28 bg-white" aria-labelledby="uzman-baslik" id="uzman">
  <div class="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8">
    <h2 id="uzman-baslik" class="text-2xl md:text-3xl font-extrabold text-slate-900 tracking-tight">{e(baslik)}</h2>
    <div class="mt-6 rounded-[28px] border border-slate-100 bg-[#fafafa] p-6 md:p-8 flex flex-col sm:flex-row gap-5">
      <img src="{KURUCU['foto_kare']}" alt="{e(KURUCU['ad'])}" width="192" height="192" loading="lazy" class="w-24 h-24 sm:w-28 sm:h-28 shrink-0 rounded-2xl object-cover bg-slate-200">
      <div>
        <p class="text-lg font-extrabold text-slate-900">{e(KURUCU['ad'])}</p>
        <p class="text-sm font-semibold text-slate-500">{e(KURUCU['unvan'])}</p>
        <p class="mt-3 text-base text-slate-600 leading-relaxed">{e(metin)}</p>
        <a href="{KURUCU['linkedin']}" target="_blank" rel="noopener" class="mt-4 inline-flex items-center gap-2 rounded-full border border-slate-200 bg-white px-4 py-2 text-sm font-bold text-slate-900 hover:border-slate-900 transition-colors">LinkedIn profili <span aria-hidden="true">↗</span></a>
      </div>
    </div>
  </div>
</section>
<!-- ▲▲▲▲▲ BÖLÜM: UZMAN — BİTİŞ ▲▲▲▲▲ -->
'''

def sonuclar_bolumu(h):
    """Search Console'dan alınmış gerçek sonuç kartları (yalnızca kullanıcının verdiği erişimlerden, rakam uydurma)."""
    s = h.get('sonuclar')
    if not s: return ''
    kartlar = ''.join(f'''
      <li class="rounded-[28px] border border-slate-100 bg-white p-6 shadow-sm flex flex-col gap-4">
        <div><a href="{x['adres']}" target="_blank" rel="noopener" class="text-lg font-extrabold text-slate-900 hover:underline">{e(x['ad'])} <span aria-hidden="true">↗</span></a><p class="text-xs font-bold tracking-wider text-slate-500">{e(buyuk(x['tur']))}</p></div>
        <dl class="grid grid-cols-3 gap-2 text-center">
          <div class="rounded-2xl bg-sky-50 px-2 py-3"><dt class="text-[11px] font-semibold text-slate-500">Tıklama</dt><dd class="text-lg font-extrabold text-slate-900 tabular-nums">{x['tiklama']}</dd></div>
          <div class="rounded-2xl bg-sky-50 px-2 py-3"><dt class="text-[11px] font-semibold text-slate-500">Gösterim</dt><dd class="text-lg font-extrabold text-slate-900 tabular-nums">{x['gosterim']}</dd></div>
          <div class="rounded-2xl bg-[#D8F83C] px-2 py-3"><dt class="text-[11px] font-semibold text-slate-700">Ort. sıra</dt><dd class="text-lg font-extrabold text-slate-900 tabular-nums">{x['konum']}</dd></div>
        </dl>
        <p class="text-sm text-slate-600">{e(x['not'])}</p>
        <ul class="grid gap-1.5 text-sm">{''.join(f'<li class="flex items-baseline justify-between gap-3 border-t border-slate-100 pt-1.5"><span class="text-slate-700">“{e(q)}”</span><span class="shrink-0 font-bold text-slate-900 tabular-nums">ort. {p}</span></li>' for q, p in x['ornek'])}</ul>
      </li>''' for x in s['siteler'])
    return f'''
<!-- ▼▼▼▼▼ BÖLÜM: SONUÇLAR — BAŞLANGIÇ ▼▼▼▼▼ -->
<section class="pb-20 md:pb-28 bg-white" aria-labelledby="sonuclar">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="max-w-3xl">
      <p class="inline-flex items-center gap-1.5 text-xs font-bold tracking-widest text-slate-500"><span class="w-1.5 h-1.5 rounded-full bg-slate-900"></span>GERÇEK VERİ</p>
      <h2 id="sonuclar" class="mt-4 text-2xl md:text-3xl font-extrabold text-slate-900 tracking-tight">SEO çalışmasını yürüttüğümüz sitelerden sonuçlar</h2>
      <p class="mt-4 text-base md:text-lg text-slate-600 leading-relaxed">Rakamlar sitelerin Google Search Console verileridir: {e(s['donem'])}. Ortalama sıra, sitenin göründüğü tüm aramaların ortalamasıdır; altında örnek aramalar ve bu aramalardaki ortalama sıraları var.</p>
    </div>
    <ul class="mt-10 grid grid-cols-1 md:grid-cols-3 gap-6">{kartlar}
    </ul>
  </div>
</section>
<!-- ▲▲▲▲▲ BÖLÜM: SONUÇLAR — BİTİŞ ▲▲▲▲▲ -->
'''

def projeler_bolumu(h):
    """Web tasarım sayfasında yayındaki müşteri sitelerinin ekran görüntüleri (site/assets/img/projeler/)."""
    if not h.get('projeler'): return ''
    def kart(ad, tur, dosya, url, g, y):
        tam = len(h['projeler']) % 2 and (ad, tur, dosya, url, g, y) == h['projeler'][-1]
        baslik = f'<a href="{url}" target="_blank" rel="noopener" class="hover:underline">{e(ad)} <span aria-hidden="true">↗</span></a>' if url else e(ad)
        return f'''
      <li class="bg-white rounded-[28px] p-3 border border-slate-100 shadow-sm{' md:col-span-2' if tam else ''}">
        <div class="rounded-[20px] overflow-hidden border border-slate-200 bg-white">
          <div class="flex items-center gap-1.5 h-8 px-4 bg-slate-100 border-b border-slate-200" aria-hidden="true"><span class="w-2.5 h-2.5 rounded-full bg-[#ff5f57]"></span><span class="w-2.5 h-2.5 rounded-full bg-[#febc2e]"></span><span class="w-2.5 h-2.5 rounded-full bg-[#28c840]"></span><span class="ml-3 h-4 flex-1 max-w-[220px] rounded-full bg-white"></span></div>
          <img src="/assets/img/projeler/{dosya}.jpg" srcset="/assets/img/projeler/{dosya}-800.jpg 800w, /assets/img/projeler/{dosya}.jpg {g}w" sizes="{'(min-width: 1280px) 1200px, 100vw' if tam else '(min-width: 768px) 50vw, 100vw'}" alt="{e(ad)} web sitesinin açılış sayfası" width="{g}" height="{y}" loading="lazy" class="block w-full h-auto">
        </div>
        <div class="px-3 pt-4 pb-2"><h3 class="text-base font-bold text-slate-900">{baslik}</h3><p class="text-xs text-slate-500 mt-0.5">{e(tur)}</p></div>
      </li>'''
    return f'''
<!-- ▼▼▼▼▼ BÖLÜM: PROJELER — BAŞLANGIÇ ▼▼▼▼▼ -->
<section class="py-20 md:py-28 mb-20 md:mb-28 bg-[#fafafa]" aria-labelledby="projeler">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="max-w-3xl">
      <p class="inline-flex items-center gap-1.5 text-xs font-bold tracking-widest text-slate-500"><span class="w-1.5 h-1.5 rounded-full bg-slate-900"></span>PROJELER</p>
      <h2 id="projeler" class="mt-4 text-2xl md:text-3xl font-extrabold text-slate-900 tracking-tight">Tasarladığımız web sitelerinden bazıları</h2>
      <p class="mt-4 text-base md:text-lg text-slate-600 leading-relaxed">Görseller sitelerin yayındaki açılış sayfalarıdır.</p>
    </div>
    <ul class="mt-10 grid grid-cols-1 md:grid-cols-2 gap-6">{''.join(kart(*p) for p in h['projeler'])}
    </ul>
  </div>
</section>
<!-- ▲▲▲▲▲ BÖLÜM: PROJELER — BİTİŞ ▲▲▲▲▲ -->
'''

def araclar_bolumu(h):
    """Çalışılan yapay zeka araçları (logolar site/assets/img/araclar/, Lobe Icons, MIT)."""
    if not h.get('araclar'): return ''
    logolar = ''.join(f'<li class="flex items-center gap-3 rounded-2xl border border-slate-100 bg-white px-4 py-3 shadow-sm"><img src="/assets/img/araclar/{d}.svg" alt="" width="28" height="28" loading="lazy" class="w-7 h-7 shrink-0"><span class="text-sm font-bold text-slate-900">{e(a)}</span></li>' for a, d in h['araclar'])
    return f'''
<!-- ▼▼▼▼▼ BÖLÜM: ARAÇLAR — BAŞLANGIÇ ▼▼▼▼▼ -->
<section class="pb-20 md:pb-28 bg-white" aria-labelledby="araclar">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="rounded-[32px] bg-[#fafafa] border border-slate-100 p-6 md:p-10">
      <h2 id="araclar" class="text-2xl md:text-3xl font-extrabold text-slate-900 tracking-tight">Çalıştığımız yapay zeka araçları</h2>
      <p class="mt-3 max-w-2xl text-base text-slate-600 leading-relaxed">Tek bir araca bağlı değiliz. Dil modellerinden görsel üretime ve otomasyona kadar önde gelen araçlarla çalışıyor, işinize ve veri güvenliği ihtiyacınıza uygun olanı seçiyoruz.</p>
      <ul class="mt-8 grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-4 gap-3" aria-label="Yapay zeka araçları">{logolar}</ul>
    </div>
  </div>
</section>
<!-- ▲▲▲▲▲ BÖLÜM: ARAÇLAR — BİTİŞ ▲▲▲▲▲ -->
'''

def hizmet_sayfasi(h):
    adres = f'/{h["adres"]}/'
    ust = next((x for x in HIZMETLER if x['adres'] == h.get('ust')), None)   # Ankara sayfalarında bağlı olduğu hizmet
    kirinti = (ust['kisa'], f'/{ust["adres"]}/') if ust else ('Hizmetler', '/#hizmetler')
    alt_sayfalar = [x for x in ANKARA if x['ust'] == h['adres']]
    metin = ''.join(f'''
      <h2 class="mt-12 first:mt-0 text-2xl md:text-3xl font-extrabold text-slate-900 tracking-tight">{e(b)}</h2>
      <p class="mt-4 text-base md:text-lg text-slate-600 leading-relaxed [&_a]:font-semibold [&_a]:text-slate-900 [&_a]:underline">{satir_ici(p)}</p>''' for b, p in h.get('metin', []))
    metin_bolumu = f'''<!-- ▼▼▼▼▼ BÖLÜM: AÇIKLAMA — BAŞLANGIÇ ▼▼▼▼▼ -->
<section class="pb-20 md:pb-28 bg-white">
  <div class="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8">{metin}
  </div>
</section>
<!-- ▲▲▲▲▲ BÖLÜM: AÇIKLAMA — BİTİŞ ▲▲▲▲▲ -->
''' if metin else ''
    ozel = (f'<p class="text-center text-xs font-bold tracking-widest text-slate-500">ANKARA’YA ÖZEL</p><ul class="mt-5 mb-10 flex flex-wrap justify-center gap-3">'
            + ''.join(f'<li><a href="/{x["adres"]}/" class="inline-flex items-center gap-2 rounded-full bg-[#D8F83C] px-4 py-2.5 text-sm font-semibold text-black hover:bg-[#c7e92e] transition-colors">{e(x["kisa"])} <span aria-hidden="true">↗</span></a></li>' for x in alt_sayfalar)
            + '</ul>') if alt_sayfalar else ''
    sektorler = [x for x in SEKTORLER if x['ust'] == h['adres']]
    ozel += (f'<p class="text-center text-xs font-bold tracking-widest text-slate-500">SEKTÖRE ÖZEL</p><ul class="mt-5 mb-10 flex flex-wrap justify-center gap-3">'
             + ''.join(f'<li><a href="/{x["adres"]}/" class="inline-flex items-center gap-2 rounded-full bg-[#D8F83C] px-4 py-2.5 text-sm font-semibold text-black hover:bg-[#c7e92e] transition-colors">{e(x["kisa"])} <span aria-hidden="true">↗</span></a></li>' for x in sektorler)
             + '</ul>') if sektorler else ''
    on, yazi, alt, rozet = KART_RENK[h['renk']]
    kartlar = ''.join(f'''
      <li class="bento-card-interactive bg-white rounded-[28px] p-6 md:p-7 border border-slate-100 shadow-sm">
        <span class="flex items-center justify-between" aria-hidden="true"><span class="w-11 h-11 rounded-2xl bg-[#D8F83C] text-black flex items-center justify-center">{kart_simgesi(b)}</span><span class="text-xs font-bold text-slate-300">{i:02d}</span></span>
        <h3 class="mt-5 text-lg font-extrabold text-slate-900 tracking-tight">{e(b)}</h3>
        <p class="mt-2 text-sm text-slate-600 leading-relaxed">{e(a)}</p>
      </li>''' for i, (b, a) in enumerate(h['kartlar'], 1))
    adimlar = ''.join(f'''
        <li class="flex gap-4"><span class="w-8 h-8 shrink-0 rounded-full {['bg-[#D8F83C] text-black','bg-white text-sky-700','bg-[#111315] text-white','bg-sky-200 text-sky-900'][i-1]} text-sm font-bold flex items-center justify-center">{i}</span><span><b class="block text-white">{e(b)}</b><span class="text-sm text-white/90 leading-relaxed">{e(a)}</span></span></li>''' for i, (b, a) in enumerate(h['adimlar'], 1))
    sss = ''.join(f'''
      <details class="group rounded-[24px] bg-white border border-slate-100 shadow-sm open:shadow-md transition-shadow">
        <summary class="cursor-pointer list-none flex items-center justify-between gap-4 p-5 md:p-6 font-bold text-slate-900">{e(s)}<span class="w-8 h-8 shrink-0 rounded-full bg-slate-100 flex items-center justify-center text-lg transition-transform group-open:rotate-45" aria-hidden="true">+</span></summary>
        <p class="px-5 md:px-6 pb-6 -mt-1 text-sm md:text-base text-slate-600 leading-relaxed">{e(c)}</p>
      </details>''' for s, c in h['sss'])
    diger = ''.join(f'<li><a href="/{x["adres"]}/" class="inline-flex items-center gap-2 rounded-full border border-slate-200 bg-white px-4 py-2.5 text-sm font-semibold text-slate-800 hover:border-slate-900 transition-colors">{e(x["kisa"])} <span aria-hidden="true">↗</span></a></li>' for x in HIZMETLER if x is not h)

    ld = {"@context": "https://schema.org", "@graph": [
      {"@type": "Service", "name": h['kisa'], "serviceType": h['kisa'], "description": h['description'], "disambiguatingDescription": TANIMLAR[h['adres']], "url": ALAN + adres,
       "provider": {"@id": ALAN + "/#isletme"},
       "areaServed": [{"@type": "City", "name": "Ankara"}] + ([] if ust and not h.get('sektor') else [{"@type": "Country", "name": "Türkiye"}])},
      {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Ana sayfa", "item": ALAN + "/"},
        {"@type": "ListItem", "position": 2, "name": kirinti[0], "item": ALAN + kirinti[1]},
        {"@type": "ListItem", "position": 3, "name": h['kisa'], "item": ALAN + adres}]},
      {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": s, "acceptedAnswer": {"@type": "Answer", "text": c}} for s, c in h['sss']]}]}
    if h['adres'] in UZMAN_METNI:
        ld['@graph'].append({"@type": "Person", "@id": ALAN + "/#sakir-yavuz", "name": KURUCU['ad'], "jobTitle": "Kurucu", "image": ALAN + KURUCU['foto'],
                             "worksFor": {"@id": ALAN + "/#isletme"}, "url": ALAN + "/ankara-seo/#uzman", "sameAs": [KURUCU['linkedin']]})
    if h.get('guncelleme'):
        ld['@graph'].append({"@type": "WebPage", "url": ALAN + adres, "name": h['title'], "dateModified": h['guncelleme']})
    ld_html = '<script type="application/ld+json">\n' + json.dumps(ld, ensure_ascii=False, indent=1) + '\n</script>\n'

    return bas(h['title'], h['description'], adres, ld_html) + f'''<div class="font-sans antialiased text-slate-800 bg-white selection:bg-brand-lime selection:text-black" id="top">
<a href="#icerik" class="sr-only focus:not-sr-only focus:fixed focus:top-3 focus:left-3 focus:z-50 focus:bg-white focus:px-4 focus:py-2 focus:rounded-full focus:font-bold">İçeriğe geç</a>

<!-- ▼▼▼▼▼ BÖLÜM: SAYFA BAŞI — BAŞLANGIÇ ▼▼▼▼▼ -->
<section class="on-blue relative pt-5 pb-16 md:pb-24 overflow-hidden rounded-b-[40px] md:rounded-b-[56px]" style="background:linear-gradient(160deg,#0866c9 0%,#1283e8 55%,#48a6fb 100%)" aria-labelledby="h1">
{menu()}
  <div class="relative z-20 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pt-12 md:pt-20 grid grid-cols-1 lg:grid-cols-12 gap-12 lg:gap-8 items-center">
    <div class="lg:col-span-7">
    <nav aria-label="Konum" class="text-xs font-semibold text-white/85"><ol class="flex flex-wrap items-center gap-2"><li><a href="/" class="hover:text-white">Ana sayfa</a></li><li aria-hidden="true">/</li><li><a href="{kirinti[1]}" class="hover:text-white">{e(kirinti[0])}</a></li><li aria-hidden="true">/</li><li aria-current="page" class="text-white">{e(h['kisa'])}</li></ol></nav>
    <h1 id="h1" class="mt-6 max-w-4xl text-4xl sm:text-5xl md:text-6xl lg:text-5xl xl:text-6xl font-bold text-white tracking-tight leading-[1.08]" style="text-wrap:balance">{e(h['h1'])}</h1>
    <p class="mt-6 max-w-2xl text-base md:text-lg text-white leading-relaxed">{e(h['giris'])}</p>
    <div class="mt-8 flex flex-wrap items-center gap-3.5">
      <a class="inline-flex items-center justify-center gap-2 px-6 py-3 rounded-full text-xs font-bold tracking-wider text-black bg-[#D8F83C] hover:bg-[#c7e92e] transition-all shadow-lg hover:scale-105" href="#teklif"><span>ÜCRETSİZ ÖN GÖRÜŞME</span><span class="w-5 h-5 rounded-full bg-black text-[#D8F83C] flex items-center justify-center text-xs" aria-hidden="true">↗</span></a>
      <a class="inline-flex items-center justify-center px-6 py-3 rounded-full text-xs font-bold tracking-wider text-white bg-black/25 hover:bg-black/35 border border-white/20 transition-all" href="{WHATSAPP}" target="_blank" rel="noopener">WHATSAPP’TAN YAZIN</a>
    </div>
    </div>
    <div class="lg:col-span-5">{cizim(h['adres'])}</div>
  </div>
</section>
<!-- ▲▲▲▲▲ BÖLÜM: SAYFA BAŞI — BİTİŞ ▲▲▲▲▲ -->

<main id="icerik">
<!-- ▼▼▼▼▼ BÖLÜM: KISACA — BAŞLANGIÇ ▼▼▼▼▼ -->
<section class="pt-14 md:pt-20 bg-white" aria-label="Kısaca">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="rounded-[28px] bg-sky-50 border border-sky-100 p-6 md:p-8 md:flex md:gap-8">
      <p class="shrink-0 self-start inline-flex items-center gap-2 text-xs font-bold tracking-widest text-sky-700 md:w-32 md:pt-1.5"><span class="w-1.5 h-1.5 rounded-full bg-sky-600"></span>KISACA</p>
      <div class="mt-3 md:mt-0"><p class="text-base md:text-lg text-slate-700 leading-relaxed">{e(TANIMLAR[h['adres']])}</p>{f'<p class="mt-3 text-xs font-semibold text-slate-500">Son güncelleme: <time datetime="{h["guncelleme"]}">{tarih_tr(h["guncelleme"])}</time></p>' if h.get('guncelleme') else ''}</div>
    </div>
  </div>
</section>
<!-- ▲▲▲▲▲ BÖLÜM: KISACA — BİTİŞ ▲▲▲▲▲ -->

<!-- ▼▼▼▼▼ BÖLÜM: NELER YAPIYORUZ — BAŞLANGIÇ ▼▼▼▼▼ -->
<section class="py-20 md:py-28 bg-white" aria-labelledby="neler">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="max-w-2xl">
      <p class="inline-flex items-center gap-1.5 text-xs font-bold tracking-widest text-slate-500"><span class="w-1.5 h-1.5 rounded-full bg-slate-900"></span>KAPSAM</p>
      <h2 id="neler" class="mt-4 text-3xl sm:text-4xl md:text-5xl font-extrabold text-slate-900 tracking-tight leading-tight">{e(h.get('kapsam', h['kisa'] + ' hizmetimizde neler var?'))}</h2>
    </div>
    <ul class="mt-12 grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">{kartlar}
    </ul>
  </div>
</section>
<!-- ▲▲▲▲▲ BÖLÜM: NELER YAPIYORUZ — BİTİŞ ▲▲▲▲▲ -->

{metin_bolumu}{projeler_bolumu(h)}{sonuclar_bolumu(h)}{araclar_bolumu(h)}{uzman_bolumu(h)}
<!-- ▼▼▼▼▼ BÖLÜM: SÜREÇ VE NEDEN BİZ — BAŞLANGIÇ ▼▼▼▼▼ -->
<section class="pb-20 md:pb-28 bg-white" aria-labelledby="surec">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 grid grid-cols-1 md:grid-cols-12 gap-6">
    <div class="on-blue md:col-span-7 rounded-[32px] p-7 md:p-10 bg-gradient-to-br from-sky-500 to-sky-700 text-white">
      <h2 id="surec" class="text-2xl md:text-3xl font-extrabold tracking-tight">Nasıl çalışıyoruz?</h2>
      <ol class="mt-8 grid gap-6">{adimlar}
      </ol>
    </div>
    <div class="md:col-span-5 grid gap-6">
      <div class="bento-card-interactive rounded-[32px] bg-[#D8F83C] p-7 flex flex-col justify-between gap-6">
        <p class="text-xs font-bold tracking-wider text-slate-800">2013’TEN BERİ</p>
        <p class="text-4xl md:text-5xl font-extrabold text-slate-900 tracking-tight">300+ çalışma</p>
        <p class="text-sm text-slate-800 leading-relaxed">Sağlıktan eğitime, inşaattan havacılığa 50’den fazla markayla çalıştık.</p>
      </div>
      <div class="bento-card-interactive rounded-[32px] bg-[#111315] text-white p-7">
        <p class="text-lg font-extrabold">Ankara’da ofis, Türkiye genelinde hizmet</p>
        <p class="mt-2 text-sm text-slate-300 leading-relaxed">Çayyolu’ndaki ofisimizde yüz yüze görüşüyor, diğer şehirlerdeki müşterilerimizle süreci online yürütüyoruz.</p>
      </div>
    </div>
  </div>
</section>
<!-- ▲▲▲▲▲ BÖLÜM: SÜREÇ VE NEDEN BİZ — BİTİŞ ▲▲▲▲▲ -->

<!-- ▼▼▼▼▼ BÖLÜM: REFERANSLAR — BAŞLANGIÇ ▼▼▼▼▼ -->
<section class="py-12 bg-[#fafafa] border-y border-slate-100" aria-labelledby="refs">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <h2 id="refs" class="text-center text-xs font-bold tracking-widest text-slate-500">BİRLİKTE ÇALIŞTIĞIMIZ MARKALARDAN</h2>
    {referans_seridi()}
  </div>
</section>
<!-- ▲▲▲▲▲ BÖLÜM: REFERANSLAR — BİTİŞ ▲▲▲▲▲ -->

<!-- ▼▼▼▼▼ BÖLÜM: SIK SORULANLAR — BAŞLANGIÇ ▼▼▼▼▼ -->
<section class="py-20 md:py-28 bg-white" aria-labelledby="sss">
  <div class="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8">
    <h2 id="sss" class="text-3xl sm:text-4xl font-extrabold text-slate-900 tracking-tight text-center">Sık sorulan sorular</h2>
    <div class="mt-10 grid gap-4">{sss}
    </div>
  </div>
</section>
<!-- ▲▲▲▲▲ BÖLÜM: SIK SORULANLAR — BİTİŞ ▲▲▲▲▲ -->

{ilgili_yazilar(h.get('ust', h['adres']), h.get('ilgili'))}
<!-- ▼▼▼▼▼ BÖLÜM: GÖRÜŞME ÇAĞRISI — BAŞLANGIÇ ▼▼▼▼▼ -->
<section id="teklif" class="pb-20 md:pb-28 bg-white" aria-labelledby="cagri">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="on-blue rounded-[40px] md:rounded-[56px] p-6 sm:p-10 md:p-14 text-white grid md:grid-cols-12 gap-8 md:gap-10 items-center" style="background:linear-gradient(160deg,#0866c9 0%,#1283e8 45%,#48a6fb 100%)">
      <div class="md:col-span-5">
        <h2 id="cagri" class="text-3xl md:text-5xl font-extrabold tracking-tight leading-[1.05]" style="text-wrap:balance">{'Ücretsiz ön görüşme ayarlayalım' if ust else e(h['kisa']) + ' için görüşelim'}</h2>
        <p class="mt-4 max-w-md text-white leading-relaxed">Formu doldurun, çalışma saatlerinde sizi arayalım. İhtiyacınızı dinleyip size uygun bir yol haritası çıkaralım; ilk görüşme ücretsiz.</p>
        <div class="mt-6 flex flex-wrap gap-3">
          <a class="inline-flex items-center px-5 py-2.5 rounded-full text-xs font-bold tracking-wider text-white bg-black/25 hover:bg-black/35 border border-white/20 transition-all" href="{TEL_LINK}">{TEL_GORUNEN}</a>
          <a class="inline-flex items-center px-5 py-2.5 rounded-full text-xs font-bold tracking-wider text-white bg-black/25 hover:bg-black/35 border border-white/20 transition-all" href="{WHATSAPP}" target="_blank" rel="noopener">WHATSAPP’TAN YAZIN</a>
        </div>
      </div>
      <div class="md:col-span-7">
        <form data-form="hizmet" action="/contact.php" method="post" novalidate class="relative bg-white rounded-[28px] p-6 sm:p-8 shadow-2xl grid gap-4 text-slate-900">
          <input type="hidden" name="tur" value="geri_arama"><input type="hidden" name="kaynak" value="{adres}"><input type="hidden" name="services[]" value="{e(h['kisa'])}">
          <div class="grid sm:grid-cols-2 gap-4">
            <div class="grid gap-1.5 content-start"><label for="h-name" class="text-xs font-bold text-slate-700">Adınız</label><input id="h-name" name="name" autocomplete="name" maxlength="100" data-zorunlu="Adınızı yazın." class="rounded-full bg-slate-50 border border-slate-200 px-5 py-3 text-sm focus:outline-none focus:ring-2 focus:ring-sky-500" placeholder="Ad Soyad"><p class="form-hata hidden text-xs font-semibold text-red-600"></p></div>
            <div class="grid gap-1.5 content-start"><label for="h-reach" class="text-xs font-bold text-slate-700">Telefon veya e-posta</label><input id="h-reach" name="reach" autocomplete="tel" maxlength="150" data-zorunlu="Size ulaşabileceğimiz bir telefon veya e-posta yazın." class="rounded-full bg-slate-50 border border-slate-200 px-5 py-3 text-sm focus:outline-none focus:ring-2 focus:ring-sky-500" placeholder="05xx xxx xx xx"><p class="form-hata hidden text-xs font-semibold text-red-600"></p></div>
          </div>
          <div class="grid gap-1.5"><label for="h-note" class="text-xs font-bold text-slate-700">Kısaca ihtiyacınız <span class="font-medium text-slate-400">(isteğe bağlı)</span></label><textarea id="h-note" name="note" rows="3" maxlength="2000" class="rounded-[20px] bg-slate-50 border border-slate-200 px-5 py-3 text-sm focus:outline-none focus:ring-2 focus:ring-sky-500" placeholder="Örneğin: Hedefimiz, bütçemiz ve ne zaman başlamak istediğimiz."></textarea></div>
          <div class="absolute -left-[9999px]" aria-hidden="true"><label for="h-website">Bu alanı boş bırakın</label><input id="h-website" name="website" tabindex="-1" autocomplete="off"></div>
          <div class="flex flex-wrap items-center gap-4">
            <button type="submit" class="inline-flex items-center gap-2 px-6 py-3 rounded-full text-xs font-bold tracking-wider text-black bg-[#D8F83C] hover:bg-[#c7e92e] transition-all shadow-lg hover:scale-105"><span data-etiket>GERİ ARAMA İSTE</span><span class="w-5 h-5 rounded-full bg-black text-[#D8F83C] flex items-center justify-center" aria-hidden="true">↗</span></button>
            <p class="text-xs text-slate-500 leading-relaxed sm:max-w-[22rem]">Paylaştığınız bilgiler talebinizi değerlendirmek ve sizinle iletişime geçmek için Clickbait Medya Limited Şirketi tarafından işlenir. Ayrıntılar: <a href="/kvkk/" class="font-semibold text-slate-700 underline decoration-slate-300 underline-offset-2">KVKK Aydınlatma Metni</a>.</p>
          </div>
          <div data-sonuc hidden tabindex="-1" role="status" class="rounded-[20px] bg-slate-50 p-5 text-sm leading-relaxed"></div>
        </form>
      </div>
    </div>
    <div class="mt-12">
      {ozel}
      <p class="text-center text-xs font-bold tracking-widest text-slate-500">DİĞER HİZMETLERİMİZ</p>
      <ul class="mt-5 flex flex-wrap justify-center gap-3">{diger}</ul>
    </div>
  </div>
</section>
<!-- ▲▲▲▲▲ BÖLÜM: GÖRÜŞME ÇAĞRISI — BİTİŞ ▲▲▲▲▲ -->
</main>

{alt_bilgi()}
</div>
<script src="/assets/js/site.js"></script>
</body>
</html>
'''

def blok_degistir(dosya, ad, yeni):
    p = os.path.join(KOK, dosya); s = open(p, encoding='utf-8').read()
    a = s.index(f'<!-- ▼▼▼▼▼ BÖLÜM: {ad} — BAŞLANGIÇ ▼▼▼▼▼ -->'); b = s.index(f'<!-- ▲▲▲▲▲ BÖLÜM: {ad} — BİTİŞ ▲▲▲▲▲ -->') + len(f'<!-- ▲▲▲▲▲ BÖLÜM: {ad} — BİTİŞ ▲▲▲▲▲ -->')
    open(p, 'w', encoding='utf-8').write(s[:a] + yeni + s[b:])

def site_haritasi():
    son = max([y['tarih'] for y in YAZILAR], default=BUGUN)
    urller = [('/', 'weekly', '1.0', BUGUN)] + [(f'/{h["adres"]}/', 'monthly', '0.9', BUGUN) for h in HIZMETLER] \
           + [(f'/{h["adres"]}/', 'monthly', '0.8', BUGUN) for h in ANKARA + SEKTORLER] \
           + [('/blog/', 'weekly', '0.7', son)] + [(f'/blog/{y["adres"]}/', 'monthly', '0.6', y['tarih']) for y in YAZILAR] + [('/kvkk/', 'yearly', '0.2', BUGUN)]
    satir = ''.join(f'  <url><loc>{ALAN}{u}</loc><lastmod>{t}</lastmod><changefreq>{c}</changefreq><priority>{p}</priority></url>\n' for u, c, p, t in urller)
    open(os.path.join(KOK, 'sitemap.xml'), 'w', encoding='utf-8').write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + satir + '</urlset>\n')

def llms_txt():
    """site/llms.txt: yapay zeka araçları için sitenin kısa özeti (llmstxt.org biçimi)."""
    hiz = '\n'.join(f'- [{h["kisa"]}]({ALAN}/{h["adres"]}/): {TANIMLAR[h["adres"]]}' for h in HIZMETLER)
    ank = '\n'.join(f'- [{h["kisa"]}]({ALAN}/{h["adres"]}/): {TANIMLAR[h["adres"]]}' for h in ANKARA)
    sek = '\n'.join(f'- [{h["kisa"]}]({ALAN}/{h["adres"]}/): {TANIMLAR[h["adres"]]}' for h in SEKTORLER)
    yaz = '\n'.join(f'- [{y["baslik"]}]({ALAN}/blog/{y["adres"]}/): {y.get("kisa_cevap") or y["description"]}' for y in YAZILAR)
    metin = f"""# Clickbait Dijital

> Clickbait Dijital, Ankara Çayyolu'nda 2013'ten beri hizmet veren bir dijital ajanstır (resmî unvan: Clickbait Medya Limited Şirketi). Yapay zeka danışmanlığı, web tasarım, dijital pazarlama (Google Ads, Meta reklamları, SEO), sosyal medya yönetimi ve kreatif hizmetler sunar. Ankara'daki işletmelerle yüz yüze, Türkiye'nin her yerinden işletmelerle online çalışır.

- Adres: Ümit Mah. Meksika Cad. No:56/21, Çayyolu, Ankara
- Telefon ve WhatsApp: {TEL_GORUNEN}
- E-posta: info@clickbait.com.tr
- Çalışma saatleri: Pazartesi–Cumartesi, 09:00–18:00
- Web sitesi: {ALAN}/
- Instagram: {INSTAGRAM}
- LinkedIn: {LINKEDIN}
- 2013'ten beri 300'den fazla çalışma, 50'den fazla marka.

## Hizmetler

{hiz}

## Ankara'ya özel hizmetler

{ank}

## Sektörlere özel hizmetler

{sek}

## Blog

{yaz}

## Diğer

- [İletişim ve teklif formu]({ALAN}/#iletisim)
- [KVKK aydınlatma metni]({ALAN}/kvkk/)
"""
    open(os.path.join(KOK, 'llms.txt'), 'w', encoding='utf-8').write(metin)

# ---------------------------------------------------------------- Blog
# Yazılar dev/blog/*.md dosyalarındadır. Üstte "---" arasında başlık bilgileri, altında Markdown metin.
# Desteklenen biçimler: ## ara başlık, ### alt başlık, - madde, 1. numaralı madde, > not kutusu, **kalın**, [bağlantı](adres)
AYLAR = ['Ocak', 'Şubat', 'Mart', 'Nisan', 'Mayıs', 'Haziran', 'Temmuz', 'Ağustos', 'Eylül', 'Ekim', 'Kasım', 'Aralık']
def tarih_tr(t):
    y, a, g = t.split('-'); return f'{int(g)} {AYLAR[int(a) - 1]} {y}'

def kisa_ad(s):
    tablo = str.maketrans('çğıöşüÇĞİÖŞÜ', 'cgiosuCGIOSU')
    return re.sub(r'[^a-z0-9]+', '-', s.translate(tablo).lower()).strip('-')

def satir_ici(t):
    t = e(t)
    t = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', t)
    t = re.sub(r'\[(.+?)\]\((.+?)\)', r'<a href="\2">\1</a>', t)
    return t

def grafik_html(baslik, satirlar, kaynak=''):
    """::: grafik bloğu → yatay çubuk grafik. Satır: '- Etiket | değer | gösterilecek metin' (değer 0–100 arası yüzde)."""
    ogeler = ''
    for x in satirlar:
        etiket, deger, metin = [p.strip() for p in (x.split('|') + ['', ''])[:3]]
        v = max(0.0, min(100.0, float(deger.replace(',', '.'))))
        ogeler += (f'<li class="yazi-grafik-satir"><span class="yazi-grafik-etiket">{satir_ici(etiket)}</span>'
                   f'<span class="yazi-grafik-cubuk" aria-hidden="true"><span style="width:{v:.1f}%"></span></span>'
                   f'<span class="yazi-grafik-deger">{e(metin or deger)}</span></li>')
    alt = f'<p class="yazi-grafik-kaynak">{satir_ici(kaynak)}</p>' if kaynak else ''
    return f'<figure class="yazi-grafik"><figcaption>{satir_ici(baslik)}</figcaption><ul>{ogeler}</ul>{alt}</figure>'

def tablo_html(satirlar):
    """| a | b | biçimindeki Markdown tablosu (2. satır ayırıcı |---|)."""
    hucre = lambda r: [c.strip() for c in r.strip().strip('|').split('|')]
    bas, govde = hucre(satirlar[0]), [hucre(r) for r in satirlar[2:]]
    th = ''.join(f'<th scope="col">{satir_ici(c)}</th>' for c in bas)
    tr = ''.join('<tr>' + ''.join(f'<td>{satir_ici(c)}</td>' for c in r) + '</tr>' for r in govde)
    return f'<div class="yazi-tablo"><table><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table></div>'

def md_html(metin):
    out, icindekiler, para = [], [], []
    liste = None
    blok = None   # ('grafik', başlık, kaynak, satırlar) ya da ('tablo', satırlar)
    def para_bitir():
        if para:
            out.append('<p>' + satir_ici(' '.join(para)) + '</p>'); para.clear()
    def liste_bitir():
        nonlocal liste
        if liste:
            out.append(f'<{liste[0]}>' + ''.join(f'<li>{satir_ici(x)}</li>' for x in liste[1]) + f'</{liste[0]}>')
            liste = None
    for satir in metin.split('\n'):
        s = satir.rstrip()
        if blok and blok[0] == 'grafik':
            if s == ':::':
                out.append(grafik_html(blok[1], blok[3], blok[2])); blok = None
            elif s.startswith('kaynak: '): blok = (blok[0], blok[1], s[8:], blok[3])
            elif s.startswith('- '): blok[3].append(s[2:])
            continue
        if s.startswith('::: grafik '):
            para_bitir(); liste_bitir(); blok = ('grafik', s[11:], '', []); continue
        if s.startswith('|'):
            para_bitir(); liste_bitir()
            if not blok: blok = ('tablo', [])
            blok[1].append(s); continue
        elif blok and blok[0] == 'tablo':
            out.append(tablo_html(blok[1])); blok = None
        m_ul, m_ol = re.match(r'^- (.*)', s), re.match(r'^\d+\. (.*)', s)
        if not s:
            para_bitir(); liste_bitir(); continue
        if s.startswith('## ') or s.startswith('### '):
            para_bitir(); liste_bitir()
            seviye = 2 if s.startswith('## ') else 3
            yazi = s[seviye + 1:]
            kimlik = kisa_ad(yazi)
            if seviye == 2: icindekiler.append((kimlik, yazi))
            out.append(f'<h{seviye} id="{kimlik}">{satir_ici(yazi)}</h{seviye}>')
        elif s.startswith('> '):
            para_bitir(); liste_bitir()
            out.append('<aside class="yazi-not"><p>' + satir_ici(s[2:]) + '</p></aside>')
        elif m_ul or m_ol:
            para_bitir()
            tur = 'ul' if m_ul else 'ol'
            if not liste or liste[0] != tur:
                liste_bitir(); liste = (tur, [])
            liste[1].append((m_ul or m_ol).group(1))
        else:
            liste_bitir(); para.append(s)
    if blok and blok[0] == 'tablo': out.append(tablo_html(blok[1]))
    para_bitir(); liste_bitir()
    return '\n'.join(out), icindekiler

def yazilari_oku():
    klasor = os.path.join(os.path.dirname(__file__), 'blog')
    yazilar = []
    for ad in (sorted(os.listdir(klasor)) if os.path.isdir(klasor) else []):
        if not ad.endswith('.md'): continue
        ham = open(os.path.join(klasor, ad), encoding='utf-8').read()
        _, ust, govde = ham.split('---', 2)
        y = {}
        for satir in ust.strip().split('\n'):
            k, v = satir.split(':', 1); y[k.strip()] = v.strip()
        y['adres'] = ad[:-3]
        y['govde'], y['icindekiler'] = md_html(govde.strip())
        y['dakika'] = max(1, round(len(re.sub('<[^>]+>', ' ', y['govde']).split()) / 200))
        yazilar.append(y)
    return sorted(yazilar, key=lambda y: (y['tarih'], y['adres']), reverse=True)

YAZILAR = yazilari_oku()
def hizmet_adi(adres): return next((h['kisa'] for h in HIZMETLER if h['adres'] == adres), '')
def etiket_baslik(s): return s[:1] + s[1:].replace('I', 'ı').replace('İ', 'i').lower()

def yazi_karti(y):
    return f"""
      <li class="bento-card-interactive overflow-hidden rounded-[28px] bg-white border border-slate-100 shadow-sm">
        <a href="/blog/{y['adres']}/" class="flex h-full flex-col">
          {blog_kapagi(y)}
          <span class="flex flex-1 flex-col gap-5 p-6">
          <span class="self-start text-[10px] font-bold tracking-wider rounded-full bg-[#eefbb8] text-slate-800 px-2.5 py-1">{e(y['etiket'])}</span>
          <span class="text-lg font-bold text-slate-900 leading-snug">{e(y['baslik'])}</span>
          <span class="text-sm text-slate-600 leading-relaxed">{e(y['ozet'])}</span>
          <span class="mt-auto text-xs font-semibold text-slate-500">{tarih_tr(y['tarih'])} · {y['dakika']} dk okuma</span>
          </span>
        </a>
      </li>"""

def ilgili_yazilar(kume, adresler=None):
    if adresler:   # sayfaya özel liste (sırasıyla, var olanlardan ilk 3)
        ilgili = [y for a in adresler for y in YAZILAR if y['adres'] == a][:3]
    else:
        ilgili = [y for y in YAZILAR if y['kume'] == kume][:3]
    if not ilgili: return ''
    return f"""<!-- ▼▼▼▼▼ BÖLÜM: İLGİLİ YAZILAR — BAŞLANGIÇ ▼▼▼▼▼ -->
<section class="pb-20 md:pb-28 bg-white" aria-labelledby="ilgili">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="flex flex-wrap items-end justify-between gap-4">
      <h2 id="ilgili" class="text-3xl sm:text-4xl font-extrabold text-slate-900 tracking-tight">Konuyla ilgili yazılar</h2>
      <a href="/blog/" class="text-sm font-bold text-slate-900 hover:underline">Tüm yazılar ↗</a>
    </div>
    <ul class="mt-10 grid grid-cols-1 md:grid-cols-3 gap-6">{''.join(yazi_karti(y) for y in ilgili)}
    </ul>
  </div>
</section>
<!-- ▲▲▲▲▲ BÖLÜM: İLGİLİ YAZILAR — BİTİŞ ▲▲▲▲▲ -->
"""

def sayfa_basi(baslik_html, ust_bilgi, alt_html='', yan=''):
    if yan:   # yazı sayfası: sağda kapak (yalnızca geniş ekranda)
        return f"""<section class="on-blue relative pt-5 pb-16 md:pb-20 overflow-hidden rounded-b-[40px] md:rounded-b-[56px]" style="background:linear-gradient(160deg,#0866c9 0%,#1283e8 55%,#48a6fb 100%)" aria-labelledby="h1">
{menu()}
  <div class="relative z-20 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pt-12 md:pt-16 grid grid-cols-1 lg:grid-cols-12 gap-10 items-center">
    <div class="lg:col-span-7">
    {ust_bilgi}
    {baslik_html}
    {alt_html}
    </div>
    <div class="hidden lg:block lg:col-span-5"><span class="block overflow-hidden rounded-[28px] shadow-2xl shadow-sky-950/30">{yan}</span></div>
  </div>
</section>"""
    return f"""<section class="on-blue relative pt-5 pb-16 md:pb-20 overflow-hidden rounded-b-[40px] md:rounded-b-[56px]" style="background:linear-gradient(160deg,#0866c9 0%,#1283e8 55%,#48a6fb 100%)" aria-labelledby="h1">
{menu()}
  <div class="relative z-20 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pt-12 md:pt-16">
    {ust_bilgi}
    {baslik_html}
    {alt_html}
  </div>
</section>"""

def ld_script(veri): return '<script type="application/ld+json">\n' + json.dumps(veri, ensure_ascii=False, indent=1) + '\n</script>\n'

def blog_liste():
    ld = {"@context": "https://schema.org", "@type": "Blog", "name": "Clickbait Blog", "url": ALAN + "/blog/", "inLanguage": "tr-TR",
          "publisher": {"@id": ALAN + "/#isletme"},
          "blogPost": [{"@type": "BlogPosting", "headline": y['baslik'], "url": f"{ALAN}/blog/{y['adres']}/", "datePublished": y['tarih']} for y in YAZILAR]}
    bas_html = bas('Blog: Yapay Zeka, Web Tasarım, Dijital Pazarlama | Clickbait',
                   'Yapay zeka, web tasarım, dijital pazarlama ve sosyal medya üzerine işletmeler için uygulanabilir rehberler. Clickbait Dijital kurucusu Şakir Yavuz’dan yazılar.', '/blog/', ld_script(ld))
    ust = '<nav aria-label="Konum" class="text-xs font-semibold text-white/85"><ol class="flex flex-wrap items-center gap-2"><li><a href="/" class="hover:text-white">Ana sayfa</a></li><li aria-hidden="true">/</li><li aria-current="page" class="text-white">Blog</li></ol></nav>'
    h1 = '<h1 id="h1" class="mt-6 max-w-4xl text-4xl sm:text-5xl md:text-6xl font-bold text-white tracking-tight leading-[1.08]" style="text-wrap:balance">Blog</h1>'
    alt = '<p class="mt-5 max-w-2xl text-base md:text-lg text-white leading-relaxed">Yapay zeka, web tasarım, dijital pazarlama ve sosyal medya üzerine işletmeler için uygulanabilir rehberler.</p>'
    kartlar = ''.join(yazi_karti(y) for y in YAZILAR)
    return bas_html + f"""<div class="font-sans antialiased text-slate-800 bg-white selection:bg-brand-lime selection:text-black" id="top">
{sayfa_basi(h1, ust, alt)}
<main id="icerik" class="py-16 md:py-24 bg-[#fafafa]">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <ul class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">{kartlar}
    </ul>
  </div>
</main>
{alt_bilgi()}
</div>
<script src="/assets/js/site.js"></script>
</body>
</html>
"""

def kisa_cevap_kutusu(y):
    """Yazının başında, başlıktaki soruya 2–3 cümlelik cevap (ön bilgide kisa_cevap)."""
    if not y.get('kisa_cevap'): return ''
    return (f'<div class="rounded-[24px] bg-sky-50 border border-sky-100 p-5 md:p-6"><p class="!mt-0 text-xs font-bold tracking-widest text-sky-700">KISA CEVAP</p>'
            f'<p class="!mt-2 text-slate-800 font-medium">{e(y["kisa_cevap"])}</p></div>\n')

def yazi_sayfasi(y):
    adres = f"/blog/{y['adres']}/"
    gorsel = f"/assets/img/blog/{y['adres']}.jpg"   # dev/kapaklar.py üretir
    if not os.path.exists(os.path.join(KOK, gorsel.lstrip('/'))): gorsel = '/assets/img/og-clickbait.jpg'
    hizmet = hizmet_adi(y['kume'])
    ld = {"@context": "https://schema.org", "@graph": [
      {"@type": "BlogPosting", "headline": y['baslik'], "description": y['description'], "url": ALAN + adres, "mainEntityOfPage": ALAN + adres,
       "datePublished": y['tarih'], "dateModified": y.get('guncelleme', y['tarih']), "inLanguage": "tr-TR",
       **({"abstract": y['kisa_cevap']} if y.get('kisa_cevap') else {}),
       "image": ALAN + gorsel,
       "author": {"@type": "Person", "@id": ALAN + "/#sakir-yavuz", "name": KURUCU['ad'], "jobTitle": "Kurucu", "image": ALAN + KURUCU['foto'], "worksFor": {"@id": ALAN + "/#isletme"}, "url": ALAN + "/ankara-seo/#uzman", "sameAs": [KURUCU['linkedin']]}, "publisher": {"@id": ALAN + "/#isletme"}},
      {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Ana sayfa", "item": ALAN + "/"},
        {"@type": "ListItem", "position": 2, "name": "Blog", "item": ALAN + "/blog/"},
        {"@type": "ListItem", "position": 3, "name": y['baslik'], "item": ALAN + adres}]}]}
    ekler = ld_script(ld) + f'<meta property="article:published_time" content="{y["tarih"]}">\n'
    ust = f'<nav aria-label="Konum" class="text-xs font-semibold text-white/85"><ol class="flex flex-wrap items-center gap-2"><li><a href="/" class="hover:text-white">Ana sayfa</a></li><li aria-hidden="true">/</li><li><a href="/blog/" class="hover:text-white">Blog</a></li><li aria-hidden="true">/</li><li aria-current="page" class="text-white">{e(etiket_baslik(y["etiket"]))}</li></ol></nav>'
    h1 = f'<h1 id="h1" class="mt-6 max-w-4xl text-3xl sm:text-4xl md:text-5xl font-bold text-white tracking-tight leading-[1.1]" style="text-wrap:balance">{e(y["baslik"])}</h1>'
    alt = f'<p class="mt-6 flex flex-wrap items-center gap-x-4 gap-y-2 text-sm text-white/90"><span class="text-[10px] font-bold tracking-wider rounded-full bg-[#D8F83C] text-black px-2.5 py-1">{e(y["etiket"])}</span><span>{e(KURUCU["ad"])}</span><time datetime="{y["tarih"]}">{tarih_tr(y["tarih"])}</time><span>{y["dakika"]} dk okuma</span></p>'
    toc = ''.join(f'<li><a href="#{k}" class="hover:text-slate-900">{e(b)}</a></li>' for k, b in y['icindekiler'])
    diger = [x for x in YAZILAR if x is not y][:3]
    diger_html = (f"""
<section class="py-16 md:py-24 bg-[#fafafa]" aria-labelledby="diger">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <h2 id="diger" class="text-3xl font-extrabold text-slate-900 tracking-tight">Diğer yazılar</h2>
    <ul class="mt-8 grid grid-cols-1 md:grid-cols-3 gap-6">{''.join(yazi_karti(x) for x in diger)}
    </ul>
  </div>
</section>""" if diger else '')
    sayfa = bas(y['title'], y['description'], adres, ekler, gorsel).replace('<meta property="og:type" content="website">', '<meta property="og:type" content="article">')
    return sayfa + f"""<div class="font-sans antialiased text-slate-800 bg-white selection:bg-brand-lime selection:text-black" id="top">
<a href="#icerik" class="sr-only focus:not-sr-only focus:fixed focus:top-3 focus:left-3 focus:z-50 focus:bg-white focus:px-4 focus:py-2 focus:rounded-full focus:font-bold">İçeriğe geç</a>
{sayfa_basi(h1, ust, alt, blog_kapagi(y, 'text-base'))}
<main id="icerik" class="py-14 md:py-20 bg-white">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 grid grid-cols-1 lg:grid-cols-12 gap-10">
    <article class="yazi lg:col-span-8 min-w-0">
{kisa_cevap_kutusu(y)}{y['govde']}
<div class="!mt-12 flex gap-4 items-start rounded-[24px] border border-slate-100 bg-[#fafafa] p-5 md:p-6"><img src="{KURUCU['foto_kare']}" alt="" width="96" height="96" loading="lazy" class="w-14 h-14 shrink-0 rounded-full object-cover bg-slate-200"><div><p class="!mt-0 text-xs font-bold tracking-widest text-slate-500">YAZAR</p><p class="!mt-1 font-extrabold text-slate-900">{e(KURUCU['ad'])}</p><p class="!mt-2 text-base text-slate-600">{e(KURUCU['yazar_notu'])}</p><p class="!mt-2 text-sm"><a href="{KURUCU['linkedin']}" target="_blank" rel="noopener">LinkedIn profili ↗</a></p></div></div>
    </article>
    <aside class="lg:col-span-4">
      <div class="lg:sticky lg:top-8 grid gap-6">
        <nav class="rounded-[24px] bg-[#fafafa] border border-slate-100 p-6" aria-label="İçindekiler">
          <p class="text-xs font-bold tracking-widest text-slate-500">İÇİNDEKİLER</p>
          <ol class="mt-4 grid gap-2.5 text-sm text-slate-600">{toc}</ol>
        </nav>
        <div class="on-blue rounded-[24px] p-6 text-white" style="background:linear-gradient(160deg,#0866c9 0%,#1283e8 55%,#48a6fb 100%)">
          <p class="text-xs font-bold tracking-widest text-white/85">İLGİLİ HİZMET</p>
          <p class="mt-2 text-xl font-extrabold">{e(hizmet)}</p>
          <p class="mt-2 text-sm text-white leading-relaxed">Ankara’daki ofisimizde ya da online görüşebiliriz. İlk görüşme ücretsiz.</p>
          <div class="mt-5 flex flex-wrap gap-2">
            <a href="/{y['kume']}/" class="inline-flex items-center gap-2 rounded-full bg-white text-slate-900 px-4 py-2 text-xs font-bold tracking-wider hover:scale-105 transition-all">HİZMETİ İNCELE ↗</a>
            <a href="/#iletisim" class="inline-flex items-center gap-2 rounded-full bg-[#D8F83C] text-black px-4 py-2 text-xs font-bold tracking-wider hover:scale-105 transition-all">GÖRÜŞME AYARLA</a>
          </div>
        </div>
      </div>
    </aside>
  </div>
</main>
{diger_html}
{alt_bilgi()}
</div>
<script src="/assets/js/site.js"></script>
</body>
</html>
"""

def ana_sayfa_blogu():
    kartlar = ''.join(yazi_karti(y) for y in YAZILAR[:3])
    return f"""<!-- ▼▼▼▼▼ BÖLÜM: BLOG — BAŞLANGIÇ ▼▼▼▼▼ -->
<section id="blog" class="py-20 md:py-24 bg-[#fafafa]" aria-labelledby="bt">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="flex flex-col sm:flex-row sm:items-end sm:justify-between gap-3">
      <div>
        <div class="inline-flex items-center gap-1.5 text-xs font-bold tracking-widest text-slate-500"><span class="w-1.5 h-1.5 rounded-full bg-slate-900"></span><span>BLOG</span></div>
        <h2 id="bt" class="mt-4 text-3xl sm:text-4xl font-extrabold text-slate-900 tracking-tight">Dijital üzerine notlar</h2>
      </div>
      <a href="/blog/" class="inline-flex self-start sm:self-auto items-center gap-2 rounded-full bg-[#111315] text-white px-5 py-2.5 text-xs font-bold tracking-wider hover:scale-105 transition-all">TÜM YAZILAR <span aria-hidden="true">↗</span></a>
    </div>
    <ul class="mt-10 grid grid-cols-1 md:grid-cols-3 gap-6">{kartlar}
    </ul>
  </div>
</section>
<!-- ▲▲▲▲▲ BÖLÜM: BLOG — BİTİŞ ▲▲▲▲▲ -->"""

def bloglari_yaz():
    os.makedirs(os.path.join(KOK, 'blog'), exist_ok=True)
    open(os.path.join(KOK, 'blog', 'index.html'), 'w', encoding='utf-8').write(blog_liste())
    for y in YAZILAR:
        os.makedirs(os.path.join(KOK, 'blog', y['adres']), exist_ok=True)
        open(os.path.join(KOK, 'blog', y['adres'], 'index.html'), 'w', encoding='utf-8').write(yazi_sayfasi(y))
        print('yazı:', y['adres'])
    if YAZILAR:
        blok_degistir('index.html', 'BLOG', ana_sayfa_blogu())
    p = os.path.join(KOK, 'index.html'); s = open(p, encoding='utf-8').read()
    open(p, 'w', encoding='utf-8').write(s.replace('href="#blog"', 'href="/blog/"'))


if __name__ == '__main__':
    for h in HIZMETLER + ANKARA + SEKTORLER:
        os.makedirs(os.path.join(KOK, h['adres']), exist_ok=True)
        open(os.path.join(KOK, h['adres'], 'index.html'), 'w', encoding='utf-8').write(hizmet_sayfasi(h))
        print('yazıldı:', h['adres'])
    bloglari_yaz()
    for d in ['index.html', 'kvkk/index.html']:
        blok_degistir(d, 'ALT BİLGİ', alt_bilgi())
    blok_degistir('index.html', 'MENÜ', menu(ana=True).lstrip())
    # Ana sayfa, hizmetler bölümünün altı: Ankara'ya özel sayfalara bağlantılar
    p = os.path.join(KOK, 'index.html'); s = open(p, encoding='utf-8').read()
    baglantilar = ''.join(f'<li><a href="/{x["adres"]}/" class="inline-flex items-center gap-2 rounded-full border border-slate-200 bg-white px-4 py-2.5 text-sm font-semibold text-slate-800 hover:border-slate-900 transition-colors">{e(x["kisa"])} <span aria-hidden="true">↗</span></a></li>' for x in ANKARA)
    blok = f'<!-- ANKARA BAĞLANTILARI -->\n    <div class="mt-12"><p class="text-center text-xs font-bold tracking-widest text-slate-500">ANKARA’YA ÖZEL HİZMETLER</p><ul class="mt-5 flex flex-wrap justify-center gap-3">{baglantilar}</ul></div>\n    <!-- /ANKARA BAĞLANTILARI -->'
    s = re.sub(r'<!-- ANKARA BAĞLANTILARI -->.*?<!-- /ANKARA BAĞLANTILARI -->', lambda _: blok, s, flags=re.S)
    open(p, 'w', encoding='utf-8').write(s)
    site_haritasi()
    llms_txt()
    print('alt bilgi, site haritası ve llms.txt güncellendi')
