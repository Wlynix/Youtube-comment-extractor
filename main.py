import tkinter as tk
from tkinter import messagebox, filedialog
import pandas as pd
from googleapiclient.discovery import build

def yorumlari_getir():
    api_key = api_entry.get().strip()
    raw_url = url_entry.get().strip()
    
    if not api_key or not raw_url:
        messagebox.showerror("Hata", "Lütfen API Anahtarını ve Video Linkini girin!")
        return

    # Video ID ayıklama
    video_id = ""
    if "v=" in raw_url:
        video_id = raw_url.split("v=")[1].split("&")[0]
    elif "youtu.be/" in raw_url:
        video_id = raw_url.split("youtu.be/")[1].split("?")[0]
    else:
        video_id = raw_url

    try:
        # YouTube API bağlantısı
        youtube = build('youtube', 'v3', developerKey=api_key)
        yorumlar = []
        
        # İlk sayfa isteği# Mevcut kodundaki request kısmını şu şekilde değiştir:

        request = youtube.commentThreads().list(
            part="snippet,replies", # Yanıtları da işin içine katmak için
            videoId=video_id,
            maxResults=100,
            order="time", # En yeni yorumlardan başlayarak çekmesini sağlar
            textFormat="plainText"
        )
           
        while request:
            response = request.execute()
            for item in response['items']:
                snippet = item['snippet']['topLevelComment']['snippet']
                yorumlar.append({
                    'Yazar': snippet['authorDisplayName'],
                    'Yorum': snippet['textDisplay'],
                    'Beğeni': snippet['likeCount'],
                    'Tarih': snippet['publishedAt']
                })
            
            # Sonraki sayfa var mı kontrol et (Kota dostu döngü)
            request = youtube.commentThreads().list_next(request, response)
            
            # GitHub sürümü için opsiyonel sınır: 
            # if len(yorumlar) > 2000: break 

        if not yorumlar:
            messagebox.showwarning("Uyarı", "Yorum bulunamadı veya video yorumlara kapalı.")
            return

        # Kaydetme ekranı
        dosya_yolu = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel Dosyası", "*.xlsx")])
        if dosya_yolu:
            df = pd.DataFrame(yorumlar)
            df.to_excel(dosya_yolu, index=False)
            messagebox.showinfo("Başarılı", f"{len(yorumlar)} adet yorum başarıyla kaydedildi!")

    except Exception as e:
        messagebox.showerror("API Hatası", f"Bir sorun oluştu. API anahtarınızın doğru olduğundan ve YouTube Data API v3'ün aktif olduğundan emin olun.\n\nHata: {str(e)}")

# --- ARAYÜZ ---
root = tk.Tk()
root.title("YouTube Comment Extractor (API Version)")
root.geometry("500x300")

tk.Label(root, text="Google API Key (YouTube Data API v3):", font=("Arial", 10, "bold")).pack(pady=10)
api_entry = tk.Entry(root, width=60, show="*")
api_entry.pack(pady=5)

tk.Label(root, text="YouTube Video Linki:", font=("Arial", 10, "bold")).pack(pady=10)
url_entry = tk.Entry(root, width=60)
url_entry.pack(pady=5)

tk.Button(root, text="Yorumları API ile Çek", command=yorumlari_getir, bg="#28a745", fg="white", font=("Arial", 10, "bold"), padx=20, pady=10).pack(pady=25)

root.mainloop()