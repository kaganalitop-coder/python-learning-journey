# ========================================
# CONSTANTS (SABİTLER)
# ========================================

# Constant = Değeri değişmeyen değişken

print("="*60)
print("CONSTANTS (SABİTLER)")
print("="*60)

# ============================================
# 1. Constant Nedir?
# ============================================
print("\n📌 1. Constant (Sabit) Nedir?")
print("-"*60)

print("""
Constant = Programın çalışması boyunca değişmemesi gereken değişken

Özellikler:
• Değeri sabit kalır
• Değiştirilmemeli
• Tüm programda kullanılır
• Python'da özel constant tipi YOK
• Programcılar BÜYÜK HARF kullanarak sabit olduğunu belirtir
""")

# ============================================
# 2. Constant Nasıl Yazılır?
# ============================================
print("\n" + "="*60)
print("📌 2. Constant Nasıl Yazılır?")
print("-"*60)

# KURAL: Tüm harfler BÜYÜK OLUR
MAX_CONNECTIONS = 5000
PI = 3.14159
SPEED_OF_LIGHT = 300_000_000

print(f"MAX_CONNECTIONS = {MAX_CONNECTIONS}")
print(f"PI = {PI}")
print(f"SPEED_OF_LIGHT = {SPEED_OF_LIGHT:,}")

print("\n💡 BÜYÜK HARF = Bu değişkeni değiştirme!")
print("💡 Python engellemez ama programcılar kuraldır.")

# ============================================
# 3. Normal Değişken vs Constant
# ============================================
print("\n" + "="*60)
print("📌 3. Normal Değişken vs Constant")
print("-"*60)

# Normal değişken (küçük harf)
user_count = 10
print(f"Normal değişken: user_count = {user_count}")
user_count = 20  # Değiştirilebilir
print(f"Değiştirildi: user_count = {user_count}")

# Constant (BÜYÜK HARF)
MAX_USERS = 1000
print(f"\nConstant: MAX_USERS = {MAX_USERS}")
print(f"Değiştirilmemeli! (Kural)")

# Teknik olarak değiştirilebilir ama YAPMAYIN!
# MAX_USERS = 2000  # ❌ Yapılmamalı!

print("""
┌─────────────────┬──────────────┬───────────────┐
│   Özellik       │  Değişken    │  Constant     │
├─────────────────┼──────────────┼───────────────┤
│ İsimlendirme    │ küçük_harf   │  BÜYÜK_HARF   │
│ Değiştirilebilir│ Evet ✓       │  Hayır ✗      │
│ Kullanım        │ Geçici       │  Tüm program  │
└─────────────────┴──────────────┴───────────────┘
""")

# ============================================
# 4. Yaygın Constant Örnekleri
# ============================================
print("\n" + "="*60)
print("📌 4. Yaygın Constant Örnekleri")
print("-"*60)

# Matematik sabitleri
PI = 3.141592653589793
E = 2.718281828459045
GOLDEN_RATIO = 1.618033988749895

print("--- Matematik Sabitleri ---")
print(f"PI = {PI}")
print(f"E = {E}")
print(f"Altın Oran = {GOLDEN_RATIO}")

# Fizik sabitleri
SPEED_OF_LIGHT = 299_792_458  # m/s
GRAVITY = 9.81  # m/s²

print("\n--- Fizik Sabitleri ---")
print(f"Işık Hızı = {SPEED_OF_LIGHT:,} m/s")
print(f"Yerçekimi = {GRAVITY} m/s²")

# Uygulama sabitleri
MAX_LOGIN_ATTEMPTS = 3
SESSION_TIMEOUT = 30  # dakika
MAX_FILE_SIZE = 10_485_760  # 10 MB (bytes)

print("\n--- Uygulama Sabitleri ---")
print(f"Maksimum giriş denemesi: {MAX_LOGIN_ATTEMPTS}")
print(f"Oturum zaman aşımı: {SESSION_TIMEOUT} dakika")
print(f"Maksimum dosya boyutu: {MAX_FILE_SIZE:,} bytes")

# ============================================
# 5. Constant Kullanım Alanları
# ============================================
print("\n" + "="*60)
print("📌 5. Constant Kullanım Alanları")
print("-"*60)

# Örnek 1: Daire alanı hesaplama
PI = 3.14159
yaricap = 5
alan = PI * yaricap ** 2
print(f"Daire alanı (r={yaricap}): {alan:.2f}")

# Örnek 2: Giriş kontrolü
MAX_LOGIN_ATTEMPTS = 3
deneme_sayisi = 0

print(f"\n--- Giriş Kontrolü ---")
while deneme_sayisi < MAX_LOGIN_ATTEMPTS:
    deneme_sayisi += 1
    print(f"Deneme {deneme_sayisi}/{MAX_LOGIN_ATTEMPTS}")
    if deneme_sayisi == 2:  # Örnek olarak 2. denemede başarılı
        print("✓ Giriş başarılı!")
        break
else:
    print("✗ Maksimum deneme sayısına ulaşıldı!")

# Örnek 3: Ürün fiyatı (KDV dahil)
KDV_ORANI = 0.20  # %20
urun_fiyati = 100

kdv_tutari = urun_fiyati * KDV_ORANI
toplam_fiyat = urun_fiyati + kdv_tutari

print(f"\n--- Fiyat Hesaplama ---")
print(f"Ürün fiyatı: {urun_fiyati} TL")
print(f"KDV (%{KDV_ORANI*100:.0f}): {kdv_tutari} TL")
print(f"Toplam: {toplam_fiyat} TL")

# ============================================
# 6. Neden Constant Kullanırız?
# ============================================
print("\n" + "="*60)
print("📌 6. Neden Constant Kullanırız?")
print("-"*60)

print("""
Avantajlar:

1. 🔒 Güvenlik:
   Yanlışlıkla değiştirilmesini engeller (kodlama kuralı)
   
2. 📖 Okunabilirlik:
   MAX_USERS daha anlaşılır bir isim
   1000 sayısından daha açıklayıcı
   
3. 🔧 Bakım Kolaylığı:
   Değer değiştiğinde tek yerden değiştirirsiniz
   
4. 🐛 Hata Önleme:
   Sihirli sayılardan kurtulursunuz
   
Örnek:
❌ KÖTÜ:
   if user_count > 1000:  # 1000 nereden geldi?
   
✅ İYİ:
   if user_count > MAX_USERS:  # Açık ve net!
""")

# ============================================
# 7. Magic Numbers (Sihirli Sayılar)
# ============================================
print("\n" + "="*60)
print("📌 7. Magic Numbers'tan Kaçının!")
print("-"*60)

print("❌ KÖTÜ ÖRNEK (Magic Numbers):")
print("""
alan = 3.14159 * 5 ** 2
cevre = 2 * 3.14159 * 5
hacim = (4/3) * 3.14159 * 5 ** 3
# 3.14159 ne? 5 ne? Anlaşılmaz!
""")

print("\n✅ İYİ ÖRNEK (Constants):")
PI = 3.14159
YARICAP = 5
alan = PI * YARICAP ** 2
cevre = 2 * PI * YARICAP
hacim = (4/3) * PI * YARICAP ** 3
print(f"Alan: {alan:.2f}")
print(f"Çevre: {cevre:.2f}")
print(f"Hacim: {hacim:.2f}")
print("# Çok daha açık ve anlaşılır!")

# ============================================
# 8. Birden Fazla Constant
# ============================================
print("\n" + "="*60)
print("📌 8. Birden Fazla Constant Tanımlama")
print("-"*60)

# Genelde dosyanın başında tanımlanır
# Uygulama ayarları
APP_NAME = "Python Öğreniyorum"
APP_VERSION = "1.0.0"
MAX_USERS = 1000
MAX_CONNECTIONS = 5000
TIMEOUT = 30
DEBUG_MODE = True

print(f"Uygulama: {APP_NAME} v{APP_VERSION}")
print(f"Maksimum kullanıcı: {MAX_USERS}")
print(f"Maksimum bağlantı: {MAX_CONNECTIONS}")
print(f"Timeout: {TIMEOUT} saniye")
print(f"Debug modu: {'Açık' if DEBUG_MODE else 'Kapalı'}")

# ============================================
# ÖZET
# ============================================
print("\n" + "="*60)
print("📚 CONSTANTS ÖZET")
print("="*60)
print("""
Constant (Sabit):

Tanım:
✓ Değeri değişmeyen değişken
✓ Tüm program boyunca sabit kalır

Yazım Kuralı:
✓ Tüm harfler BÜYÜK yazılır
✓ Kelimeler _ ile ayrılır
✓ Örnek: MAX_USERS, PI, SPEED_OF_LIGHT

Python'da:
⚠️ Python constant'ı teknik olarak engellemez
⚠️ Sadece bir kodlama kuralıdır
⚠️ Programcılar bu kurala uyar

Neden Kullanırız:
✓ Okunabilirlik artar
✓ Bakımı kolaylaştırır
✓ Hata önler
✓ Magic numbers'tan kurtulur

Yaygın Örnekler:
• PI = 3.14159
• MAX_USERS = 1000
• TIMEOUT = 30
• KDV_ORANI = 0.20

💡 İpucu:
   Programın başında constant'ları tanımlayın
   Değeri hiç değişmeyen her şey constant olabilir
""")
print("="*60)
