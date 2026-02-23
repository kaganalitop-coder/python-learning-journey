# ========================================
# STRIPPING - Boşluk Temizleme
# ========================================

# Stripping = String'in başındaki ve sonundaki boşlukları temizlemek

print("="*60)
print("STRIPPING - BOŞLUK TEMİZLEME")
print("="*60)

# ============================================
# 1. rstrip() - Sağdaki Boşlukları Temizle
# ============================================
print("\n📌 1. rstrip() - Sağdaki Boşlukları Temizle (Right)")
print("-"*60)

favorite_language = 'python '
print(f"Orijinal: '{favorite_language}'")
print(f"Boşluk var mı? Evet, sağda boşluk var!")

temizlenmis = favorite_language.rstrip()
print(f"rstrip() sonrası: '{temizlenmis}'")
print(f"Boşluk var mı? Hayır, temizlendi!")

print("\n⚠️ DİKKAT: Orijinal değişken değişmedi!")
print(f"favorite_language hala: '{favorite_language}'")

print("\n✅ Kalıcı yapmak için tekrar atama yapın:")
favorite_language = favorite_language.rstrip()
print(f"Şimdi kalıcı: '{favorite_language}'")

# ============================================
# 2. lstrip() - Soldaki Boşlukları Temizle
# ============================================
print("\n" + "="*60)
print("📌 2. lstrip() - Soldaki Boşlukları Temizle (Left)")
print("-"*60)

language = '   javascript'
print(f"Orijinal: '{language}'")
print(f"lstrip() sonrası: '{language.lstrip()}'")

# ============================================
# 3. strip() - Her İki Taraftaki Boşlukları Temizle
# ============================================
print("\n" + "="*60)
print("📌 3. strip() - Her İki Tarafı Temizle")
print("-"*60)

messy_language = '   python   '
print(f"Orijinal: '{messy_language}'")
print(f"rstrip(): '{messy_language.rstrip()}'  → Sadece sağ temizlendi")
print(f"lstrip(): '{messy_language.lstrip()}'  → Sadece sol temizlendi")
print(f"strip():  '{messy_language.strip()}'  → Her iki taraf temizlendi")

# ============================================
# 4. Tab ve Newline'ı da Temizler
# ============================================
print("\n" + "="*60)
print("📌 4. Tab ve Newline'ı da Temizler")
print("-"*60)

karmasik = '\t\n  Python  \n\t'
print(f"Orijinal: '{karmasik}'")
print(f"strip() sonrası: '{karmasik.strip()}'")
print("\n💡 strip() sadece boşluk değil, tab (\\t) ve newline (\\n) da temizler!")

# ============================================
# 5. Gerçek Hayat Örneği: Kullanıcı Girişi
# ============================================
print("\n" + "="*60)
print("📌 5. Gerçek Hayat: Kullanıcı Girişi Temizleme")
print("-"*60)

# Kullanıcı yanlışlıkla boşlukla yazabilir
kullanici_adi_1 = '  admin  '
kullanici_adi_2 = 'admin'

print("❌ Boşluksuz karşılaştırma:")
if kullanici_adi_1 == kullanici_adi_2:
    print("   Eşit")
else:
    print(f"   Eşit değil: '{kullanici_adi_1}' != '{kullanici_adi_2}'")

print("\n✅ strip() ile karşılaştırma:")
if kullanici_adi_1.strip() == kullanici_adi_2.strip():
    print("   Eşit! Giriş başarılı!")
else:
    print("   Eşit değil")

# ============================================
# 6. Gerçek Hayat Örneği: Form Verisi
# ============================================
print("\n" + "="*60)
print("📌 6. Gerçek Hayat: Form Verilerini Temizleme")
print("-"*60)

# Kullanıcıdan gelen veriler
ad_soyad = "  Ahmet Yılmaz  "
email = "  ahmet@email.com  "
telefon = "  0555 123 45 67  "

print("❌ TEMIZLENMEMIŞ VERİ:")
print(f"Ad Soyad: '{ad_soyad}'")
print(f"Email   : '{email}'")
print(f"Telefon : '{telefon}'")

# Verileri temizle
ad_soyad_temiz = ad_soyad.strip()
email_temiz = email.strip().lower()  # Lowercase da yap
telefon_temiz = telefon.strip()

print("\n✅ TEMİZLENMİŞ VERİ:")
print(f"Ad Soyad: '{ad_soyad_temiz}'")
print(f"Email   : '{email_temiz}'")
print(f"Telefon : '{telefon_temiz}'")

# ============================================
# 7. Gerçek Hayat Örneği: Veri Tabanı
# ============================================
print("\n" + "="*60)
print("📌 7. Gerçek Hayat: Veri Tabanına Kaydetme")
print("-"*60)

print("\nKullanıcı kayıt formu:")

# Kullanıcı girişleri (boşluklarla)
isim_input = "  Ali  "
soyisim_input = "  Kağan  "
sehir_input = "  istanbul  "

# Veri tabanına kaydetmeden önce temizle
isim_db = isim_input.strip().title()  # Temizle + İlk harf büyük
soyisim_db = soyisim_input.strip().title()
sehir_db = sehir_input.strip().title()

print(f"\nVeri tabanına kaydedilen:")
print(f"{'='*40}")
print(f"İsim   : {isim_db}")
print(f"Soyisim: {soyisim_db}")
print(f"Şehir  : {sehir_db}")
print(f"{'='*40}")

# ============================================
# 8. Pratik: String Karşılaştırma
# ============================================
print("\n" + "="*60)
print("📌 8. String Karşılaştırma Problemleri")
print("-"*60)

# Programcıya aynı görünür ama programa farklı!
str1 = "python"
str2 = "python "
str3 = " python "

print(f"str1: '{str1}'")
print(f"str2: '{str2}'")
print(f"str3: '{str3}'")

print(f"\nstr1 == str2? {str1 == str2} (Sağda boşluk var!)")
print(f"str1 == str3? {str1 == str3} (Sağda ve solda boşluk var!)")

print("\n✅ strip() ile:")
print(f"str1 == str2.strip()? {str1 == str2.strip()}")
print(f"str1 == str3.strip()? {str1 == str3.strip()}")

print("\n💡 Her zaman kullanıcı girdisini strip() ile temizleyin!")

# ============================================
# 9. Hangi Metodu Kullanmalı?
# ============================================
print("\n" + "="*60)
print("📌 9. Hangi Metodu Ne Zaman Kullanmalı?")
print("-"*60)

print("""
┌─────────────┬──────────────────────────────┬─────────────┐
│   Metod     │   Ne Yapar?                  │  Ne Zaman?  │
├─────────────┼──────────────────────────────┼─────────────┤
│ strip()     │ Her iki tarafı temizler      │  Genelde bu│
│ rstrip()    │ Sadece sağı temizler         │  Nadiren   │
│ lstrip()    │ Sadece solu temizler         │  Nadiren   │
└─────────────┴──────────────────────────────┴─────────────┘

💡 En çok kullanılan: strip()
""")

# ============================================
# ÖZET
# ============================================
print("\n" + "="*60)
print("📚 STRIPPING ÖZET")
print("="*60)
print("""
Stripping = Boşlukları temizlemek

✓ strip()   → Her iki tarafı temizle (en yaygın)
✓ rstrip()  → Sağdaki boşlukları temizle
✓ lstrip()  → Soldaki boşlukları temizle

Neyi Temizler?
• Boşluk karakteri ( )
• Tab (\\t)
• Newline (\\n)

Neden Önemli?
• Kullanıcı girdilerini temizlemek
• String karşılaştırmaları
• Veri tabanına kaydetmeden önce
• Form verilerini işlemek

⚠️ DİKKAT: Orijinal string değişmez!
   Kalıcı yapmak için yeniden atama yapın:
   text = text.strip()
""")
print("="*60)
