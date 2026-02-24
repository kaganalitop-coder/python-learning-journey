# ========================================
# FLOATS (ONDALIKLI SAYILAR)
# ========================================

# Float = Ondalık noktalı sayılar (3.14, 0.5, 2.0)

print("="*60)
print("FLOATS (ONDALIKLI SAYILAR)")
print("="*60)

# ============================================
# 1. Float Nedir?
# ============================================
print("\n📌 1. Float Nedir?")
print("-"*60)

print("Float = Ondalık noktalı sayılar")
print("\nÖrnekler:")
print(f"3.14")
print(f"0.5")
print(f"2.0")
print(f"0.1")

print("\n💡 Ondalık nokta sayının herhangi bir yerinde olabilir!")

# ============================================
# 2. Temel Float İşlemleri
# ============================================
print("\n" + "="*60)
print("📌 2. Temel Float İşlemleri")
print("-"*60)

print(f"0.1 + 0.1 = {0.1 + 0.1}")
print(f"0.2 + 0.2 = {0.2 + 0.2}")
print(f"2 * 0.1 = {2 * 0.1}")
print(f"2 * 0.2 = {2 * 0.2}")

print("\n💡 Çoğu durumda beklediğiniz sonucu alırsınız!")

# ============================================
# 3. Float'ların Garip Davranışı
# ============================================
print("\n" + "="*60)
print("📌 3. ⚠️ Float'ların Garip Davranışı")
print("-"*60)

print(f"0.2 + 0.1 = {0.2 + 0.1}")
print(f"3 * 0.1 = {3 * 0.1}")

print("\n⚠️ Neden 0.30000000000000004 gibi garip bir sonuç?")
print("""
Sebep: Bilgisayarlar ondalık sayıları binary (ikili sayı sistemi) 
       ile saklar. Bazı sayılar binary'de tam olarak temsil edilemez.

💡 Endişelenmeyin! 
   • Bu tüm programlama dillerinde olur
   • Çoğu durumda sorun olmaz
   • İleriki bölümlerde nasıl düzelteceğinizi öğreneceksiniz
   • Şimdilik ekstra basamakları görmezden gelin
""")

# ============================================
# 4. Integer ve Float Karışımı
# ============================================
print("\n" + "="*60)
print("📌 4. Integer ve Float Karışımı")
print("-"*60)

print("İki integer'ı bölerseniz, float alırsınız:")
print(f"4 / 2 = {4 / 2}")
print(f"Type: {type(4 / 2)}")

print("\nInteger ve float karıştırırsanız, sonuç float olur:")
print(f"1 + 2.0 = {1 + 2.0}")
print(f"2 * 3.0 = {2 * 3.0}")
print(f"3.0 ** 2 = {3.0 ** 2}")

print("\n💡 Herhangi bir işlemde float varsa, sonuç float olur!")

# ============================================
# 5. Float Detaylı Örnekler
# ============================================
print("\n" + "="*60)
print("📌 5. Detaylı Örnekler")
print("-"*60)

# Tam sayı gibi görünen float'lar
tam_gibi = 10.0
print(f"10.0 bir float'tur: {tam_gibi} (type: {type(tam_gibi)})")

# Çok küçük sayılar
kucuk = 0.0001
print(f"Çok küçük: {kucuk}")

# Çok büyük sayılar
buyuk = 123456.789
print(f"Çok büyük: {buyuk:,}")

# ============================================
# 6. Type Kontrolü
# ============================================
print("\n" + "="*60)
print("📌 6. Type (Tip) Kontrolü")
print("-"*60)

sayi1 = 5
sayi2 = 5.0

print(f"{sayi1} → Type: {type(sayi1)}")
print(f"{sayi2} → Type: {type(sayi2)}")

print(f"\n{sayi1} == {sayi2}? {sayi1 == sayi2} (Değer aynı)")
print(f"Type'ları aynı mı? {type(sayi1) == type(sayi2)} (Tip farklı)")

# ============================================
# 7. Float Formatlama
# ============================================
print("\n" + "="*60)
print("📌 7. Float Formatlama (İleriki Konular)")
print("-"*60)

pi = 3.141592653589793

print(f"Normal: {pi}")
print(f"2 basamak: {pi:.2f}")
print(f"4 basamak: {pi:.4f}")
print(f"6 basamak: {pi:.6f}")

print("\n💡 :.2f = 2 ondalık basamak göster")

# ============================================
# 8. Pratik Kullanım Örnekleri
# ============================================
print("\n" + "="*60)
print("📌 8. Pratik Kullanım Örnekleri")
print("-"*60)

# Örnek 1: Fiyat hesaplama
urun_fiyati = 19.99
adet = 3
toplam = urun_fiyati * adet
print(f"Ürün fiyatı: {urun_fiyati} TL")
print(f"Adet: {adet}")
print(f"Toplam: {toplam:.2f} TL")

# Örnek 2: Ortalama hesaplama
print("\n--- Ortalama Hesaplama ---")
notlar = [85, 92, 78, 90, 88]
ortalama = sum(notlar) / len(notlar)
print(f"Notlar: {notlar}")
print(f"Ortalama: {ortalama:.2f}")

# Örnek 3: Yüzde hesaplama
print("\n--- Yüzde Hesaplama ---")
fiyat = 100
indirim_yuzdesi = 20
indirim = fiyat * (indirim_yuzdesi / 100)
yeni_fiyat = fiyat - indirim
print(f"Orijinal fiyat: {fiyat} TL")
print(f"İndirim: %{indirim_yuzdesi}")
print(f"İndirim miktarı: {indirim} TL")
print(f"Yeni fiyat: {yeni_fiyat} TL")

# Örnek 4: BMI hesaplama
print("\n--- BMI (Vücut Kitle İndeksi) ---")
kilo = 70.5  # kg
boy = 1.75   # metre
bmi = kilo / (boy ** 2)
print(f"Kilo: {kilo} kg")
print(f"Boy: {boy} m")
print(f"BMI: {bmi:.2f}")

# ============================================
# 9. Bilimsel Notasyon
# ============================================
print("\n" + "="*60)
print("📌 9. Bilimsel Notasyon (e Notation)")
print("-"*60)

# Çok büyük veya çok küçük sayılar için
cok_buyuk = 1.23e6  # 1.23 × 10^6
cok_kucuk = 1.23e-6  # 1.23 × 10^-6

print(f"1.23e6 = {cok_buyuk:,}")
print(f"1.23e-6 = {cok_kucuk}")

# Işık hızı
isik_hizi = 3e8  # 300,000,000 m/s
print(f"\nIşık hızı: {isik_hizi:,} m/s")

# ============================================
# 10. Integer'a Çevirme
# ============================================
print("\n" + "="*60)
print("📌 10. Float'u Integer'a Çevirme")
print("-"*60)

ondalikli = 3.7
tam_sayi = int(ondalikli)  # Ondalık kısmı atar

print(f"Float: {ondalikli}")
print(f"Integer'a çevrildi: {tam_sayi}")
print("\n⚠️ Dikkat: Ondalık kısmı yuvarlamaz, atar!")

print(f"\nÖrnekler:")
print(f"int(3.1) = {int(3.1)}")
print(f"int(3.9) = {int(3.9)}")
print(f"int(5.5) = {int(5.5)}")

# Yuvarlama
print("\n--- Yuvarlama (round) ---")
print(f"round(3.1) = {round(3.1)}")
print(f"round(3.5) = {round(3.5)}")
print(f"round(3.9) = {round(3.9)}")
print(f"round(3.14159, 2) = {round(3.14159, 2)}")

# ============================================
# ÖZET
# ============================================
print("\n" + "="*60)
print("📚 FLOATS ÖZET")
print("="*60)
print("""
Float (Ondalıklı Sayılar):

Tanım:
✓ Ondalık noktalı sayılar (3.14, 0.5, 2.0)
✓ Float kelimesi "floating point" (yüzen nokta) demek

Özellikler:
✓ Ondalık nokta herhangi bir yerde olabilir
✓ Tüm matematiksel işlemler yapılabilir
✓ Integer ile karışırsa sonuç float olur
✓ Bölme (/) her zaman float döner

⚠️ Float Hassasiyeti:
• Bazen garip ondalık basamaklar görebilirsiniz
  Örnek: 0.2 + 0.1 = 0.30000000000000004
• Bu tüm dillerde olur, endişelenmeyin
• İleriki bölümlerde nasıl düzeltileceğini öğreneceksiniz

Kullanım Alanları:
• Fiyat hesaplamaları
• Ortalama hesapları
• Bilimsel hesaplamalar
• Yüzde hesaplamaları

💡 İpuçları:
• :.2f ile 2 ondalık basamak gösterebilirsiniz
• round() ile yuvarlayabilirsiniz
• int() ile tam sayıya çevirebilirsiniz
""")
print("="*60)
