#!/usr/bin/env python3
"""Yeni ya da değişen sayfaları IndexNow ile Bing'e (ve IndexNow kullanan diğer arama motorlarına) bildirir.

    python3 dev/indexnow.py https://clickbait.com.tr/blog/yeni-yazi/   # belirli adresler
    python3 dev/indexnow.py --hepsi                                     # site haritasındaki tüm adresler

Yayından SONRA çalıştırılır (sayfalar ve anahtar dosyası canlıda olmalı).
Anahtar: site/<32 karakter>.txt dosyası; içeriği dosya adıyla aynıdır (gizli değildir, herkese açık olması gerekir).
"""
import glob, json, os, re, sys, urllib.request

KOK = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'site')
ALAN = 'https://clickbait.com.tr'

anahtarlar = [os.path.basename(p)[:-4] for p in glob.glob(os.path.join(KOK, '*.txt')) if re.fullmatch(r'[0-9a-f]{32}\.txt', os.path.basename(p))]
if len(anahtarlar) != 1:
    sys.exit(f'site/ içinde tek bir IndexNow anahtar dosyası olmalı, bulunan: {anahtarlar}')
anahtar = anahtarlar[0]

if '--hepsi' in sys.argv:
    urller = re.findall(r'<loc>([^<]+)</loc>', open(os.path.join(KOK, 'sitemap.xml'), encoding='utf-8').read())
else:
    urller = [u for u in sys.argv[1:] if u.startswith(ALAN)]
if not urller:
    sys.exit('Bildirilecek adres yok. Örnek: python3 dev/indexnow.py https://clickbait.com.tr/blog/yeni-yazi/')

veri = json.dumps({'host': 'clickbait.com.tr', 'key': anahtar, 'keyLocation': f'{ALAN}/{anahtar}.txt', 'urlList': urller}).encode()
istek = urllib.request.Request('https://api.indexnow.org/indexnow', data=veri, headers={'Content-Type': 'application/json; charset=utf-8'})
try:
    with urllib.request.urlopen(istek, timeout=30) as cevap:
        print(f'IndexNow: {cevap.status} — {len(urller)} adres bildirildi')   # 200 ya da 202 = alındı
except urllib.error.HTTPError as e:
    sys.exit(f'IndexNow hatası: {e.code} {e.read()[:200]!r}')
