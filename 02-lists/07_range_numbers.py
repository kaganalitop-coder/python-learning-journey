# ========================================
# RANGE() VE SAYISAL LİSTELER
# ========================================
# Sayı dizileri oluşturma

print("="*70)
print("RANGE() VE SAYISAL LİSTELER")
print("="*70)

# ============================================
# 1. range() Nedir?
# ============================================
print("\n📌 1. range() Nedir?")
print("-"*70)

print("""
range() Fonksiyonu:
• Sayı dizileri oluşturur
• For döngülerinde kullanılır
• Bellek dostu (tüm sayıları saklamaz)
• Çok hızlıdır

Syntax:
range(start, stop, step)
• start: Başlangıç (dahil)
• stop: Bitiş (hariç!)
• step: Adım (isteğe bağlı)

💡 stop değeri dahil DEĞİL!
""")

# ============================================
# 2. Temel range() Kullanımı
# ============================================
print("\n" + "="*70)
print("📌 2. Temel range() Kullanımı")
print("-"*70)

# 1'den 5'e kadar
print("--- range(1, 5) ---")
for sayi in range(1, 5):
    print(sayi)

print("\n💡 5 yazdırılmadı! Stop değeri hariç!")

# 1'den 5'e kadar (5 dahil)
print("\n--- 1'den 5'e (5 dahil) ---")
for sayi in range(1, 6):
    print(sayi)

print("\n💡 5 dahil etmek için 6 yazmalıyız!")

# ============================================
# 3. range() Varyasyonları
# ============================================
print("\n" + "="*70)
print("📌 3. range() Varyasyonları")
print("-"*70)

# Tek argüman - 0'dan başlar
print("--- range(6) - 0'dan başlar ---")
for sayi in range(6):
    print(sayi, end=" ")
print()

# İki argüman - başlangıç ve bitiş
print("\n--- range(3, 8) ---")
for sayi in range(3, 8):
    print(sayi, end=" ")
print()

# Üç argüman - adım ile
print("\n--- range(0, 11, 2) - 2'şer ---")
for sayi in range(0, 11, 2):
    print(sayi, end=" ")
print()

print("""
Özetlersek:
range(5)        → 0, 1, 2, 3, 4
range(1, 5)     → 1, 2, 3, 4
range(1, 10, 2) → 1, 3, 5, 7, 9
""")

# ============================================
# 4. range() ile Liste Oluşturma
# ============================================
print("\n" + "="*70)
print("📌 4. range() ile Liste Oluşturma")
print("-"*70)

# list() ile listeye çevirme
sayilar = list(range(1, 6))
print(f"Liste: {sayilar}")

# Çift sayılar
cift_sayilar = list(range(2, 11, 2))
print(f"Çift sayılar: {cift_sayilar}")

# Tek sayılar
tek_sayilar = list(range(1, 11, 2))
print(f"Tek sayılar: {tek_sayilar}")

# 5'in katları
besler = list(range(0, 51, 5))
print(f"5'in katları: {besler}")

print("\n💡 list(range()) = Sayı listesi oluştur!")

# ============================================
# 5. Kareler Listesi Oluşturma
# ============================================
print("\n" + "="*70)
print("📌 5. Kareler Listesi Oluşturma")
print("-"*70)

# Uzun yol
print("--- Uzun Yol ---")
kareler = []
for sayi in range(1, 11):
    kare = sayi ** 2
    kareler.append(kare)

print(f"Kareler: {kareler}")

# Kısa yol
print("\n--- Kısa Yol ---")
kareler = []
for sayi in range(1, 11):
    kareler.append(sayi ** 2)

print(f"Kareler: {kareler}")

print("\n💡 ** operatörü üs alma için kullanılır!")
print("   5 ** 2 = 25")
print("   2 ** 3 = 8")

# ============================================
# 6. Sayılarla İstatistikler
# ============================================
print("\n" + "="*70)
print("📌 6. Liste İstatistikleri: min(), max(), sum()")
print("-"*70)

sayilar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(f"Sayılar: {sayilar}")

# Temel fonksiyonlar
print(f"\nEn küçük: {min(sayilar)}")
print(f"En büyük: {max(sayilar)}")
print(f"Toplam: {sum(sayilar)}")
print(f"Ortalama: {sum(sayilar) / len(sayilar):.2f}")

# Büyük listelerle
buyuk_liste = list(range(1, 1001))
print(f"\n1-1000 arası sayılar:")
print(f"En küçük: {min(buyuk_liste)}")
print(f"En büyük: {max(buyuk_liste)}")
print(f"Toplam: {sum(buyuk_liste):,}")
print(f"Ortalama: {sum(buyuk_liste) / len(buyuk_liste):.2f}")

print("\n💡 Milyonlarca sayı ile bile çalışır!")

# ============================================
# 7. Pratik Örnekler
# ============================================
print("\n" + "="*70)
print("📌 7. Pratik Örnekler")
print("-"*70)

# Örnek 1: 1-20 arası sayılar
print("--- 1'den 20'ye Kadar ---")
for sayi in range(1, 21):
    print(sayi, end=" ")
print()

# Örnek 2: 1-100 arası tek sayılar
print("\n--- 1-100 Arası Tek Sayılar (İlk 10) ---")
tek_sayilar = list(range(1, 100, 2))
print(tek_sayilar[:10])
print(f"... toplam {len(tek_sayilar)} sayı")

# Örnek 3: 3'ün katları
print("\n--- 3'ün Katları (3-30) ---")
ucun_katlari = list(range(3, 31, 3))
print(ucun_katlari)

# Örnek 4: Küpler
print("\n--- İlk 10 Sayının Küpleri ---")
kupler = []
for sayi in range(1, 11):
    kupler.append(sayi ** 3)

print(kupler)

# ============================================
# 8. Büyük Sayılarla Çalışma
# ============================================
print("\n" + "="*70)
print("📌 8. Büyük Sayılarla Çalışma")
print("-"*70)

# 1 milyon sayı
print("--- 1 Milyon Sayı ---")
milyon = list(range(1, 1_000_001))
print(f"Liste uzunluğu: {len(milyon):,}")
print(f"İlk 5: {milyon[:5]}")
print(f"Son 5: {milyon[-5:]}")
print(f"En küçük: {min(milyon):,}")
print(f"En büyük: {max(milyon):,}")
print(f"Toplam: {sum(milyon):,}")

print("\n💡 Python milyonlarca sayıyı saniyeler içinde işler!")

# ============================================
# 9. Ters Sıralı range()
# ============================================
print("\n" + "="*70)
print("📌 9. Ters Sıralı range()")
print("-"*70)

# 10'dan 1'e
print("--- Geri Sayım ---")
for sayi in range(10, 0, -1):
    print(sayi, end=" ")
print("🚀")

# 20'den 0'a (2'şer)
print("\n--- 20'den 0'a (2'şer) ---")
for sayi in range(20, -1, -2):
    print(sayi, end=" ")
print()

print("\n💡 Negatif step ile geriye gidebilirsiniz!")

# ============================================
# 10. range() ile Indeksleme
# ============================================
print("\n" + "="*70)
print("📌 10. range() ile İndeksleme")
print("-"*70)

# Liste indekslerini döndürme
meyveler = ['elma', 'armut', 'muz', 'çilek']
print(f"Meyveler: {meyveler}")

print("\n--- İndeks ile Erişim ---")
for i in range(len(meyveler)):
    print(f"İndeks {i}: {meyveler[i]}")

# Daha iyi yol: enumerate()
print("\n--- enumerate() ile (Daha İyi) ---")
for i, meyve in enumerate(meyveler):
    print(f"İndeks {i}: {meyve}")

print("\n💡 İndekse ihtiyacınız varsa enumerate() kullanın!")

# ============================================
# 11. range() Bellek Verimliliği
# ============================================
print("\n" + "="*70)
print("📌 11. range() Bellek Verimliliği")
print("-"*70)

print("""
range() Neden Hızlı?

Liste Oluşturma:
liste = [1, 2, 3, ..., 1000000]
→ 1 milyon sayıyı bellekte tutar
→ Çok bellek kullanır

range() Kullanma:
for i in range(1, 1000001):
→ Sadece gerekli sayıyı üretir
→ Az bellek kullanır
→ Çok hızlıdır!

💡 range() bir generator'dır!
   Sayıları lazım oldukça üretir.
""")

# Boyut karşılaştırması
import sys

liste = list(range(100000))
range_obj = range(100000)

print(f"\nListe boyutu: {sys.getsizeof(liste):,} bytes")
print(f"range() boyutu: {sys.getsizeof(range_obj):,} bytes")
print(f"Fark: {sys.getsizeof(liste) // sys.getsizeof(range_obj)}x daha az!")

# ============================================
# 12. range() ile Matematiksel İşlemler
# ============================================
print("\n" + "="*70)
print("📌 12. Matematiksel İşlemler")
print("-"*70)

# Faktöriyel hesaplama
print("--- 5! (Faktöriyel) ---")
faktöriyel = 1
for sayi in range(1, 6):
    faktöriyel *= sayi
    print(f"{sayi}! = {faktöriyel}")

# Fibonacci dizisi
print("\n--- Fibonacci (İlk 10) ---")
fib = [0, 1]
for i in range(8):
    fib.append(fib[-1] + fib[-2])
print(fib)

# Toplam formülü doğrulama
print("\n--- Gauss Formülü Doğrulama ---")
n = 100
toplam_dongü = sum(range(1, n + 1))
toplam_formul = n * (n + 1) // 2
print(f"Döngü ile: {toplam_dongü:,}")
print(f"Formül ile: {toplam_formul:,}")
print(f"Eşit mi? {toplam_dongü == toplam_formul}")

# ============================================
# 13. range() Hataları
# ============================================
print("\n" + "="*70)
print("📌 13. ⚠️ Yaygın Hatalar")
print("-"*70)

print("""
HATA 1: Stop Değeri Dahil Sanmak
❌ range(1, 5) → 1, 2, 3, 4 (5 YOK!)
✅ range(1, 6) → 1, 2, 3, 4, 5

HATA 2: Float Kullanmak
❌ range(1.5, 5.5) → HATA!
✅ range(2, 6) → Sadece int

HATA 3: Ters Sıralama
❌ range(10, 1) → Boş! (adım +1)
✅ range(10, 0, -1) → 10'dan 1'e

HATA 4: Büyükten Küçüğe (Pozitif Step)
❌ range(10, 1, 2) → Boş!
✅ range(10, 0, -2) → Çalışır

💡 Stop değeri her zaman hariç!
💡 Sadece integer kullan!
💡 Ters için negatif step!
""")

# ============================================
# 14. İleri Seviye Örnekler
# ============================================
print("\n" + "="*70)
print("📌 14. İleri Seviye Örnekler")
print("-"*70)

# Örnek 1: Asal sayılar (basit)
print("--- Asal Sayılar (2-50) ---")
asallar = []
for sayi in range(2, 51):
    asal_mi = True
    for bolen in range(2, int(sayi ** 0.5) + 1):
        if sayi % bolen == 0:
            asal_mi = False
            break
    if asal_mi:
        asallar.append(sayi)

print(asallar)
print(f"Toplam {len(asallar)} asal sayı")

# Örnek 2: Çarpım tablosu
print("\n--- Çarpım Tablosu (5x5) ---")
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i}x{j}={i*j:2}", end="  ")
    print()

# Örnek 3: Piramit
print("\n--- Yıldız Piramidi ---")
for i in range(1, 6):
    print("*" * i)

# ============================================
# ÖZET
# ============================================
print("\n" + "="*70)
print("📚 RANGE() VE SAYISAL LİSTELER ÖZET")
print("="*70)
print("""
range() Fonksiyonu:

Syntax:
range(stop)              → 0'dan stop'a (hariç)
range(start, stop)       → start'tan stop'a (hariç)
range(start, stop, step) → Adımlı

Örnekler:
range(5)          → 0, 1, 2, 3, 4
range(1, 6)       → 1, 2, 3, 4, 5
range(0, 11, 2)   → 0, 2, 4, 6, 8, 10
range(10, 0, -1)  → 10, 9, 8, ..., 1

Liste Oluşturma:
list(range(1, 6))  → [1, 2, 3, 4, 5]

İstatistikler:
min(liste)   → En küçük
max(liste)   → En büyük
sum(liste)   → Toplam
len(liste)   → Uzunluk

Özellikler:
✓ Bellek verimli
✓ Çok hızlı
✓ Milyonlarla çalışır
✓ Generator (lazım oldukça üretir)

Dikkat:
✗ stop dahil DEĞİL!
✗ Sadece integer
✗ Ters için negatif step
✗ Float kullanılamaz

Üs Alma:
2 ** 3  = 8   (2 üzeri 3)
5 ** 2  = 25  (5 üzeri 2)
10 ** 6 = 1000000

💡 İpuçları:
• range() for döngüsü ile kullan
• Liste lazımsa list(range())
• Bellek için range() tercih et
• Büyük sayılardan korkma!

Sırada:
→ List comprehensions
→ Tek satırda liste oluşturma
→ Gelişmiş liste işlemleri
""")
print("="*70)
