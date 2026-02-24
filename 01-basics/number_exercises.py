# ========================================
# NUMBER EXERCISES - Sayı Alıştırmaları
# ========================================
# Kitaptan: Chapter 2 - Numbers

print("="*60)
print("SAYI ALIŞTIRMALARI")
print("="*60)

# ============================================
# 2-8. Number Eight
# ============================================
print("\n📌 ALIŞTIRMA 2-8: Number Eight")
print("-"*60)
print("Görev: Toplama, çıkarma, çarpma ve bölme ile 8 sonucunu elde edin.")
print()

# Çözüm:
print(5 + 3)      # Toplama
print(10 - 2)     # Çıkarma
print(2 * 4)      # Çarpma
print(16 / 2)     # Bölme

print("\n💡 Her işlem farklı yolla 8 sonucunu verdi!")

# Bonus: Daha fazla örnek
print("\n--- Bonus Örnekler ---")
print(2 ** 3)           # Üs alma: 2³ = 8
print(64 // 8)          # Tam bölme: 64 / 8 = 8
print(100 - 92)         # Çıkarma: 100 - 92 = 8
print((2 + 2) * 2)      # Parantezli: (2 + 2) * 2 = 8
print(40 // 5)          # Tam bölme: 40 / 5 = 8

# ============================================
# 2-9. Favorite Number
# ============================================
print("\n" + "="*60)
print("📌 ALIŞTIRMA 2-9: Favorite Number")
print("-"*60)
print("Görev: Favori sayınızı değişkende saklayın ve mesaj oluşturun.")
print()

# Çözüm:
favorite_number = 7
message = f"My favorite number is {favorite_number}."
print(message)

# Alternatif çözümler:
print("\n--- Alternatif Çözümler ---")

# Versiyon 2: Türkçe
favori_sayi = 42
mesaj = f"Benim favori sayım {favori_sayi}."
print(mesaj)

# Versiyon 3: Daha detaylı
fav_num = 13
print(f"Biliyor musun? Benim favori sayım {fav_num}!")
print(f"Çünkü {fav_num} şanslı bir sayıdır.")

# Versiyon 4: Matematiksel bilgi
en_sevilen = 3
print(f"\n{en_sevilen} benim favori sayım.")
print(f"{en_sevilen} asal bir sayıdır.")
print(f"{en_sevilen}² = {en_sevilen ** 2}")
print(f"{en_sevilen}³ = {en_sevilen ** 3}")

# ============================================
# BONUS ALIŞTIRMALAR
# ============================================
print("\n" + "="*60)
print("🎁 BONUS ALIŞTIRMALAR")
print("="*60)

# BONUS 1: Yaş Hesaplama
print("\n📌 BONUS 1: Yaş Hesaplama")
print("-"*60)
dogum_yili = 1995
su_anki_yil = 2026
yas = su_anki_yil - dogum_yili
print(f"Doğum yılı: {dogum_yili}")
print(f"Şu anki yıl: {su_anki_yil}")
print(f"Yaşınız: {yas}")

# BONUS 2: Alan ve Çevre
print("\n📌 BONUS 2: Dikdörtgen Alan ve Çevre")
print("-"*60)
en = 12
boy = 5
alan = en * boy
cevre = 2 * (en + boy)
print(f"En: {en}, Boy: {boy}")
print(f"Alan: {alan}")
print(f"Çevre: {cevre}")

# BONUS 3: Sıcaklık Dönüşümü
print("\n📌 BONUS 3: Celsius → Fahrenheit")
print("-"*60)
celsius = 25
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C = {fahrenheit}°F")

# Ters dönüşüm
fahrenheit2 = 77
celsius2 = (fahrenheit2 - 32) * 5/9
print(f"{fahrenheit2}°F = {celsius2:.1f}°C")

# BONUS 4: Alışveriş Sepeti
print("\n📌 BONUS 4: Alışveriş Sepeti")
print("-"*60)
urun1_fiyat = 29.99
urun2_fiyat = 49.99
urun3_fiyat = 15.50

ara_toplam = urun1_fiyat + urun2_fiyat + urun3_fiyat
kdv = ara_toplam * 0.20  # %20 KDV
kargo = 15.00
genel_toplam = ara_toplam + kdv + kargo

print(f"Ürün 1: {urun1_fiyat} TL")
print(f"Ürün 2: {urun2_fiyat} TL")
print(f"Ürün 3: {urun3_fiyat} TL")
print(f"Ara Toplam: {ara_toplam:.2f} TL")
print(f"KDV (%20): {kdv:.2f} TL")
print(f"Kargo: {kargo:.2f} TL")
print(f"Genel Toplam: {genel_toplam:.2f} TL")

# BONUS 5: Zaman Dönüşümleri
print("\n📌 BONUS 5: Zaman Dönüşümleri")
print("-"*60)
saniye = 3665  # Toplam saniye

saat = saniye // 3600
kalan = saniye % 3600
dakika = kalan // 60
saniye_kalan = kalan % 60

print(f"Toplam: {saniye} saniye")
print(f"= {saat} saat, {dakika} dakika, {saniye_kalan} saniye")

# BONUS 6: İki Sayının Ortalaması
print("\n📌 BONUS 6: Ortalama Hesaplama")
print("-"*60)
sayi1 = 85
sayi2 = 92
sayi3 = 78
sayi4 = 95

ortalama = (sayi1 + sayi2 + sayi3 + sayi4) / 4
print(f"Sayılar: {sayi1}, {sayi2}, {sayi3}, {sayi4}")
print(f"Ortalama: {ortalama:.2f}")

# BONUS 7: Compound Interest (Bileşik Faiz)
print("\n📌 BONUS 7: Bileşik Faiz Hesaplama")
print("-"*60)
ana_para = 10_000  # TL
faiz_orani = 0.15  # %15
yil = 5

son_tutar = ana_para * (1 + faiz_orani) ** yil
kazanc = son_tutar - ana_para

print(f"Ana para: {ana_para:,} TL")
print(f"Faiz oranı: %{faiz_orani * 100:.0f}")
print(f"Süre: {yil} yıl")
print(f"Son tutar: {son_tutar:,.2f} TL")
print(f"Kazanç: {kazanc:,.2f} TL")

# BONUS 8: Pitagor Teoremi
print("\n📌 BONUS 8: Pitagor Teoremi (a² + b² = c²)")
print("-"*60)
a = 3
b = 4
c_kare = a**2 + b**2
c = c_kare ** 0.5  # Karekök

print(f"Dik kenarlar: a = {a}, b = {b}")
print(f"a² = {a**2}")
print(f"b² = {b**2}")
print(f"c² = {c_kare}")
print(f"Hipotenüs c = {c:.2f}")

# BONUS 9: BMI (Vücut Kitle İndeksi)
print("\n📌 BONUS 9: BMI Hesaplama")
print("-"*60)
kilo = 75  # kg
boy = 1.80  # metre
bmi = kilo / (boy ** 2)

print(f"Kilo: {kilo} kg")
print(f"Boy: {boy} m")
print(f"BMI: {bmi:.2f}")

if bmi < 18.5:
    kategori = "Zayıf"
elif bmi < 25:
    kategori = "Normal"
elif bmi < 30:
    kategori = "Fazla Kilolu"
else:
    kategori = "Obez"
print(f"Kategori: {kategori}")

# BONUS 10: Sayı Özellikleri
print("\n📌 BONUS 10: Sayı Özellikleri")
print("-"*60)
MY_NUMBER = 24

print(f"Sayı: {MY_NUMBER}")
print(f"Karesi: {MY_NUMBER ** 2}")
print(f"Küpü: {MY_NUMBER ** 3}")
print(f"Yarısı: {MY_NUMBER / 2}")
print(f"İki katı: {MY_NUMBER * 2}")
print(f"Çift mi? {MY_NUMBER % 2 == 0}")
print(f"5'e bölünebilir mi? {MY_NUMBER % 5 == 0}")

# ============================================
# ÖZET
# ============================================
print("\n" + "="*60)
print("📚 ALIŞTIRMA ÖZETİ")
print("="*60)
print("""
Bu alıştırmalarla öğrendikleriniz:

✓ Temel matematik işlemleri (+, -, *, /)
✓ Üs alma (**)
✓ Tam bölme (//) ve mod (%)
✓ Değişken kullanımı
✓ F-string ile mesaj oluşturma
✓ Float ve integer karışımı
✓ Gerçek hayat hesaplamaları
✓ Formül uygulamaları

🎯 Sırada: Listeler ve veri yapıları!
""")
print("="*60)
