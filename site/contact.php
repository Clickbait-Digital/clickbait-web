<?php
/* Clickbait Digital — iletişim formu
   Formdan gelen talebi aşağıdaki adrese e-posta olarak gönderir.
   Yanıt: {"ok":true} ya da {"ok":false,"hata":"..."} */

$ALICI      = 'info@clickbait.com.tr';   // Talepler bu adrese gelir
$GONDEREN   = 'info@clickbait.com.tr';   // Alan adınıza ait bir adres olmalı
$BEKLEME_SN = 30;                        // Aynı kişiden iki gönderim arası en az süre

@date_default_timezone_set('Europe/Istanbul');
header('Content-Type: application/json; charset=utf-8');
header('Cache-Control: no-store');

function cevap($ok, $kod, $hata) {
  http_response_code($kod);
  $c = array('ok' => $ok);
  if ($hata !== '') $c['hata'] = $hata;
  echo json_encode($c);
  exit;
}
function al($ad) { return isset($_POST[$ad]) ? $_POST[$ad] : ''; }
function kisalt($s, $max) { return function_exists('mb_substr') ? mb_substr($s, 0, $max, 'UTF-8') : substr($s, 0, $max); }
function tek_satir($v, $max) { return kisalt(trim(preg_replace('/[\r\n\t]+/', ' ', (string)$v)), $max); }

if ($_SERVER['REQUEST_METHOD'] !== 'POST') cevap(false, 405, 'yalnizca_post');

// Bot tuzağı: gerçek ziyaretçi bu alanı görmez
if (al('website') !== '') cevap(true, 200, '');

$ad     = tek_satir(al('name'), 100);
$marka  = tek_satir(al('company'), 120);
$ulasim = tek_satir(al('reach'), 150);
$not    = kisalt(trim(str_replace("\r", '', (string)al('note'))), 2000);
$hizmet = array();
if (isset($_POST['services']) && is_array($_POST['services'])) {
  foreach (array_slice($_POST['services'], 0, 10) as $h) $hizmet[] = tek_satir($h, 60);
}
if ($ad === '' || $ulasim === '') cevap(false, 422, 'eksik_alan');

// Basit sıklık sınırı (IP başına)
$ip = isset($_SERVER['REMOTE_ADDR']) ? $_SERVER['REMOTE_ADDR'] : 'x';
$iz = sys_get_temp_dir() . '/cb_form_' . md5($ip);
if (is_file($iz) && (time() - filemtime($iz)) < $BEKLEME_SN) cevap(false, 429, 'cok_sik');

if (!function_exists('mail')) cevap(false, 500, 'mail_fonksiyonu_kapali');

$govde  = "Web sitesinden yeni geri arama talebi\n\n";
$govde .= "Ad: $ad\n";
if ($marka !== '') $govde .= "Marka: $marka\n";
$govde .= "Telefon / e-posta: $ulasim\n";
if ($hizmet) $govde .= "İlgilendiği hizmetler: " . implode(', ', $hizmet) . "\n";
if ($not !== '') $govde .= "\nNot:\n$not\n";
$govde .= "\nTarih: " . date('d.m.Y H:i') . "\nIP: $ip\n";

$konu = '=?UTF-8?B?' . base64_encode('Web sitesi: Geri arama talebi - ' . $ad) . '?=';
$basliklar  = "From: =?UTF-8?B?" . base64_encode('Clickbait Web Formu') . "?= <$GONDEREN>\r\n";
if (filter_var($ulasim, FILTER_VALIDATE_EMAIL)) $basliklar .= "Reply-To: $ulasim\r\n";
$basliklar .= "MIME-Version: 1.0\r\nContent-Type: text/plain; charset=UTF-8\r\nContent-Transfer-Encoding: 8bit";

$ok = @mail($ALICI, $konu, $govde, $basliklar, '-f' . $GONDEREN);
if (!$ok) $ok = @mail($ALICI, $konu, $govde, $basliklar);   // bazı sunucular -f'yi kabul etmez
if (!$ok) cevap(false, 500, 'mail_gonderilemedi');

@touch($iz);
cevap(true, 200, '');
