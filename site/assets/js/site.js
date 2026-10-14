/* Clickbait Digital — site davranışları */
(function () {
  /* ---- Mobil menü ---- */
  var btn = document.getElementById('menuBtn'), menu = document.getElementById('mobileMenu');
  function setMenu(open) { menu.hidden = !open; btn.setAttribute('aria-expanded', open); btn.textContent = open ? 'KAPAT' : 'MENÜ'; }
  btn.addEventListener('click', function () { setMenu(menu.hidden); });
  menu.querySelectorAll('a').forEach(function (a) { a.addEventListener('click', function () { setMenu(false); }); });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && !menu.hidden) { setMenu(false); btn.focus(); } });

  /* ---- Açılıştaki kart kavisini mobilde ortadan başlat ---- */
  var arc = document.getElementById('arc');
  function center() { arc.scrollLeft = (arc.scrollWidth - arc.clientWidth) / 2; }
  center(); window.addEventListener('load', center);

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
  var form = document.getElementById('form'), result = document.getElementById('result'), success = document.getElementById('success');
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
    if (ok) { form.reset(); success.hidden = false; success.focus(); }
    else { msg.textContent = buildText(); result.hidden = false; result.focus(); }
  });
  document.getElementById('copyMsg').addEventListener('click', async function (e) { var ok = await copy(msg.textContent, msg); e.target.textContent = ok ? 'KOPYALANDI' : 'METİN SEÇİLDİ, CTRL+C'; });
  document.getElementById('editForm').addEventListener('click', function () { result.hidden = true; form.hidden = false; document.getElementById('f-name').focus(); });
})();
