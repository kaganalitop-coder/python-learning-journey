# ========================================
# F-STRING BASIT ANLATIM
# ========================================
# F-string = String içine değişken koymak

print("="*60)
print("F-STRING NEDİR? - BASİT ANLATIM")
print("="*60)

# ============================================
# ÖRNEK 1: En Basit Kullanım
# ============================================
print("\n📌 ÖRNEK 1: Değişkeni String İçinde Kullanmak")
print("-"*60)

isim = "Ahmet"

# ESKİ YÖNTEM (Karmaşık)
print("Eski yöntem:")
mesaj_eski = "Merhaba " + isim
print(mesaj_eski)

# YENİ YÖNTEM (F-string - Basit!)
print("\nF-string ile:")
mesaj_yeni = f"Merhaba {isim}"
print(mesaj_yeni)

print("\n💡 İkisi de aynı şeyi yapıyor ama f-string daha kolay!")

# ============================================
# ÖRNEK 2: Birden Fazla Değişken
# ============================================
print("\n" + "="*60)
print("📌 ÖRNEK 2: Birden Fazla Değişken")
print("-"*60)

isim = "Ayşe"
soyisim = "Yılmaz"
yas = 28

# ESKİ YÖNTEM (Çok karmaşık!)
print("Eski yöntem:")
mesaj = "Adı: " + isim + " " + soyisim + ", Yaşı: " + str(yas)
print(mesaj)

# YENİ YÖNTEM (Çok kolay!)
print("\nF-string ile:")
mesaj = f"Adı: {isim} {soyisim}, Yaşı: {yas}"
print(mesaj)

print("\n💡 Gördünüz mü? + işaretleri kayboldu, str() gerek yok!")

# ============================================
# ÖRNEK 3: Matematik İşlemleri
# ============================================
print("\n" + "="*60)
print("📌 ÖRNEK 3: String İçinde İşlem Yapmak")
print("-"*60)

fiyat = 100
indirim = 20

# F-string içinde işlem yapabilirsiniz!
print(f"Ürün fiyatı: {fiyat} TL")
print(f"İndirim: %{indirim}")
print(f"İndirimli fiyat: {fiyat - (fiyat * indirim / 100)} TL")

print("\n💡 Süslü parantez içinde matematiksel işlem yapabiliyorsunuz!")

# ============================================
# ÖRNEK 4: Gerçek Hayat - E-Ticaret
# ============================================
print("\n" + "="*60)
print("📌 ÖRNEK 4: E-Ticaret Sepeti")
print("-"*60)

urun = "Laptop"
adet = 2
birim_fiyat = 15000

toplam = adet * birim_fiyat

# Sepet özeti
print(f"""
🛒 SEPETİNİZ:
------------------------
Ürün        : {urun}
Adet        : {adet}
Birim Fiyat : {birim_fiyat} TL
------------------------
TOPLAM      : {toplam} TL
""")

print("💡 Bu kadar kolay! Hepsini tek string içinde yazdık!")

# ============================================
# ÖRNEK 5: Gerçek Hayat - Öğrenci Notu
# ============================================
print("\n" + "="*60)
print("📌 ÖRNEK 5: Öğrenci Not Sistemi")
print("-"*60)

ogrenci_adi = "Mehmet Kaya"
vize = 70
final = 85
ortalama = (vize * 0.4) + (final * 0.6)

# Durum kontrolü
durum = "GEÇTİ ✓" if ortalama >= 60 else "KALDI ✗"

# Not bilgisi
print(f"""
{'='*40}
      ÖĞRENCİ NOT BİLGİSİ
{'='*40}
Öğrenci : {ogrenci_adi}
Vize    : {vize}
Final   : {final}
Ortalama: {ortalama:.1f}
Durum   : {durum}
{'='*40}
""")

print("💡 Tek bir f-string ile karmaşık rapor oluşturduk!")

# ============================================
# ÖRNEK 6: Neden F-String Kullanmalıyız?
# ============================================
print("\n" + "="*60)
print("🎯 NEDEN F-STRING KULLANMALIYIZ?")
print("="*60)

ad = "Ali"
sehir = "İstanbul"
yas = 30

print("\n1️⃣ ESKİ YÖNTEM (+ ile birleştirme):")
print("   Mesaj: " + ad + " " + str(yas) + " yaşında ve " + sehir + "'da yaşıyor")
print("   ❌ Karmaşık, okuması zor, str() gerekli")

print("\n2️⃣ YENİ YÖNTEM (F-string):")
print(f"   Mesaj: {ad} {yas} yaşında ve {sehir}'da yaşıyor")
print("   ✅ Temiz, okunabilir, kolay!")

# ============================================
# ÖZET
# ============================================
print("\n" + "="*60)
print("📚 F-STRING ÖZET")
print("="*60)
print("""
F-string = String içine değişken koymak!

Nasıl kullanılır?
1. String'in başına 'f' koy
2. Değişkenleri {süslü_parantez} içine koy

Örnek:
    isim = "Ali"
    print(f"Merhaba {isim}!")
    
Avantajları:
✅ Daha okunabilir
✅ Daha kısa kod
✅ str() dönüşümü otomatik
✅ İşlem yapabilirsiniz
✅ Modern Python yöntemi (3.6+)

Eski yöntem yerine F-string kullanın!
""")
print("="*60)
