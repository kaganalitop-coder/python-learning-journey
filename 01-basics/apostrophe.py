# ========================================
# APOSTROPHE ve SYNTAX ERRORS
# ========================================

# Apostrophe (') kullanırken dikkat edilmesi gerekenler

print("="*60)
print("APOSTROPHE ve SYNTAX ERRORS (SÖZDİZİMİ HATALARI)")
print("="*60)

# ============================================
# 1. DOĞRU Kullanım - Çift Tırnak İçinde Apostrophe
# ============================================
print("\n📌 1. ✅ DOĞRU: Çift Tırnak İçinde Apostrophe")
print("-"*60)

message = "One of Python's strengths is its diverse community."
print(message)

print("\n💡 Çift tırnak kullanınca, içindeki apostrophe sorun olmaz!")

# ============================================
# 2. HATALI Kullanım - Tek Tırnak İçinde Apostrophe
# ============================================
print("\n" + "="*60)
print("📌 2. ❌ HATALI: Tek Tırnak İçinde Apostrophe")
print("-"*60)

print("Bu kod hata verir:")
print("message = 'One of Python's strengths is its diverse community.'")
print("                            ^ Hata burada!")
print("\nPython burada string'in bittiğini sanır ve karışır.")

# HATA MESAJI:
print("\n--- HATA MESAJI ---")
print("SyntaxError: invalid syntax")

# ============================================
# 3. Çözüm 1: Çift Tırnak Kullan
# ============================================
print("\n" + "="*60)
print("📌 3. ÇÖZÜM 1: Çift Tırnak Kullan")
print("-"*60)

# İçinde apostrophe varsa, dışta çift tırnak kullan
mesaj1 = "Python'un gücü harika!"
print(mesaj1)

mesaj2 = "Don't worry, be happy!"
print(mesaj2)

mesaj3 = "It's a beautiful day!"
print(mesaj3)

# ============================================
# 4. Çözüm 2: Escape Karakteri Kullan
# ============================================
print("\n" + "="*60)
print("📌 4. ÇÖZÜM 2: Escape Karakteri (\\) Kullan")
print("-"*60)

# Tek tırnak içinde apostrophe kullanmak zorundaysanız, \' yapın
mesaj4 = 'Python\'un gücü harika!'
print(mesaj4)

mesaj5 = 'Don\'t worry, be happy!'
print(mesaj5)

print("\n💡 \\' = Apostrophe'u escape et (özel karakter olarak işaretle)")

# ============================================
# 5. Tırnak İçinde Tırnak
# ============================================
print("\n" + "="*60)
print("📌 5. Tırnak İçinde Tırnak Kullanımı")
print("-"*60)

# Çift tırnak içinde tek tırnak
cumle1 = "O dedi ki: 'Merhaba!'"
print(cumle1)

# Tek tırnak içinde çift tırnak
cumle2 = 'Kitap adı: "Python Öğreniyorum"'
print(cumle2)

# İkisi birden - escape ile
cumle3 = "O dedi ki: \"Merhaba!\""
print(cumle3)

# ============================================
# 6. Gerçek Hayat Örnekleri
# ============================================
print("\n" + "="*60)
print("📌 6. Gerçek Hayat Örnekleri")
print("-"*60)

# Türkçe metinlerde sık kullanılan
ornek1 = "Python'un sözdizimi çok temiz."
ornek2 = "Bugün hava çok güzel, değil mi?"
ornek3 = "Ahmet'in bilgisayarı çok hızlı."
ornek4 = "\"Merhaba\" kelimesini kullanıyoruz."

print(ornek1)
print(ornek2)
print(ornek3)
print(ornek4)

# ============================================
# 7. Çok Satırlı String'lerde Tırnak Kullanımı
# ============================================
print("\n" + "="*60)
print("📌 7. Çok Satırlı String'lerde (Üç Tırnak)")
print("-"*60)

# Üç tırnak kullanınca, içinde istediğiniz gibi tırnak kullanabilirsiniz
metin = """
Ahmet dedi ki: "Python'un sözdizimi harika!"
Ayşe de ekledi: 'Bence de öyle!'
İkisi de "It's amazing!" dedi.
"""
print(metin)

print("💡 Üç tırnak (''' veya \"\"\") kullanınca içeride serbest!")

# ============================================
# 8. Yaygın Hatalar ve Çözümleri
# ============================================
print("\n" + "="*60)
print("📌 8. Yaygın Hatalar ve Çözümleri")
print("-"*60)

print("""
┌────────────────────────────────┬─────────────────────────────┐
│  ❌ HATALI                     │  ✅ DOĞRU                   │
├────────────────────────────────┼─────────────────────────────┤
│ 'It's great'                   │ "It's great"                │
│                                │ veya 'It\\'s great'          │
├────────────────────────────────┼─────────────────────────────┤
│ "He said "Hi""                 │ 'He said "Hi"'              │
│                                │ veya "He said \\"Hi\\""       │
├────────────────────────────────┼─────────────────────────────┤
│ 'Python's cool'                │ "Python's cool"             │
│                                │ veya 'Python\\'s cool'       │
└────────────────────────────────┴─────────────────────────────┘
""")

# ============================================
# 9. Pratik Kurallar
# ============================================
print("\n" + "="*60)
print("📌 9. Pratik Kurallar")
print("-"*60)

print("""
🎯 BASIT KURAL:

1. İçinde APOSTROPHE (') varsa  → Dışta ÇİFT tırnak (") kullan
2. İçinde ÇİFT TIRNAK (") varsa → Dışta TEK tırnak (') kullan
3. İkisi de varsa               → Escape (\\) kullan veya üç tırnak (\""")

Örnekler:
✓ "Python's great"    → İçinde ', dışta "
✓ 'He said "Hi"'      → İçinde ", dışta '
✓ "Say \\"Hello\\""     → Escape ile
✓ \"""It's "cool"\"""    → Üç tırnak ile
""")

# ============================================
# 10. Editor Yardımı
# ============================================
print("\n" + "="*60)
print("📌 10. Editor (Cursor) Size Yardımcı Olur")
print("-"*60)

print("""
Cursor/VSCode gibi editorler:
• Syntax highlighting ile renklendirme yapar
• Yanlış tırnak kullanımını gösterir
• String'in nerede bittiğini gösterir

Eğer Python kodu İngilizce gibi,
veya İngilizce Python kodu gibi görünüyorsa,
→ Tırnak hatası var demektir!
""")

# ============================================
# ÖZET
# ============================================
print("\n" + "="*60)
print("📚 APOSTROPHE ÖZET")
print("="*60)
print("""
Apostrophe (') Kullanımı:

✓ İçinde apostrophe varsa, dışta çift tırnak (")
  Örnek: "Python's great"

✓ Tek tırnak kullanmak zorundaysan, escape et (\\')
  Örnek: 'Python\\'s great'

✓ Çift tırnak içinde çift tırnak → Escape (\\")
  Örnek: "He said \\"Hi\\""

✓ Çok satırlı ve karışıksa → Üç tırnak (\""" veya ''')

⚠️ SYNTAX ERROR:
   Python kodun yapısını anlamadığında verdiği hata.
   Çoğunlukla tırnak, parantez hatalarından kaynaklanır.

💡 İPUCU:
   Editörünüz (Cursor) renklendirmeyle yardımcı olur.
   Kod garip görünüyorsa, tırnaklara bakın!
""")
print("="*60)
