# Clickbait Digital — web sitesi

clickbait.com.tr'nin kaynak dosyaları.

## Nasıl yayına çıkar?
- `site/` klasörü sunucudaki `public_html` klasörünün birebir kopyasıdır.
- Sunucudaki `guncelle.php` (bu repoda yok, gizli anahtar içerir) cron ile 5 dakikada bir `site/SURUM` dosyasını kontrol eder.
  Sürüm değiştiyse `site/` içeriğini indirip `public_html`'e yazar.
- Bir değişikliği yayına almak için: dosyaları düzenle, `site/SURUM` içindeki sayıyı bir artır, `main` dalına gönder.
- Sunucudan bir dosya silinecekse yolunu `site/SILINECEKLER` dosyasına satır satır yaz.

## Tasarım sınıfları
`site/index.html`'e yeni Tailwind sınıfı eklendiğinde CSS'i yeniden derle:

    npx tailwindcss@3.4.17 -c dev/tailwind.config.js -i dev/in.css -o site/assets/css/tailwind.css --minify

## Bölümler
`site/index.html` içindeki her bölüm `BÖLÜM: … — BAŞLANGIÇ` ve `BÖLÜM: … — BİTİŞ` yorumlarıyla işaretlidir.
