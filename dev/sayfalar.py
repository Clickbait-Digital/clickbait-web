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
    'title': 'Yapay Zeka Danışmanlığı | Ankara ve Türkiye Geneli | Clickbait',
    'description': 'İşletmeniz için yapay zeka danışmanlığı: zaman kaybettiren işleri belirliyor, doğru araçları kurup ekibinizi eğitiyoruz. Ankara’da yüz yüze, Türkiye genelinde online.',
    'h1': 'Yapay zeka danışmanlığı: işinize gerçekten zaman kazandıran kurulumlar',
    'giris': 'Yapay zekayı denemek kolay, işin içine yerleştirmek zor. Ekibinizin her hafta tekrar eden işlerini birlikte buluyor, doğru aracı seçip iş akışınıza bağlıyor ve ekibinizi kullanımına alıştırıyoruz. Ankara’daki işletmelerle ofisimizde, Türkiye’nin her yerinden işletmelerle online çalışıyoruz.',
    'kartlar': [
      ('İhtiyaç analizi', 'Hangi işlerin otomatikleşebileceğini, hangilerinin insanda kalması gerektiğini birlikte çıkarıyoruz.'),
      ('Raporlama ve otomasyon', 'Haftalık raporlar, veri derleme, e-posta ve doküman hazırlığı gibi tekrar eden işleri otomatikleştiriyoruz.'),
      ('İçerik ve görsel üretimi', 'Sosyal medya, blog ve reklam metinleri için markanızın diline uygun yapay zeka iş akışları kuruyoruz.'),
      ('Müşteri iletişimi', 'Sık sorulan sorulara ilk yanıtı veren, gerektiğinde ekibinize aktaran asistanlar tasarlıyoruz.'),
      ('Ekip eğitimi', 'Ekibinize doğru komut yazmayı, sonuçları kontrol etmeyi ve araçları güvenle kullanmayı öğretiyoruz.'),
      ('Veri güvenliği ve KVKK', 'Hangi verinin hangi araçla paylaşılabileceğini belirleyen kullanım kuralları hazırlıyoruz.'),
    ],
    'adimlar': [
      ('Keşif görüşmesi', 'Ekibinizin bir haftasını konuşuyoruz: hangi işler tekrar ediyor, nerede vakit kaybediliyor.'),
      ('Pilot uygulama', 'Tek bir işle başlıyor, kazandırdığı zamanı ölçüyoruz.'),
      ('Yaygınlaştırma', 'İşe yarayan kurulumu diğer süreçlere ve ekiplere taşıyoruz.'),
      ('Eğitim ve takip', 'Ekibinizi eğitiyor, ilk haftalarda kullanımı birlikte takip ediyoruz.'),
    ],
    'sss': [
      ('Yapay zeka danışmanlığı hangi işletmeler için uygun?', 'Raporlama, teklif hazırlama, içerik üretimi ya da müşteri yazışmaları gibi her hafta tekrar eden işleri olan her ölçekte işletme için uygundur. Küçük ekiplerde kazanılan zaman çoğu zaman daha belirgin olur.'),
      ('Teknik bir ekibimiz olması gerekiyor mu?', 'Hayır. Kurulumu biz yapıyoruz, ekibinize günlük kullanımı öğretiyoruz. Yazılım ekibiniz varsa onlarla birlikte de çalışabiliriz.'),
      ('Verilerimiz güvende olur mu?', 'Kurulumdan önce hangi verinin hangi araçla paylaşılabileceğini birlikte belirliyoruz. Kişisel ve gizli verileri KVKK’ya uygun şekilde ayıran kullanım kuralları hazırlıyoruz.'),
      ('Ankara dışındaki işletmelere de hizmet veriyor musunuz?', 'Evet. Görüşmeleri, kurulumu ve eğitimleri online yürütebiliyoruz. Ankara’daki işletmelerle Çayyolu’ndaki ofisimizde de buluşuyoruz.'),
      ('İlk görüşme nasıl ilerliyor?', 'Ekibinizin iş akışını dinliyoruz ve görüşmenin sonunda yapay zekayla başlanabilecek ilk işi öneriyoruz.'),
    ],
  },
  {
    'adres': 'web-tasarim', 'kisa': 'Web tasarım', 'renk': 'sky',
    'title': 'Ankara Web Tasarım | Kurumsal Web Sitesi Yaptırma | Clickbait',
    'description': 'Ankara web tasarım: kurumsal web sitesi yaptırmak isteyen işletmeler için mobil uyumlu, hızlı ve Google’a hazır siteler; hosting ve bakım dahil. Türkiye geneline online hizmet.',
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
    'sss': [
      ('Ankara dışındaki firmalarla da çalışıyor musunuz?', 'Evet. Görüşmeleri online yapıyor, süreci uzaktan yürütüyoruz. Ankara’daki müşterilerimizle Çayyolu’ndaki ofisimizde de buluşuyoruz.'),
      ('Bir web sitesi ne kadar sürede hazır olur?', 'Sayfa sayısına, özel özelliklere ve içeriklerin hazır olmasına göre değişir. Keşif görüşmesinden sonra size net bir takvim veriyoruz.'),
      ('Web sitesi fiyatı neye göre belirleniyor?', 'Sayfa sayısı, özel tasarım ihtiyacı, e-ticaret gibi ek özellikler ve içerik üretimi fiyatı belirler. İhtiyacınızı dinledikten sonra kalem kalem teklif hazırlıyoruz.'),
      ('Siteyi kendimiz güncelleyebilir miyiz?', 'İsterseniz yönetim paneli kuruyor ve ekibinize kullanımını gösteriyoruz. Güncellemeleri bizim yapmamızı da tercih edebilirsiniz.'),
      ('Mevcut sitemizi yenileyebilir misiniz?', 'Evet. Önce mevcut sitenin hızını, arama motoru durumunu ve içeriklerini inceliyoruz. Google’daki sıralamanızı korumak için eski adresleri yeni sayfalara yönlendiriyoruz.'),
    ],
  },
  {
    'adres': 'dijital-pazarlama', 'kisa': 'Dijital pazarlama', 'renk': 'blue',
    'title': 'Ankara Dijital Pazarlama Ajansı | Google Ads, Meta, SEO | Clickbait',
    'description': 'Ankara’da dijital pazarlama: Google Ads ve Meta reklam yönetimi, SEO ve dijital medya planlama. Bütçenizi doğru kanala koyuyor, sonuçları ölçülebilir şekilde raporluyoruz.',
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
    'sss': [
      ('Reklam bütçesi ne kadar olmalı?', 'Sektörünüze, hedef bölgenize ve hedeflerinize göre değişir. Küçük bir test bütçesiyle başlayıp sonuçlara göre artırmayı öneriyoruz.'),
      ('SEO sonuçları ne zaman görülür?', 'SEO uzun vadeli bir çalışmadır; ilk iyileşmeler genellikle birkaç ay içinde görülmeye başlar. Süreyi rekabet ve sitenizin mevcut durumu belirler.'),
      ('Reklamları sadece Ankara’yı hedefleyecek şekilde ayarlayabilir misiniz?', 'Evet. Reklamları il, ilçe ya da belirli bir mesafe içindeki kullanıcılarla sınırlayabiliyoruz. Türkiye geneline açılan kampanyalar da hazırlıyoruz.'),
      ('Reklam hesapları kimin adına açılıyor?', 'Hesapların sizin adınıza açılmasını ve sahipliğin sizde kalmasını öneriyoruz; biz yönetici olarak erişiyoruz.'),
      ('Raporları ne sıklıkla paylaşıyorsunuz?', 'Her ay rapor paylaşıyoruz; kampanya dönemlerinde ihtiyaca göre daha sık özetler de hazırlıyoruz.'),
    ],
  },
  {
    'adres': 'sosyal-medya-yonetimi', 'kisa': 'Sosyal medya yönetimi', 'renk': 'dark',
    'title': 'Ankara Sosyal Medya Ajansı | Sosyal Medya Yönetimi | Clickbait',
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
    'sss': [
      ('Hangi platformlarda hizmet veriyorsunuz?', 'Ağırlıklı olarak Instagram ve LinkedIn’de çalışıyoruz. Markanıza uygunsa diğer platformlar için de plan hazırlıyoruz.'),
      ('İçerikleri yayından önce görebilir miyiz?', 'Evet. Aylık plan ve tasarımlar onayınıza sunulur, yalnızca onaylanan içerikler yayınlanır.'),
      ('Ayda kaç paylaşım yapılıyor?', 'Paylaşım sayısı hedeflerinize ve seçtiğiniz pakete göre belirlenir; teklifte net sayıyı yazıyoruz.'),
      ('Sponsorlu reklamlar dahil mi?', 'Sponsorlu paylaşımları dijital pazarlama hizmetimiz kapsamında yönetiyoruz. İki hizmeti birlikte alabilirsiniz.'),
      ('Ankara dışındaki markalarla çalışıyor musunuz?', 'Evet. Planlama, onay ve raporlama süreçlerini online yürütüyoruz.'),
    ],
  },
  {
    'adres': 'kreatif-hizmetler', 'kisa': 'Kreatif hizmetler', 'renk': 'lime',
    'title': 'Ankara Logo Tasarım ve Kurumsal Kimlik | Clickbait',
    'description': 'Ankara logo tasarım ve kurumsal kimlik: markanızın her yerde aynı dili konuşması için logo, renk, yazı tipi, şablon ve basılı işler. Türkiye geneline online hizmet.',
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
    'title': 'Ankara SEO Ajansı | Google’da Üst Sıralar İçin SEO | Clickbait',
    'description': 'Ankara SEO hizmeti: teknik SEO, yerel SEO, Google İşletme Profili ve içerik çalışmasıyla sitenizi Google’da üst sıralara taşımak için çalışıyoruz. Her ay şeffaf rapor.',
    'h1': 'Ankara SEO: Google’da sizi arayan müşteriler sizi bulsun',
    'giris': 'Sitenizin teknik altyapısını düzeltiyor, müşterilerinizin Ankara’da ve Türkiye genelinde gerçekten aradığı kelimelere göre içerik planlıyor, Google İşletme Profilinizi güçlendiriyoruz. Her ay neyin değiştiğini sade bir raporla paylaşıyoruz.',
    'kapsam': 'Ankara SEO çalışmamızda neler var?',
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
      ('SEO mu, Google Ads mi?', 'Google Ads ile reklam verdiğiniz sürece üst sıralarda görünürsünüz; bütçe bittiğinde görünürlük de durur. SEO ise organik sonuçlarda kalıcı bir yer edinmek için yapılan çalışmadır: sonuç vermesi zaman alır ama tıklama başına ödeme yapmazsınız. Çoğu işletmeye ikisini birlikte yürütmeyi, reklamdan gelen verilerle SEO önceliklerini belirlemeyi öneriyoruz. Farkları [Google Ads mi SEO mu?](/blog/google-ads-mi-seo-mu/) yazımızda karşılaştırdık; reklam tarafı için [Ankara Google Ads ajansı](/ankara-google-ads-ajansi/) sayfamıza bakabilirsiniz.'),
      ('Neyi söz veriyoruz, neyi vermiyoruz?', 'Sıralamayı Google kendi algoritmasıyla belirler; “bir ayda ilk sıra” gibi sözler veren bir ajansa temkinli yaklaşmanızı öneririz. Bizim sözümüz yaptığımız her işi açıkça raporlamak, Google’ın kurallarına uygun çalışmak ve sonuçları Search Console verileriyle ölçmektir. Sitenizi yeniliyorsanız sıralamanızı kaybetmemek için eski adresleri yeni sayfalara yönlendirmeyi de bu sürece dahil ediyoruz.'),
    ],
    'sss': [
      ('SEO ne kadar sürede sonuç verir?', 'İlk iyileşmeler genellikle birkaç ay içinde görülmeye başlar. Rekabetin yüksek olduğu kelimelerde bu süre uzar. Sitenizin mevcut durumuna bakıp size gerçekçi bir takvim veriyoruz.'),
      ('SEO fiyatları neye göre belirlenir?', 'Sitenizin teknik durumu, hedeflediğiniz kelimelerin sayısı ve rekabeti, ne kadar içerik üretileceği fiyatı belirler. Denetimden sonra kalem kalem teklif hazırlıyoruz.'),
      ('Sitemizi siz yapmadınız, yine de SEO yapabilir misiniz?', 'Evet. Önce mevcut sitenin altyapısını inceliyoruz. Düzeltilmesi gereken teknik sorunları raporluyor, sitenizi yapan ekiple ya da doğrudan biz düzenliyoruz.'),
      ('Yerel SEO nedir?', 'İşletmenizin “Ankara” ya da “yakınımdaki” gibi konum içeren aramalarda ve Google Haritalar’da görünmesi için yapılan çalışmadır. Google İşletme Profili, müşteri yorumları ve tutarlı iletişim bilgileri bu çalışmanın temelidir.'),
      ('Aylık raporda neler oluyor?', 'Hangi aramalarda göründüğünüz, sıralama değişimleri, siteye gelen ziyaretçi ve talep sayısı ile o ay yaptığımız işler. Bir sonraki ayın planını da rapora ekliyoruz.'),
    ],
  },
  {
    'adres': 'ankara-google-ads-ajansi', 'kisa': 'Ankara Google Ads ajansı', 'ust': 'dijital-pazarlama', 'renk': 'blue',
    'title': 'Ankara Google Ads Ajansı | Google Reklam Yönetimi | Clickbait',
    'description': 'Ankara Google Ads ajansı: arama, YouTube ve Performance Max kampanyalarınızı kuruyor, dönüşüm takibiyle ölçüyor, her ay raporluyoruz. Reklam bütçeniz müşteri getiren aramalara gitsin.',
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
      ('Bütçe ne kadar olmalı?', 'Tek bir doğru rakam yoktur; sektörünüzdeki rekabet, hedef bölgenin büyüklüğü ve bir müşterinin size kazandırdığı tutar belirler. Küçük bir test bütçesiyle başlayıp hangi kelimelerin gerçekten talep getirdiğini görmeyi, sonra bütçeyi bu kelimelere yoğunlaştırmayı öneriyoruz. Konuyu [Google Ads mi SEO mu?](/blog/google-ads-mi-seo-mu/) yazımızda da ele aldık.'),
      ('Reklam hesabı kimin adına açılır?', 'Hesabın sizin adınıza açılmasını ve sahipliğin sizde kalmasını öneriyoruz; biz yönetici olarak erişiyoruz. Böylece birlikte çalışmayı bıraksanız bile geçmiş veriler ve kampanyalar sizde kalır. Organik görünürlük için reklamla birlikte [Ankara SEO](/ankara-seo/) çalışması da yürütebiliriz.'),
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
    'adres': 'ankara-reklam-ajansi', 'kisa': 'Ankara reklam ajansı', 'ust': 'dijital-pazarlama', 'renk': 'dark',
    'title': 'Ankara Reklam Ajansı | Dijital Reklam ve Kreatif | Clickbait',
    'description': 'Ankara’da dijital reklam ajansı: Google ve Meta reklamları, sosyal medya, reklam kreatifleri ve web sitesi tek ekipte. 2013’ten beri Ankara’daki markalarla çalışıyoruz.',
    'h1': 'Ankara reklam ajansı: dijitalde reklam, kreatif ve web tek ekipte',
    'giris': 'Reklam fikrini, tasarımını, yayınlanacağı kanalı ve ölçümünü aynı ekipte yürütüyoruz. Google ve Instagram reklamlarından sosyal medya içeriklerine, reklamın yönlendirdiği web sayfasına kadar her parçayı birlikte planlıyoruz. 2013’ten beri Çayyolu’ndaki ofisimizden Ankara’daki markalarla çalışıyoruz.',
    'kapsam': 'Reklam ajansı olarak neler yapıyoruz?',
    'kartlar': [
      ('Google reklamları', 'Arama, YouTube ve görüntülü reklam kampanyalarını kuruyor ve yönetiyoruz.'),
      ('Instagram ve Facebook reklamları', 'Hedef kitle, kreatif ve bütçe yönetimiyle Meta reklamları.'),
      ('Reklam kreatifleri', 'Reklam görselleri, kısa videolar ve reklam metinleri üretiyoruz.'),
      ('Sosyal medya yönetimi', 'Reklamlarınızı destekleyen düzenli ve markanıza ait içerikler.'),
      ('Açılış sayfası ve web sitesi', 'Reklamdan gelen ziyaretçiyi müşteriye çeviren sayfalar tasarlıyoruz.'),
      ('Ölçüm ve raporlama', 'Hangi kanalın ne kadar talep getirdiğini ölçüp her ay raporluyoruz.'),
    ],
    'adimlar': [
      ('Tanışma', 'Markanızı, hedef kitlenizi, rakiplerinizi ve bütçenizi konuşuyoruz.'),
      ('Plan', 'Hangi kanalda, hangi mesajla, ne kadar bütçeyle görüneceğinizi planlıyoruz.'),
      ('Üretim ve yayın', 'Kreatifleri hazırlıyor, onayınızdan sonra kampanyaları yayına alıyoruz.'),
      ('Ölçüm', 'Sonuçları izliyor, işe yarayan kanala daha fazla bütçe ayırıyoruz.'),
    ],
    'metin': [
      ('Dijital reklam ajansı ne yapar?', 'Geleneksel bir reklam ajansı televizyon, radyo ya da açık hava reklamlarıyla geniş kitlelere ulaşır. Dijital reklam ajansı ise reklamı doğrudan ilgilenen kişiye gösterir ve sonucunu ölçer: kaç kişinin reklamı gördüğünü, kaçının sitenize girdiğini ve kaçının sizi aradığını bilirsiniz. Uzmanlığımız dijital kanallardadır; televizyon, radyo ve açık hava reklamı yapmıyoruz.'),
      ('Ankara’daki bir işletme için doğru kanal hangisi?', 'Sizi zaten arayan müşterilere ulaşmak istiyorsanız Google arama reklamları en hızlı yoldur. Ürününüz ya da hizmetiniz görsel olarak güçlüyse ve henüz kimse sizi aramıyorsa Instagram reklamları ilgi uyandırmak için daha uygundur. Kalıcı görünürlük için bunlara [SEO](/ankara-seo/) eklenir. Çoğu zaman doğru cevap küçük bütçelerle birkaç kanalı test edip sonuç vereni büyütmektir. Google tarafını [Ankara Google Ads ajansı](/ankara-google-ads-ajansi/) sayfamızda ayrıntılı anlattık.'),
      ('Neden tek ekip?', 'Reklamı bir ajans, tasarımı başka bir tasarımcı, web sitesini üçüncü bir firma yaptığında mesajlar birbirini tutmaz ve sorun çıktığında kimin sorumlu olduğu belirsizleşir. Reklam, kreatif, [web sitesi](/web-tasarim/) ve [sosyal medya](/sosyal-medya-yonetimi/) aynı ekipte olduğunda kampanya tek bir plandan çıkar ve sonuçlar tek raporda görülür.'),
    ],
    'sss': [
      ('Televizyon, radyo ya da billboard reklamı yapıyor musunuz?', 'Hayır. Uzmanlığımız dijital kanallar: Google, Instagram, Facebook, YouTube, sosyal medya ve web sitesi.'),
      ('Küçük bir bütçeyle başlayabilir miyiz?', 'Evet. Küçük bir test bütçesiyle başlayıp sonuç veren kanalı büyütmeyi öneriyoruz.'),
      ('Reklam görsellerini ve videolarını siz mi hazırlıyorsunuz?', 'Evet. Reklam görsellerini, kısa videoları ve metinleri ekibimiz hazırlıyor; tüm içerikler yayından önce onayınıza sunuluyor.'),
      ('Sonuçları nasıl görüyoruz?', 'Her ay hangi kanala ne kadar harcandığını ve kaç talep geldiğini gösteren sade bir rapor paylaşıyoruz.'),
      ('Ankara dışındaki markalarla çalışıyor musunuz?', 'Evet. Planlama, onay ve raporlama süreçlerini online yürütüyoruz; Ankara’daki müşterilerimizle Çayyolu’ndaki ofisimizde de buluşuyoruz.'),
    ],
  },
  {
    'adres': 'ankara-e-ticaret-sitesi', 'kisa': 'Ankara e-ticaret sitesi', 'ust': 'web-tasarim', 'renk': 'sky',
    'title': 'Ankara E-Ticaret Sitesi Kurulumu | Online Mağaza | Clickbait',
    'description': 'Ankara’da e-ticaret sitesi kurulumu: mobil uyumlu mağaza tasarımı, ürün yönetimi, ödeme ve kargo entegrasyonları, SEO altyapısı ve reklam ölçümüyle satış yapan online mağazalar.',
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
    'title': 'Ankara Instagram Reklam Ajansı | Meta Reklam Yönetimi | Clickbait',
    'description': 'Ankara Instagram reklam ajansı: Instagram ve Facebook reklamlarınızı hedef kitle, kreatif ve bütçe yönetimiyle kuruyor, talepleri ölçüyor ve her ay raporluyoruz.',
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

def menu():
    linkler = [('/#hizmetler', 'Hizmetler'), ('/#projeler', 'Projeler'), ('/#hakkimizda', 'Hakkımızda'), ('/blog/', 'Blog'), ('/#iletisim', 'İletişim')]
    ust = ''.join(f'\n        <a class="hover:text-white transition-colors" href="{u}">{buyuk(a)}</a>' for u, a in linkler)
    mob = ''.join(f'\n        <a class="px-4 py-3.5 rounded-2xl text-lg font-bold text-slate-900 hover:bg-slate-100" href="{u}">{a}</a>' for u, a in linkler)
    return f'''  <!-- ▼▼▼▼▼ BÖLÜM: MENÜ — BAŞLANGIÇ ▼▼▼▼▼ -->
  <header class="relative z-40 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="flex items-center justify-between h-14 gap-4">
      <a aria-label="Clickbait, ana sayfa" class="flex items-center group" href="/">
        <img src="/assets/img/logo-beyaz.svg" alt="Clickbait" width="137" height="32" class="h-7 sm:h-8 w-auto drop-shadow-sm transition-transform group-hover:scale-105">
      </a>
      <nav aria-label="Ana menü" class="hidden md:flex items-center gap-8 lg:gap-9 text-xs font-semibold tracking-wider text-white/90">{ust}
      </nav>
      <div class="flex items-center gap-2">
        <a class="hidden sm:inline-flex items-center justify-center px-5 py-2.5 rounded-full text-xs font-bold tracking-wider text-black bg-[#D8F83C] hover:bg-[#c9eb2f] transition-all shadow-md shadow-black/5 hover:scale-[1.03]" href="/#iletisim">TEKLİF ALIN</a>
        <button id="menuBtn" class="md:hidden inline-flex items-center px-4 py-2.5 rounded-full text-xs font-bold tracking-wider text-white bg-black/25 backdrop-blur-md border border-white/25" aria-expanded="false" aria-controls="mobileMenu">MENÜ</button>
      </div>
    </div>
    <div id="mobileMenu" hidden class="md:hidden absolute left-4 right-4 top-16 bg-white rounded-3xl shadow-2xl p-3">
      <nav aria-label="Mobil menü" class="grid">{mob}
        <a class="mt-2 text-center px-5 py-3.5 rounded-full text-sm font-bold tracking-wider text-black bg-[#D8F83C]" href="/#iletisim">TEKLİF ALIN</a>
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
      {"@type": "Service", "name": h['kisa'], "serviceType": h['kisa'], "description": h['description'], "url": ALAN + adres,
       "provider": {"@id": ALAN + "/#isletme"},
       "areaServed": [{"@type": "City", "name": "Ankara"}] + ([] if ust else [{"@type": "Country", "name": "Türkiye"}])},
      {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Ana sayfa", "item": ALAN + "/"},
        {"@type": "ListItem", "position": 2, "name": kirinti[0], "item": ALAN + kirinti[1]},
        {"@type": "ListItem", "position": 3, "name": h['kisa'], "item": ALAN + adres}]},
      {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": s, "acceptedAnswer": {"@type": "Answer", "text": c}} for s, c in h['sss']]}]}
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

{metin_bolumu}
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

{ilgili_yazilar(h.get('ust', h['adres']))}
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
           + [(f'/{h["adres"]}/', 'monthly', '0.8', BUGUN) for h in ANKARA] \
           + [('/blog/', 'weekly', '0.7', son)] + [(f'/blog/{y["adres"]}/', 'monthly', '0.6', y['tarih']) for y in YAZILAR] + [('/kvkk/', 'yearly', '0.2', BUGUN)]
    satir = ''.join(f'  <url><loc>{ALAN}{u}</loc><lastmod>{t}</lastmod><changefreq>{c}</changefreq><priority>{p}</priority></url>\n' for u, c, p, t in urller)
    open(os.path.join(KOK, 'sitemap.xml'), 'w', encoding='utf-8').write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + satir + '</urlset>\n')

def llms_txt():
    """site/llms.txt: yapay zeka araçları için sitenin kısa özeti (llmstxt.org biçimi)."""
    hiz = '\n'.join(f'- [{h["kisa"]}]({ALAN}/{h["adres"]}/): {h["description"]}' for h in HIZMETLER)
    ank = '\n'.join(f'- [{h["kisa"]}]({ALAN}/{h["adres"]}/): {h["description"]}' for h in ANKARA)
    yaz = '\n'.join(f'- [{y["baslik"]}]({ALAN}/blog/{y["adres"]}/): {y["description"]}' for y in YAZILAR)
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

def md_html(metin):
    out, icindekiler, para = [], [], []
    liste = None
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

def ilgili_yazilar(kume):
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
    bas_html = bas('Blog: Yapay Zeka, Web Tasarım ve Dijital Pazarlama | Clickbait',
                   'Yapay zeka, web tasarım, dijital pazarlama ve sosyal medya üzerine işletmeler için uygulanabilir rehberler. Clickbait ekibinden yazılar.', '/blog/', ld_script(ld))
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

def yazi_sayfasi(y):
    adres = f"/blog/{y['adres']}/"
    gorsel = f"/assets/img/blog/{y['adres']}.jpg"   # dev/kapaklar.py üretir
    if not os.path.exists(os.path.join(KOK, gorsel.lstrip('/'))): gorsel = '/assets/img/og-clickbait.jpg'
    hizmet = hizmet_adi(y['kume'])
    ld = {"@context": "https://schema.org", "@graph": [
      {"@type": "BlogPosting", "headline": y['baslik'], "description": y['description'], "url": ALAN + adres, "mainEntityOfPage": ALAN + adres,
       "datePublished": y['tarih'], "dateModified": y.get('guncelleme', y['tarih']), "inLanguage": "tr-TR",
       "image": ALAN + gorsel,
       "author": {"@type": "Organization", "name": "Clickbait Dijital", "url": ALAN + "/"}, "publisher": {"@id": ALAN + "/#isletme"}},
      {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Ana sayfa", "item": ALAN + "/"},
        {"@type": "ListItem", "position": 2, "name": "Blog", "item": ALAN + "/blog/"},
        {"@type": "ListItem", "position": 3, "name": y['baslik'], "item": ALAN + adres}]}]}
    ekler = ld_script(ld) + f'<meta property="article:published_time" content="{y["tarih"]}">\n'
    ust = f'<nav aria-label="Konum" class="text-xs font-semibold text-white/85"><ol class="flex flex-wrap items-center gap-2"><li><a href="/" class="hover:text-white">Ana sayfa</a></li><li aria-hidden="true">/</li><li><a href="/blog/" class="hover:text-white">Blog</a></li><li aria-hidden="true">/</li><li aria-current="page" class="text-white">{e(etiket_baslik(y["etiket"]))}</li></ol></nav>'
    h1 = f'<h1 id="h1" class="mt-6 max-w-4xl text-3xl sm:text-4xl md:text-5xl font-bold text-white tracking-tight leading-[1.1]" style="text-wrap:balance">{e(y["baslik"])}</h1>'
    alt = f'<p class="mt-6 flex flex-wrap items-center gap-x-4 gap-y-2 text-sm text-white/90"><span class="text-[10px] font-bold tracking-wider rounded-full bg-[#D8F83C] text-black px-2.5 py-1">{e(y["etiket"])}</span><span>Clickbait ekibi</span><time datetime="{y["tarih"]}">{tarih_tr(y["tarih"])}</time><span>{y["dakika"]} dk okuma</span></p>'
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
{y['govde']}
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
    for h in HIZMETLER + ANKARA:
        os.makedirs(os.path.join(KOK, h['adres']), exist_ok=True)
        open(os.path.join(KOK, h['adres'], 'index.html'), 'w', encoding='utf-8').write(hizmet_sayfasi(h))
        print('yazıldı:', h['adres'])
    bloglari_yaz()
    for d in ['index.html', 'kvkk/index.html']:
        blok_degistir(d, 'ALT BİLGİ', alt_bilgi())
    # Ana sayfa, hizmetler bölümünün altı: Ankara'ya özel sayfalara bağlantılar
    p = os.path.join(KOK, 'index.html'); s = open(p, encoding='utf-8').read()
    baglantilar = ''.join(f'<li><a href="/{x["adres"]}/" class="inline-flex items-center gap-2 rounded-full border border-slate-200 bg-white px-4 py-2.5 text-sm font-semibold text-slate-800 hover:border-slate-900 transition-colors">{e(x["kisa"])} <span aria-hidden="true">↗</span></a></li>' for x in ANKARA)
    blok = f'<!-- ANKARA BAĞLANTILARI -->\n    <div class="mt-12"><p class="text-center text-xs font-bold tracking-widest text-slate-500">ANKARA’YA ÖZEL HİZMETLER</p><ul class="mt-5 flex flex-wrap justify-center gap-3">{baglantilar}</ul></div>\n    <!-- /ANKARA BAĞLANTILARI -->'
    s = re.sub(r'<!-- ANKARA BAĞLANTILARI -->.*?<!-- /ANKARA BAĞLANTILARI -->', lambda _: blok, s, flags=re.S)
    open(p, 'w', encoding='utf-8').write(s)
    site_haritasi()
    llms_txt()
    print('alt bilgi, site haritası ve llms.txt güncellendi')
