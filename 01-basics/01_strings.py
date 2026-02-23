# ========================================
# STRING (METİN DİZİSİ) - Python'da Metinler
# ========================================

# String nedir?
# Tırnak içindeki her şey bir string'dir (metin dizisi)

# 1. TEK TIRNAK ile string
print("=== 1. Tek Tırnak Kullanımı ===")
mesaj1 = 'Bu bir string\'dir'
print(mesaj1)

# 2. ÇİFT TIRNAK ile string
print("\n=== 2. Çift Tırnak Kullanımı ===")
mesaj2 = "Bu da bir string'dir"
print(mesaj2)

# 3. İÇİNDE TIRNAK OLAN STRINGLER
print("\n=== 3. İçinde Tırnak Kullanımı ===")

# Çift tırnak içinde tek tırnak
mesaj3 = "Arkadaşıma 'Python harika!' dedim"
print(mesaj3)

# Tek tırnak içinde çift tırnak
mesaj4 = 'O dedi ki, "Sen de öğren!"'
print(mesaj4)

# 4. ÖZEL DURUMLAR
print("\n=== 4. Türkçe Karakterler ve Özel Durumlar ===")
turkce = "Python'un gücü, çeşitli ve destekleyici topluluğundadır"
print(turkce)

isim = 'Python dili, "Monty Python" grubundan alınmıştır'
print(isim)

# 5. ÇOK SATIRLI STRINGLER (Üç tırnak)
print("\n=== 5. Çok Satırlı Metinler ===")
uzun_metin = """
Bu bir çok satırlı 
string örneğidir.
İstediğiniz kadar satır yazabilirsiniz!
"""
print(uzun_metin)

# 6. STRING BİRLEŞTİRME
print("\n=== 6. String Birleştirme ===")
ad = "Ali"
soyad = "Kağan"
tam_isim = ad + " " + soyad
print("Merhaba, " + tam_isim + "!")

# 7. STRING ÇARPMA (Tekrarlama)
print("\n=== 7. String Tekrarlama ===")
yildiz = "*" * 20
print(yildiz)
print("  HOŞ GELDİNİZ")
print(yildiz)

# 8. STRING UZUNLUĞU
print("\n=== 8. String Uzunluğu ===")
kelime = "Merhaba Dünya"
print(f"'{kelime}' kelimesinin uzunluğu: {len(kelime)} karakter")

# 9. STRING METODları (Büyük/Küçük harf)
print("\n=== 9. String Metodları ===")
mesaj = "python öğreniyorum"
print(f"Orijinal: {mesaj}")
print(f"Büyük harf: {mesaj.upper()}")
print(f"Küçük harf: {mesaj.lower()}")
print(f"İlk harf büyük: {mesaj.title()}")
print(f"İlk harf büyük (cümle): {mesaj.capitalize()}")

# 10. BOŞLUKları TEMİZLEME
print("\n=== 10. Boşluk Temizleme ===")
bosluklu = "   fazla boşluk var   "
print(f"Orijinal: '{bosluklu}'")
print(f"Sol temizle: '{bosluklu.lstrip()}'")
print(f"Sağ temizle: '{bosluklu.rstrip()}'")
print(f"Her iki taraf: '{bosluklu.strip()}'")

# 11. STRING İÇİNDE ARAMA
print("\n=== 11. String İçinde Arama ===")
cumle = "Python programlama dilini öğreniyorum"
if "Python" in cumle:
    print("✓ 'Python' kelimesi cümlede var!")

if "Java" not in cumle:
    print("✓ 'Java' kelimesi cümlede yok!")

# 12. STRING DİLİMLEME (Slicing)
print("\n=== 12. String Dilimleme ===")
alfabe = "ABCDEFGH"
print(f"İlk 3 karakter: {alfabe[:3]}")
print(f"3. indexten sonrası: {alfabe[3:]}")
print(f"Ortadaki karakterler: {alfabe[2:6]}")
print(f"Tersten yazdır: {alfabe[::-1]}")

# 13. F-STRING (Modern kullanım)
print("\n=== 13. F-String (Modern Yöntem) ===")
isim = "Ali"
yas = 25
print(f"Benim adım {isim} ve {yas} yaşındayım")
print(f"5 yıl sonra {yas + 5} yaşında olacağım")

# ========================================
# ÖZET
# ========================================
print("\n" + "="*50)
print("STRING ÖZET:")
print("="*50)
print("✓ String = Tırnak içindeki metinler")
print("✓ Tek (') veya çift (\") tırnak kullanabilirsiniz")
print("✓ İçinde tırnak kullanmak için dış tırnağı değiştirin")
print("✓ Stringler birleştirilebilir (+)")
print("✓ Stringler tekrarlanabilir (*)")
print("✓ len() ile uzunluğu öğrenilir")
print("="*50)
