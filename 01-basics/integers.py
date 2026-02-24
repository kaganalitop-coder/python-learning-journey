# ========================================
# INTEGERS (TAM SAYILAR)
# ========================================

# Integer = Ondalık kısmı olmayan sayılar (1, 2, 3, -5, 0)

print("="*60)
print("INTEGERS (TAM SAYILAR)")
print("="*60)

# ============================================
# 1. Temel Matematiksel İşlemler
# ============================================
print("\n📌 1. Temel Matematiksel İşlemler")
print("-"*60)

# Toplama (+)
print(f"2 + 3 = {2 + 3}")

# Çıkarma (-)
print(f"3 - 2 = {3 - 2}")

# Çarpma (*)
print(f"2 * 3 = {2 * 3}")

# Bölme (/)
print(f"3 / 2 = {3 / 2}")

print("\n💡 Bölme işlemi her zaman float (ondalıklı) döner!")

# ============================================
# 2. Üs Alma (Exponents)
# ============================================
print("\n" + "="*60)
print("📌 2. Üs Alma İşlemi (**)") 
print("-"*60)

# ** işareti üs almak için kullanılır
print(f"3 ** 2 = {3 ** 2}")      # 3'ün karesi
print(f"3 ** 3 = {3 ** 3}")      # 3'ün küpü
print(f"10 ** 6 = {10 ** 6}")    # 10'un 6. kuvveti

print("\n💡 ** = Üs alma (3 ** 2 = 3²)")

# Daha fazla örnek
print("\nDaha fazla örnek:")
print(f"2 ** 8 = {2 ** 8}")      # 256
print(f"5 ** 3 = {5 ** 3}")      # 125
print(f"10 ** 3 = {10 ** 3}")    # 1000

# ============================================
# 3. İşlem Önceliği (Order of Operations)
# ============================================
print("\n" + "="*60)
print("📌 3. İşlem Önceliği")
print("-"*60)

# Python matematikteki işlem sırasını takip eder
# 1. Parantez
# 2. Üs
# 3. Çarpma ve Bölme
# 4. Toplama ve Çıkarma

print(f"2 + 3 * 4 = {2 + 3 * 4}")      # Önce 3*4, sonra +2
print(f"(2 + 3) * 4 = {(2 + 3) * 4}")  # Önce parantez içi

print("\n💡 Parantez kullanarak işlem sırasını değiştirebilirsiniz!")

# Daha fazla örnek
print("\nDaha fazla örnek:")
print(f"10 + 5 * 2 = {10 + 5 * 2}")         # 20
print(f"(10 + 5) * 2 = {(10 + 5) * 2}")     # 30
print(f"20 - 10 / 2 = {20 - 10 / 2}")       # 15.0
print(f"(20 - 10) / 2 = {(20 - 10) / 2}")   # 5.0

# ============================================
# 4. Boşluklar Önemli Değil
# ============================================
print("\n" + "="*60)
print("📌 4. Boşluklar (Whitespace)")
print("-"*60)

# Boşluklar sonucu değiştirmez, sadece okunabilirlik için
print(f"3+5 = {3+5}")
print(f"3 + 5 = {3 + 5}")
print(f"3  +  5 = {3  +  5}")

print("\n💡 Sonuç aynı, ama okunabilirlik için boşluk kullanın!")

# Okunabilir kod:
sonuc1 = 2 + 3 * 4
sonuc2 = (2 + 3) * 4
print(f"\nOkunabilir: {sonuc1} vs {sonuc2}")

# ============================================
# 5. Diğer İşlemler
# ============================================
print("\n" + "="*60)
print("📌 5. Diğer Matematiksel İşlemler")
print("-"*60)

# Tam bölme (//)
print(f"7 / 2 = {7 / 2}")    # Normal bölme (float)
print(f"7 // 2 = {7 // 2}")  # Tam bölme (integer)

print("\n💡 // = Tam bölme (ondalık kısmı atmaz)")

# Mod alma (%)
print(f"\n7 % 2 = {7 % 2}")    # 7'nin 2'ye bölümünden kalan
print(f"10 % 3 = {10 % 3}")    # 10'un 3'e bölümünden kalan
print(f"15 % 5 = {15 % 5}")    # 15'in 5'e bölümünden kalan

print("\n💡 % = Mod (kalanı bulur)")

# ============================================
# 6. Pratik Örnekler
# ============================================
print("\n" + "="*60)
print("📌 6. Pratik Örnekler")
print("-"*60)

# Örnek 1: Çift mi kontrol et
sayi = 7
if sayi % 2 == 0:
    print(f"{sayi} çift sayıdır")
else:
    print(f"{sayi} tek sayıdır")

# Örnek 2: Alan hesaplama
en = 5
boy = 10
alan = en * boy
print(f"\nDikdörtgen alanı: {en} × {boy} = {alan}")

# Örnek 3: Üçgenin alanı
taban = 8
yukseklik = 5
ucgen_alan = (taban * yukseklik) / 2
print(f"Üçgen alanı: ({taban} × {yukseklik}) / 2 = {ucgen_alan}")

# Örnek 4: Küpün hacmi
kenar = 3
hacim = kenar ** 3
print(f"Küp hacmi: {kenar}³ = {hacim}")

# ============================================
# 7. Negatif Sayılar
# ============================================
print("\n" + "="*60)
print("📌 7. Negatif Sayılar")
print("-"*60)

print(f"5 + (-3) = {5 + (-3)}")
print(f"-5 + 3 = {-5 + 3}")
print(f"-5 * 2 = {-5 * 2}")
print(f"-10 / 2 = {-10 / 2}")
print(f"(-2) ** 3 = {(-2) ** 3}")

# ============================================
# 8. Büyük Sayılar
# ============================================
print("\n" + "="*60)
print("📌 8. Büyük Sayılar")
print("-"*60)

milyon = 1000000
milyar = 1000000000
trilyon = 1000000000000

print(f"1 milyon = {milyon:,}")
print(f"1 milyar = {milyar:,}")
print(f"1 trilyon = {trilyon:,}")

# İşlemler
print(f"\n2 milyon × 3 = {2 * milyon:,}")
print(f"5 milyar / 1000 = {5 * milyar / 1000:,}")

# ============================================
# ÖZET
# ============================================
print("\n" + "="*60)
print("📚 INTEGERS ÖZET")
print("="*60)
print("""
Tam Sayılar (Integers):

Temel İşlemler:
✓ +  → Toplama
✓ -  → Çıkarma
✓ *  → Çarpma
✓ /  → Bölme (sonuç float)
✓ // → Tam bölme (sonuç integer)
✓ %  → Mod (kalan)
✓ ** → Üs alma

İşlem Önceliği:
1. Parantez ()
2. Üs **
3. Çarpma * ve Bölme /
4. Toplama + ve Çıkarma -

💡 İpuçları:
• Bölme (/) her zaman float döner
• Parantez ile sırayı değiştirebilirsiniz
• Boşluklar sonucu değiştirmez
• Mod (%) çift/tek kontrolü için kullanışlı
""")
print("="*60)
