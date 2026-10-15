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
