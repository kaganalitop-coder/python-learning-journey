# ========================================
# STRING METODLARI - Büyük/Küçük Harf Değişimi
# ========================================

# ÖRNEK 1: title() metodu
# Her kelimenin ilk harfini büyük yapar
print("=== 1. title() Metodu ===")
name = "ada lovelace"
print(name.title())
# Çıktı: Ada Lovelace

print("\n" + "-"*50 + "\n")

# ÖRNEK 2: upper() ve lower() metodları
print("=== 2. upper() ve lower() Metodları ===")
name = "Ada Lovelace"
print(name.upper())  # Tümü büyük harf
print(name.lower())  # Tümü küçük harf

print("\n" + "-"*50 + "\n")

# AÇIKLAMA:
# title() - Her kelimenin ilk harfini büyük yapar
# upper() - Tüm harfleri büyük yapar
# lower() - Tüm harfleri küçük yapar

# NEDEN KULLANILIR?
# Kullanıcı "Ada", "ADA" veya "ada" yazsa da,
# hepsini aynı şekilde tanımak için lower() kullanabiliriz:

print("=== 3. Pratik Kullanım ===")
kullanici_girisi1 = "Ada"
kullanici_girisi2 = "ADA"
kullanici_girisi3 = "ada"

# Hepsini küçük harfe çevirip karşılaştır
if kullanici_girisi1.lower() == kullanici_girisi2.lower() == kullanici_girisi3.lower():
    print("✓ Tüm girdiler aynı ismi temsil ediyor!")
    print(f"  Ekranda gösterelim: {kullanici_girisi1.title()}")

print("\n" + "-"*50 + "\n")

# GERÇEK HAYAT ÖRNEĞİ
print("=== 4. Gerçek Hayat Örneği ===")

# Veri tabanında küçük harfle sakla
veritabani_isim = "john doe"  # küçük harfle saklandı

# Kullanıcıya gösterirken düzgün göster
print(f"Hoş geldin, {veritabani_isim.title()}!")
print(f"E-posta adresin: {veritabani_isim.lower().replace(' ', '.')}@example.com")

# Çıktı:
# Hoş geldin, John Doe!
# E-posta adresin: john.doe@example.com
