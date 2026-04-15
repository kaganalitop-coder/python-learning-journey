# ========================================
# FOR DÖNGÜLERI (FOR LOOPS)
# ========================================
# Liste üzerinde döngü ve indentation

print("="*70)
print("FOR DÖNGÜLERI (FOR LOOPS)")
print("="*70)

# ============================================
# 1. For Döngüsü Nedir?
# ============================================
print("\n📌 1. For Döngüsü Nedir?")
print("-"*70)

print("""
For Döngüsü:
• Bir listedeki her öğe üzerinde işlem yapma
• Tekrarlayan işlemleri otomatikleştirme
• Liste boyutu önemli değil (3 öğe veya 1 milyon)
• Python otomatik olarak yönetir

Syntax:
for öğe in liste:
    işlem_yap()

💡 Döngü = Bilgisayarın tekrarlayan işleri otomasyonu!
""")

# ============================================
# 2. İlk For Döngüsü
# ============================================
print("\n" + "="*70)
print("📌 2. İlk For Döngüsü")
print("-"*70)

# Basit örnek
print("--- Sihirbazlar Listesi ---")
sihirbazlar = ['alice', 'david', 'carolina']

for sihirbaz in sihirbazlar:
    print(sihirbaz)

print("\n💡 Her sihirbaz için print() çalıştı!")

# Türkçe örnek
print("\n--- Türkçe Örnek ---")
ogrenciler = ['Ali', 'Ayşe', 'Mehmet', 'Zeynep']

for ogrenci in ogrenciler:
    print(ogrenci)

# ============================================
# 3. Döngü Nasıl Çalışır?
# ============================================
print("\n" + "="*70)
print("📌 3. Döngü Nasıl Çalışır?")
print("-"*70)

print("""
Adım Adım:

1. Python listeden ilk öğeyi alır
   → sihirbaz = 'alice'
   
2. İçerideki kodu çalıştırır
   → print('alice')
   
3. Listede başka öğe var mı kontrol eder
   → Evet, 'david' var
   
4. İkinci öğeyi alır ve tekrarlar
   → sihirbaz = 'david'
   → print('david')
   
5. Liste bitene kadar devam eder

💡 1 milyon öğe olsa bile aynı şekilde çalışır!
""")

# Görsel örnek
meyveler = ['elma', 'armut', 'muz']
print(f"Liste: {meyveler}\n")

print("Döngü çalışıyor:")
for meyve in meyveler:
    print(f"  → Şimdi işlenen: {meyve}")

# ============================================
# 4. Anlamlı Değişken İsimleri
# ============================================
print("\n" + "="*70)
print("📌 4. Anlamlı Değişken İsimleri")
print("-"*70)

print("""
İyi Örnekler:

for cat in cats:          # Kediler listesi
for dog in dogs:          # Köpekler listesi
for item in items:        # Genel öğeler
for student in students:  # Öğrenciler
for book in books:        # Kitaplar

Kötü Örnekler:

for x in cats:            # x ne anlama geliyor?
for i in students:        # i tekil değil
for thing in books:       # thing çok genel

💡 Liste çoğul, döngü değişkeni tekil olmalı!
""")

# Pratik örnekler
print("\n--- İyi İsimlendirme Örnekleri ---")

kediler = ['Pamuk', 'Tekir', 'Minnoş']
for kedi in kediler:
    print(f"  {kedi} miyavladı!")

arabalar = ['BMW', 'Audi', 'Toyota']
for araba in arabalar:
    print(f"  {araba} hızlı bir arabadır.")

# ============================================
# 5. Döngü İçinde İşlemler
# ============================================
print("\n" + "="*70)
print("📌 5. Döngü İçinde İşlemler")
print("-"*70)

# Basit mesaj
print("--- Basit Mesajlar ---")
sihirbazlar = ['alice', 'david', 'carolina']

for sihirbaz in sihirbazlar:
    print(f"{sihirbaz.title()}, harika bir numaraydı!")

# Çok satırlı işlemler
print("\n--- Çok Satırlı İşlemler ---")
sihirbazlar = ['alice', 'david', 'carolina']

for sihirbaz in sihirbazlar:
    print(f"{sihirbaz.title()}, harika bir numaraydı!")
    print(f"Bir sonraki numaranı merakla bekliyorum, {sihirbaz.title()}.\n")

print("💡 Girintili her satır, her öğe için tekrarlanır!")

# ============================================
# 6. Döngü Sonrası İşlemler
# ============================================
print("\n" + "="*70)
print("📌 6. Döngü Sonrası İşlemler")
print("-"*70)

# Döngüden sonra tek sefer çalışan kod
sihirbazlar = ['alice', 'david', 'carolina']

for sihirbaz in sihirbazlar:
    print(f"{sihirbaz.title()}, harika bir numaraydı!")
    print(f"Bir sonraki numaranı merakla bekliyorum, {sihirbaz.title()}.\n")

# Bu satır girintili DEĞİL - döngü dışında
print("Herkese teşekkürler. Harika bir gösteriydi!")

print("\n💡 Girintili OLMAYAN satır sadece bir kez çalışır!")

# ============================================
# 7. Indentation (Girinti) Nedir?
# ============================================
print("\n" + "="*70)
print("📌 7. Indentation (Girinti) Nedir?")
print("-"*70)

print("""
Indentation = Girintileme:
• Python kodun yapısını girintilerle anlar
• Hangi kod döngü içinde?
• Hangi kod döngü dışında?
• 4 boşluk (space) standart

Doğru Kullanım:

for item in items:
    print(item)      # 4 boşluk - döngü içinde
    do_something()   # 4 boşluk - döngü içinde
print("Done!")       # 0 boşluk - döngü dışında

💡 Python diğer dillerden farklı - { } yok, girinti var!
""")

# ============================================
# 8. Girinti Hataları
# ============================================
print("\n" + "="*70)
print("📌 8. ⚠️ Yaygın Girinti Hataları")
print("-"*70)

print("""
HATA 1: Girintiyi Unutmak
❌ YANLIŞ:
for item in items:
print(item)          # Hata! Girintili olmalı

✅ DOĞRU:
for item in items:
    print(item)      # 4 boşluk


HATA 2: Bazı Satırları Unutmak
❌ YANLIŞ:
for item in items:
    print(item)
print("Next!")       # Döngü dışında (istemeden!)

✅ DOĞRU:
for item in items:
    print(item)
    print("Next!")   # Döngü içinde


HATA 3: Gereksiz Girinti
❌ YANLIŞ:
message = "Hello"
    print(message)   # Gereksiz girinti!

✅ DOĞRU:
message = "Hello"
print(message)       # Girinti yok


HATA 4: Döngü Sonrası Yanlış Girinti
❌ YANLIŞ:
for item in items:
    print(item)
    print("Done!")   # Her seferinde yazdırır!

✅ DOĞRU:
for item in items:
    print(item)
print("Done!")       # Bir kez yazdırır


HATA 5: İki Nokta Üst Üste (:) Unutmak
❌ YANLIŞ:
for item in items
    print(item)      # Syntax Error!

✅ DOĞRU:
for item in items:
    print(item)
""")

# ============================================
# 9. Hata Örnekleri (Çalışan Kod)
# ============================================
print("\n" + "="*70)
print("📌 9. Hata Örnekleri (Düzeltilmiş)")
print("-"*70)

# Örnek 1: Doğru kullanım
print("--- Doğru Kullanım ---")
sayilar = [1, 2, 3]
for sayi in sayilar:
    print(f"Sayı: {sayi}")
    print(f"Karesi: {sayi ** 2}\n")

# Örnek 2: Döngü sonrası işlem
print("--- Döngü Sonrası İşlem ---")
toplam = 0
sayilar = [1, 2, 3, 4, 5]

for sayi in sayilar:
    toplam += sayi
    print(f"  Şu anki toplam: {toplam}")

print(f"\nNihai toplam: {toplam}")

# ============================================
# 10. Pratik Örnekler
# ============================================
print("\n" + "="*70)
print("📌 10. Pratik Örnekler")
print("-"*70)

# Örnek 1: Kareler
print("--- Sayıların Kareleri ---")
sayilar = [1, 2, 3, 4, 5]

for sayi in sayilar:
    kare = sayi ** 2
    print(f"{sayi} sayısının karesi: {kare}")

# Örnek 2: Fiyat hesaplama
print("\n--- KDV Hesaplama ---")
fiyatlar = [100, 200, 150, 300]

for fiyat in fiyatlar:
    kdv = fiyat * 0.20
    toplam = fiyat + kdv
    print(f"{fiyat} TL + KDV = {toplam} TL")

# Örnek 3: Öğrenci notları
print("\n--- Öğrenci Durumu ---")
notlar = [85, 92, 65, 78, 45, 90]

for not_ in notlar:
    if not_ >= 60:
        print(f"{not_} → Geçti ✅")
    else:
        print(f"{not_} → Kaldı ❌")

# Örnek 4: Liste oluşturma
print("\n--- Çift Sayıları Bulma ---")
sayilar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
cift_sayilar = []

for sayi in sayilar:
    if sayi % 2 == 0:
        cift_sayilar.append(sayi)

print(f"Çift sayılar: {cift_sayilar}")

# ============================================
# 11. İç İçe Döngüler
# ============================================
print("\n" + "="*70)
print("📌 11. İç İçe Döngüler (Nested Loops)")
print("-"*70)

print("--- Çarpım Tablosu ---")
for i in [1, 2, 3]:
    for j in [1, 2, 3]:
        print(f"{i} x {j} = {i * j}")
    print()  # Boş satır

# Matris yazdırma
print("--- Matris Yazdırma ---")
matris = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for satir in matris:
    for eleman in satir:
        print(eleman, end=" ")
    print()

# ============================================
# 12. enumerate() ile İndeks
# ============================================
print("\n" + "="*70)
print("📌 12. enumerate() ile İndeks")
print("-"*70)

# enumerate() kullanımı
print("--- Sıralı Liste ---")
meyveler = ['elma', 'armut', 'muz', 'çilek']

for indeks, meyve in enumerate(meyveler):
    print(f"{indeks + 1}. {meyve}")

# Sıfırdan başlatma
print("\n--- Sıfırdan Başlayan İndeks ---")
for indeks, meyve in enumerate(meyveler):
    print(f"İndeks {indeks}: {meyve}")

# 1'den başlatma
print("\n--- 1'den Başlatma ---")
for indeks, meyve in enumerate(meyveler, 1):
    print(f"{indeks}. {meyve}")

# ============================================
# 13. İpuçları ve Best Practices
# ============================================
print("\n" + "="*70)
print("📌 13. İpuçları ve Best Practices")
print("-"*70)

print("""
✅ YAPILMASI GEREKENLER:

1. Anlamlı değişken isimleri kullan
   for student in students: ✓
   
2. 4 boşluk girinti kullan
   Tab tuşuna bas (editor 4 boşluk ekler)
   
3. İki nokta üst üste koy
   for item in items:
   
4. Döngü içi/dışı net olmalı
   Hangi kod tekrarlanmalı?
   
5. Uzun döngülerde yorum yaz
   # Her öğrenci için not hesapla

❌ YAPILMAMASI GEREKENLER:

1. Anlamsız isimler kullanma
   for x in students: ✗
   
2. Girintiyi unutma
   Syntax hatası!
   
3. İki nokta üst üste unutma
   Syntax hatası!
   
4. Her satırı girintileme
   Sadece döngü içi kod!
   
5. Tab ve space karıştırma
   Sadece space kullan!

💡 Editor'ünüzü doğru ayarlayın:
• Tab → 4 space
• Görsel girinti rehberi
• Auto-indent aktif
""")

# ============================================
# 14. Performans İpuçları
# ============================================
print("\n" + "="*70)
print("📌 14. Performans İpuçları")
print("-"*70)

print("""
Döngüler Hızlıdır:
• 1 milyon öğe → Saniyeler içinde
• Python optimize edilmiştir
• Liste boyutundan korkmayın

Yavaşlatan Şeyler:
• Her iterasyonda dosya okuma
• Her iterasyonda veritabanı sorgusu
• Karmaşık hesaplamalar

Hızlandırma:
• Döngü dışında hazırlık yap
• Gereksiz işlem yapma
• Yerleşik fonksiyonları kullan
""")

# Performans örneği
print("\n--- Performans Örneği ---")
import time

# Yavaş yol
start = time.time()
sonuc = []
for i in range(100000):
    sonuc.append(i * 2)
yavas = time.time() - start

# Hızlı yol (list comprehension)
start = time.time()
sonuc = [i * 2 for i in range(100000)]
hizli = time.time() - start

print(f"Döngü ile: {yavas:.4f} saniye")
print(f"Comprehension ile: {hizli:.4f} saniye")
print(f"Fark: {(yavas/hizli):.2f}x daha hızlı")

# ============================================
# ÖZET
# ============================================
print("\n" + "="*70)
print("📚 FOR DÖNGÜLERI ÖZET")
print("="*70)
print("""
For Döngüsü:

Syntax:
for öğe in liste:
    işlem_yap()      # 4 boşluk girinti
    başka_işlem()    # 4 boşluk girinti
print("Bitti!")      # Girinti yok

Özellikler:
✓ Liste boyutu önemli değil
✓ Otomatik yönetim
✓ Temiz ve okunabilir
✓ Pythonic

Girinti (Indentation):
✓ 4 boşluk standart
✓ Döngü içi kod girintili
✓ Döngü dışı kod girintisiz
✓ Tab → 4 space ayarla

Yaygın Hatalar:
✗ Girintiyi unutmak
✗ : (iki nokta üst üste) unutmak
✗ Yanlış girintileme
✗ Tab ve space karıştırma

İsimlendirme:
✓ for cat in cats         (tekil in çoğul)
✓ for student in students
✓ for item in items

Yararlı:
✓ enumerate() - İndeks ile
✓ İç içe döngüler
✓ break ve continue (ileriki ders)

💡 İpuçları:
• Her zaman 4 boşluk
• Anlamlı isimler
• Döngü dışı kodu girinti yapma
• Editor'ü doğru ayarla
• Pratik yap!

Sırada:
→ range() fonksiyonu
→ Sayısal listeler
→ List comprehensions
""")
print("="*70)
