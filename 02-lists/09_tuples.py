# ========================================
# TUPLES (DEĞİŞMEZ LİSTELER)
# ========================================
# Immutable (değiştirilemez) veri yapısı

print("="*70)
print("TUPLES (DEĞİŞMEZ LİSTELER)")
print("="*70)

# ============================================
# 1. Tuple Nedir?
# ============================================
print("\n📌 1. Tuple Nedir?")
print("-"*70)

print("""
Tuple:
• Liste gibi ama değiştirilemez (immutable)
• Parantez ( ) ile gösterilir
• Daha hızlıdır
• Daha az bellek kullanır
• Güvenlidir (değişmez)

Liste vs Tuple:
Liste   = [1, 2, 3]   → Değiştirilebilir
Tuple   = (1, 2, 3)   → Değiştirilemez

💡 Değişmemesi gereken veriler için tuple kullanın!
""")

# ============================================
# 2. Tuple Oluşturma
# ============================================
print("\n" + "="*70)
print("📌 2. Tuple Oluşturma")
print("-"*70)

# Basit tuple
boyutlar = (200, 50)
print(f"Boyutlar: {boyutlar}")
print(f"Tip: {type(boyutlar)}")

# Çeşitli tuple'lar
sayilar = (1, 2, 3, 4, 5)
print(f"Sayılar: {sayilar}")

renkler = ('kırmızı', 'yeşil', 'mavi')
print(f"Renkler: {renkler}")

karisik = (1, 'Python', 3.14, True)
print(f"Karışık: {karisik}")

# Boş tuple
bos = ()
print(f"Boş tuple: {bos}")

# Tek elemanlı tuple (virgül önemli!)
tek = (5,)
print(f"Tek elemanlı: {tek}")
print(f"Tip: {type(tek)}")

# Virgülsüz (bu tuple değil!)
virgulsuz = (5)
print(f"Virgülsüz: {virgulsuz}")
print(f"Tip: {type(virgulsuz)}")  # int!

print("\n💡 Tek elemanlı tuple için virgül şart!")

# ============================================
# 3. Tuple'a Erişim
# ============================================
print("\n" + "="*70)
print("📌 3. Tuple Öğelerine Erişim")
print("-"*70)

# İndeksle erişim
boyutlar = (200, 50)
print(f"Boyutlar: {boyutlar}")
print(f"Genişlik: {boyutlar[0]}")
print(f"Yükseklik: {boyutlar[1]}")

# Negatif indeks
renkler = ('kırmızı', 'yeşil', 'mavi', 'sarı')
print(f"\nRenkler: {renkler}")
print(f"İlk renk: {renkler[0]}")
print(f"Son renk: {renkler[-1]}")
print(f"Sondan 2.: {renkler[-2]}")

print("\n💡 Tuple'a erişim liste gibidir!")

# ============================================
# 4. Tuple Değiştirilemez!
# ============================================
print("\n" + "="*70)
print("📌 4. Tuple Değiştirilemez (Immutable)")
print("-"*70)

print("""
Tuple'ı değiştirmeye çalışırsanız:

boyutlar = (200, 50)
boyutlar[0] = 250  # ❌ TypeError!

Hata:
TypeError: 'tuple' object does not support item assignment

💡 Bu iyi bir şeydir! Verileriniz güvende.
""")

# Hata örneği (yorum satırı)
boyutlar = (200, 50)
print(f"Orijinal: {boyutlar}")

try:
    boyutlar[0] = 250
except TypeError as e:
    print(f"⚠️ Hata: {e}")

print("\n💡 Tuple değiştirilemeyen bir veri yapısıdır!")

# ============================================
# 5. Tuple Üzerinde Döngü
# ============================================
print("\n" + "="*70)
print("📌 5. Tuple Üzerinde Döngü")
print("-"*70)

# For döngüsü
boyutlar = (200, 50)
print("Boyutlar:")
for boyut in boyutlar:
    print(f"  {boyut}")

# Renkler
renkler = ('kırmızı', 'yeşil', 'mavi', 'sarı')
print("\nRenkler:")
for renk in renkler:
    print(f"  - {renk}")

# Koordinatlar
koordinatlar = (10, 20, 30)
print(f"\n3D Koordinat: {koordinatlar}")
for i, koordinat in enumerate(koordinatlar):
    eksen = ['X', 'Y', 'Z'][i]
    print(f"  {eksen}: {koordinat}")

# ============================================
# 6. Tuple'ı Yeniden Yazma
# ============================================
print("\n" + "="*70)
print("📌 6. Tuple'ı Yeniden Yazma")
print("-"*70)

print("""
Tuple değiştirilemez ama yeniden atanabilir!

✅ YAPILIR:
boyutlar = (200, 50)
boyutlar = (400, 100)  # Yeni tuple

❌ YAPILMAZ:
boyutlar[0] = 400  # Değiştirme!

💡 Değişkeni yeni bir tuple'a atayabilirsiniz!
""")

# Örnek
boyutlar = (200, 50)
print("Orijinal boyutlar:")
for boyut in boyutlar:
    print(f"  {boyut}")

# Yeniden yazma
boyutlar = (400, 100)
print("\nYeni boyutlar:")
for boyut in boyutlar:
    print(f"  {boyut}")

print("\n💡 Değişken aynı, tuple yeni!")

# ============================================
# 7. Liste vs Tuple
# ============================================
print("\n" + "="*70)
print("📌 7. Liste vs Tuple Karşılaştırma")
print("-"*70)

print("""
┌─────────────────┬──────────────┬─────────────┐
│   Özellik       │    Liste     │    Tuple    │
├─────────────────┼──────────────┼─────────────┤
│ Syntax          │ [1, 2, 3]    │ (1, 2, 3)   │
│ Değiştirilebilir│ ✅ Evet      │ ❌ Hayır    │
│ Hız             │ Yavaş        │ Hızlı       │
│ Bellek          │ Fazla        │ Az          │
│ Metodlar        │ Çok          │ Az          │
│ Kullanım        │ Dinamik      │ Sabit       │
└─────────────────┴──────────────┴─────────────┘

Liste Kullan:
✓ Değişecek veriler
✓ Ekleme/çıkarma olacak
✓ Sık güncelleme

Tuple Kullan:
✓ Sabit veriler
✓ Koordinatlar (x, y)
✓ RGB renkleri (255, 0, 0)
✓ Tarih (2024, 4, 15)
✓ Performans önemli

💡 Değişmeyecekse tuple, değişecekse liste!
""")

# Performans karşılaştırması
import sys

liste = [1, 2, 3, 4, 5]
tuple_ = (1, 2, 3, 4, 5)

print(f"\nListe boyutu: {sys.getsizeof(liste)} bytes")
print(f"Tuple boyutu: {sys.getsizeof(tuple_)} bytes")
print(f"Fark: {sys.getsizeof(liste) - sys.getsizeof(tuple_)} bytes")

# ============================================
# 8. Tuple Metodları
# ============================================
print("\n" + "="*70)
print("📌 8. Tuple Metodları")
print("-"*70)

sayilar = (1, 2, 3, 2, 4, 2, 5)
print(f"Tuple: {sayilar}")

# count() - Kaç tane var?
print(f"\n2 kaç tane? {sayilar.count(2)}")
print(f"4 kaç tane? {sayilar.count(4)}")
print(f"10 kaç tane? {sayilar.count(10)}")  # 0

# index() - İlk indeksi bul
print(f"\n2'nin ilk indeksi: {sayilar.index(2)}")
print(f"5'in indeksi: {sayilar.index(5)}")

# Tuple uzunluğu
print(f"\nUzunluk: {len(sayilar)}")

# Max, Min, Sum
print(f"En büyük: {max(sayilar)}")
print(f"En küçük: {min(sayilar)}")
print(f"Toplam: {sum(sayilar)}")

print("""
Tuple Metodları (Sadece 2 tane!):
✓ count(x)  → x kaç tane?
✓ index(x)  → x'in indeksi?

Liste Metodları (Çok fazla):
✓ append(), insert(), remove()
✓ pop(), clear(), sort()
✓ reverse(), extend()

💡 Tuple daha basit çünkü değiştirilemez!
""")

# ============================================
# 9. Tuple Unpacking
# ============================================
print("\n" + "="*70)
print("📌 9. Tuple Unpacking (Açma)")
print("-"*70)

# Basit unpacking
koordinatlar = (10, 20)
x, y = koordinatlar
print(f"Koordinatlar: {koordinatlar}")
print(f"x = {x}, y = {y}")

# Çoklu unpacking
bilgi = ('Ali', 25, 'İstanbul')
isim, yas, sehir = bilgi
print(f"\nİsim: {isim}")
print(f"Yaş: {yas}")
print(f"Şehir: {sehir}")

# RGB renk
renk = (255, 0, 128)
r, g, b = renk
print(f"\nRGB: {renk}")
print(f"Red: {r}, Green: {g}, Blue: {b}")

# Değişken değiştirme (swap)
a, b = 10, 20
print(f"\nÖnce: a = {a}, b = {b}")
a, b = b, a
print(f"Sonra: a = {a}, b = {b}")

print("\n💡 Tuple unpacking çok güçlüdür!")

# ============================================
# 10. Tuple Slicing
# ============================================
print("\n" + "="*70)
print("📌 10. Tuple Slicing")
print("-"*70)

sayilar = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
print(f"Tuple: {sayilar}")

# Slicing
print(f"\nİlk 3: {sayilar[:3]}")
print(f"Son 3: {sayilar[-3:]}")
print(f"Orta: {sayilar[3:7]}")
print(f"2'şer: {sayilar[::2]}")
print(f"Tersten: {sayilar[::-1]}")

print("\n💡 Tuple slicing liste gibidir!")

# ============================================
# 11. Pratik Kullanım Örnekleri
# ============================================
print("\n" + "="*70)
print("📌 11. Pratik Kullanım Örnekleri")
print("-"*70)

# Örnek 1: Koordinatlar
print("--- Koordinat Sistemi ---")
nokta = (100, 200)
print(f"Nokta: {nokta}")
print(f"X: {nokta[0]}, Y: {nokta[1]}")

# Örnek 2: RGB Renkler
print("\n--- RGB Renkleri ---")
KIRMIZI = (255, 0, 0)
YESIL = (0, 255, 0)
MAVI = (0, 0, 255)
print(f"Kırmızı: {KIRMIZI}")
print(f"Yeşil: {YESIL}")
print(f"Mavi: {MAVI}")

# Örnek 3: Tarih
print("\n--- Tarihler ---")
dogum_tarihi = (1990, 5, 15)
yil, ay, gun = dogum_tarihi
print(f"Doğum tarihi: {gun}/{ay}/{yil}")

# Örnek 4: Fonksiyon dönüşü
print("\n--- Fonksiyon Dönüşü ---")
def min_max(liste):
    return (min(liste), max(liste))

sonuc = min_max([3, 7, 2, 9, 1])
print(f"Min-Max: {sonuc}")
minimum, maksimum = sonuc
print(f"En küçük: {minimum}, En büyük: {maksimum}")

# Örnek 5: Sabitler
print("\n--- Sabitler ---")
PI = (3.14159,)  # Tek elemanlı tuple
HAFTANIN_GUNLERI = ('Pzt', 'Sal', 'Çar', 'Per', 'Cum', 'Cmt', 'Paz')
print(f"Pi: {PI[0]}")
print(f"Günler: {HAFTANIN_GUNLERI}")

# ============================================
# 12. Tuple içinde Liste
# ============================================
print("\n" + "="*70)
print("📌 12. Tuple İçinde Liste")
print("-"*70)

# Tuple içinde liste olabilir
veri = (1, 2, [3, 4, 5])
print(f"Orijinal: {veri}")

# Liste değiştirilebilir!
veri[2][0] = 999
print(f"Değişti: {veri}")

print("""
⚠️ DİKKAT:
Tuple değiştirilemez ama içindeki liste değişir!

veri = (1, 2, [3, 4])
veri[2][0] = 999  # ✅ Çalışır!
veri[0] = 10      # ❌ Hata!

💡 Tuple kendisi değişmez ama içindekiler değişebilir!
""")

# ============================================
# 13. Tuple'ı Listeye, Listeyi Tuple'a
# ============================================
print("\n" + "="*70)
print("📌 13. Dönüşümler")
print("-"*70)

# Tuple → Liste
tuple1 = (1, 2, 3, 4, 5)
liste1 = list(tuple1)
print(f"Tuple: {tuple1}")
print(f"Liste: {liste1}")

# Liste → Tuple
liste2 = [10, 20, 30]
tuple2 = tuple(liste2)
print(f"\nListe: {liste2}")
print(f"Tuple: {tuple2}")

# String → Tuple
metin = "Python"
tuple3 = tuple(metin)
print(f"\nString: {metin}")
print(f"Tuple: {tuple3}")

print("\n💡 list() ve tuple() fonksiyonları!")

# ============================================
# 14. Tuple İpuçları
# ============================================
print("\n" + "="*70)
print("📌 14. İpuçları ve Best Practices")
print("-"*70)

print("""
✅ Tuple Kullan:

1. Sabit veriler
   boyutlar = (1920, 1080)
   
2. Fonksiyon dönüşü
   return (min_val, max_val)
   
3. Koordinatlar
   nokta = (x, y, z)
   
4. RGB, RGBA
   renk = (255, 0, 0)
   
5. Tarih, zaman
   tarih = (2024, 4, 15)
   
6. Sözlük anahtarı
   {(0, 0): "Başlangıç"}

❌ Liste Kullan:

1. Değişken veriler
   notlar = [85, 90, 78]
   
2. Ekleme/çıkarma gerekli
   oyuncular.append('Ali')
   
3. Sıralama gerekli
   sayilar.sort()
   
4. Dinamik içerik
   mesajlar.remove(mesaj)

💡 Kurallar:
• Değişmeyecekse → Tuple
• Değişecekse → Liste
• Performans önemliyse → Tuple
• Güvenlik önemliyse → Tuple
• Tek elemanlı tuple → Virgül unutma!
• Büyük harfle sabitleri tuple yap

İsimlendirme:
✓ koordinatlar = (x, y)
✓ boyutlar = (w, h)
✓ RGB = (255, 0, 0)
✓ SABITLER = (val1, val2)
""")

# ============================================
# ÖZET
# ============================================
print("\n" + "="*70)
print("📚 TUPLES ÖZET")
print("="*70)
print("""
Tuple (Değişmez Liste):

Oluşturma:
tuple1 = (1, 2, 3)        → Normal
tuple2 = (5,)             → Tek elemanlı (virgül!)
tuple3 = ()               → Boş
tuple4 = 1, 2, 3          → Parantez opsiyonel

Erişim:
tuple1[0]      → İlk öğe
tuple1[-1]     → Son öğe
tuple1[1:3]    → Slicing

Özellikler:
✓ Değiştirilemez (immutable)
✓ Daha hızlı
✓ Daha az bellek
✓ Güvenli
✓ Sözlük anahtarı olabilir

Metodlar:
count(x)   → x kaç tane?
index(x)   → x'in indeksi?

Unpacking:
x, y = (10, 20)
a, b = b, a  # Swap

Liste vs Tuple:
[1, 2, 3]   → Değişir
(1, 2, 3)   → Değişmez

Kullanım:
✓ Koordinatlar: (x, y)
✓ RGB: (255, 0, 0)
✓ Tarih: (2024, 4, 15)
✓ Fonksiyon dönüşü
✓ Sabitler

💡 İpuçları:
• Tek elemanlı virgül unutma!
• Değişmeyecek → Tuple
• Değişecek → Liste
• Performans → Tuple
• Güvenlik → Tuple

Sırada:
→ Index hataları ve çözümleri
→ Liste ipuçları
→ Best practices
""")
print("="*70)
