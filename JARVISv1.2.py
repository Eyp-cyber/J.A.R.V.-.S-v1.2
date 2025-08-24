import os
import subprocess as sub
import tkinter as tk
import wikipedia
import requests  # Google API için gerekli

# Türkçe sonuç almak için dil ayarı
wikipedia.set_lang("tr")


# --- Program Açma Fonksiyonları ---
def notpad():
    sub.Popen("notepad.exe")

def hesap_makinesi():
    sub.Popen("calc.exe")

def google():
    sub.Popen(r"C:\Program Files\Google\Chrome\Application\chrome.exe")

def chatgpt():
    try:
        sub.Popen("chatgpt")
    except FileNotFoundError:
        sonuc.config(text="ChatGPT bulunamadı!")

def spotify():
    try:
        sub.Popen("spotify")
    except FileNotFoundError:
        sonuc.config(text="Spotify bulunamadı!")


def wiki_ara(konu):
    try:
        bilgi = wikipedia.summary(konu, sentences=2)
        sonuc.config(text=bilgi)
    except wikipedia.exceptions.DisambiguationError as e:
        sonuc.config(text=f"Birden fazla sonuç bulundu: {e.options[:3]}")
    except wikipedia.exceptions.PageError:
        sonuc.config(text="Aradığınız konu bulunamadı!")

# --- Matematik Fonksiyonları ---
def topla(a, b):
    return a + b

def cikar(a, b):
    return a - b

def carp(a, b):
    return a * b

def bol(a, b):
    if b == 0:
        return "Sıfıra bölme hatası!"
    return a / b



# --- Komut çalıştırma fonksiyonu ---
def komut_calistir(event=None):
    soru1 = giris.get().lower().strip()

    if soru1 in ["google", "google aç", "googleı aç"]:
        google()
        sonuc.config(text="Google açılıyor...")

    elif soru1.startswith("google ara "):
        kelime = soru1.replace("google ara ", "")
        sonuc.config(text=google_ara(kelime))

    elif soru1 in ["notepad", "not defteri", "note pad", "notdefteri aç", "not defterini aç"]:
        notpad()
        sonuc.config(text="Not Defteri açılıyor...")

    elif soru1 in ["hesap makinesi", "hesap makinesini aç", "hesapmakinesi aç"]:
        hesap_makinesi()
        sonuc.config(text="Hesap Makinesi açılıyor...")

    elif soru1 in ["gpt aç", "chatgpt"]:
        chatgpt()
        sonuc.config(text="ChatGPT açılıyor efendim...")

    elif soru1 in ["spotify aç", "spo aç", "spotify"]:
        spotify()
        sonuc.config(text="Spotify açılıyor...")

    elif soru1.startswith("wikipedia "):
        konu = soru1.replace("wikipedia ", "")
        wiki_ara(konu)

    # Matematik işlemleri
    elif soru1.startswith("topla "):
        try:
            sayilar = soru1.replace("topla ", "").split()
            sonuc.config(text=f"Sonuç: {topla(float(sayilar[0]), float(sayilar[1]))}")
        except:
            sonuc.config(text="Lütfen iki sayı girin! (örn: topla 5 3)")

    elif soru1.startswith("çıkar "):
        try:
            sayilar = soru1.replace("çıkar ", "").split()
            sonuc.config(text=f"Sonuç: {cikar(float(sayilar[0]), float(sayilar[1]))}")
        except:
            sonuc.config(text="Lütfen iki sayı girin! (örn: çıkar 10 4)")

    elif soru1.startswith("çarp "):
        try:
            sayilar = soru1.replace("çarp ", "").split()
            sonuc.config(text=f"Sonuç: {carp(float(sayilar[0]), float(sayilar[1]))}")
        except:
            sonuc.config(text="Lütfen iki sayı girin! (örn: çarp 6 7)")

    elif soru1.startswith("böl "):
        try:
            sayilar = soru1.replace("böl ", "").split()
            sonuc.config(text=f"Sonuç: {bol(float(sayilar[0]), float(sayilar[1]))}")
        except:
            sonuc.config(text="Lütfen iki sayı girin! (örn: böl 20 5)")

    elif soru1.startswith("mutlak "):
        try:
            sayi = float(soru1.replace("mutlak ", ""))
            sonuc.config(text=f"Bu sayının mutlak değeri: {abs(sayi)}")
        except:
            sonuc.config(text="Lütfen geçerli bir sayı girin! (örn: mutlak -12)")

    
    else:
        sonuc.config(text="Komut anlaşılamadı!")

    giris.delete(0, tk.END)

# --- Pencereyi kapatma fonksiyonu ---
def pencereyi_kapat(event=None):
    pen.destroy()

# --- Tkinter Penceresi ---
pen = tk.Tk()
pen.title("J.A.R.V.I.S v1.2")
pen.geometry("500x400")

etiket = tk.Label(pen, text="Bugün Size Nasıl Yardımcı Olabilirim Efendim: ", font=("Arial", 12))
etiket.pack(pady=5)

giris = tk.Entry(pen, font=("Arial", 12))
giris.pack(pady=5, fill="x", padx=10)

buton = tk.Button(pen, text="gönder", command=komut_calistir)
buton.pack(pady=10)

sonuc = tk.Label(pen, text="", font=("Arial", 10), fg="green", wraplength=450, justify="left")
sonuc.pack(pady=5)

kisayollar = tk.Label(
    pen,
    text="Kısayollar:\n[Enter] → Komutu çalıştır\n[ESC] → Pencereyi kapat\n"
         "Wikipedia: wikipedia <konu>\n"
         "Google Arama: google ara <konu>\n"
         "Matematik: topla/çıkar/çarp/böl <sayı1> <sayı2>\n"
         "Mutlak: mutlak <sayı>\n",
    font=("Arial", 10),
    fg="black",
    justify="left"
)
kisayollar.pack(pady=15)

pen.bind("<Return>", komut_calistir)
pen.bind("<Escape>", pencereyi_kapat)

pen.mainloop()
