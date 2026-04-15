# ========================================
# LİSTE DÜZENLEME VE SIRALAMA
# ========================================
# sort(), sorted(), reverse()

print("="*70)
print("LİSTE DÜZENLEME VE SIRALAMA")
print("="*70)

# ============================================
# 1. sort() - Kalıcı Sıralama
# ============================================
print("\n📌 1. sort() - Kalıcı Sıralama")
print("-"*70)

# Alfabetik sıralama
arabalar = ['bmw', 'audi', 'toyota', 'subaru']
print(f"Orijinal: {arabalar}")

arabalar.sort()
print(f"Sıralandı: {arabalar}")

print("\n💡 sort() listeyi kalıcı olarak değiştirir!")

# Sayıları sıralama
sayilar = [5, 2, 8, 1, 9, 3]
print(f"\nÖnce: {sayilar}")
sayilar.sort()
print(f"Sonra: {sayilar}")

# Türkçe karakterler
print("\n--- Türkçe Karakterler ---")
sehirler = ['İzmir', 'Ankara', 'İstanbul', 'Bursa', 'Çanakkale']
print(f"Önce: {sehirler}")
sehirler.sort()
print(f"Sonra: {sehirler}")
print("⚠️ Türkçe karakterlerde sorun olabilir!")

# ============================================
# 2. sort(reverse=True) - Ters Sıralama
# ============================================
print("\n" + "="*70)
print("📌 2. sort(reverse=True) - Ters Sıralama")
print("-"*70)

# Tersten sıralama
arabalar = ['bmw', 'audi', 'toyota', 'subaru']
print(f"Önce: {arabalar}")

arabalar.sort(reverse=True)
print(f"Tersten: {arabalar}")

# Sayıları tersten sıralama
sayilar = [5, 2, 8, 1, 9, 3]
print(f"\nÖnce: {sayilar}")
sayilar.sort(reverse=True)
print(f"Büyükten küçüğe: {sayilar}")

print("\n💡 reverse=True büyükten küçüğe sıralar!")

# ============================================
# 3. sorted() - Geçici Sıralama
# ============================================
print("\n" + "="*70)
print("📌 3. sorted() - Geçici Sıralama")
print("-"*70)

# Orijinali koruyarak sıralama
arabalar = ['bmw', 'audi', 'toyota', 'subaru']
print(f"Orijinal liste: {arabalar}")
print(f"Sıralı görünüm: {sorted(arabalar)}")
print(f"Hala orijinal: {arabalar}")

print("\n💡 sorted() orijinali değiştirmez!")
print("   Yeni bir liste döndürür!")

# sort() vs sorted()
print("\n--- sort() vs sorted() ---")

# sort() - Kalıcı
liste1 = [3, 1, 4, 1, 5, 9]
print(f"sort() önce: {liste1}")
liste1.sort()
print(f"sort() sonra: {liste1}")  # Değişti!

# sorted() - Geçici
liste2 = [3, 1, 4, 1, 5, 9]
print(f"\nsorted() önce: {liste2}")
sirali = sorted(liste2)
print(f"Sıralı: {sirali}")
print(f"Orijinal: {liste2}")  # Değişmedi!

# ============================================
# 4. reverse() - Tersine Çevirme
# ============================================
print("\n" + "="*70)
print("📌 4. reverse() - Tersine Çevirme")
print("-"*70)

# Listeyi ters çevirme
arabalar = ['bmw', 'audi', 'toyota', 'subaru']
print(f"Önce: {arabalar}")

arabalar.reverse()
print(f"Sonra: {arabalar}")

# Tekrar ters çevirme
arabalar.reverse()
print(f"Tekrar ters: {arabalar}")

print("\n💡 reverse() sıralamaz, sadece tersine çevirir!")
print("   Kronolojik sırayı tersine çevirmek için kullanışlı!")

# Tarihsel sıra örneği
print("\n--- Tarihsel Sıra ---")
yillar = [2020, 2021, 2022, 2023, 2024]
print(f"Eskiden yeniye: {yillar}")

yillar.reverse()
print(f"Yeniden eskiye: {yillar}")

# ============================================
# 5. Sıralama Karşılaştırması
# ============================================
print("\n" + "="*70)
print("📌 5. Sıralama Metodlarını Karşılaştırma")
print("-"*70)

print("""
sort()            : Kalıcı sıralama (A-Z)
sort(reverse=True): Kalıcı ters sıralama (Z-A)
sorted()          : Geçici sıralama, orijinali korur
reverse()         : Sırayı tersine çevir (sıralamaz!)

Hangisini Kullanmalı?

✓ sort()       : Liste artık sıralı kalmalı
✓ sorted()     : Sadece o an sıralı görmek istiyorum
✓ reverse()    : Kronolojik sırayı tersine çevir
""")

# Pratik karşılaştırma
ogrenciler = ['Zeynep', 'Ali', 'Mehmet', 'Ayşe']
print(f"Orijinal: {ogrenciler}")

# Geçici görüntü
print(f"Sıralı görünüm: {sorted(ogrenciler)}")
print(f"Hala orijinal: {ogrenciler}")

# Kalıcı değişiklik
ogrenciler.sort()
print(f"Kalıcı sıralı: {ogrenciler}")

# ============================================
# 6. Özel Sıralama - key Parametresi
# ============================================
print("\n" + "="*70)
print("📌 6. Özel Sıralama - key Parametresi")
print("-"*70)

# Uzunluğa göre sıralama
kelimeler = ['python', 'java', 'c', 'javascript', 'go']
print(f"Önce: {kelimeler}")

kelimeler.sort(key=len)
print(f"Uzunluğa göre: {kelimeler}")

# Sayıları string olarak
sayilar_str = ['1', '10', '2', '20', '3']
print(f"\nÖnce: {sayilar_str}")
sayilar_str.sort()
print(f"String sıralama: {sayilar_str}")  # Yanlış!

sayilar_str.sort(key=int)
print(f"Sayı sıralama: {sayilar_str}")  # Doğru!

# Büyük/küçük harf duyarsız
print("\n--- Büyük/Küçük Harf Duyarsız ---")
isimler = ['ali', 'Zeynep', 'mehmet', 'Ayşe']
print(f"Önce: {isimler}")
isimler.sort(key=str.lower)
print(f"Sonra: {isimler}")

print("\n💡 key=len uzunluğa göre sıralar")
print("   key=str.lower büyük/küçük harf duyarsız")

# ============================================
# 7. Pratik Örnekler
# ============================================
print("\n" + "="*70)
print("📌 7. Pratik Örnekler")
print("-"*70)

# Örnek 1: En yüksek notlar
print("--- En Yüksek 3 Not ---")
notlar = [85, 92, 78, 95, 88, 90, 82]
print(f"Tüm notlar: {notlar}")

sirali_notlar = sorted(notlar, reverse=True)
en_yuksek_3 = sirali_notlar[:3]
print(f"En yüksek 3: {en_yuksek_3}")

# Örnek 2: Alfabetik üye listesi
print("\n--- Üye Listesi ---")
uyeler = ['Zeynep', 'Ali', 'Mehmet', 'Ayşe', 'Can']
print(f"Kayıt sırası: {uyeler}")

uyeler.sort()
print(f"Alfabetik: {uyeler}")

# Örnek 3: Fiyat sıralaması
print("\n--- Ürün Fiyatları ---")
fiyatlar = [1500, 800, 2200, 950, 1800]
print(f"Karışık: {fiyatlar}")

fiyatlar.sort()
print(f"Ucuzdan pahalıya: {fiyatlar}")

en_ucuz = fiyatlar[0]
en_pahali = fiyatlar[-1]
print(f"En ucuz: {en_ucuz} TL")
print(f"En pahalı: {en_pahali} TL")

# Örnek 4: Son 3 aktivite
print("\n--- Son Aktiviteler ---")
aktiviteler = ['Giriş', 'Profil', 'Ayarlar', 'Çıkış', 'Mesaj']
print(f"Kronolojik: {aktiviteler}")

# Son 3'ü göster (ters çevir)
aktiviteler.reverse()
son_3 = aktiviteler[:3]
print(f"Son 3 aktivite: {son_3}")

# ============================================
# 8. Karmaşık Veri Sıralama
# ============================================
print("\n" + "="*70)
print("📌 8. Karmaşık Veri Sıralama")
print("-"*70)

# Tuple listesi sıralama
print("--- Öğrenci Notları ---")
ogrenciler = [
    ('Ali', 85),
    ('Ayşe', 92),
    ('Mehmet', 78),
    ('Zeynep', 95)
]

# İsme göre sırala
ogrenciler.sort(key=lambda x: x[0])
print("İsme göre:")
for isim, not_ in ogrenciler:
    print(f"  {isim}: {not_}")

# Nota göre sırala
ogrenciler.sort(key=lambda x: x[1], reverse=True)
print("\nNota göre:")
for isim, not_ in ogrenciler:
    print(f"  {isim}: {not_}")

print("\n💡 lambda fonksiyonu ile özel sıralama!")

# ============================================
# 9. Sıralama Hataları
# ============================================
print("\n" + "="*70)
print("📌 9. ⚠️ Sıralama Hataları")
print("-"*70)

print("""
Yaygın Hatalar:

1. Karışık tip sıralama:
   liste = [1, '2', 3]
   liste.sort()  # HATA! int ve str karışık
   
2. None değeri:
   liste = [1, None, 3]
   liste.sort()  # HATA! None sıralanamaz
   
3. sort() vs sorted() karışıklığı:
   sirali = liste.sort()  # HATA! sort() None döndürür
   sirali = sorted(liste)  # DOĞRU!
   
4. Orijinali kaybetme:
   liste.sort()  # Orijinal kayboldu!
   # Önce kopyala: yedek = liste.copy()

💡 İpuçları:
• Tek tip veri sıralayın
• Orijinali korumak isterseniz sorted() kullanın
• sort() None döndürür, listeyi değiştirir!
""")

# Doğru kullanım örnekleri
print("\n--- Doğru Kullanım ---")

# ✅ Kopyalayıp sıralama
orijinal = [3, 1, 4, 1, 5]
yedek = orijinal.copy()
yedek.sort()
print(f"Orijinal: {orijinal}")
print(f"Sıralı: {yedek}")

# ✅ sorted() kullanma
sayilar = [3, 1, 4, 1, 5]
sirali = sorted(sayilar)
print(f"\nOrijinal: {sayilar}")
print(f"Sıralı: {sirali}")

# ============================================
# 10. İleri Seviye - Çoklu Kriter Sıralama
# ============================================
print("\n" + "="*70)
print("📌 10. İleri Seviye - Çoklu Kriter")
print("-"*70)

# Önce nota, sonra isme göre sırala
ogrenciler = [
    ('Zeynep', 90),
    ('Ali', 90),
    ('Mehmet', 85),
    ('Ayşe', 90)
]

print("Orijinal:")
for isim, not_ in ogrenciler:
    print(f"  {isim}: {not_}")

# Önce nota (yüksekten alçağa), sonra isme (A-Z)
ogrenciler.sort(key=lambda x: (-x[1], x[0]))

print("\nSıralı (Not↓, İsim↑):")
for isim, not_ in ogrenciler:
    print(f"  {isim}: {not_}")

print("\n💡 Tuple döndürerek çoklu kriter!")

# ============================================
# ÖZET
# ============================================
print("\n" + "="*70)
print("📚 LİSTE DÜZENLEME ÖZET")
print("="*70)
print("""
Kalıcı Sıralama:
✓ liste.sort()              : A-Z sırala
✓ liste.sort(reverse=True)  : Z-A sırala
✓ liste.reverse()           : Tersine çevir

Geçici Sıralama:
✓ sorted(liste)             : Orijinal korunur
✓ sorted(liste, reverse=True): Ters sıralı görünüm

Özel Sıralama:
✓ sort(key=len)             : Uzunluğa göre
✓ sort(key=str.lower)       : Büyük/küçük harf duyarsız
✓ sort(key=lambda x: x[1])  : Özel kriter

Farklar:
sort()    → Kalıcı, None döndürür
sorted()  → Geçici, yeni liste döndürür
reverse() → Tersine çevir (sıralamaz!)

💡 İpuçları:
• Orijinali korumak için sorted()
• Kalıcı değişim için sort()
• Sıralama değil ters çevirme için reverse()
• Özel kriter için key parametresi
• Karışık tip sıralama hatası verir!

Sırada:
→ Slicing (dilimleme)
→ Liste kopyalama
→ Liste birleştirme
""")
print("="*70)
