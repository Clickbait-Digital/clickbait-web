#!/usr/bin/env python3
"""Clickbait — hizmet sayfası üreticisi.

Hizmet sayfalarını (site/<adres>/index.html), ortak alt bilgiyi ve site haritasını üretir.
Metinleri değiştirmek için aşağıdaki HIZMETLER listesini düzenleyip çalıştırın:

    python3 dev/sayfalar.py
"""
import json, os, re, datetime, html

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
    'title': 'Ankara Web Tasarım | Kurumsal Web Sitesi ve E-Ticaret | Clickbait',
    'description': 'Ankara’da kurumsal web sitesi ve e-ticaret tasarımı. Mobil uyumlu, hızlı ve arama motorlarına hazır siteler; hosting ve bakım dahil. Türkiye geneline online hizmet.',
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
    'title': 'Ankara Sosyal Medya Yönetimi | Instagram ve LinkedIn | Clickbait',
    'description': 'Ankara’da sosyal medya yönetimi: aylık içerik planı, post ve story tasarımı, paylaşım takvimi ve raporlama. Instagram ve LinkedIn’de markanızın sesi oluyoruz.',
    'h1': 'Ankara sosyal medya yönetimi: planlı, tutarlı ve markanıza ait içerikler',
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
    'title': 'Ankara Kurumsal Kimlik, Logo ve Grafik Tasarım | Clickbait',
    'description': 'Ankara’da kurumsal kimlik, logo ve grafik tasarım. Markanızın her yerde aynı dili konuşması için logo, renk, yazı tipi, şablon ve basılı işler. Türkiye geneline online hizmet.',
    'h1': 'Kurumsal kimlik ve grafik tasarım: markanız her yerde aynı dili konuşsun',
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

# ---------------------------------------------------------------- Parçalar
def e(s): return html.escape(s, quote=True)

IKON_IG = '<svg class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1" fill="currentColor" stroke="none"/></svg>'
IKON_LI = '<svg class="w-5 h-5" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M4.98 3.5a2.5 2.5 0 11-.01 5 2.5 2.5 0 01.01-5zM3 9h4v12H3zM9 9h3.8v1.7h.05c.53-1 1.83-2.05 3.77-2.05 4.03 0 4.78 2.65 4.78 6.1V21h-4v-5.4c0-1.3-.02-2.95-1.8-2.95-1.8 0-2.08 1.4-2.08 2.86V21H9z"/></svg>'

def alt_bilgi():
    hiz = ''.join(f'<li><a class="hover:text-slate-900" href="/{h["adres"]}/">{e(h["kisa"])}</a></li>' for h in HIZMETLER)
    return f'''<!-- ▼▼▼▼▼ BÖLÜM: ALT BİLGİ — BAŞLANGIÇ ▼▼▼▼▼ -->
<footer class="bg-white border-t border-slate-200 pt-12 pb-[calc(2.5rem+env(safe-area-inset-bottom,0px))]">
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
        <ul class="mt-4 grid gap-2.5"><li><a class="hover:text-slate-900" href="/#projeler">Projeler</a></li><li><a class="hover:text-slate-900" href="/#hakkimizda">Hakkımızda</a></li><li><a class="hover:text-slate-900" href="/#blog">Blog</a></li><li><a class="hover:text-slate-900" href="/kvkk/">KVKK</a></li></ul>
      </nav>
      <div class="md:col-span-3">
        <p class="text-xs font-bold tracking-widest text-slate-900">İLETİŞİM</p>
        <ul class="mt-4 grid gap-2.5"><li><a class="hover:text-slate-900" href="{TEL_LINK}">{TEL_GORUNEN}</a></li><li><a class="hover:text-slate-900" href="mailto:info@clickbait.com.tr">info@clickbait.com.tr</a></li><li><a class="hover:text-slate-900" href="{HARITA}" target="_blank" rel="noopener">Ümit Mah. Meksika Cad. No:56/21<br>Çayyolu, Ankara</a></li><li><a class="inline-flex items-center gap-1.5 font-semibold text-slate-900 hover:underline" href="{HARITA}" target="_blank" rel="noopener">Haritada aç <span aria-hidden="true">↗</span></a></li><li><a class="inline-flex items-center gap-1.5 font-semibold text-slate-900 hover:underline" href="{YORUM}" target="_blank" rel="noopener">Google’da bizi değerlendirin <span aria-hidden="true">★</span></a></li></ul>
      </div>
    </div>
    <div class="mt-12 pt-6 border-t border-slate-100 text-xs text-slate-500">© 2013–{datetime.date.today().year} Clickbait Medya Limited Şirketi, Ankara. Tüm hakları saklıdır.</div>
  </div>
</footer>
<!-- ▲▲▲▲▲ BÖLÜM: ALT BİLGİ — BİTİŞ ▲▲▲▲▲ -->'''

def menu():
    linkler = [('/#hizmetler', 'Hizmetler'), ('/#projeler', 'Projeler'), ('/#hakkimizda', 'Hakkımızda'), ('/#blog', 'Blog'), ('/#iletisim', 'İletişim')]
    ust = ''.join(f'\n        <a class="hover:text-white transition-colors" href="{u}">{a.upper().replace("i","İ") if False else a.replace("i","İ").upper()}</a>' for u, a in linkler)
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

def bas(baslik, aciklama, adres, ekler=''):
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
<meta property="og:site_name" content="Clickbait">
<meta property="og:url" content="{ALAN}{adres}">
<meta property="og:title" content="{e(baslik)}">
<meta property="og:description" content="{e(aciklama)}">
<meta property="og:image" content="{ALAN}/assets/img/og-clickbait.jpg">
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
    m = re.search(r'<ul class="mt-7 grid grid-cols-3.*?</ul>', s, re.S)
    return m.group(0).replace('src="assets/', 'src="/assets/') if m else ''

def hizmet_sayfasi(h):
    adres = f'/{h["adres"]}/'
    on, yazi, alt, rozet = KART_RENK[h['renk']]
    kartlar = ''.join(f'''
      <li class="bento-card-interactive bg-white rounded-[28px] p-6 md:p-7 border border-slate-100 shadow-sm">
        <span class="w-9 h-9 rounded-full bg-[#D8F83C] text-black text-xs font-bold flex items-center justify-center" aria-hidden="true">{i:02d}</span>
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
       "areaServed": [{"@type": "City", "name": "Ankara"}, {"@type": "Country", "name": "Türkiye"}]},
      {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Ana sayfa", "item": ALAN + "/"},
        {"@type": "ListItem", "position": 2, "name": "Hizmetler", "item": ALAN + "/#hizmetler"},
        {"@type": "ListItem", "position": 3, "name": h['kisa'], "item": ALAN + adres}]},
      {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": s, "acceptedAnswer": {"@type": "Answer", "text": c}} for s, c in h['sss']]}]}
    ld_html = '<script type="application/ld+json">\n' + json.dumps(ld, ensure_ascii=False, indent=1) + '\n</script>\n'

    return bas(h['title'], h['description'], adres, ld_html) + f'''<div class="font-sans antialiased text-slate-800 bg-white selection:bg-brand-lime selection:text-black" id="top">
<a href="#icerik" class="sr-only focus:not-sr-only focus:fixed focus:top-3 focus:left-3 focus:z-50 focus:bg-white focus:px-4 focus:py-2 focus:rounded-full focus:font-bold">İçeriğe geç</a>

<!-- ▼▼▼▼▼ BÖLÜM: SAYFA BAŞI — BAŞLANGIÇ ▼▼▼▼▼ -->
<section class="on-blue relative pt-5 pb-16 md:pb-24 overflow-hidden rounded-b-[40px] md:rounded-b-[56px]" style="background:linear-gradient(160deg,#0866c9 0%,#1283e8 55%,#48a6fb 100%)" aria-labelledby="h1">
{menu()}
  <div class="relative z-20 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pt-12 md:pt-20">
    <nav aria-label="Konum" class="text-xs font-semibold text-white/85"><ol class="flex flex-wrap items-center gap-2"><li><a href="/" class="hover:text-white">Ana sayfa</a></li><li aria-hidden="true">/</li><li><a href="/#hizmetler" class="hover:text-white">Hizmetler</a></li><li aria-hidden="true">/</li><li aria-current="page" class="text-white">{e(h['kisa'])}</li></ol></nav>
    <h1 id="h1" class="mt-6 max-w-4xl text-4xl sm:text-5xl md:text-6xl font-bold text-white tracking-tight leading-[1.08]" style="text-wrap:balance">{e(h['h1'])}</h1>
    <p class="mt-6 max-w-2xl text-base md:text-lg text-white leading-relaxed">{e(h['giris'])}</p>
    <div class="mt-8 flex flex-wrap items-center gap-3.5">
      <a class="inline-flex items-center justify-center gap-2 px-6 py-3 rounded-full text-xs font-bold tracking-wider text-black bg-[#D8F83C] hover:bg-[#c7e92e] transition-all shadow-lg hover:scale-105" href="/#iletisim"><span>ÜCRETSİZ ÖN GÖRÜŞME</span><span class="w-5 h-5 rounded-full bg-black text-[#D8F83C] flex items-center justify-center text-xs" aria-hidden="true">↗</span></a>
      <a class="inline-flex items-center justify-center px-6 py-3 rounded-full text-xs font-bold tracking-wider text-white bg-black/25 hover:bg-black/35 border border-white/20 transition-all" href="{WHATSAPP}" target="_blank" rel="noopener">WHATSAPP’TAN YAZIN</a>
    </div>
  </div>
</section>
<!-- ▲▲▲▲▲ BÖLÜM: SAYFA BAŞI — BİTİŞ ▲▲▲▲▲ -->

<main id="icerik">
<!-- ▼▼▼▼▼ BÖLÜM: NELER YAPIYORUZ — BAŞLANGIÇ ▼▼▼▼▼ -->
<section class="py-20 md:py-28 bg-white" aria-labelledby="neler">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="max-w-2xl">
      <p class="inline-flex items-center gap-1.5 text-xs font-bold tracking-widest text-slate-500"><span class="w-1.5 h-1.5 rounded-full bg-slate-900"></span>KAPSAM</p>
      <h2 id="neler" class="mt-4 text-3xl sm:text-4xl md:text-5xl font-extrabold text-slate-900 tracking-tight leading-tight">{e(h['kisa'])} hizmetimizde neler var?</h2>
    </div>
    <ul class="mt-12 grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">{kartlar}
    </ul>
  </div>
</section>
<!-- ▲▲▲▲▲ BÖLÜM: NELER YAPIYORUZ — BİTİŞ ▲▲▲▲▲ -->

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

<!-- ▼▼▼▼▼ BÖLÜM: GÖRÜŞME ÇAĞRISI — BAŞLANGIÇ ▼▼▼▼▼ -->
<section class="pb-20 md:pb-28 bg-white" aria-labelledby="cagri">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="on-blue rounded-[40px] md:rounded-[56px] p-8 sm:p-12 md:p-16 text-white text-center" style="background:linear-gradient(160deg,#0866c9 0%,#1283e8 45%,#48a6fb 100%)">
      <h2 id="cagri" class="text-3xl md:text-5xl font-extrabold tracking-tight" style="text-wrap:balance">{e(h['kisa'])} için görüşelim</h2>
      <p class="mt-4 max-w-xl mx-auto text-white leading-relaxed">İhtiyacınızı dinleyelim, size uygun bir yol haritası çıkaralım. İlk görüşme ücretsiz.</p>
      <div class="mt-8 flex flex-wrap justify-center gap-3.5">
        <a class="inline-flex items-center gap-2 px-6 py-3 rounded-full text-xs font-bold tracking-wider text-black bg-[#D8F83C] hover:bg-[#c7e92e] transition-all shadow-lg hover:scale-105" href="/#iletisim"><span>GERİ ARAMA İSTE</span><span class="w-5 h-5 rounded-full bg-black text-[#D8F83C] flex items-center justify-center" aria-hidden="true">↗</span></a>
        <a class="inline-flex items-center px-6 py-3 rounded-full text-xs font-bold tracking-wider text-white bg-black/25 hover:bg-black/35 border border-white/20 transition-all" href="{TEL_LINK}">{TEL_GORUNEN}</a>
      </div>
    </div>
    <div class="mt-12">
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
    urller = [('/', 'weekly', '1.0')] + [(f'/{h["adres"]}/', 'monthly', '0.9') for h in HIZMETLER] + [('/kvkk/', 'yearly', '0.2')]
    satir = ''.join(f'  <url><loc>{ALAN}{u}</loc><lastmod>{BUGUN}</lastmod><changefreq>{c}</changefreq><priority>{p}</priority></url>\n' for u, c, p in urller)
    open(os.path.join(KOK, 'sitemap.xml'), 'w', encoding='utf-8').write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + satir + '</urlset>\n')

if __name__ == '__main__':
    for h in HIZMETLER:
        os.makedirs(os.path.join(KOK, h['adres']), exist_ok=True)
        open(os.path.join(KOK, h['adres'], 'index.html'), 'w', encoding='utf-8').write(hizmet_sayfasi(h))
        print('yazıldı:', h['adres'])
    for d in ['index.html', 'kvkk/index.html']:
        blok_degistir(d, 'ALT BİLGİ', alt_bilgi())
    site_haritasi()
    print('alt bilgi ve site haritası güncellendi')
