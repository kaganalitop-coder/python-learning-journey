# ========================================
# WHITESPACE - Boşluk Karakterleri
# ========================================

# Whitespace = Görünmeyen karakterler (boşluk, tab, yeni satır)

print("="*60)
print("WHITESPACE (BOŞLUK KARAKTERLERİ)")
print("="*60)

# ============================================
# 1. TAB (\t) - Sekme Boşluğu
# ============================================
print("\n📌 1. TAB (\\t) - Sekme Boşluğu")
print("-"*60)

print("Normal:")
print("Python")

print("\nTab ile:")
print("\tPython")

print("\nİki tab ile:")
print("\t\tPython")

print("\n💡 \\t = Bir sekme boşluğu ekler (genelde 4 boşluk)")

# ============================================
# 2. NEWLINE (\n) - Yeni Satır
# ============================================
print("\n" + "="*60)
print("📌 2. NEWLINE (\\n) - Yeni Satır")
print("-"*60)

print("Normal:")
print("Languages:PythonCJavaScript")

print("\nYeni satırlar ile:")
print("Languages:\nPython\nC\nJavaScript")

print("\n💡 \\n = Yeni satıra geçer")

# ============================================
# 3. TAB ve NEWLINE Birlikte
# ============================================
print("\n" + "="*60)
print("📌 3. TAB ve NEWLINE Kombinasyonu")
print("-"*60)

# Hem yeni satır hem de girintili
print("Languages:\n\tPython\n\tC\n\tJavaScript")

print("\n💡 \\n\\t = Yeni satıra geç ve girinti ekle")

# ============================================
# 4. Pratik Örnek: Menü Oluşturma
# ============================================
print("\n" + "="*60)
print("📌 4. Pratik Örnek: Menü")
print("-"*60)

menu = "RESTORAN MENÜSÜ:\n\n\tAna Yemekler:\n\t\t- Köfte\n\t\t- Tavuk\n\t\t- Balık\n\n\tTatlılar:\n\t\t- Baklava\n\t\t- Sütlaç\n\t\t- Kazandibi"
print(menu)

# ============================================
# 5. Pratik Örnek: Adres Formatı
# ============================================
print("\n" + "="*60)
print("📌 5. Pratik Örnek: Adres Kartı")
print("-"*60)

ad = "Ahmet Yılmaz"
telefon = "0555 123 45 67"
adres = "Atatürk Cad. No:123\nBeşiktaş\nİstanbul"

kart = f"\n{'='*40}\n\t  KİŞİ BİLGİLERİ\n{'='*40}\nAd Soyad : {ad}\nTelefon  : {telefon}\nAdres    : {adres}\n{'='*40}"
print(kart)

# ============================================
# 6. Pratik Örnek: Fatura
# ============================================
print("\n" + "="*60)
print("📌 6. Pratik Örnek: Fatura")
print("-"*60)

fatura = """
╔════════════════════════════════╗
║         SATIŞ FATURASI         ║
╚════════════════════════════════╝

Ürünler:
\t1. Laptop\t\t15,000 TL
\t2. Mouse\t\t   150 TL
\t3. Klavye\t\t   450 TL
\t\t\t\t─────────────
\t\tTOPLAM:\t\t15,600 TL

Ödeme Yöntemi: Kredi Kartı
Tarih: 23.02.2026
"""
print(fatura)

# ============================================
# 7. Escape Karakterleri Özet
# ============================================
print("\n" + "="*60)
print("📌 7. ESCAPE KARAKTERLERİ ÖZET")
print("-"*60)

print("\n\\t = Tab (sekme)")
print("\\n = Newline (yeni satır)")
print("\\\\ = Backslash (ters bölü)")
print("\\' = Tek tırnak")
print('\\\" = Çift tırnak')

# Örnekler
print("\n--- ÖRNEKLER ---")
print("Klasör yolu: C:\\Users\\Documents")  # \\ kullanımı
print('O dedi ki: \'Merhaba!\'')  # \' kullanımı
print("Kitap adı: \"Python Öğreniyorum\"")  # \" kullanımı

# ============================================
# ÖZET
# ============================================
print("\n" + "="*60)
print("📚 WHITESPACE ÖZET")
print("="*60)
print("""
Whitespace = Görünmeyen karakterler

✓ \\t  → Tab (sekme boşluğu)
✓ \\n  → Yeni satır
✓ \\n\\t → Yeni satır + girinti

Kullanım Alanları:
• Menüler
• Listeler
• Faturalar
• Raporlar
• Her türlü formatlı çıktı
""")
print("="*60)
