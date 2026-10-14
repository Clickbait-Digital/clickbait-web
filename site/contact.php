<?php
/* Clickbait Digital — iletişim formu
   Talebi e-posta olarak gönderir. Yanıt: {"ok":true} ya da {"ok":false,"hata":"..."}

   E-posta ayarları (şifre dahil) bu dosyada DEĞİL, public_html'in bir üst klasöründeki
   clickbait-ayarlar.php dosyasındadır. O dosya GitHub'a konmaz ve dışarıdan açılamaz. */

$ALICI      = 'info@clickbait.com.tr';   // Talepler bu adrese gelir
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
function b64baslik($s) { return '=?UTF-8?B?' . base64_encode($s) . '?='; }

/* ---------- SMTP ile gönderim ---------- */
function smtp_oku($fp) {
  $yanit = '';
  while (($satir = fgets($fp, 1024)) !== false) {
    $yanit .= $satir;
    if (strlen($satir) < 4 || $satir[3] === ' ') break;
  }
  return (int)substr($yanit, 0, 3);
}
function smtp_komut($fp, $komut, $beklenen) {
  fwrite($fp, $komut . "\r\n");
  return in_array(smtp_oku($fp), (array)$beklenen);
}
function smtp_gonder($a, $alici, $konu, $govde, $yanitla) {
  $guvenlik = isset($a['guvenlik']) ? $a['guvenlik'] : 'ssl';
  $ctx = stream_context_create(array('ssl' => array('verify_peer' => false, 'verify_peer_name' => false, 'allow_self_signed' => true)));
  $adres = ($guvenlik === 'ssl' ? 'ssl://' : 'tcp://') . $a['sunucu'] . ':' . $a['port'];
  $fp = @stream_socket_client($adres, $no, $msj, 20, STREAM_CLIENT_CONNECT, $ctx);
  if (!$fp) return 'smtp_baglanti';
  stream_set_timeout($fp, 20);
  $ben = isset($_SERVER['SERVER_NAME']) ? $_SERVER['SERVER_NAME'] : 'localhost';
  if (smtp_oku($fp) !== 220) { fclose($fp); return 'smtp_karsilama'; }
  if (!smtp_komut($fp, "EHLO $ben", 250)) { fclose($fp); return 'smtp_ehlo'; }
  if ($guvenlik === 'tls') {
    if (!smtp_komut($fp, 'STARTTLS', 220)) { fclose($fp); return 'smtp_starttls'; }
    if (!@stream_socket_enable_crypto($fp, true, STREAM_CRYPTO_METHOD_TLS_CLIENT)) { fclose($fp); return 'smtp_tls'; }
    if (!smtp_komut($fp, "EHLO $ben", 250)) { fclose($fp); return 'smtp_ehlo'; }
  }
  if (!smtp_komut($fp, 'AUTH LOGIN', 334)
   || !smtp_komut($fp, base64_encode($a['kullanici']), 334)
   || !smtp_komut($fp, base64_encode($a['sifre']), 235)) { fclose($fp); return 'smtp_giris'; }
  if (!smtp_komut($fp, 'MAIL FROM:<' . $a['kullanici'] . '>', 250)) { fclose($fp); return 'smtp_gonderen'; }
  if (!smtp_komut($fp, "RCPT TO:<$alici>", array(250, 251))) { fclose($fp); return 'smtp_alici'; }
  if (!smtp_komut($fp, 'DATA', 354)) { fclose($fp); return 'smtp_data'; }
  $mesaj  = 'Date: ' . date('r') . "\r\n";
  $mesaj .= 'From: ' . b64baslik('Clickbait Web Formu') . ' <' . $a['kullanici'] . ">\r\n";
  $mesaj .= "To: <$alici>\r\n";
  if ($yanitla !== '') $mesaj .= "Reply-To: <$yanitla>\r\n";
  $mesaj .= 'Subject: ' . b64baslik($konu) . "\r\n";
  $mesaj .= 'Message-ID: <' . md5(uniqid('', true)) . '@' . $ben . ">\r\n";
  $mesaj .= "MIME-Version: 1.0\r\nContent-Type: text/plain; charset=UTF-8\r\nContent-Transfer-Encoding: base64\r\n\r\n";
  $mesaj .= rtrim(chunk_split(base64_encode($govde), 76, "\r\n")) . "\r\n.";
  if (!smtp_komut($fp, $mesaj, 250)) { fclose($fp); return 'smtp_reddedildi'; }
  smtp_komut($fp, 'QUIT', 221);
  fclose($fp);
  return '';
}

/* ---------- Form ---------- */
if ($_SERVER['REQUEST_METHOD'] !== 'POST') cevap(false, 405, 'yalnizca_post');
if (al('website') !== '') cevap(true, 200, '');   // bot tuzağı

$ad     = tek_satir(al('name'), 100);
$marka  = tek_satir(al('company'), 120);
$ulasim = tek_satir(al('reach'), 150);
$not    = kisalt(trim(str_replace("\r", '', (string)al('note'))), 2000);
$hizmet = array();
if (isset($_POST['services']) && is_array($_POST['services'])) {
  foreach (array_slice($_POST['services'], 0, 10) as $h) $hizmet[] = tek_satir($h, 60);
}
if ($ad === '' || $ulasim === '') cevap(false, 422, 'eksik_alan');

$ip = isset($_SERVER['REMOTE_ADDR']) ? $_SERVER['REMOTE_ADDR'] : 'x';
$iz = sys_get_temp_dir() . '/cb_form_' . md5($ip);
if (is_file($iz) && (time() - filemtime($iz)) < $BEKLEME_SN) cevap(false, 429, 'cok_sik');

$govde  = "Web sitesinden yeni geri arama talebi\n\n";
$govde .= "Ad: $ad\n";
if ($marka !== '') $govde .= "Marka: $marka\n";
$govde .= "Telefon / e-posta: $ulasim\n";
if ($hizmet) $govde .= "İlgilendiği hizmetler: " . implode(', ', $hizmet) . "\n";
if ($not !== '') $govde .= "\nNot:\n$not\n";
$govde .= "\nTarih: " . date('d.m.Y H:i') . "\nIP: $ip\n";
$konu    = 'Web sitesi: Geri arama talebi - ' . $ad;
$yanitla = filter_var($ulasim, FILTER_VALIDATE_EMAIL) ? $ulasim : '';

$ayarDosyasi = dirname(__DIR__) . '/clickbait-ayarlar.php';
$ayar = is_file($ayarDosyasi) ? include $ayarDosyasi : null;

if (is_array($ayar) && !empty($ayar['sifre']) && $ayar['sifre'] !== 'BURAYA_SIFRE') {
  $hata = smtp_gonder($ayar, $ALICI, $konu, $govde, $yanitla);
  if ($hata !== '') cevap(false, 500, $hata);
} elseif (function_exists('mail')) {
  $bas  = 'From: ' . b64baslik('Clickbait Web Formu') . " <$ALICI>\r\n";
  if ($yanitla !== '') $bas .= "Reply-To: $yanitla\r\n";
  $bas .= "MIME-Version: 1.0\r\nContent-Type: text/plain; charset=UTF-8\r\nContent-Transfer-Encoding: 8bit";
  if (!@mail($ALICI, b64baslik($konu), $govde, $bas)) cevap(false, 500, 'mail_gonderilemedi');
} else {
  cevap(false, 500, 'smtp_ayari_yok');
}

@touch($iz);
cevap(true, 200, '');
