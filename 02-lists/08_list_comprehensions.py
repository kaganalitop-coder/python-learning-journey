# ========================================
# LIST COMPREHENSIONS
# ========================================
# Tek satırda liste oluşturma

print("="*70)
print("LIST COMPREHENSIONS")
print("="*70)

# ============================================
# 1. List Comprehension Nedir?
# ============================================
print("\n📌 1. List Comprehension Nedir?")
print("-"*70)

print("""
List Comprehension:
• Tek satırda liste oluşturma
• For döngüsünün kısa hali
• Daha temiz ve okunabilir kod
• Python'un en güçlü özelliklerinden biri
• Daha hızlı çalışır

Klasik Yol vs Comprehension:
# Klasik (4 satır)
liste = []
for x in range(10):
    liste.append(x ** 2)

# Comprehension (1 satır)
liste = [x ** 2 for x in range(10)]

💡 Aynı sonuç, daha az kod!
""")

# ============================================
# 2. İlk List Comprehension
# ============================================
print("\n" + "="*70)
print("📌 2. İlk List Comprehension")
print("-"*70)

# Klasik yol
print("--- Klasik Yol ---")
kareler_klasik = []
for sayi in range(1, 11):
    kareler_klasik.append(sayi ** 2)
print(f"Kareler: {kareler_klasik}")

# List comprehension
print("\n--- List Comprehension ---")
kareler = [sayi ** 2 for sayi in range(1, 11)]
print(f"Kareler: {kareler}")

print("\n💡 Tek satır, aynı sonuç!")

# ============================================
# 3. Syntax Açıklaması
# ============================================
print("\n" + "="*70)
print("📌 3. Syntax Açıklaması")
print("-"*70)

print("""
List Comprehension Syntax:

[ifade for öğe in liste]

Parçalar:
1. [       → Liste başlangıcı
2. ifade   → Ne yapılacak (x ** 2)
3. for     → Döngü
4. öğe     → Döngü değişkeni
5. in      → İçinden
6. liste   → Veri kaynağı
7. ]       → Liste bitişi

Örnek:
[x * 2 for x in range(5)]
 ↓     ↓           ↓
 Ne    Döngü      Nereden

Adım Adım:
1. range(5) → 0, 1, 2, 3, 4
2. Her x için → x * 2
3. Listeye ekle → [0, 2, 4, 6, 8]
""")

# Örnekler
print("\n--- Basit Örnekler ---")

# Sayıları 2 ile çarp
sonuc1 = [x * 2 for x in range(5)]
print(f"2 ile çarp: {sonuc1}")

# Sayıları 10 ile çarp
sonuc2 = [x * 10 for x in range(1, 6)]
print(f"10 ile çarp: {sonuc2}")

# String'leri büyüt
isimler = ['ali', 'ayşe', 'mehmet']
buyuk_isimler = [isim.upper() for isim in isimler]
print(f"Büyük harfler: {buyuk_isimler}")

# ============================================
# 4. Matematiksel İşlemler
# ============================================
print("\n" + "="*70)
print("📌 4. Matematiksel İşlemler")
print("-"*70)

# Kareler
kareler = [x ** 2 for x in range(1, 11)]
print(f"Kareler (1-10): {kareler}")

# Küpler
kupler = [x ** 3 for x in range(1, 11)]
print(f"Küpler (1-10): {kupler}")

# Çift sayılar
ciftler = [x * 2 for x in range(1, 11)]
print(f"Çift sayılar: {ciftler}")

# Karelerin toplamı
kare_toplam = sum([x ** 2 for x in range(1, 11)])
print(f"Karelerin toplamı: {kare_toplam}")

# ============================================
# 5. Koşullu List Comprehension
# ============================================
print("\n" + "="*70)
print("📌 5. Koşullu List Comprehension")
print("-"*70)

print("""
Koşul Ekleme:

[ifade for öğe in liste if koşul]

Örnek:
[x for x in range(10) if x % 2 == 0]
→ Sadece çift sayılar

💡 if koşulu sonuna eklenir!
""")

# Çift sayılar
cift_sayilar = [x for x in range(20) if x % 2 == 0]
print(f"Çift sayılar: {cift_sayilar}")

# Tek sayılar
tek_sayilar = [x for x in range(20) if x % 2 != 0]
print(f"Tek sayılar: {tek_sayilar}")

# 3'e bölünenler
ucebolunen = [x for x in range(30) if x % 3 == 0]
print(f"3'e bölünenler: {ucebolunen}")

# 50'den büyükler
sayilar = [10, 25, 50, 75, 100, 125]
buyukler = [x for x in sayilar if x > 50]
print(f"50'den büyük: {buyukler}")

# ============================================
# 6. String İşlemleri
# ============================================
print("\n" + "="*70)
print("📌 6. String İşlemleri")
print("-"*70)

# Başharfleri büyüt
isimler = ['ali', 'ayşe', 'mehmet', 'zeynep']
basharfler = [isim.title() for isim in isimler]
print(f"Başharfler: {basharfler}")

# Uzunlukları al
kelimeler = ['Python', 'JavaScript', 'C++', 'Go']
uzunluklar = [len(kelime) for kelime in kelimeler]
print(f"Uzunluklar: {uzunluklar}")

# 5 harften uzun olanlar
uzun_kelimeler = [kelime for kelime in kelimeler if len(kelime) > 5]
print(f"5+ harf: {uzun_kelimeler}")

# İlk harfleri al
ilk_harfler = [isim[0] for isim in isimler]
print(f"İlk harfler: {ilk_harfler}")

# ============================================
# 7. İç İçe Döngüler
# ============================================
print("\n" + "="*70)
print("📌 7. İç İçe Döngüler")
print("-"*70)

# Çarpım tablosu (düz liste)
carpim = [i * j for i in range(1, 4) for j in range(1, 4)]
print(f"Çarpımlar: {carpim}")

# İki listenin kombinasyonu
renkler = ['kırmızı', 'mavi']
nesneler = ['araba', 'ev']
kombinasyon = [f"{renk} {nesne}" for renk in renkler for nesne in nesneler]
print(f"Kombinasyonlar: {kombinasyon}")

# Matris düzleştirme
matris = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
duz = [sayi for satir in matris for sayi in satir]
print(f"Düz liste: {duz}")

# ============================================
# 8. If-Else ile Comprehension
# ============================================
print("\n" + "="*70)
print("📌 8. If-Else ile Comprehension")
print("-"*70)

print("""
If-Else Kullanımı:

[ifade_doğru if koşul else ifade_yanlış for öğe in liste]

⚠️ Dikkat: if-else ÖNCE gelir!

Örnek:
['Çift' if x % 2 == 0 else 'Tek' for x in range(5)]
""")

# Çift mi Tek mi?
sayilar = range(10)
etiketler = ['Çift' if x % 2 == 0 else 'Tek' for x in sayilar]
print(f"Etiketler: {etiketler}")

# Pozitif/Negatif/Sıfır
sayilar2 = [-5, -2, 0, 3, 7]
isaret = ['Pozitif' if x > 0 else 'Negatif' if x < 0 else 'Sıfır' for x in sayilar2]
print(f"İşaretler: {isaret}")

# Geçti/Kaldı
notlar = [45, 60, 75, 30, 85, 50]
durum = ['Geçti' if not_ >= 50 else 'Kaldı' for not_ in notlar]
print(f"Durum: {durum}")

# ============================================
# 9. Pratik Örnekler
# ============================================
print("\n" + "="*70)
print("📌 9. Pratik Örnekler")
print("-"*70)

# Örnek 1: Sesli harfleri bul
cumle = "Python programlama"
sesliler = [harf for harf in cumle.lower() if harf in 'aeiouöüıâîû']
print(f"Sesli harfler: {sesliler}")

# Örnek 2: Sayıların karelerini al (50'den küçük)
kareler_50 = [x ** 2 for x in range(1, 20) if x ** 2 < 50]
print(f"50'den küçük kareler: {kareler_50}")

# Örnek 3: Fiyatlara KDV ekle
fiyatlar = [100, 200, 150, 300]
kdv_dahil = [fiyat * 1.20 for fiyat in fiyatlar]
print(f"KDV dahil: {kdv_dahil}")

# Örnek 4: Kelime uzunlukları sözlüğü
kelimeler = ['Python', 'Java', 'C++', 'JavaScript']
uzunluk_sozluk = {kelime: len(kelime) for kelime in kelimeler}
print(f"Uzunluklar: {uzunluk_sozluk}")

# Örnek 5: İki liste çarpımı
liste1 = [1, 2, 3]
liste2 = [4, 5, 6]
carpimlar = [a * b for a, b in zip(liste1, liste2)]
print(f"Çarpımlar: {carpimlar}")

# ============================================
# 10. Performans Karşılaştırması
# ============================================
print("\n" + "="*70)
print("📌 10. Performans Karşılaştırması")
print("-"*70)

import time

n = 100000

# Klasik for döngüsü
start = time.time()
liste1 = []
for x in range(n):
    liste1.append(x ** 2)
sure1 = time.time() - start

# List comprehension
start = time.time()
liste2 = [x ** 2 for x in range(n)]
sure2 = time.time() - start

print(f"For döngüsü: {sure1:.4f} saniye")
print(f"Comprehension: {sure2:.4f} saniye")
print(f"Hız farkı: {sure1/sure2:.2f}x daha hızlı")

print("\n💡 List comprehension daha hızlıdır!")

# ============================================
# 11. Ne Zaman Kullanmalı?
# ============================================
print("\n" + "="*70)
print("📌 11. Ne Zaman Kullanmalı?")
print("-"*70)

print("""
✅ List Comprehension Kullan:

1. Basit dönüşümler
   [x * 2 for x in liste]
   
2. Filtreleme
   [x for x in liste if x > 0]
   
3. Tek satıra sığan işlemler
   [x.upper() for x in liste]
   
4. Matematiksel işlemler
   [x ** 2 for x in range(10)]

❌ Kullanma:

1. Karmaşık mantık
   → Normal for döngüsü kullan
   
2. Çok uzun satırlar
   → Okunabilirlik önemli
   
3. Birden fazla işlem
   → For döngüsü daha net
   
4. Yan etkiler (side effects)
   → print(), dosya yazma vb.

💡 Kural: Okunabilir mi? 
   Evet → Comprehension kullan
   Hayır → For döngüsü kullan
""")

# İyi örnek
iyi = [x ** 2 for x in range(10)]
print(f"\n✅ İyi: {iyi}")

# Kötü örnek (çok karmaşık - kullanmayın)
# karmasik = [x if x > 0 else -x if x < 0 else 0 for x in [-5, 0, 5]]
# Bu yerine normal for döngüsü kullanın

# ============================================
# 12. Dictionary Comprehension
# ============================================
print("\n" + "="*70)
print("📌 12. Dictionary Comprehension (Bonus)")
print("-"*70)

# Dictionary oluşturma
kareler_dict = {x: x ** 2 for x in range(1, 6)}
print(f"Kareler dict: {kareler_dict}")

# String uzunlukları
kelimeler = ['Python', 'Java', 'C++']
uzunluk_dict = {kelime: len(kelime) for kelime in kelimeler}
print(f"Uzunluklar: {uzunluk_dict}")

# Koşullu dictionary
sayilar = range(10)
cift_dict = {x: x ** 2 for x in sayilar if x % 2 == 0}
print(f"Çift sayılar: {cift_dict}")

# ============================================
# 13. Set Comprehension
# ============================================
print("\n" + "="*70)
print("📌 13. Set Comprehension (Bonus)")
print("-"*70)

# Set oluşturma (tekrarsız)
kareler_set = {x ** 2 for x in range(-5, 6)}
print(f"Kareler set: {kareler_set}")

# Son rakamlar
son_rakamlar = {x % 10 for x in range(100)}
print(f"Son rakamlar: {son_rakamlar}")

print("\n💡 { } ile set, { x: y } ile dictionary!")

# ============================================
# 14. İleri Seviye Örnekler
# ============================================
print("\n" + "="*70)
print("📌 14. İleri Seviye Örnekler")
print("-"*70)

# Örnek 1: Fibonacci (ilk 10)
fib = [0, 1]
[fib.append(fib[-1] + fib[-2]) for _ in range(8)]
print(f"Fibonacci: {fib}")

# Örnek 2: Matris transpose
matris = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transpose = [[satir[i] for satir in matris] for i in range(3)]
print(f"Orijinal: {matris}")
print(f"Transpose: {transpose}")

# Örnek 3: Kelime frekansları
cumle = "python python java python java c++"
kelimeler = cumle.split()
frekans = {kelime: kelimeler.count(kelime) for kelime in set(kelimeler)}
print(f"Frekanslar: {frekans}")

# Örnek 4: Asal sayılar (basit)
asallar = [x for x in range(2, 50) 
           if all(x % i != 0 for i in range(2, int(x ** 0.5) + 1))]
print(f"Asal sayılar: {asallar}")

# ============================================
# ÖZET
# ============================================
print("\n" + "="*70)
print("📚 LIST COMPREHENSIONS ÖZET")
print("="*70)
print("""
List Comprehension:

Temel Syntax:
[ifade for öğe in liste]

Koşullu (Filtreli):
[ifade for öğe in liste if koşul]

If-Else:
[ifade1 if koşul else ifade2 for öğe in liste]

İç İçe:
[x * y for x in liste1 for y in liste2]

Örnekler:
[x ** 2 for x in range(10)]              → Kareler
[x for x in range(20) if x % 2 == 0]    → Çift sayılar
[x.upper() for x in kelimeler]          → Büyük harfler
[x if x > 0 else 0 for x in sayilar]    → Pozitife çevir

Avantajlar:
✓ Daha kısa kod
✓ Daha hızlı
✓ Daha okunabilir (basit işlemler için)
✓ Pythonic

Dezavantajlar:
✗ Karmaşık mantık zor okunur
✗ Debug yapmak zor
✗ Uzun satırlar kötü

Dictionary:
{anahtar: değer for öğe in liste}

Set:
{ifade for öğe in liste}

💡 İpuçları:
• Basit işlemler için kullan
• Okunabilirlik öncelik
• 1 satıra sığmalı
• Karmaşıksa for döngüsü kullan
• Pratik yap!

Sırada:
→ Tuples (Değişmez listeler)
→ Index hataları
→ PEP 8 stil rehberi
""")
print("="*70)
