"""Hizmet sayfalarının açılış bölümündeki çizimler.

Her hizmete (ve Ankara sayfasına) özel, HTML + Tailwind ile çizilmiş arayüz görselleri.
Görsel dosya yok; hepsi sayfanın içinde, ekran okuyuculardan gizli (aria-hidden).
Kural: çizimlerde rakam/sonuç uydurma; yalnızca hizmetin ne yaptığını gösteren örnek ekranlar.
"""

# ---------------------------------------------------------------- Simgeler (çizgi simgeler, currentColor)
def _svg(yol, boyut='w-4 h-4'):
    return f'<svg class="{boyut} shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">{yol}</svg>'

ONAY = '<path d="M5 12.5l4.5 4.5L19 7"/>'
SIMSEK = '<path d="M13 3L5 13.5h6L10 21l9-11h-6l1-7z"/>'
KALP = '<path d="M12 20s-7-4.4-7-10a4 4 0 017-2.6A4 4 0 0119 10c0 5.6-7 10-7 10z"/>'
YORUM = '<path d="M5 18l1.2-3.6A7 7 0 1110 18.3L5 18z"/>'
ARA = '<circle cx="11" cy="11" r="6.5"/><path d="M20 20l-4.2-4.2"/>'
PARILTI = '<path d="M12 3l1.8 5.2L19 10l-5.2 1.8L12 17l-1.8-5.2L5 10l5.2-1.8z"/><path d="M19 16l.7 1.8 1.8.7-1.8.7L19 21l-.7-1.8-1.8-.7 1.8-.7z"/>'
GONDER = '<path d="M5 12h13M13 6l6 6-6 6"/>'
SAAT = '<circle cx="12" cy="12" r="8"/><path d="M12 8v4l2.5 2"/>'
KONUM = '<path d="M12 21s6.5-6 6.5-11.5a6.5 6.5 0 00-13 0C5.5 15 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.3"/>'
TELEFON = '<path d="M6.5 4h3l1.5 4-2 1.2a10 10 0 005 5l1.2-2 4 1.5v3A2 2 0 0117 19 13 13 0 015 7a2 2 0 011.5-3z"/>'
SEPET = '<path d="M4 5h2l2 10h9l2-7H7.2"/><circle cx="9.5" cy="19" r="1.3"/><circle cx="16.5" cy="19" r="1.3"/>'
KILIT = '<rect x="5.5" y="10.5" width="13" height="9" rx="2"/><path d="M8.5 10.5V8a3.5 3.5 0 017 0v2.5"/>'
GRAFIK = '<path d="M4 18l5-6 4 3 7-8"/><path d="M15 7h5v5"/>'
TAKVIM = '<rect x="4" y="5.5" width="16" height="14" rx="2.5"/><path d="M4 10h16M9 3.5v4M15 3.5v4"/>'
HEDEF = '<circle cx="12" cy="12" r="8"/><circle cx="12" cy="12" r="4"/><circle cx="12" cy="12" r=".8" fill="currentColor"/>'
MESAJ = '<path d="M4 6.5A2.5 2.5 0 016.5 4h11A2.5 2.5 0 0120 6.5v7a2.5 2.5 0 01-2.5 2.5H10l-4.5 4v-4h0A2.5 2.5 0 014 13.5z"/>'


# ---------------------------------------------------------------- Ortak parçalar
def _rozet(ic, konum, renk='bg-white text-slate-900', gecikme='0s'):
    """Ana kartın etrafında hafifçe yüzen küçük bilgi kartı."""
    return (f'<div class="cizim-yuz absolute {konum} z-10 inline-flex items-center gap-2 rounded-2xl {renk} px-3.5 py-2.5 '
            f'text-[11px] sm:text-xs font-bold shadow-xl shadow-sky-950/25 whitespace-nowrap" style="animation-delay:{gecikme}">{ic}</div>')

def _ikon_kutu(yol, renk='bg-[#D8F83C] text-black'):
    return f'<span class="w-7 h-7 rounded-xl {renk} flex items-center justify-center">{_svg(yol, "w-3.5 h-3.5")}</span>'

def _cubuk(gen, renk='bg-slate-200', yuk='h-2'):
    return f'<span class="block {yuk} {gen} rounded-full {renk}"></span>'

def _kart(ic, sinif=''):
    return f'<div class="relative rounded-[26px] bg-white shadow-2xl shadow-sky-950/30 {sinif}">{ic}</div>'

def _tarayici(adres, ic):
    return _kart(f'''<div class="flex items-center gap-1.5 px-4 py-3 border-b border-slate-100"><span class="w-2.5 h-2.5 rounded-full bg-[#ff5f57]"></span><span class="w-2.5 h-2.5 rounded-full bg-[#febc2e]"></span><span class="w-2.5 h-2.5 rounded-full bg-[#28c840]"></span><span class="ml-3 flex-1 flex items-center gap-1.5 rounded-full bg-slate-100 px-3 py-1 text-[10px] font-semibold text-slate-500">{_svg(KILIT, "w-3 h-3")}{adres}</span></div>{ic}''', 'overflow-hidden')

def _telefon(ic, sinif='w-[210px] sm:w-[230px]'):
    return f'<div class="relative {sinif} rounded-[34px] bg-[#111315] p-2 shadow-2xl shadow-sky-950/40"><div class="relative overflow-hidden rounded-[27px] bg-white"><span class="absolute left-1/2 top-2 z-10 -translate-x-1/2 h-4 w-16 rounded-full bg-[#111315]"></span>{ic}</div></div>'

def _sahne(ic):
    """Çizimin dış çerçevesi: sabit yükseklik, ortalanmış."""
    return f'<div class="cizim relative mx-auto w-full max-w-[440px] h-[330px] sm:h-[380px] flex items-center justify-center select-none" aria-hidden="true">{ic}</div>'


# ---------------------------------------------------------------- Hizmetlere özel çizimler
def yapay_zeka():
    sohbet = _kart(f'''
      <div class="flex items-center gap-2.5 px-5 py-4 border-b border-slate-100">{_ikon_kutu(PARILTI)}<span class="text-xs font-extrabold text-slate-900">Yapay zeka asistanı</span><span class="ml-auto inline-flex items-center gap-1.5 text-[10px] font-semibold text-emerald-600"><span class="w-1.5 h-1.5 rounded-full bg-emerald-500"></span>Hazır</span></div>
      <div class="px-5 py-4 grid gap-3">
        <p class="justify-self-end max-w-[80%] rounded-2xl rounded-br-md bg-[#111315] px-3.5 py-2.5 text-[11px] leading-relaxed text-white">Bu haftaki satış toplantısı notlarını özetle, görevleri çıkar.</p>
        <div class="max-w-[88%] rounded-2xl rounded-bl-md bg-sky-50 border border-sky-100 px-3.5 py-3 text-[11px] text-slate-700">
          <p class="font-bold text-slate-900">Özet hazır:</p>
          <ul class="mt-2 grid gap-1.5">{''.join(f'<li class="flex items-center gap-2"><span class="text-sky-600">{_svg(ONAY, "w-3.5 h-3.5")}</span>{m}</li>' for m in ('Alınan kararlar', 'Görevler ve sorumlular', 'Bir sonraki adımlar'))}</ul>
        </div>
      </div>
      <div class="mx-5 mb-5 flex items-center gap-2 rounded-full bg-slate-100 pl-4 pr-1.5 py-1.5 text-[11px] text-slate-400">Bir iş yazın…<span class="ml-auto w-7 h-7 rounded-full bg-[#D8F83C] text-black flex items-center justify-center">{_svg(GONDER, "w-3.5 h-3.5")}</span></div>''',
      'w-[300px] sm:w-[340px]')
    return _sahne(sohbet
      + _rozet(f'{_svg(ONAY)}Rapor hazır', '-top-6 right-0 sm:right-2', 'bg-[#D8F83C] text-black')
      + _rozet(f'<span class="text-[#D8F83C]">{_svg(SAAT)}</span>Her pazartesi 09:00 · otomatik', 'bottom-1 left-0', 'bg-[#111315] text-white', '-3s'))

def web_tasarim():
    sayfa = _tarayici('markaniz.com.tr', f'''
      <div class="p-4">
        <div class="flex items-center justify-between">{_cubuk("w-14", "bg-slate-900")}<span class="flex gap-2">{_cubuk("w-7")}{_cubuk("w-7")}{_cubuk("w-7")}</span></div>
        <div class="mt-4 rounded-2xl p-4 bg-gradient-to-br from-sky-500 to-sky-700">
          <span class="grid gap-2">{_cubuk("w-4/5", "bg-white", "h-3")}{_cubuk("w-3/5", "bg-white/90", "h-3")}{_cubuk("w-2/3", "bg-white/50")}</span>
          <span class="mt-4 inline-block h-6 w-24 rounded-full bg-[#D8F83C]"></span>
        </div>
        <div class="mt-3 grid grid-cols-3 gap-2">{''.join(f'<span class="rounded-xl bg-slate-50 border border-slate-100 p-2.5 grid gap-1.5"><span class="w-5 h-5 rounded-lg {r}"></span>{_cubuk("w-full")}{_cubuk("w-2/3")}</span>' for r in ("bg-[#D8F83C]", "bg-sky-200", "bg-slate-900"))}</div>
      </div>''')
    telefon = _telefon(f'''<div class="pt-8 px-2.5 pb-3"><div class="rounded-xl p-2.5 bg-gradient-to-br from-sky-500 to-sky-700 grid gap-1.5">{_cubuk("w-4/5", "bg-white", "h-2")}{_cubuk("w-1/2", "bg-white/70", "h-2")}<span class="mt-1 h-3.5 w-12 rounded-full bg-[#D8F83C]"></span></div><div class="mt-2 grid gap-1.5">{_cubuk("w-full")}{_cubuk("w-5/6")}{_cubuk("w-2/3")}</div><div class="mt-2 grid grid-cols-2 gap-1.5"><span class="h-9 rounded-lg bg-slate-100"></span><span class="h-9 rounded-lg bg-slate-100"></span></div></div>''', 'w-[104px]')
    return _sahne(f'<div class="w-[300px] sm:w-[350px]">{sayfa}</div>'
      + f'<div class="absolute -bottom-1 right-0 sm:right-1 z-10">{telefon}</div>'
      + _rozet(f'<span class="text-sky-600">{_svg(ONAY)}</span>Mobil uyumlu', 'top-0 left-0')
      + _rozet(f'{_svg(SIMSEK)}Hızlı açılış', 'bottom-0 left-0', 'bg-[#D8F83C] text-black', '-2.5s'))

def dijital_pazarlama():
    panel = _kart(f'''
      <div class="p-5">
        <div class="flex items-center justify-between"><span class="text-xs font-extrabold text-slate-900">Kampanya performansı</span><span class="rounded-full bg-slate-100 px-2.5 py-1 text-[10px] font-bold text-slate-500">Bu ay</span></div>
        <div class="mt-2 flex gap-3 text-[10px] font-semibold text-slate-500"><span class="inline-flex items-center gap-1.5"><span class="w-2 h-2 rounded-full bg-sky-500"></span>Google Ads</span><span class="inline-flex items-center gap-1.5"><span class="w-2 h-2 rounded-full bg-[#b5d61c]"></span>Meta Ads</span></div>
        <svg class="mt-3 w-full h-28" viewBox="0 0 300 110" preserveAspectRatio="none" fill="none">
          <defs><linearGradient id="cizimAlan" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#0ea5e9" stop-opacity=".28"/><stop offset="1" stop-color="#0ea5e9" stop-opacity="0"/></linearGradient></defs>
          <path d="M0 30H300M0 65H300M0 100H300" stroke="#f1f5f9" stroke-width="1"/>
          <path d="M0 92 C40 88 60 70 95 72 S150 50 185 46 S250 22 300 12 V110 H0Z" fill="url(#cizimAlan)"/>
          <path d="M0 92 C40 88 60 70 95 72 S150 50 185 46 S250 22 300 12" stroke="#0ea5e9" stroke-width="3" stroke-linecap="round"/>
          <path d="M0 100 C50 98 80 86 120 84 S200 70 240 60 S280 50 300 44" stroke="#b5d61c" stroke-width="3" stroke-linecap="round" stroke-dasharray="1 0"/>
          <circle cx="300" cy="12" r="5" fill="#0ea5e9" stroke="#fff" stroke-width="2"/>
        </svg>
        <div class="mt-3 grid grid-cols-3 gap-2">{''.join(f'<span class="rounded-xl bg-slate-50 border border-slate-100 px-2.5 py-2"><span class="block text-[10px] font-semibold text-slate-500">{a}</span><span class="mt-0.5 flex items-center gap-1 text-xs font-extrabold {r}">{_svg(GRAFIK, "w-3.5 h-3.5")}{y}</span></span>' for a, y, r in (("Tıklama", "Artıyor", "text-sky-600"), ("Talep", "Artıyor", "text-emerald-600"), ("Ölçüm", "Açık", "text-slate-900")))}</div>
      </div>''', 'w-[300px] sm:w-[350px]')
    return _sahne(panel
      + _rozet(f'{_ikon_kutu(MESAJ)}<span class="grid"><span>Yeni form talebi</span><span class="text-[10px] font-semibold text-slate-400">az önce</span></span>', '-top-2 right-0 sm:-right-2')
      + _rozet(f'<span class="text-[#D8F83C]">{_svg(HEDEF)}</span>Dönüşüm takibi kurulu', '-bottom-1 left-0', 'bg-[#111315] text-white', '-3s'))

def sosyal_medya():
    renkler = ('from-sky-400 to-sky-600', 'from-[#D8F83C] to-lime-300', 'from-slate-800 to-slate-950', 'from-rose-300 to-orange-300',
               'from-sky-200 to-sky-400', 'from-violet-400 to-fuchsia-400', 'from-amber-200 to-orange-400', 'from-emerald-300 to-teal-500', 'from-sky-600 to-indigo-600')
    profil = _telefon(f'''<div class="pt-9 px-3 pb-3">
        <div class="flex items-center gap-3"><span class="w-12 h-12 rounded-full p-[2px] bg-gradient-to-tr from-amber-400 via-rose-500 to-fuchsia-600"><span class="block w-full h-full rounded-full border-2 border-white bg-gradient-to-br from-sky-400 to-sky-700"></span></span>
        <span class="flex-1 grid grid-cols-3 text-center text-[9px] text-slate-500">{''.join(f'<span><span class="block mx-auto mb-1 h-2 w-5 rounded-full bg-slate-800"></span>{a}</span>' for a in ("gönderi", "takipçi", "takip"))}</span></div>
        <div class="mt-2.5 grid gap-1.5">{_cubuk("w-20", "bg-slate-800")}{_cubuk("w-32")}</div>
        <span class="mt-2.5 block rounded-lg bg-sky-500 py-1.5 text-center text-[10px] font-bold text-white">Takip et</span>
        <div class="mt-3 grid grid-cols-3 gap-1">{''.join(f'<span class="aspect-square rounded-[6px] bg-gradient-to-br {r}"></span>' for r in renkler)}</div>
      </div>''')
    gunler = ''.join(f'<li class="flex items-center gap-2"><span class="w-1.5 h-1.5 rounded-full {r}"></span><span class="w-7 text-slate-400">{g}</span>{t}</li>'
                     for g, t, r in (('Pzt', 'Reels', 'bg-rose-400'), ('Çar', 'Gönderi', 'bg-sky-500'), ('Cum', 'Hikâye', 'bg-[#b5d61c]')))
    takvim = (f'<div class="cizim-yuz absolute top-6 right-0 z-10 w-[150px] rounded-2xl bg-white p-3.5 shadow-xl shadow-sky-950/25" style="animation-delay:-2s">'
              f'<p class="flex items-center gap-1.5 text-[11px] font-extrabold text-slate-900"><span class="text-sky-600">{_svg(TAKVIM, "w-3.5 h-3.5")}</span>İçerik takvimi</p>'
              f'<ul class="mt-2.5 grid gap-1.5 text-[10px] font-semibold text-slate-600">{gunler}</ul></div>')
    return _sahne(f'<div class="-translate-x-8 sm:-translate-x-10">{profil}</div>' + takvim
      + _rozet(f'<span class="text-rose-500">{_svg(KALP)}</span>Yeni beğeni', 'top-[54%] left-0')
      + _rozet(f'<span class="text-[#D8F83C]">{_svg(YORUM)}</span>Yorumlara cevap verildi', 'bottom-4 right-0', 'bg-[#111315] text-white', '-4s'))

def kreatif():
    tuval = _kart(f'''
      <div class="flex items-center gap-2 px-4 py-3 border-b border-slate-100">{''.join(f'<span class="w-6 h-6 rounded-lg {r}"></span>' for r in ("bg-slate-900", "bg-slate-100", "bg-slate-100", "bg-slate-100"))}</div>
      <div class="m-4 rounded-2xl bg-[radial-gradient(#e2e8f0_1px,transparent_1px)] [background-size:14px_14px] border border-dashed border-sky-300 h-[150px] flex items-center justify-center gap-3">
        <svg class="w-14 h-14" viewBox="0 0 64 64"><rect width="64" height="64" rx="18" fill="#111315"/><path d="M42 22.5a13 13 0 100 19" stroke="#D8F83C" stroke-width="8" stroke-linecap="round" fill="none"/><circle cx="44" cy="32" r="4.5" fill="#fff"/></svg>
        <span class="grid gap-1"><span class="text-2xl font-extrabold tracking-tight text-slate-900 leading-none">markanız</span><span class="text-[9px] font-bold tracking-[.3em] text-slate-400">ANKARA</span></span>
      </div>
      <div class="px-4 pb-4 grid grid-cols-4 gap-2">{''.join(f'<span class="rounded-xl overflow-hidden border border-slate-100"><span class="block h-8 {r}"></span><span class="block px-1.5 py-1 text-[9px] font-bold text-slate-500">{k}</span></span>' for r, k in (("bg-[#D8F83C]", "#D8F83C"), ("bg-[#111315]", "#111315"), ("bg-sky-500", "#0EA5E9"), ("bg-slate-100", "#F1F5F9")))}</div>''',
      'w-[300px] sm:w-[340px]')
    yazi = ('<div class="cizim-yuz absolute -top-1 right-0 z-10 rounded-2xl bg-white px-4 py-3 shadow-xl shadow-sky-950/25" style="animation-delay:-2s">'
            '<span class="block text-3xl font-extrabold leading-none text-slate-900">Aa</span><span class="mt-1 block text-[10px] font-bold text-slate-500">Kurumsal yazı tipi</span></div>')
    return _sahne(tuval + yazi
      + _rozet(f'{_svg(ONAY)}Logo onaylandı', '-bottom-1 left-0', 'bg-[#D8F83C] text-black', '-3.5s'))

def _arama_sonucu(ust, baslik, vurgu=False, etiket=''):
    cerceve = 'border-l-4 border-[#D8F83C] bg-lime-50/60 -mx-1 pl-3 pr-2 py-2.5 rounded-r-xl' if vurgu else 'py-2.5'
    return (f'<div class="{cerceve}"><p class="flex items-center gap-1.5 text-[10px] text-slate-500">{etiket}<span class="w-4 h-4 rounded-full {"bg-sky-600" if vurgu else "bg-slate-200"}"></span>{ust}</p>'
            f'<p class="mt-1 text-[13px] font-bold {"text-sky-700" if vurgu else "text-slate-400"}">{baslik}</p><span class="mt-1.5 grid gap-1">{_cubuk("w-full", "bg-slate-200", "h-1.5")}{_cubuk("w-4/5", "bg-slate-200", "h-1.5")}</span></div>')

def _arama_kutusu(sorgu):
    return f'<div class="flex items-center gap-2 rounded-full border border-slate-200 px-4 py-2.5 text-[12px] font-semibold text-slate-800 shadow-sm"><span class="text-sky-600">{_svg(ARA)}</span>{sorgu}</div>'

def ankara_seo():
    sonuc = _kart(f'''<div class="p-5">{_arama_kutusu("ankara diş kliniği")}
      <div class="mt-3 grid divide-y divide-slate-100">{_arama_sonucu("markaniz.com.tr › ankara", "Firmanız — Ankara Çayyolu", True)}{_arama_sonucu("ornek-site.com", "Başka bir sonuç")}{_arama_sonucu("rehber-sitesi.com", "Başka bir sonuç")}</div></div>''',
      'w-[300px] sm:w-[340px]')
    return _sahne(sonuc
      + _rozet(f'<span class="text-rose-500">{_svg(KONUM)}</span>Google Haritalar’da görünür', '-top-2 right-0 sm:-right-2')
      + _rozet(f'<span class="text-[#D8F83C]">{_svg(SIMSEK)}</span>Hız · Mobil uyum · İçerik', '-bottom-1 left-0', 'bg-[#111315] text-white', '-3s'))

def ankara_google_ads():
    reklam = _kart(f'''<div class="p-5">{_arama_kutusu("ankara muhasebe bürosu")}
      <div class="mt-4 rounded-2xl border border-sky-100 bg-sky-50/60 p-3.5">
        <p class="text-[10px] text-slate-600"><b class="text-slate-900">Sponsorlu</b> · markaniz.com.tr</p>
        <p class="mt-1 text-[13px] font-bold text-sky-700">Firmanız | Ankara’da hemen teklif alın</p>
        <span class="mt-1.5 grid gap-1">{_cubuk("w-full", "bg-slate-200", "h-1.5")}{_cubuk("w-3/4", "bg-slate-200", "h-1.5")}</span>
        <div class="mt-3 flex flex-wrap gap-1.5">{''.join(f'<span class="rounded-full bg-white border border-slate-200 px-2.5 py-1 text-[10px] font-semibold text-sky-700">{a}</span>' for a in ("Hizmetler", "İletişim", "Teklif al"))}<span class="inline-flex items-center gap-1 rounded-full bg-sky-600 px-2.5 py-1 text-[10px] font-bold text-white">{_svg(TELEFON, "w-3 h-3")}Ara</span></div>
      </div>
      <div class="mt-2">{_arama_sonucu("ornek-site.com", "Başka bir sonuç")}</div></div>''', 'w-[300px] sm:w-[340px]')
    butce = ('<div class="cizim-yuz absolute -bottom-1 left-0 z-10 w-[170px] rounded-2xl bg-[#111315] text-white p-3.5 shadow-xl shadow-sky-950/30" style="animation-delay:-3s">'
             '<p class="text-[11px] font-bold">Günlük bütçe kontrolde</p><span class="mt-2 block h-1.5 rounded-full bg-white/15"><span class="block h-full w-3/5 rounded-full bg-[#D8F83C]"></span></span></div>')
    return _sahne(reklam + butce
      + _rozet(f'{_ikon_kutu(TELEFON)}<span class="grid"><span>Reklamdan arama</span><span class="text-[10px] font-semibold text-slate-400">az önce</span></span>', '-top-3 right-0 sm:-right-2'))

def ankara_reklam():
    kanallar = (('TV', 'w-[78%]', 'bg-sky-500'), ('Açık hava', 'w-[62%]', 'bg-[#b5d61c]'),
                ('Google ve Instagram', 'w-[54%]', 'bg-gradient-to-r from-amber-400 via-rose-500 to-fuchsia-600'), ('Radyo', 'w-[38%]', 'bg-slate-800'))
    plan = _kart(f'''<div class="p-5">
      <div class="flex items-center justify-between"><span class="text-xs font-extrabold text-slate-900">Kampanya planı</span><span class="rounded-full bg-[#D8F83C] px-2.5 py-1 text-[10px] font-bold text-black">Yayında</span></div>
      <ul class="mt-4 grid gap-3.5">{''.join(f'<li><span class="flex justify-between text-[11px] font-semibold text-slate-600">{a}</span><span class="mt-1.5 block h-2.5 rounded-full bg-slate-100"><span class="block h-full {g} rounded-full {r}"></span></span></li>' for a, g, r in kanallar)}</ul>
      <div class="mt-5 grid grid-cols-3 gap-2">{''.join(f'<span class="aspect-[4/5] rounded-xl bg-gradient-to-br {r}"></span>' for r in ("from-sky-400 to-sky-700", "from-[#D8F83C] to-lime-400", "from-slate-700 to-slate-950"))}</div></div>''',
      'w-[300px] sm:w-[340px]')
    return _sahne(plan
      + _rozet(f'<span class="text-sky-600">{_svg(PARILTI)}</span>Kreatifler hazır', 'bottom-16 right-0 sm:-right-2')
      + _rozet(f'<span class="text-[#D8F83C]">{_svg(GRAFIK)}</span>Aylık rapor gönderildi', '-bottom-1 left-0', 'bg-[#111315] text-white', '-3s'))

def ankara_e_ticaret():
    urun = _tarayici('magazaniz.com.tr', f'''<div class="p-4 grid grid-cols-[1fr_1.1fr] gap-4 items-center">
      <div class="aspect-square rounded-2xl bg-gradient-to-br from-sky-100 to-sky-300 flex items-center justify-center"><svg class="w-16 h-16" viewBox="0 0 64 64" fill="none"><path d="M14 22h36l-3 30H17z" fill="#111315"/><path d="M24 22v-4a8 8 0 0116 0v4" stroke="#111315" stroke-width="4"/><circle cx="32" cy="36" r="5" fill="#D8F83C"/></svg></div>
      <div class="grid gap-2">{_cubuk("w-full", "bg-slate-800", "h-2.5")}{_cubuk("w-2/3", "bg-slate-800", "h-2.5")}
        <span class="flex gap-0.5 text-amber-400">{"★" * 5}</span>{_cubuk("w-1/2", "bg-sky-500", "h-3")}
        <span class="mt-1 flex items-center justify-center gap-1.5 rounded-full bg-[#D8F83C] py-2 text-[11px] font-extrabold text-black">{_svg(SEPET, "w-3.5 h-3.5")}Sepete ekle</span>
      </div></div>
      <div class="px-4 pb-4 grid grid-cols-4 gap-2">{''.join(f'<span class="aspect-square rounded-xl {r}"></span>' for r in ("bg-slate-100", "bg-sky-100", "bg-lime-100", "bg-slate-100"))}</div>''')
    return _sahne(f'<div class="w-[300px] sm:w-[350px]">{urun}</div>'
      + _rozet(f'{_ikon_kutu(SEPET)}<span class="grid"><span>Yeni sipariş</span><span class="text-[10px] font-semibold text-slate-400">az önce</span></span>', '-top-3 right-0 sm:-right-2')
      + _rozet(f'<span class="text-[#D8F83C]">{_svg(KILIT)}</span>Güvenli ödeme', '-bottom-1 left-0', 'bg-[#111315] text-white', '-3s'))

def ankara_instagram():
    gonderi = _telefon(f'''<div class="pt-8">
      <div class="flex items-center gap-2 px-3 pb-2"><span class="w-7 h-7 rounded-full bg-gradient-to-br from-sky-400 to-sky-700"></span><span class="grid"><span class="text-[10px] font-bold text-slate-900">markaniz</span><span class="text-[9px] text-slate-500">Sponsorlu</span></span></div>
      <div class="aspect-square bg-gradient-to-br from-sky-500 via-sky-600 to-indigo-700 p-4 flex flex-col justify-end"><span class="text-xl font-extrabold leading-tight text-white">Yeni sezon<br>Ankara’da</span><span class="mt-2 inline-block h-4 w-16 rounded-full bg-[#D8F83C]"></span></div>
      <div class="flex items-center justify-between bg-sky-600 px-3 py-2 text-[10px] font-bold text-white">Daha fazla bilgi<span>›</span></div>
      <div class="flex gap-3 px-3 py-2.5 text-slate-800">{_svg(KALP)}{_svg(YORUM)}{_svg(GONDER)}</div></div>''')
    return _sahne(f'<div class="-translate-x-6">{gonderi}</div>'
      + _rozet(f'<span class="text-sky-600">{_svg(HEDEF)}</span>Hedef kitle: Ankara', 'top-[40%] left-0')
      + _rozet(f'{_ikon_kutu(MESAJ)}<span class="grid"><span>Yeni mesaj</span><span class="text-[10px] font-semibold text-slate-400">reklamdan</span></span>', 'top-8 right-0', 'bg-white text-slate-900', '-2s')
      + _rozet(f'<span class="text-[#D8F83C]">{_svg(GRAFIK)}</span>Bütçe en iyi görsele', 'bottom-10 right-0', 'bg-[#111315] text-white', '-4s'))


def insaat():
    bloklar = (('h-24', 'from-sky-400 to-sky-600'), ('h-32', 'from-slate-700 to-slate-900'), ('h-20', 'from-sky-300 to-sky-500'))
    pencere = '<span class="h-1.5 rounded-sm bg-white/60"></span>' * 6
    proje = _tarayici('projeniz.com.tr', f'''<div class="p-4">
      <div class="rounded-2xl bg-gradient-to-b from-sky-100 to-white px-4 pt-4 flex items-end justify-center gap-2.5">{''.join(f'<span class="w-12 {y} rounded-t-lg bg-gradient-to-b {r} grid grid-cols-2 gap-1 p-1.5 content-start">{pencere}</span>' for y, r in bloklar)}</div>
      <div class="mt-3 flex flex-wrap gap-1.5">{''.join(f'<span class="rounded-full bg-slate-100 px-2.5 py-1 text-[10px] font-bold text-slate-700">{d}</span>' for d in ("2+1", "3+1", "4+1", "Villa"))}</div>
      <div class="mt-3 grid grid-cols-[1fr_auto] gap-2 items-center"><span class="grid gap-1.5">{_cubuk("w-4/5", "bg-slate-800", "h-2.5")}{_cubuk("w-1/2")}</span><span class="inline-flex items-center gap-1.5 rounded-full bg-[#D8F83C] px-3 py-2 text-[11px] font-extrabold text-black">{_svg(TAKVIM, "w-3.5 h-3.5")}Randevu al</span></div>
    </div>''')
    return _sahne(f'<div class="w-[300px] sm:w-[340px]">{proje}</div>'
      + _rozet(f'{_ikon_kutu(TAKVIM)}<span class="grid"><span>Satış ofisi randevusu</span><span class="text-[10px] font-semibold text-slate-400">reklamdan · az önce</span></span>', '-top-3 right-0 sm:-right-2')
      + _rozet(f'<span class="text-[#D8F83C]">{_svg(KONUM)}</span>Hedef: proje bölgesi', '-bottom-1 left-0', 'bg-[#111315] text-white', '-3s'))


CIZIMLER = {
  'yapay-zeka-danismanligi': yapay_zeka,
  'web-tasarim': web_tasarim,
  'dijital-pazarlama': dijital_pazarlama,
  'sosyal-medya-yonetimi': sosyal_medya,
  'kreatif-hizmetler': kreatif,
  'ankara-seo': ankara_seo,
  'ankara-google-ads-ajansi': ankara_google_ads,
  'ankara-reklam-ajansi': ankara_reklam,
  'ankara-e-ticaret-sitesi': ankara_e_ticaret,
  'ankara-instagram-reklam-ajansi': ankara_instagram,
  'insaat-firmalari-icin-reklam-ajansi': insaat,
}

def cizim(adres):
    f = CIZIMLER.get(adres)
    return f() if f else ''


# ---------------------------------------------------------------- "Kapsam" kartlarının simgeleri
DISLI = '<circle cx="12" cy="12" r="3"/><path d="M12 3v2.5M12 18.5V21M4.2 7.5l2.2 1.2M17.6 15.3l2.2 1.2M4.2 16.5l2.2-1.2M17.6 8.7l2.2-1.2"/>'
KEP = '<path d="M3 9.5L12 5l9 4.5-9 4.5z"/><path d="M7 11.5v4c1.5 1.5 3 2 5 2s3.5-.5 5-2v-4M21 9.5v5"/>'
KALKAN = '<path d="M12 3l7 3v5.5c0 4.5-3 7.8-7 9.5-4-1.7-7-5-7-9.5V6z"/><path d="M9 12l2 2 4-4"/>'
SITE = '<rect x="3" y="4.5" width="18" height="15" rx="2.5"/><path d="M3 9h18M7 6.8h.01M9.5 6.8h.01"/>'
KALEM = '<path d="M4 20l1-4.5L15.5 5a2.1 2.1 0 013 3L8 18.5z"/><path d="M13.5 7l3 3"/>'
FIRCA = '<path d="M14 4l6 6-7.5 7.5-6-6z"/><path d="M6.5 11.5L4 20l8.5-2.5"/>'
SUNUCU = '<rect x="4" y="4" width="16" height="7" rx="2"/><rect x="4" y="13" width="16" height="7" rx="2"/><path d="M8 7.5h.01M8 16.5h.01"/>'
KAMERA = '<path d="M4 8.5A2 2 0 016 6.5h2l1.5-2h5l1.5 2h2a2 2 0 012 2V17a2 2 0 01-2 2H6a2 2 0 01-2-2z"/><circle cx="12" cy="12.5" r="3.3"/>'
BELGE = '<path d="M7 3.5h7l4 4V19a1.5 1.5 0 01-1.5 1.5h-9A1.5 1.5 0 016 19V5a1.5 1.5 0 011-1.5z"/><path d="M14 3.5V8h4M9 12.5h6M9 16h4"/>'
OYNAT = '<rect x="3" y="5" width="18" height="14" rx="3.5"/><path d="M10.5 9.5v5l4-2.5z" fill="currentColor"/>'
SEKIL = '<circle cx="8.5" cy="8.5" r="4.5"/><rect x="12" y="12" width="8" height="8" rx="1.5"/>'
KITAP = '<path d="M4 5.5A1.5 1.5 0 015.5 4H11v16H5.5A1.5 1.5 0 014 18.5zM20 5.5A1.5 1.5 0 0018.5 4H13v16h5.5a1.5 1.5 0 001.5-1.5z"/>'
KART = '<rect x="3" y="6" width="18" height="12" rx="2.5"/><path d="M7 10.5h5M7 13.5h3M15.5 11h2"/>'
IZGARA = '<rect x="4" y="4" width="7" height="7" rx="1.5"/><rect x="13" y="4" width="7" height="7" rx="1.5"/><rect x="4" y="13" width="7" height="7" rx="1.5"/><rect x="13" y="13" width="7" height="7" rx="1.5"/>'
SUNUM = '<rect x="3" y="4" width="18" height="12" rx="2"/><path d="M12 16v4M8.5 20h7M8 12l2.5-3 2 2 3-4"/>'
KOD = '<path d="M8.5 8L4.5 12l4 4M15.5 8l4 4-4 4M13.5 5.5l-3 13"/>'
FILTRE = '<path d="M4 5h16l-6 7.5V19l-4-2v-4.5z"/>'
KREDI = '<rect x="3" y="5.5" width="18" height="13" rx="2.5"/><path d="M3 10h18M7 15h4"/>'
KAMYON = '<path d="M3 6.5h11v9H3zM14 9.5h3.5L21 13v2.5h-7"/><circle cx="7" cy="17.5" r="1.8"/><circle cx="17" cy="17.5" r="1.8"/>'
KUTU = '<path d="M4 7.5L12 4l8 3.5v9L12 20l-8-3.5z"/><path d="M4 7.5L12 11l8-3.5M12 11v9"/>'
YENILE = '<path d="M19.5 12a7.5 7.5 0 01-13 5.1M4.5 12a7.5 7.5 0 0113-5.1"/><path d="M17.5 3.5v3.4h-3.4M6.5 20.5v-3.4h3.4"/>'
KITLE = '<circle cx="9" cy="8.5" r="3.2"/><path d="M3.5 19a5.5 5.5 0 0111 0"/><circle cx="17" cy="9.5" r="2.4"/><path d="M15.5 14.2A4.5 4.5 0 0120.5 19"/>'
DUYURU = '<path d="M4 10v4a1 1 0 001 1h2l5 4V5L7 9H5a1 1 0 00-1 1z"/><path d="M16 9a4 4 0 010 6M18.5 6.5a7.5 7.5 0 010 11"/>'
DUZEN = '<rect x="3.5" y="4" width="17" height="16" rx="2.5"/><path d="M3.5 9.5h17M9.5 9.5V20"/>'

KART_SIMGE = {
  'İhtiyaç analizi': ARA, 'Raporlama ve otomasyon': DISLI, 'İçerik ve görsel üretimi': PARILTI, 'Müşteri iletişimi': MESAJ,
  'Ekip eğitimi': KEP, 'Kurumsal yapay zeka eğitimi': KEP, 'Veri güvenliği ve KVKK': KALKAN,
  'Kurumsal web sitesi': SITE, 'E-ticaret ve WooCommerce': SEPET, 'UI/UX tasarım': DUZEN, 'Özel ikon ve illüstrasyon': FIRCA,
  'Hosting ve bakım': SUNUCU, 'Performans ve güvenlik denetimi': SIMSEK,
  'Google Ads yönetimi': ARA, 'Meta reklamları': HEDEF, 'SEO': GRAFIK, 'Dijital medya planlama': TAKVIM, 'Dönüşüm takibi': HEDEF, 'Raporlama': BELGE,
  'Aylık içerik planı': TAKVIM, 'Post, story ve reels': OYNAT, 'Metin yazımı': KALEM, 'Paylaşım takvimi': SAAT,
  'Fotoğraf ve video çekimi': KAMERA, 'Aylık raporlama': GRAFIK,
  'Logo tasarımı': SEKIL, 'Kurumsal kimlik kılavuzu': KITAP, 'Kartvizit ve basılı işler': KART, 'Sosyal medya şablonları': IZGARA,
  'Sunum ve katalog': SUNUM,
  'Teknik SEO': KOD, 'Anahtar kelime araştırması': ARA, 'Yerel SEO': KONUM, 'Sayfa içi SEO': BELGE, 'İçerik planı': KALEM, 'Aylık rapor': GRAFIK,
  'Arama ağı kampanyaları': ARA, 'Performance Max ve Alışveriş': SEPET, 'YouTube ve görüntülü reklam': OYNAT,
  'Kelime ve negatif kelime yönetimi': FILTRE, 'Konum ve saat hedefleme': KONUM,
  'Google reklamları': ARA, 'Instagram ve Facebook reklamları': HEDEF, 'Reklam kreatifleri': FIRCA, 'Sosyal medya yönetimi': KALP,
  'Açılış sayfası ve web sitesi': SITE, 'Ölçüm ve raporlama': GRAFIK,
  'Kampanya fikri ve strateji': PARILTI, 'TV reklam filmi': OYNAT, 'Medya planlama ve satın alma': TAKVIM,
  'Radyo reklamı': DUYURU, 'Açık hava reklamı': SUNUM,
  'Mağaza tasarımı': SITE, 'Ürün ve stok yönetimi': KUTU, 'Ödeme altyapısı': KREDI, 'Kargo bağlantısı': KAMYON,
  'E-ticaret SEO’su': GRAFIK, 'Reklam ve ölçüm': DUYURU,
  'Proje lansman kampanyası': PARILTI, 'Proje web sitesi': SITE, 'Açık hava ve saha': SUNUM, 'Talep ve satış ölçümü': GRAFIK,
  'Hedef kitle kurgusu': KITLE, 'Mesaj ve form kampanyaları': MESAJ, 'Yeniden pazarlama': YENILE, 'Ölçüm kurulumu': HEDEF,
}

def kart_simgesi(baslik):
    """Kapsam kartının simgesi; listede yoksa parıltı simgesi."""
    return _svg(KART_SIMGE.get(baslik, PARILTI), 'w-5 h-5')


# ---------------------------------------------------------------- Blog kapakları
# Yazının ön bilgisindeki `kapak` (kısa etiket) ve `simge` (aşağıdaki adlardan biri) kullanılır.
BLOG_SIMGE = {'site': SITE, 'ara': ARA, 'parilti': PARILTI, 'konum': KONUM, 'kredi': KREDI, 'hedef': HEDEF, 'kep': KEP,
              'grafik': GRAFIK, 'takvim': TAKVIM, 'kalem': KALEM, 'sepet': SEPET, 'kalkan': KALKAN, 'mesaj': MESAJ, 'sekil': SEKIL, 'kalp': KALP}

# küme → (zemin, yazı rengi, ikon kutusu, nokta deseni rengi, logo dosyası)
KAPAK_TEMA = {
  'yapay-zeka-danismanligi': ('bg-[#D8F83C]', 'text-slate-900', 'bg-[#111315] text-[#D8F83C]', '#00000014', 'logo-siyah.svg'),
  'web-tasarim': ('bg-gradient-to-br from-sky-500 to-sky-700', 'text-white', 'bg-[#D8F83C] text-black', '#ffffff22', 'logo-beyaz.svg'),
  'dijital-pazarlama': ('bg-gradient-to-br from-sky-100 to-sky-200', 'text-slate-900', 'bg-sky-500 text-white', '#0284c71f', 'logo-siyah.svg'),
}
KAPAK_TEMA_VARSAYILAN = KAPAK_TEMA['dijital-pazarlama']

def _kapak_motif(y, olcek=''):
    """Kapakların sağındaki üst üste iki kart: arkada eğik bir kart, önde simge ve satırlar."""
    zemin, yazi, kutu, desen, logo = KAPAK_TEMA.get(y['kume'], KAPAK_TEMA_VARSAYILAN)
    cip = 'bg-[#111315] text-white'
    arka = 'bg-sky-300/60' if 'sky-100' in zemin else 'bg-white/35'   # arkadaki eğik kart
    simge = BLOG_SIMGE.get(y.get('simge', ''), PARILTI)
    return (f'<span class="absolute right-[7%] top-1/2 -translate-y-1/2 w-[38%] {olcek}">'
            f'<span class="absolute inset-0 rotate-6 translate-x-[8%] rounded-[18%_18%_18%_18%/22%] {arka}"></span>'
            f'<span class="relative block rounded-[14%/18%] bg-white p-[9%] shadow-2xl shadow-black/20">'
            f'<span class="flex w-[34%] aspect-square rounded-[28%] {kutu} items-center justify-center">{_svg(simge, "w-1/2 h-1/2")}</span>'
            f'<span class="mt-[12%] block h-[0.55em] w-full rounded-full bg-slate-800"></span>'
            f'<span class="mt-[6%] block h-[0.55em] w-3/4 rounded-full bg-slate-800"></span>'
            f'<span class="mt-[10%] block h-[0.35em] w-full rounded-full bg-slate-200"></span>'
            f'<span class="mt-[5%] block h-[0.35em] w-5/6 rounded-full bg-slate-200"></span>'
            f'<span class="mt-[5%] block h-[0.35em] w-2/3 rounded-full bg-slate-200"></span>'
            f'</span>'
            f'<span class="absolute -bottom-[10%] -right-[6%] inline-flex items-center gap-[0.4em] rounded-[0.7em] bg-[#111315] px-[0.8em] py-[0.5em] text-[0.7em] font-bold {cip} shadow-xl whitespace-nowrap">{_svg(ONAY, "w-[1.1em] h-[1.1em]")}{y.get("rozet", "Rehber")}</span>'
            f'</span>')

def blog_kapagi(y, sinif='text-[11px] sm:text-xs'):
    """Blog kartlarının ve yazı sayfasının üstündeki kapak (16:9)."""
    zemin, yazi, kutu, desen, logo = KAPAK_TEMA.get(y['kume'], KAPAK_TEMA_VARSAYILAN)
    return (f'<span class="relative block overflow-hidden aspect-[16/9] {zemin} {sinif}" aria-hidden="true">'
            f'<span class="absolute inset-0" style="background-image:radial-gradient({desen} 1.2px,transparent 1.2px);background-size:16px 16px"></span>'
            f'<span class="absolute -left-[12%] -bottom-[40%] w-[60%] aspect-square rounded-full bg-white/10"></span>'
            f'<span class="absolute left-[7%] top-1/2 -translate-y-1/2 max-w-[44%] text-[1.9em] font-extrabold leading-[1.05] tracking-tight {yazi}" style="text-wrap:balance">{y.get("kapak", "")}</span>'
            f'{_kapak_motif(y)}</span>')

def paylasim_gorseli(y, baslik_html, site_kok):
    """1200x630 paylaşım görseli için bağımsız HTML sayfası (dev/kapaklar.py ekran görüntüsünü alır)."""
    zemin, yazi, kutu, desen, logo = KAPAK_TEMA.get(y['kume'], KAPAK_TEMA_VARSAYILAN)
    # file:// sayfasında yazı tipi dosyası yüklenmez; sayfaya gömülür
    import base64, os
    klasor = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'site', 'assets', 'fonts')
    import re   # site.css'teki @font-face kuralları (karakter aralıklarıyla), dosya yolu yerine gömülü veri
    css = open(os.path.join(klasor, '..', 'css', 'site.css'), encoding='utf-8').read()
    yazi_tipi = ''.join(re.findall(r'@font-face\s*\{[^}]*\}', css))
    yazi_tipi = re.sub(r'url\(/assets/fonts/([^)]+)\)', lambda m: 'url(data:font/woff2;base64,'
                       + base64.b64encode(open(os.path.join(klasor, m.group(1)), 'rb').read()).decode() + ')', yazi_tipi)
    return f'''<!DOCTYPE html><html lang="tr"><head><meta charset="utf-8">
<link rel="stylesheet" href="{site_kok}/assets/css/tailwind.css"><link rel="stylesheet" href="{site_kok}/assets/css/site.css">
<style>{yazi_tipi}
html,body{{margin:0;width:1200px;height:630px;overflow:hidden}}</style></head>
<body class="font-sans antialiased"><div class="relative w-[1200px] h-[630px] overflow-hidden {zemin} text-[30px]">
<span class="absolute inset-0" style="background-image:radial-gradient({desen} 2px,transparent 2px);background-size:28px 28px"></span>
<span class="absolute -left-[8%] -bottom-[45%] w-[50%] aspect-square rounded-full bg-white/10"></span>
<img src="{site_kok}/assets/img/{logo}" alt="" class="absolute left-[72px] top-[56px] h-[38px] w-auto">
<div class="absolute left-[72px] top-[40px] bottom-0 w-[600px] flex flex-col justify-center">
  <span class="self-start rounded-full bg-white px-4 py-1.5 text-[15px] font-bold tracking-wider text-slate-900">{y["etiket"]}</span>
  <p class="mt-5 text-[52px] font-extrabold leading-[1.06] tracking-tight {yazi}">{baslik_html}</p><!-- text-wrap:balance yok: başsız Chrome İ'nin noktasını çizmiyor -->
  <p class="mt-6 text-[20px] font-semibold {yazi} opacity-80">clickbait.com.tr/blog</p>
</div>
{_kapak_motif(y, "!w-[30%] !right-[6%]")}
</div></body></html>'''
