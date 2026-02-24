# ========================================
# SAYILARDA ÖZEL ÖZELLİKLER
# ========================================
# Underscores, Multiple Assignment, Constants

print("="*60)
print("SAYILARDA ÖZEL ÖZELLİKLER")
print("="*60)

# ============================================
# 1. Underscores in Numbers (Alt Çizgi Kullanımı)
# ============================================
print("\n📌 1. Sayılarda Alt Çizgi (_) Kullanımı")
print("-"*60)

# Büyük sayıları daha okunabilir yapmak için alt çizgi kullanabilirsiniz
universe_age = 14_000_000_000

print(f"Evrenin yaşı: {universe_age:,} yıl")
print(f"Yazdırırken alt çizgiler kaybolur!")

# Daha fazla örnek
print("\n--- Daha Fazla Örnek ---")
milyar = 1_000_000_000
milyon = 1_000_000
bin = 1_000

print(f"1 milyar: {milyar:,}")
print(f"1 milyon: {milyon:,}")
print(f"1 bin: {bin:,}")

# Alt çizgileri istediğiniz gibi kullanabilirsiniz
print("\n--- Farklı Kullanımlar ---")
sayi1 = 1_000_000  # 3'erli grup (okunabilir)
sayi2 = 10_00_00   # Başka bir grup
sayi3 = 1000000    # Alt çizgisiz

print(f"Hepsi aynı: {sayi1} = {sayi2} = {sayi3}")
print(f"Python için fark yok!")

# Float'larda da kullanılabilir
print("\n--- Float'larda da Çalışır ---")
buyuk_ondalik = 12_345.678_9
print(f"Float: {buyuk_ondalik}")

print("\n💡 Python 3.6 ve sonrasında kullanılabilir!")
print("💡 Sadece okunabilirlik için, Python'a etkisi yok!")

# ============================================
# 2. Gerçek Hayat Örnekleri
# ============================================
print("\n" + "="*60)
print("📌 2. Gerçek Hayat Örnekleri")
print("-"*60)

# Türkiye nüfusu
turkiye_nufusu = 85_000_000
print(f"Türkiye nüfusu: {turkiye_nufusu:,} kişi")

# Araba fiyatı
araba_fiyati = 1_500_000
print(f"Araba fiyatı: {araba_fiyati:,} TL")

# Dünya nüfusu
dunya_nufusu = 8_000_000_000
print(f"Dünya nüfusu: {dunya_nufusu:,} kişi")

# Işık hızı
isik_hizi = 300_000_000  # m/s
print(f"Işık hızı: {isik_hizi:,} m/s")

# Kredi kartı numarası gibi (örnek)
kart_no = 1234_5678_9012_3456
print(f"Kart numarası: {kart_no}")

# ============================================
# 3. Multiple Assignment (Çoklu Atama)
# ============================================
print("\n" + "="*60)
print("📌 3. Multiple Assignment (Çoklu Atama)")
print("-"*60)

# Birden fazla değişkene tek satırda değer atama
x, y, z = 0, 0, 0
print(f"x = {x}, y = {y}, z = {z}")

print("\n💡 Tüm değişkenlere aynı anda değer atandı!")

# Farklı değerler atama
a, b, c = 1, 2, 3
print(f"\na = {a}, b = {b}, c = {c}")

# String'lerle de çalışır
isim, soyisim, yas = "Ali", "Kağan", 25
print(f"\nİsim: {isim}, Soyisim: {soyisim}, Yaş: {yas}")

# Karışık tipler
sayi, metin, ondalik = 100, "Merhaba", 3.14
print(f"\n{sayi}, {metin}, {ondalik}")

# ============================================
# 4. Değişken Değiştirme (Swap)
# ============================================
print("\n" + "="*60)
print("📌 4. Değişken Değiştirme (Swap)")
print("-"*60)

# Python'da çok kolay!
x, y = 10, 20
print(f"Önce: x = {x}, y = {y}")

x, y = y, x  # Swap (değiştir)
print(f"Sonra: x = {x}, y = {y}")

print("\n💡 Python'da değişken değiştirmek çok kolay!")
print("   Diğer dillerde geçici değişken gerekir.")

# ============================================
# 5. Tuple Unpacking
# ============================================
print("\n" + "="*60)
print("📌 5. Tuple Unpacking (İleri Seviye)")
print("-"*60)

# Fonksiyondan birden fazla değer döndürme
def get_koordinatlar():
    return 41.0082, 28.9784  # İstanbul koordinatları

enlem, boylam = get_koordinatlar()
print(f"İstanbul koordinatları:")
print(f"Enlem: {enlem}")
print(f"Boylam: {boylam}")

# Liste unpacking
sayilar = [1, 2, 3]
bir, iki, uc = sayilar
print(f"\nListe: {sayilar}")
print(f"Ayrıldı: {bir}, {iki}, {uc}")

# ============================================
# 6. Pratik Kullanım
# ============================================
print("\n" + "="*60)
print("📌 6. Pratik Kullanım Örnekleri")
print("-"*60)

# Örnek 1: Başlangıç değerleri
print("--- Oyun Başlangıcı ---")
skor, can, seviye = 0, 100, 1
print(f"Skor: {skor}, Can: {can}, Seviye: {seviye}")

# Örnek 2: Koordinat sistemi
print("\n--- Koordinat Noktası ---")
x, y, z = 10, 20, 30
print(f"3D Nokta: ({x}, {y}, {z})")

# Örnek 3: RGB renk
print("\n--- RGB Renk ---")
red, green, blue = 255, 0, 128
print(f"RGB: ({red}, {green}, {blue})")

# Örnek 4: Min ve Max
print("\n--- Min ve Max ---")
minimum, maksimum = 0, 100
print(f"Aralık: {minimum} - {maksimum}")

# ============================================
# 7. Hata Durumları
# ============================================
print("\n" + "="*60)
print("📌 7. ⚠️ Dikkat Edilecek Durumlar")
print("-"*60)

print("✅ DOĞRU: Değişken sayısı = Değer sayısı")
print("   a, b, c = 1, 2, 3")

print("\n❌ HATA: Eşit değilse hata verir")
print("   a, b = 1, 2, 3  # Hata!")
print("   a, b, c = 1, 2  # Hata!")

print("\n💡 Her zaman eşit sayıda olmalı!")

# Doğru kullanım gösterimi
try:
    x, y = 10, 20, 30  # 2 değişken, 3 değer
except ValueError as e:
    print(f"\n⚠️ Hata oluştu: too many values to unpack")

# ============================================
# ÖZET
# ============================================
print("\n" + "="*60)
print("📚 ÖZEL ÖZELLİKLER ÖZET")
print("="*60)
print("""
1. UNDERSCORES IN NUMBERS (Alt Çizgi):
   ✓ Büyük sayıları okunabilir yapar
   ✓ Örnek: 1_000_000 = 1000000
   ✓ Python 3.6+
   ✓ Sadece okunabilirlik için
   
2. MULTIPLE ASSIGNMENT (Çoklu Atama):
   ✓ Tek satırda birden fazla değişkene değer
   ✓ Örnek: x, y, z = 1, 2, 3
   ✓ Değişken değiştirme: x, y = y, x
   ✓ Değişken sayısı = Değer sayısı olmalı
   
💡 İpuçları:
   • Büyük sayılar için _ kullanın
   • Başlangıç değerleri için çoklu atama kullanın
   • Kod daha temiz ve okunabilir olur
""")
print("="*60)
