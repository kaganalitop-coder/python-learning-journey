# ========================================
# TRY IT YOURSELF - ALIŞTIRMALAR
# ========================================
# Kitaptan: Chapter 2 - Variables and Simple Data Types

print("="*60)
print("STRING ALIŞTIRMALARI")
print("="*60)

# ============================================
# 2-3. Personal Message
# ============================================
print("\n📌 ALIŞTIRMA 2-3: Personal Message")
print("-"*60)
print("Görev: Bir kişinin ismini değişkende saklayın ve ona mesaj yazın.")
print()

# Çözüm:
name = "Eric"
message = f"Hello {name}, would you like to learn some Python today?"
print(message)

# Alternatif çözümler:
name2 = "Ahmet"
message2 = f"Merhaba {name2}, bugün Python öğrenmek ister misin?"
print(message2)

# ============================================
# 2-4. Name Cases
# ============================================
print("\n" + "="*60)
print("📌 ALIŞTIRMA 2-4: Name Cases")
print("-"*60)
print("Görev: Bir ismi küçük, büyük ve title case ile yazdırın.")
print()

# Çözüm:
person_name = "ada lovelace"
print(f"Küçük harf: {person_name.lower()}")
print(f"Büyük harf: {person_name.upper()}")
print(f"Title case: {person_name.title()}")

# Bonus: Türkçe örnek
isim = "ali kağan"
print(f"\nTürkçe örnek: {isim}")
print(f"Küçük: {isim.lower()}")
print(f"Büyük: {isim.upper()}")
print(f"İlk Harfler Büyük: {isim.title()}")

# ============================================
# 2-5. Famous Quote
# ============================================
print("\n" + "="*60)
print("📌 ALIŞTIRMA 2-5: Famous Quote")
print("-"*60)
print("Görev: Ünlü birinin sözünü ve yazarını yazdırın.")
print()

# Çözüm:
print('Albert Einstein once said, "A person who never made a')
print('mistake never tried anything new."')

# Alternatif: F-string ile
author = "Albert Einstein"
quote = "A person who never made a mistake never tried anything new."
print(f'\n{author} once said, "{quote}"')

# Türkçe örnek:
yazar = "Mustafa Kemal Atatürk"
soz = "Hayatta en hakiki mürşit ilimdir."
print(f'\n{yazar} demiştir ki: "{soz}"')

# ============================================
# 2-6. Famous Quote 2
# ============================================
print("\n" + "="*60)
print("📌 ALIŞTIRMA 2-6: Famous Quote 2")
print("-"*60)
print("Görev: Ünlü kişiyi ve mesajı değişkenlerde saklayın.")
print()

# Çözüm:
famous_person = "Albert Einstein"
message = f'{famous_person} once said, "A person who never made a mistake never tried anything new."'
print(message)

# Türkçe örnek:
unlu_kisi = "Yunus Emre"
mesaj = f'{unlu_kisi} demiştir ki: "İlim ilim bilmektir, ilim kendin bilmektir."'
print(f"\n{mesaj}")

# ============================================
# 2-7. Stripping Names
# ============================================
print("\n" + "="*60)
print("📌 ALIŞTIRMA 2-7: Stripping Names")
print("-"*60)
print("Görev: İsmin başında ve sonunda boşluklar olsun.")
print("Sonra lstrip(), rstrip() ve strip() kullanın.")
print()

# Çözüm:
name_with_whitespace = "\t\n  Ada Lovelace  \n\t"

# Boşluklarla birlikte yazdır
print("Boşluklarla:")
print(f"'{name_with_whitespace}'")

# lstrip() - Sol tarafı temizle
print(f"\nlstrip(): '{name_with_whitespace.lstrip()}'")

# rstrip() - Sağ tarafı temizle
print(f"rstrip(): '{name_with_whitespace.rstrip()}'")

# strip() - Her iki tarafı temizle
print(f"strip(): '{name_with_whitespace.strip()}'")

# Türkçe örnek
print("\n--- Türkçe Örnek ---")
bosluklu_isim = "\t\n  Mehmet Ali  \n\t"
print(f"Orijinal: '{bosluklu_isim}'")
print(f"lstrip(): '{bosluklu_isim.lstrip()}'")
print(f"rstrip(): '{bosluklu_isim.rstrip()}'")
print(f"strip(): '{bosluklu_isim.strip()}'")

# ============================================
# BONUS ALIŞTIRMALAR
# ============================================
print("\n" + "="*60)
print("🎁 BONUS ALIŞTIRMALAR")
print("="*60)

# BONUS 1: Tam isim oluştur
print("\n📌 BONUS 1: Tam İsim Oluşturma")
print("-"*60)
first_name = "  mehmet  "
last_name = "  yılmaz  "

# Temizle ve düzgün formatla
full_name = f"{first_name.strip().title()} {last_name.strip().title()}"
print(f"Tam isim: {full_name}")

# BONUS 2: Email oluştur
print("\n📌 BONUS 2: Email Adresi Oluşturma")
print("-"*60")
ad = "  Ali Kağan  "
soyad = "  Top  "

# Email formatı: ad.soyad@example.com (küçük harf, boşluksuz)
email = f"{ad.strip().lower()}.{soyad.strip().lower()}@example.com"
# Boşlukları nokta ile değiştir
email = email.replace(" ", ".")
print(f"Email: {email}")

# BONUS 3: Kullanıcı Kartı
print("\n📌 BONUS 3: Kullanıcı Bilgi Kartı")
print("-"*60)
kullanici = "  ahmet yılmaz  "
sehir = "  istanbul  "
yas = "  30  "

# Tüm verileri temizle ve formatla
kart = f"""
{'='*40}
    KULLANICI BİLGİLERİ
{'='*40}
Ad Soyad : {kullanici.strip().title()}
Şehir    : {sehir.strip().title()}
Yaş      : {yas.strip()}
{'='*40}
"""
print(kart)

# ============================================
# ÖZET
# ============================================
print("\n" + "="*60)
print("📚 ALIŞTIRMA ÖZETİ")
print("="*60)
print("""
Bu alıştırmalarla öğrendikleriniz:

✓ Değişken kullanımı
✓ String metodları (upper, lower, title)
✓ F-string kullanımı
✓ Tırnak ve apostrophe kullanımı
✓ Whitespace karakterleri (\\t, \\n)
✓ Stripping metodları (strip, lstrip, rstrip)
✓ Gerçek hayat uygulamaları

🎯 Sırada: Sayılar ve matematiksel işlemler!
""")
print("="*60)
