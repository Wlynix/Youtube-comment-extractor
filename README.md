# 🎥 YouTube Comment Extractor (Excel Export)

Bu araç, YouTube Data API v3 kullanarak istediğiniz videonun yorumlarını saniyeler içinde çeker ve bir **Excel (.xlsx)** dosyasına kaydeder. Kullanıcı dostu bir arayüze (GUI) sahiptir.

## ✨ Özellikler
- 🚀 Çok hızlı çalışır (API tabanlıdır).
- 📊 Yazar adı, yorum metni, beğeni sayısı ve tarih bilgilerini alır.
- 📁 Verileri düzenli bir Excel tablosu olarak sunar.
- 💻 Kurulum gerektirmeyen basit bir arayüzü vardır.

## 🛠️ Kurulum
1. Bilgisayarınızda Python yüklü olduğundan emin olun.
2. Gerekli kütüphaneleri yüklemek için terminale şunu yazın:
   ```bash
   pip install -r requirements.txt

  🔑 API Anahtarı Nasıl Alınır?
Bu programı kullanmak için kendi Google API anahtarınıza ihtiyacınız vardır:

1 Google Cloud Console adresine gidin.

2 Yeni bir proje oluşturun.

3 Library sekmesinden YouTube Data API v3'ü bulun ve etkinleştirin.

4 Credentials sayfasından Create Credentials > API Key diyerek anahtarınızı alın.
