# ========================================
# COMMENTS (YORUMLAR)
# ========================================

# Comment = Kodun açıklaması, Python çalıştırmaz

print("="*60)
print("COMMENTS (YORUMLAR)")
print("="*60)

# ============================================
# 1. Comment Nedir?
# ============================================
print("\n📌 1. Comment (Yorum) Nedir?")
print("-"*60)

print("""
Comment = Kod içinde açıklama yazmak

Özellikler:
• Python tarafından çalıştırılmaz
• Sadece insanlar için
• # işareti ile başlar
• Kodunuzu açıklamak için kullanılır
""")

# ============================================
# 2. Comment Nasıl Yazılır?
# ============================================
print("\n" + "="*60)
print("📌 2. Comment Nasıl Yazılır?")
print("-"*60)

# Bu bir yorumdur
print("Bu çalışır")

# print("Bu çalışmaz, çünkü yorum satırı")

print("\n💡 # işaretinden sonrası Python tarafından görülmez!")

# ============================================
# 3. Tek Satır Yorumlar
# ============================================
print("\n" + "="*60)
print("📌 3. Tek Satır Yorumlar")
print("-"*60)

# Satır başında yorum
print("Merhaba")

print("Dünya")  # Satır sonunda yorum

# Birden fazla tek satır yorum
# Bu birinci satır
# Bu ikinci satır
# Bu üçüncü satır
print("Yorumlar görünmüyor!")

# ============================================
# 4. Çok Satırlı Yorumlar
# ============================================
print("\n" + "="*60)
print("📌 4. Çok Satırlı Yorumlar")
print("-"*60)

"""
Bu bir çok satırlı yorum (docstring)
İstediğiniz kadar satır yazabilirsiniz
Genelde üç çift tırnak kullanılır
"""

print("Çok satırlı yorum geçildi!")

'''
Tek tırnak ile de çok satırlı yorum yapılabilir
Ama çift tırnak daha yaygın
'''

print("\n💡 Üç tırnak (\"\"\" veya ''') çok satırlı yorum için!")

# ============================================
# 5. İyi Yorum Örnekleri
# ============================================
print("\n" + "="*60)
print("📌 5. ✅ İyi Yorum Örnekleri")
print("-"*60)

# Daire alanını hesapla
yaricap = 5
alan = 3.14159 * yaricap ** 2
print(f"✅ Açıklayıcı: Daire alanı = {alan:.2f}")

# KDV dahil fiyat hesapla
fiyat = 100
kdv = fiyat * 0.20  # %20 KDV
toplam = fiyat + kdv
print(f"✅ Detay veriyor: Toplam fiyat = {toplam} TL")

# Kullanıcı girişi kontrolü
# Maksimum 3 deneme hakkı var
# Her yanlış denemede uyarı göster
max_deneme = 3
print(f"✅ Mantığı açıklıyor: Max deneme = {max_deneme}")

# ============================================
# 6. Kötü Yorum Örnekleri
# ============================================
print("\n" + "="*60)
print("📌 6. ❌ Kötü Yorum Örnekleri")
print("-"*60)

# x'e 5 ata
x = 5
print(f"❌ Gereksiz: x = {x}")
# Bu zaten belli, yoruma gerek yok!

# Topla
sonuc = 10 + 20
print(f"❌ Açıklayıcı değil: sonuc = {sonuc}")
# Ne için topluyoruz? Neden?

# Bu kod çalışır
y = 10
print(f"❌ Anlamsız: y = {y}")

print("""
💡 İyi Yorum:
   • NEDEN yapıldığını açıklar
   • NE yapıldığını değil
   • Karmaşık mantığı basitleştirir
   • Gelecekte size yardımcı olur
""")

# ============================================
# 7. Pratik Kullanım Örnekleri
# ============================================
print("\n" + "="*60)
print("📌 7. Pratik Kullanım Örnekleri")
print("-"*60)

# Örnek 1: Matematiksel formül
print("--- Daire Hesaplamaları ---")
# A = πr² formülü ile alan hesapla
PI = 3.14159
r = 7
alan = PI * r ** 2
print(f"Alan: {alan:.2f}")

# Örnek 2: İş mantığı
print("\n--- Kargo Ücreti Hesaplama ---")
urun_fiyati = 150

# 200 TL üzeri siparişlerde kargo bedava
# 200 TL altında kargo 15 TL
if urun_fiyati >= 200:
    kargo = 0
else:
    kargo = 15

print(f"Ürün: {urun_fiyati} TL")
print(f"Kargo: {kargo} TL")
print(f"Toplam: {urun_fiyati + kargo} TL")

# Örnek 3: Geçici kod devre dışı bırakma
print("\n--- Debug Modu ---")
print("Aktif kod çalışıyor")
# print("Bu kod geçici olarak kapalı")
# debug_mode = True
# if debug_mode:
#     print("Debug bilgisi")

# ============================================
# 8. Docstring (Fonksiyon Açıklaması)
# ============================================
print("\n" + "="*60)
print("📌 8. Docstring - Fonksiyon Açıklaması")
print("-"*60)

def selamla(isim):
    """
    Kullanıcıyı selamlar.
    
    Args:
        isim (str): Selamlanacak kişinin ismi
    
    Returns:
        None
    """
    print(f"Merhaba, {isim}!")

selamla("Ali")

print("""
💡 Docstring:
   • Fonksiyonların hemen altına yazılır
   • Üç çift tırnak ile başlar
   • Ne yaptığını, parametrelerini açıklar
   • İleriki bölümlerde detaylı göreceğiz
""")

# ============================================
# 9. TODO Yorumları
# ============================================
print("\n" + "="*60)
print("📌 9. TODO Yorumları")
print("-"*60)

# TODO: Burada hata kontrolü eklenecek
# FIXME: Bu kod optimize edilmeli
# HACK: Geçici çözüm, düzeltilecek
# NOTE: Dikkat edilecek önemli nokta

print("""
Özel Yorum Etiketleri:
• TODO: Yapılacak iş
• FIXME: Düzeltilmesi gereken
• HACK: Geçici çözüm
• NOTE: Önemli not
• XXX: Kritik uyarı

💡 Editörler (Cursor, VSCode) bu etiketleri vurgular!
""")

# ============================================
# 10. Yorum Yazma İpuçları
# ============================================
print("\n" + "="*60)
print("📌 10. Yorum Yazma İpuçları")
print("-"*60)

print("""
✅ YAPILMASI GEREKENLER:

1. Karmaşık mantığı açıkla
   # Fibonacci dizisinin 10. elemanını bul
   
2. NEDEN'i açıkla
   # API hız limiti için 1 saniye bekle
   
3. Takım arkadaşlarını düşün
   # Dikkat: Bu fonksiyon veritabanını siler!
   
4. Formülleri açıkla
   # BMI = kilo / (boy^2) formülü
   
5. Önemli kısımları işaretle
   # TODO: Hata kontrolü ekle

❌ YAPILMAMASI GEREKENLER:

1. Aşikar şeyleri yazma
   # x'e 5 ata (GEREKSIZ!)
   
2. Her satırı yorumlama
   # Çok fazla yorum kodu kirletir
   
3. Yalan söyleme
   # Toplama yapar (ama çarpma yapıyorsa ❌)
   
4. Eski yorumları bırakma
   # Güncel olmayan yorumlar kafa karıştırır

💡 İyi kod kendini açıklar, yorum sadece yardımcıdır!
""")

# ============================================
# 11. Kitaptan Örnek
# ============================================
print("\n" + "="*60)
print("📌 11. Kitaptan Örnek")
print("-"*60)

# Say hello to everyone.
print("Hello Python people!")

print("\nYorum Python tarafından görmezden gelindi!")
print("Sadece 'Hello Python people!' yazdırıldı.")

# ============================================
# ÖZET
# ============================================
print("\n" + "="*60)
print("📚 COMMENTS ÖZET")
print("="*60)
print("""
Yorumlar (Comments):

Syntax:
✓ Tek satır: # Bu bir yorum
✓ Çok satır: \"""Çok satırlı yorum\"""
✓ Satır sonunda: print("kod")  # yorum

Özellikler:
✓ Python tarafından çalıştırılmaz
✓ Sadece insanlar için
✓ Kodunuzu açıklar
✓ Takım çalışmasında önemli

Ne Zaman Kullanılır:
✓ Karmaşık mantık
✓ Önemli kararlar
✓ Formüller
✓ TODO/FIXME notları
✓ Fonksiyon açıklamaları

Ne Zaman Kullanılmaz:
✗ Aşikar şeyler
✗ Her satır
✗ Gereksiz açıklamalar

💡 İpuçları:
• NEDEN'i açıkla, NE'yi değil
• Gelecekteki kendinize yazın
• Kısa ve öz tutun
• Güncel tutun
• İyi kod > Çok yorum

Özel Etiketler:
• TODO: Yapılacak
• FIXME: Düzeltilecek
• HACK: Geçici çözüm
• NOTE: Önemli not
""")
print("="*60)
