# ========================================
# LİSTE DİLİMLEME (SLICING)
# ========================================
# Listenin bir bölümünü alma

print("="*70)
print("LİSTE DİLİMLEME (SLICING)")
print("="*70)

# ============================================
# 1. Slicing Nedir?
# ============================================
print("\n📌 1. Slicing (Dilimleme) Nedir?")
print("-"*70)

print("""
Slicing:
• Listenin bir bölümünü alma
• Yeni bir liste oluşturur
• Orijinali değiştirmez
• Syntax: liste[başlangıç:bitiş:adım]

Format:
liste[start:stop:step]
• start: Başlangıç indeksi (dahil)
• stop: Bitiş indeksi (hariç!)
• step: Adım sayısı (isteğe bağlı)

💡 stop indeksi dahil DEĞİL!
""")

# ============================================
# 2. Temel Slicing
# ============================================
print("\n" + "="*70)
print("📌 2. Temel Slicing")
print("-"*70)

# İlk 3 öğe
oyuncular = ['Ali', 'Ayşe', 'Mehmet', 'Zeynep', 'Can']
print(f"Tüm liste: {oyuncular}")

ilk_3 = oyuncular[0:3]
print(f"İlk 3: {ilk_3}")

# Orta 3 öğe
orta_3 = oyuncular[1:4]
print(f"Orta 3: {orta_3}")

# Son 3 öğe
son_3 = oyuncular[2:5]
print(f"Son 3: {son_3}")

print("\n💡 [0:3] = indeks 0, 1, 2 (3 dahil değil!)")

# ============================================
# 3. Kısa Yollar (Shortcuts)
# ============================================
print("\n" + "="*70)
print("📌 3. Kısa Yollar")
print("-"*70)

sayilar = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"Liste: {sayilar}")

# Baştan itibaren
print(f"\n[:5]   = {sayilar[:5]}")    # İlk 5
print(f"[:3]   = {sayilar[:3]}")    # İlk 3

# Belirli noktadan sona
print(f"\n[5:]   = {sayilar[5:]}")   # 5'ten sona
print(f"[7:]   = {sayilar[7:]}")   # 7'den sona

# Tümü (kopya)
print(f"\n[:]    = {sayilar[:]}")    # Tüm liste (kopya)

print("""
Kısa Yollar:
[:n]   → İlk n öğe
[n:]   → n'den sona
[:]    → Tüm liste (kopya)
[-n:]  → Son n öğe
[:-n]  → Son n hariç
""")

# ============================================
# 4. Negatif İndekslerle Slicing
# ============================================
print("\n" + "="*70)
print("📌 4. Negatif İndekslerle Slicing")
print("-"*70)

meyveler = ['elma', 'armut', 'muz', 'çilek', 'üzüm']
print(f"Meyveler: {meyveler}")

# Son 3 öğe
son_3 = meyveler[-3:]
print(f"\nSon 3 [-3:]: {son_3}")

# Son 2 öğe
son_2 = meyveler[-2:]
print(f"Son 2 [-2:]: {son_2}")

# Son öğe hariç
son_haric = meyveler[:-1]
print(f"Son hariç [:-1]: {son_haric}")

# Son 2 hariç
son_2_haric = meyveler[:-2]
print(f"Son 2 hariç [:-2]: {son_2_haric}")

print("\n💡 Negatif indeks sondan başlar!")

# ============================================
# 5. Step (Adım) Kullanımı
# ============================================
print("\n" + "="*70)
print("📌 5. Step (Adım) Kullanımı")
print("-"*70)

sayilar = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"Sayılar: {sayilar}")

# 2'şer atlayarak
ikiser = sayilar[::2]
print(f"\n2'şer atlayarak [::2]: {ikiser}")

# 3'er atlayarak
ucser = sayilar[::3]
print(f"3'er atlayarak [::3]: {ucser}")

# Belirli aralıkta 2'şer
aralik = sayilar[2:8:2]
print(f"2-8 arası 2'şer [2:8:2]: {aralik}")

# Tersten (negatif step)
tersten = sayilar[::-1]
print(f"Tersten [::-1]: {tersten}")

print("""
Step Örnekleri:
[::2]    → 2'şer atlayarak
[::3]    → 3'er atlayarak
[::-1]   → Tersten tümü
[2:8:2]  → 2-8 arası 2'şer
""")

# ============================================
# 6. Pratik Örnekler
# ============================================
print("\n" + "="*70)
print("📌 6. Pratik Örnekler")
print("-"*70)

# Örnek 1: İlk 3 ve Son 3
print("--- İlk 3 ve Son 3 Ürün ---")
urunler = ['Ürün1', 'Ürün2', 'Ürün3', 'Ürün4', 'Ürün5', 'Ürün6', 'Ürün7']
print(f"Tüm ürünler: {urunler}")

ilk_3 = urunler[:3]
son_3 = urunler[-3:]
print(f"İlk 3: {ilk_3}")
print(f"Son 3: {son_3}")

# Örnek 2: Takımları Ayırma
print("\n--- Takım Bölme ---")
oyuncular = ['O1', 'O2', 'O3', 'O4', 'O5', 'O6', 'O7', 'O8']
print(f"Tüm oyuncular: {oyuncular}")

takim1 = oyuncular[:len(oyuncular)//2]
takim2 = oyuncular[len(oyuncular)//2:]
print(f"Takım 1: {takim1}")
print(f"Takım 2: {takim2}")

# Örnek 3: Sayfalama
print("\n--- Sayfalama ---")
tum_kayitlar = list(range(1, 51))  # 1-50 arası kayıtlar
print(f"Toplam {len(tum_kayitlar)} kayıt")

sayfa_basina = 10
sayfa_1 = tum_kayitlar[0:10]
sayfa_2 = tum_kayitlar[10:20]
sayfa_3 = tum_kayitlar[20:30]

print(f"Sayfa 1: {sayfa_1}")
print(f"Sayfa 2: {sayfa_2}")
print(f"Sayfa 3: {sayfa_3}")

# Örnek 4: Tek ve Çift İndeksler
print("\n--- Tek ve Çift İndeksler ---")
harfler = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
print(f"Harfler: {harfler}")

cift_indeksler = harfler[::2]  # 0, 2, 4, 6
tek_indeksler = harfler[1::2]  # 1, 3, 5, 7
print(f"Çift indeksler (0,2,4...): {cift_indeksler}")
print(f"Tek indeksler (1,3,5...): {tek_indeksler}")

# ============================================
# 7. Slicing ile Kopyalama
# ============================================
print("\n" + "="*70)
print("📌 7. Slicing ile Kopyalama")
print("-"*70)

# [:] ile tam kopya
orijinal = [1, 2, 3, 4, 5]
kopya = orijinal[:]  # Tam kopya

print(f"Orijinal: {orijinal}")
print(f"Kopya: {kopya}")

kopya[0] = 999
print(f"\nKopya değişti: {kopya}")
print(f"Orijinal aynı: {orijinal}")

print("\n💡 [:] tam bir kopya oluşturur!")
print("   orijinal.copy() ile aynı!")

# Yanlış yol
print("\n--- ❌ Yanlış Kopyalama ---")
liste1 = [1, 2, 3]
liste2 = liste1  # Referans kopyası!

liste2[0] = 999
print(f"Liste1: {liste1}")  # İkisi de değişti!
print(f"Liste2: {liste2}")

# ============================================
# 8. Döngülerle Slicing
# ============================================
print("\n" + "="*70)
print("📌 8. Döngülerle Slicing")
print("-"*70)

# İlk 3 oyuncuyu yazdır
print("--- İlk 3 Oyuncu ---")
oyuncular = ['Ali', 'Ayşe', 'Mehmet', 'Zeynep', 'Can']

for oyuncu in oyuncular[:3]:
    print(f"  Oyuncu: {oyuncu}")

# Son 2 öğrenci
print("\n--- Son 2 Öğrenci ---")
ogrenciler = ['Öğr1', 'Öğr2', 'Öğr3', 'Öğr4', 'Öğr5']

for ogrenci in ogrenciler[-2:]:
    print(f"  Öğrenci: {ogrenci}")

# Her 2. öğe
print("\n--- Her 2. Öğe ---")
sayilar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for sayi in sayilar[::2]:
    print(f"  Sayı: {sayi}")

# ============================================
# 9. İleri Seviye Slicing
# ============================================
print("\n" + "="*70)
print("📌 9. İleri Seviye Slicing")
print("-"*70)

# Palindrome kontrolü (slicing ile)
kelime = "radar"
tersi = kelime[::-1]
print(f"Kelime: {kelime}")
print(f"Tersi: {tersi}")
print(f"Palindrome mu? {kelime == tersi}")

# String'i tersine çevirme
metin = "Python"
ters_metin = metin[::-1]
print(f"\n'{metin}' tersine: '{ters_metin}'")

# Her 2. karakteri alma
cumle = "Merhaba Dünya"
her_ikinci = cumle[::2]
print(f"\n'{cumle}'")
print(f"Her 2. karakter: '{her_ikinci}'")

# Liste ortası
print("\n--- Liste Ortası ---")
sayilar = [1, 2, 3, 4, 5, 6, 7, 8, 9]
orta = len(sayilar) // 2
orta_kısım = sayilar[orta-1:orta+2]
print(f"Liste: {sayilar}")
print(f"Orta kısım: {orta_kısım}")

# ============================================
# 10. Slicing Hataları ve İpuçları
# ============================================
print("\n" + "="*70)
print("📌 10. ⚠️ Slicing İpuçları")
print("-"*70)

print("""
Yaygın Hatalar:

1. Bitiş indeksi dahil değil!
   liste[0:3] → 0, 1, 2 (3 değil!)
   
2. İndeks aşımı hata vermez:
   liste[:100] → Varsa kadar alır
   
3. Negatif step dikkat:
   liste[2:5:-1] → Boş liste! (mantık hatası)
   liste[5:2:-1] → Doğru yön
   
4. Orijinal değişmez:
   dilim = liste[2:5]
   dilim[0] = 999  # Sadece dilim değişir!

💡 İpuçları:
• [:] ile tam kopya
• [::-1] ile tersine çevir
• [::2] ile 2'şer atla
• İndeks aşımı hata vermez (güvenli)
• stop dahil DEĞİL!
• Orijinali değiştirmez
""")

# Örnekler
print("\n--- İndeks Aşımı ---")
liste = [1, 2, 3, 4, 5]
print(f"Liste: {liste}")
print(f"[:100]: {liste[:100]}")  # Hata vermez!
print(f"[10:20]: {liste[10:20]}")  # Boş liste

# ============================================
# ÖZET
# ============================================
print("\n" + "="*70)
print("📚 LİSTE DİLİMLEME ÖZET")
print("="*70)
print("""
Slicing Syntax:
liste[start:stop:step]

Temel Kullanım:
✓ [0:3]   : İlk 3 öğe (0,1,2)
✓ [2:5]   : 2,3,4 indeksleri
✓ [:3]    : İlk 3
✓ [3:]    : 3'ten sona
✓ [:]     : Tüm liste (kopya)

Negatif İndeks:
✓ [-3:]   : Son 3
✓ [:-3]   : Son 3 hariç
✓ [-5:-2] : Sondan 5 ile 2 arası

Step Kullanımı:
✓ [::2]   : 2'şer atlayarak
✓ [::3]   : 3'er atlayarak
✓ [::-1]  : Tersten
✓ [1::2]  : 1'den başla, 2'şer atla

Pratik Kullanım:
✓ İlk n: [:n]
✓ Son n: [-n:]
✓ Kopya: [:]
✓ Ters: [::-1]
✓ Çift indeks: [::2]
✓ Tek indeks: [1::2]

💡 Önemli:
• stop indeksi dahil DEĞİL!
• İndeks aşımı hata vermez
• Orijinali değiştirmez
• Yeni liste döndürür

Sırada:
→ Liste comprehension
→ Liste birleştirme
→ İleri seviye işlemler
""")
print("="*70)
