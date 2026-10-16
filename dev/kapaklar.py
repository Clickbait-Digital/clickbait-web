#!/usr/bin/env python3
"""Blog yazıları için 1200x630 paylaşım görselleri (LinkedIn, WhatsApp, Google önizlemesi).

    python3 dev/kapaklar.py          # yalnızca görseli olmayan yazılar
    python3 dev/kapaklar.py --hepsi  # tümünü yeniden üret

Görseller site/assets/img/blog/<adres>.jpg olarak yazılır. Önce CSS derlenmiş olmalı (README'deki komut);
ardından `python3 dev/sayfalar.py` yazı sayfalarının og:image etiketini bu görsele bağlar.
Google Chrome ve macOS'taki `sips` gerekir.
"""
import os, sys, html, subprocess, tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sayfalar import YAZILAR, KOK
from cizimler import paylasim_gorseli

CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
SITE = os.path.abspath(KOK)
HEDEF = os.path.join(SITE, 'assets', 'img', 'blog')

def uret(y, gecici):
    cikti = os.path.join(gecici, y['adres'] + '.png')
    sayfa = os.path.join(gecici, y['adres'] + '.html')
    open(sayfa, 'w', encoding='utf-8').write(paylasim_gorseli(y, html.escape(y['baslik']), 'file://' + SITE))
    subprocess.run([CHROME, '--headless=new', '--disable-gpu', '--hide-scrollbars', '--allow-file-access-from-files',
                    '--window-size=1200,630', '--virtual-time-budget=2000', f'--screenshot={cikti}', 'file://' + sayfa],
                   check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    subprocess.run(['sips', '-s', 'format', 'jpeg', '-s', 'formatOptions', '85', cikti, '--out', os.path.join(HEDEF, y['adres'] + '.jpg')],
                   check=True, stdout=subprocess.DEVNULL)   # macOS: PNG → JPG (daha küçük dosya)
    print('görsel:', y['adres'])

if __name__ == '__main__':
    os.makedirs(HEDEF, exist_ok=True)
    hepsi = '--hepsi' in sys.argv
    with tempfile.TemporaryDirectory() as gecici:
        for y in YAZILAR:
            if hepsi or not os.path.exists(os.path.join(HEDEF, y['adres'] + '.jpg')):
                uret(y, gecici)
