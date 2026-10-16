/* Clickbait Digital — site davranışları */
/* ---- Google Analytics + çerez onayı (KVKK) ----
   Ölçüm kimliği girilene kadar hiçbir şey yüklenmez ve bant görünmez.
   Analytics yalnızca ziyaretçi "Kabul et" derse yüklenir. */
var GA_ID = 'G-3GSS5F5FTT';   // Google Analytics ölçüm kimliği
(function () {
  if (!GA_ID) return;
  var ANAHTAR = 'cb_cerez_onayi';
  function oku() { try { return localStorage.getItem(ANAHTAR); } catch (e) { return null; } }
  function yaz(v) { try { localStorage.setItem(ANAHTAR, v); } catch (e) {} }
  function yukle() {
    if (window.gtag) return;
    window.dataLayer = window.dataLayer || [];
    window.gtag = function () { dataLayer.push(arguments); };
    gtag('js', new Date());
    gtag('config', GA_ID, { anonymize_ip: true });
    var s = document.createElement('script'); s.async = true;
    s.src = 'https://www.googletagmanager.com/gtag/js?id=' + GA_ID;
    document.head.appendChild(s);
  }
  function sil() {   // onay geri çekilirse Analytics çerezlerini kaldır
    document.cookie.split(';').forEach(function (c) {
      var ad = c.split('=')[0].trim();
      if (ad.indexOf('_ga') === 0) {
        var alanlar = [location.hostname, '.' + location.hostname.replace(/^www\./, '')];
        alanlar.forEach(function (al) { document.cookie = ad + '=; expires=Thu, 01 Jan 1970 00:00:00 GMT; path=/; domain=' + al; });
        document.cookie = ad + '=; expires=Thu, 01 Jan 1970 00:00:00 GMT; path=/';
      }
    });
    if (window.gtag) window['ga-disable-' + GA_ID] = true;
  }
  function bant() {
    if (document.getElementById('cerezBandi')) return;
    var d = document.createElement('div');
    d.id = 'cerezBandi';
    d.setAttribute('role', 'dialog'); d.setAttribute('aria-live', 'polite'); d.setAttribute('aria-label', 'Çerez tercihleri');
    d.className = 'fixed z-50 left-4 right-4 bottom-24 md:left-auto md:right-6 md:bottom-6 md:max-w-md bg-white text-slate-800 rounded-[24px] shadow-2xl border border-slate-100 p-5';
    d.style.marginBottom = 'env(safe-area-inset-bottom, 0px)';
    d.innerHTML = '<p class="text-sm font-bold text-slate-900">Çerez tercihiniz</p>' +
      '<p class="mt-2 text-xs leading-relaxed text-slate-600">Sitemizin nasıl kullanıldığını anlamak için, onay verirseniz Google Analytics çerezlerini kullanırız. Zorunlu olmayan hiçbir çerez onayınız olmadan çalışmaz. Ayrıntılar için <a href="/kvkk/" class="font-semibold text-slate-900 underline">KVKK Aydınlatma Metni</a>.</p>' +
      '<div class="mt-4 flex flex-wrap gap-2"><button type="button" data-c="1" class="px-5 py-2.5 rounded-full text-xs font-bold tracking-wider text-black bg-[#D8F83C] hover:bg-[#c7e92e]">KABUL ET</button>' +
      '<button type="button" data-c="0" class="px-5 py-2.5 rounded-full text-xs font-bold tracking-wider border border-slate-300 hover:border-slate-900">REDDET</button></div>';
    d.addEventListener('click', function (e) {
      var b = e.target.closest('button[data-c]'); if (!b) return;
      var onay = b.getAttribute('data-c') === '1';
      yaz(onay ? 'evet' : 'hayir'); d.remove();
      if (onay) yukle(); else sil();
    });
    document.body.appendChild(d);
  }
  var karar = oku();
  if (karar === 'evet') yukle(); else if (karar !== 'hayir') bant();
  // Alt bilgiye "Çerez tercihleri" bağlantısı
  var kurumsal = document.querySelector('nav[aria-label="Kurumsal"] ul');
  if (kurumsal) {
    var li = document.createElement('li'), a = document.createElement('a');
    a.href = '#'; a.className = 'hover:text-slate-900'; a.textContent = 'Çerez tercihleri';
    a.addEventListener('click', function (e) { e.preventDefault(); bant(); });
    li.appendChild(a); kurumsal.appendChild(li);
  }
})();

(function () {
  /* ---- Mobil menü ---- */
  var btn = document.getElementById('menuBtn'), menu = document.getElementById('mobileMenu');
  if (btn && menu) {
  function setMenu(open) { menu.hidden = !open; btn.setAttribute('aria-expanded', open); btn.textContent = open ? 'KAPAT' : 'MENÜ'; }
  btn.addEventListener('click', function () { setMenu(menu.hidden); });
  menu.querySelectorAll('a').forEach(function (a) { a.addEventListener('click', function () { setMenu(false); }); });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && !menu.hidden) { setMenu(false); btn.focus(); } });
  }

  /* ---- Telefon / WhatsApp tıklamalarını Analytics'e bildir (yalnızca onay verildiyse yüklü) ---- */
  document.addEventListener('click', function (e) {
    var a = e.target.closest('a[href^="tel:"], a[href*="wa.me/"]');
    if (a && window.gtag) gtag('event', 'iletisim_tiklama', { yontem: a.href.indexOf('tel:') === 0 ? 'telefon' : 'whatsapp' });
  });

  /* ---- Açılıştaki kart kavisini mobilde ortadan başlat ---- */
  var arc = document.getElementById('arc');
  if (arc) {
    var center = function () { arc.scrollLeft = (arc.scrollWidth - arc.clientWidth) / 2; };
    center(); window.addEventListener('load', center);
  }

  /* ---- Kopyala düğmeleri ---- */
  async function copy(text, el) {
    try { await navigator.clipboard.writeText(text); return true; }
    catch (e) { if (el) { var r = document.createRange(); r.selectNodeContents(el); var s = getSelection(); s.removeAllRanges(); s.addRange(r); } return false; }
  }
  document.querySelectorAll('.copy').forEach(function (b) {
    b.addEventListener('click', async function () {
      var ok = await copy(b.dataset.copy, document.getElementById(b.dataset.target));
      b.textContent = ok ? 'KOPYALANDI' : 'SEÇİLDİ, CTRL+C'; setTimeout(function () { b.textContent = 'KOPYALA'; }, 2400);
    });
  });

  /* ---- İletişim formu: contact.php'ye gönderir ---- */
  var form = document.getElementById('form');
  if (!form) return;
  var result = document.getElementById('result'), success = document.getElementById('success');
  var msg = document.getElementById('msg'), submitBtn = document.getElementById('submitBtn'), submitLabel = document.getElementById('submitLabel');
  function val(id) { return document.getElementById(id).value.trim(); }
  function showErr(id, t) {
    var e = document.getElementById('e-' + id), i = document.getElementById('f-' + id);
    e.textContent = t; e.classList.toggle('hidden', !t); i.setAttribute('aria-invalid', !!t);
    if (t) i.setAttribute('aria-describedby', 'e-' + id); else i.removeAttribute('aria-describedby');
  }
  function buildText() {
    var c = val('f-company'), note = val('f-note');
    var svcs = Array.from(form.querySelectorAll('input[type=checkbox]:checked')).map(function (x) { return x.value; }).join(', ');
    return 'Merhaba Clickbait,\n\nAd: ' + val('f-name') + (c ? '\nMarka: ' + c : '') + '\nUlaşım: ' + val('f-reach') + (svcs ? '\nİlgilendiğim hizmetler: ' + svcs : '') + (note ? '\n\nNot: ' + note : '') + '\n\nBeni geri arayabilir misiniz?';
  }
  form.addEventListener('submit', async function (e) {
    e.preventDefault();
    var n = val('f-name'), r = val('f-reach');
    showErr('name', n ? '' : 'Adınızı yazın.');
    showErr('reach', r ? '' : 'Size ulaşabileceğimiz bir telefon veya e-posta yazın.');
    if (!n || !r) { document.getElementById(!n ? 'f-name' : 'f-reach').focus(); return; }
    submitBtn.disabled = true; submitLabel.textContent = 'GÖNDERİLİYOR…';
    var ok = false, kod = '';
    try {
      var res = await fetch(form.action, { method: 'POST', body: new FormData(form), headers: { 'Accept': 'application/json' } });
      kod = 'HTTP ' + res.status;
      var data = await res.json();
      ok = res.ok && data && data.ok === true;
      if (data && data.hata) kod = data.hata;
    } catch (err) { if (!kod) kod = 'baglanti'; }
    document.getElementById('errCode').textContent = ok ? '' : 'Hata kodu: ' + kod;
    submitBtn.disabled = false; submitLabel.textContent = 'GERİ ARAMA İSTE';
    form.hidden = true;
    if (ok) { form.reset(); success.hidden = false; success.focus(); if (window.gtag) gtag('event', 'generate_lead', { form: 'geri_arama' }); }
    else { msg.textContent = buildText(); result.hidden = false; result.focus(); }
  });
  document.getElementById('copyMsg').addEventListener('click', async function (e) { var ok = await copy(msg.textContent, msg); e.target.textContent = ok ? 'KOPYALANDI' : 'METİN SEÇİLDİ, CTRL+C'; });
  document.getElementById('editForm').addEventListener('click', function () { result.hidden = true; form.hidden = false; document.getElementById('f-name').focus(); });
})();

/* ---- Ortak form gönderimi: data-form="..." olan formlar (hizmet sayfası formu, ücretsiz analiz) ---- */
(function () {
  var WA = 'https://wa.me/905079238575?text=';
  function bagla(form) {
    if (form.dataset.bagli) return; form.dataset.bagli = '1';
    var sonuc = form.querySelector('[data-sonuc]'), btn = form.querySelector('button[type=submit]'), etiket = form.querySelector('[data-etiket]');
    var ilkEtiket = etiket ? etiket.textContent : '';
    function hata(alan, metin) {
      var p = alan.parentNode.querySelector('.form-hata');
      if (p) { p.textContent = metin; p.classList.toggle('hidden', !metin); }
      alan.setAttribute('aria-invalid', metin ? 'true' : 'false');
    }
    form.addEventListener('submit', async function (e) {
      e.preventDefault();
      var ilkHatali = null;
      form.querySelectorAll('[data-zorunlu]').forEach(function (alan) {
        var bos = !alan.value.trim(); hata(alan, bos ? alan.dataset.zorunlu : '');
        if (bos && !ilkHatali) ilkHatali = alan;
      });
      if (ilkHatali) { ilkHatali.focus(); return; }
      btn.disabled = true; if (etiket) etiket.textContent = 'GÖNDERİLİYOR…';
      var ok = false, kod = '';
      try {
        var res = await fetch(form.action, { method: 'POST', body: new FormData(form), headers: { 'Accept': 'application/json' } });
        kod = 'HTTP ' + res.status;
        var data = await res.json();
        ok = res.ok && data && data.ok === true;
        if (data && data.hata) kod = data.hata;
      } catch (err) { if (!kod) kod = 'baglanti'; }
      btn.disabled = false; if (etiket) etiket.textContent = ilkEtiket;
      sonuc.hidden = false;
      if (ok) {
        [].forEach.call(form.children, function (c) { if (c !== sonuc && c.type !== 'hidden') c.hidden = true; });
        sonuc.innerHTML = '<span class="w-10 h-10 rounded-full bg-[#D8F83C] flex items-center justify-center text-lg font-bold" aria-hidden="true">✓</span>' +
          '<p class="mt-3 text-xl font-extrabold tracking-tight text-slate-900">' + (form.dataset.form === 'analiz' ? 'Analiz talebiniz bize ulaştı' : 'Talebiniz bize ulaştı') + '</p>' +
          '<p class="mt-1 text-slate-600">' + (form.dataset.form === 'analiz' ? 'Sitenizi inceleyip sonucu size ileteceğiz.' : 'Çalışma saatlerinde sizi arayacağız.') + ' Acil durumlarda 0507 923 85 75 numarasından bize ulaşabilirsiniz.</p>';
        sonuc.focus();
        if (window.gtag) gtag('event', 'generate_lead', { form: form.dataset.form });
        form.dispatchEvent(new CustomEvent('gonderildi'));
      } else {
        var metin = 'Merhaba Clickbait, ' + (form.dataset.form === 'analiz' ? 'sitemin ücretsiz analizini istiyorum.' : 'geri arama istiyorum.');
        form.querySelectorAll('input[name=site_adresi], input[name=name], input[name=reach]').forEach(function (a) { if (a.value.trim()) metin += '\n' + a.value.trim(); });
        sonuc.innerHTML = '<p class="font-semibold text-slate-900">Mesajınız şu anda gönderilemedi.</p><p class="mt-1 text-slate-600">Bilgilerinizi WhatsApp’tan gönderebilir ya da 0507 923 85 75 numarasını arayabilirsiniz.</p>' +
          '<a href="' + WA + encodeURIComponent(metin) + '" target="_blank" rel="noopener" class="mt-3 inline-flex items-center px-5 py-2.5 rounded-full text-xs font-bold tracking-wider bg-[#111315] text-white">WHATSAPP’TAN GÖNDER</a>' +
          '<p class="mt-3 text-[11px] text-slate-400">Hata kodu: ' + kod + '</p>';
      }
    });
  }
  window.cbFormBagla = bagla;
  document.querySelectorAll('form[data-form]').forEach(bagla);
})();

/* ---- Ücretsiz site analizi penceresi ----
   Kendiliğinden açılma: bilgisayarda 35 sn sonra ya da fare sayfadan çıkarken; telefonda sayfanın %60'ı okunduktan sonra.
   Kapatılırsa 7 gün, form gönderildiyse bir daha kendiliğinden açılmaz. Çerez bandı açıkken açılmaz.
   Elle açmak için: data-analiz özniteliği olan bağlantı/düğme ya da adresin sonuna #analiz. */
(function () {
  var ANAHTAR = 'cb_analiz', GUN = 864e5;
  function oku() { try { return JSON.parse(localStorage.getItem(ANAHTAR)) || {}; } catch (e) { return {}; } }
  function yaz(v) { try { localStorage.setItem(ANAHTAR, JSON.stringify(v)); } catch (e) {} }
  var durum = oku(), pencere = null, onceki = null, acildi = false;
  var tik = '<svg class="w-4 h-4 shrink-0 mt-0.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12l5 5L20 7"/></svg>';
  var girdi = 'rounded-full bg-slate-50 border border-slate-200 px-5 py-3 text-sm focus:outline-none focus:ring-2 focus:ring-sky-500';
  function olustur() {
    var d = document.createElement('div');
    d.id = 'analizPenceresi'; d.hidden = true;
    d.className = 'fixed inset-0 z-[60] flex items-end sm:items-center justify-center sm:p-6';
    d.setAttribute('role', 'dialog'); d.setAttribute('aria-modal', 'true'); d.setAttribute('aria-labelledby', 'analizBaslik');
    d.innerHTML =
      '<div data-kapat class="absolute inset-0 bg-slate-950/50 backdrop-blur-sm"></div>' +
      '<div class="relative w-full sm:max-w-[880px] max-h-[92vh] overflow-y-auto bg-white rounded-t-[32px] sm:rounded-[36px] shadow-2xl grid md:grid-cols-2">' +
        '<button type="button" data-kapat aria-label="Kapat" class="absolute top-4 right-4 z-10 w-9 h-9 rounded-full bg-white/90 md:bg-slate-100 text-slate-900 text-xl leading-none flex items-center justify-center hover:bg-slate-200">×</button>' +
        '<div class="on-blue text-white p-6 sm:p-8 md:p-10 rounded-t-[32px] sm:rounded-t-[36px] md:rounded-tr-none md:rounded-l-[36px]" style="background:linear-gradient(160deg,#0866c9 0%,#1283e8 55%,#48a6fb 100%)">' +
          '<span class="inline-block rounded-full bg-[#D8F83C] text-black text-[10px] font-bold tracking-wider px-2.5 py-1">ÜCRETSİZ</span>' +
          '<h2 id="analizBaslik" class="mt-4 text-2xl sm:text-3xl md:text-4xl font-extrabold tracking-tight leading-[1.1]" style="text-wrap:balance">Web sitenizi ücretsiz analiz edelim</h2>' +
          '<p class="mt-3 text-sm sm:text-base text-white/90 leading-relaxed">Sitenizin adresini bırakın; neyin iyi gittiğini ve neyin müşteri kaybettirdiğini sade bir dille anlatalım.</p>' +
          '<ul class="mt-5 hidden sm:grid gap-2.5 text-sm font-semibold">' +
            '<li class="flex gap-2.5">' + tik + 'Hız ve mobil uyum</li>' +
            '<li class="flex gap-2.5">' + tik + 'Google’da görünürlük (SEO)</li>' +
            '<li class="flex gap-2.5">' + tik + 'Ziyaretçiyi müşteriye çevirme</li>' +
          '</ul>' +
          '<p class="mt-5 hidden sm:block text-xs text-white/80">Hiçbir yükümlülüğü yok.</p>' +
        '</div>' +
        '<form data-form="analiz" action="/contact.php" method="post" novalidate class="relative p-6 sm:p-8 md:p-10 grid gap-4 content-center text-slate-900">' +
          '<input type="hidden" name="tur" value="analiz"><input type="hidden" name="kaynak" value="' + location.pathname + '">' +
          '<div class="grid gap-1.5"><label for="a-site" class="text-xs font-bold text-slate-700">Web sitenizin adresi</label><input id="a-site" name="site_adresi" inputmode="url" autocomplete="url" maxlength="200" data-zorunlu="Sitenizin adresini yazın." class="' + girdi + '" placeholder="ornekfirma.com"><p class="form-hata hidden text-xs font-semibold text-red-600"></p></div>' +
          '<div class="grid gap-1.5"><label for="a-name" class="text-xs font-bold text-slate-700">Adınız</label><input id="a-name" name="name" autocomplete="name" maxlength="100" data-zorunlu="Adınızı yazın." class="' + girdi + '" placeholder="Ad Soyad"><p class="form-hata hidden text-xs font-semibold text-red-600"></p></div>' +
          '<div class="grid gap-1.5"><label for="a-reach" class="text-xs font-bold text-slate-700">Telefon veya e-posta</label><input id="a-reach" name="reach" autocomplete="email" maxlength="150" data-zorunlu="Sonucu nereye gönderelim? Telefon veya e-posta yazın." class="' + girdi + '" placeholder="05xx xxx xx xx ya da ad@firma.com"><p class="form-hata hidden text-xs font-semibold text-red-600"></p></div>' +
          '<div class="absolute -left-[9999px]" aria-hidden="true"><label for="a-website">Bu alanı boş bırakın</label><input id="a-website" name="website" tabindex="-1" autocomplete="off"></div>' +
          '<button type="submit" class="justify-self-start inline-flex items-center gap-2 px-6 py-3 rounded-full text-xs font-bold tracking-wider text-black bg-[#D8F83C] hover:bg-[#c7e92e] transition-all shadow-lg hover:scale-105"><span data-etiket>ÜCRETSİZ ANALİZ İSTE</span><span class="w-5 h-5 rounded-full bg-black text-[#D8F83C] flex items-center justify-center" aria-hidden="true">↗</span></button>' +
          '<p class="text-[11px] text-slate-500 leading-relaxed">Paylaştığınız bilgiler talebinizi değerlendirmek ve sizinle iletişime geçmek için Clickbait Medya Limited Şirketi tarafından işlenir. Ayrıntılar: <a href="/kvkk/" class="font-semibold text-slate-700 underline decoration-slate-300 underline-offset-2">KVKK Aydınlatma Metni</a>.</p>' +
          '<div data-sonuc hidden tabindex="-1" role="status" class="rounded-[20px] bg-slate-50 p-5 text-sm leading-relaxed"></div>' +
        '</form>' +
      '</div>';
    document.body.appendChild(d);
    d.addEventListener('click', function (e) { if (e.target.closest('[data-kapat]')) kapat(); });
    d.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') { kapat(); return; }
      if (e.key !== 'Tab') return;
      var odak = [].filter.call(d.querySelectorAll('button, a[href], input:not([type=hidden]):not([tabindex="-1"]), textarea'), function (x) { return x.offsetParent !== null; });
      var ilk = odak[0], son = odak[odak.length - 1];
      if (e.shiftKey && document.activeElement === ilk) { e.preventDefault(); son.focus(); }
      else if (!e.shiftKey && document.activeElement === son) { e.preventDefault(); ilk.focus(); }
    });
    var form = d.querySelector('form');
    if (window.cbFormBagla) window.cbFormBagla(form);
    form.addEventListener('gonderildi', function () { durum.gonderildi = Date.now(); yaz(durum); });
    return d;
  }
  function ac(kendiliginden) {
    if (kendiliginden && (acildi || !otomatikUygun())) return;
    acildi = true;
    pencere = pencere || olustur();
    onceki = document.activeElement;
    pencere.hidden = false; document.documentElement.style.overflow = 'hidden';
    setTimeout(function () { pencere.querySelector('#a-site').focus(); }, 30);
    if (window.gtag) gtag('event', 'analiz_penceresi', { acilis: kendiliginden ? 'otomatik' : 'tiklama' });
  }
  function kapat() {
    if (!pencere || pencere.hidden) return;
    pencere.hidden = true; document.documentElement.style.overflow = '';
    if (!durum.gonderildi) { durum.kapatildi = Date.now(); yaz(durum); }
    if (location.hash === '#analiz') history.replaceState(null, '', location.pathname + location.search);
    if (onceki && onceki.focus) onceki.focus();
  }
  function otomatikUygun() {
    if (durum.gonderildi) return false;
    if (durum.kapatildi && Date.now() - durum.kapatildi < 7 * GUN) return false;
    if (document.getElementById('cerezBandi')) return false;                       // önce çerez kararı
    var m = document.getElementById('mobileMenu'); if (m && !m.hidden) return false;
    var a = document.activeElement; if (a && /INPUT|TEXTAREA|SELECT/.test(a.tagName)) return false;   // ziyaretçi bir şey yazıyor
    return !/^\/kvkk\//.test(location.pathname);
  }
  // Elle açma
  document.addEventListener('click', function (e) {
    var t = e.target.closest('[data-analiz], a[href="#analiz"]');
    if (t) { e.preventDefault(); ac(false); }
  });
  if (location.hash === '#analiz') ac(false);
  // Kendiliğinden açma
  var baslangic = Date.now();
  if (window.matchMedia('(min-width: 768px)').matches) {
    setTimeout(function () { ac(true); }, 35000);
    document.addEventListener('mouseout', function (e) {
      if (!e.relatedTarget && e.clientY <= 0 && Date.now() - baslangic > 8000) ac(true);
    });
  } else {
    window.addEventListener('scroll', function () {
      var h = document.documentElement;
      if ((h.scrollTop + innerHeight) / h.scrollHeight >= 0.6 && Date.now() - baslangic > 15000) ac(true);
    }, { passive: true });
  }
})();
