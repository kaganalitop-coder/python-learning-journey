# ========================================
# İNDEX HATALARI VE İPUÇLARI
# ========================================
# Yaygın hatalar ve çözümleri

print("="*70)
print("İNDEX HATALARI VE İPUÇLARI")
print("="*70)

# ============================================
# 1. Index Errors Nedir?
# ============================================
print("\n📌 1. Index Errors Nedir?")
print("-"*70)

print("""
Index Error:
• Olmayan bir indekse erişmeye çalışmak
• Python'da en yaygın hatalardan biri
• Off-by-one hatası

Sebep:
• Python 0'dan başlar, insanlar 1'den
• Liste boyutunu yanlış hesaplama
• Boş liste

💡 Her programcı index error alır. Normal!
""")

# ============================================
# 2. Temel Index Error
# ============================================
print("\n" + "="*70)
print("📌 2. Temel Index Error")
print("-"*70)

print("""
Örnek:
motorsikletler = ['honda', 'yamaha', 'suzuki']
print(motorsikletler[3])  # ❌ IndexError!

Hata:
IndexError: list index out of range

Neden?
• Liste 3 öğeli: indeks 0, 1, 2
• İndeks 3 yok!
• Python 0'dan başlar!

[0]        [1]        [2]
'honda'    'yamaha'   'suzuki'

💡 İndeks 3 = 4. öğe (yok!)
""")

# Hata örneği
motorsikletler = ['honda', 'yamaha', 'suzuki']
print(f"Liste: {motorsikletler}")
print(f"Uzunluk: {len(motorsikletler)}")
print(f"Geçerli indeksler: 0, 1, 2")

try:
    print(motorsikletler[3])
except IndexError as e:
    print(f"\n⚠️ Hata: {e}")
    print("İndeks 3 yok! Son indeks 2.")

# ============================================
# 3. Off-by-One Hatası
# ============================================
print("\n" + "="*70)
print("📌 3. Off-by-One Hatası")
print("-"*70)

print("""
Off-by-One:
• 1 fazla/eksik indeks kullanma
• İnsanlar 1'den sayar
• Python 0'dan sayar

Örnek:
Liste: ['a', 'b', 'c']

İnsan düşüncesi:
• 1. öğe → 'a'
• 2. öğe → 'b'
• 3. öğe → 'c'

Python gerçeği:
• İndeks 0 → 'a'
• İndeks 1 → 'b'
• İndeks 2 → 'c'

💡 3. öğe indeks 2'de!
""")

# Örnek
liste = ['a', 'b', 'c']
print(f"Liste: {liste}")
print(f"1. öğe (indeks 0): {liste[0]}")
print(f"2. öğe (indeks 1): {liste[1]}")
print(f"3. öğe (indeks 2): {liste[2]}")

print("\n💡 İndeks = Pozisyon - 1")

# ============================================
# 4. Boş Liste Hatası
# ============================================
print("\n" + "="*70)
print("📌 4. Boş Liste Hatası")
print("-"*70)

print("""
Boş listeden öğe almak:

motorsikletler = []
print(motorsikletler[-1])  # ❌ IndexError!

Hata:
IndexError: list index out of range

💡 -1 bile çalışmaz! Liste boş!
""")

# Hata örneği
bos_liste = []
print(f"Boş liste: {bos_liste}")
print(f"Uzunluk: {len(bos_liste)}")

try:
    print(bos_liste[-1])
except IndexError as e:
    print(f"⚠️ Hata: {e}")
    print("Liste boş, öğe yok!")

# Çözüm
print("\n✅ Çözüm: Önce kontrol et")
if bos_liste:
    print(f"Son öğe: {bos_liste[-1]}")
else:
    print("Liste boş!")

# ============================================
# 5. Güvenli Erişim Yöntemleri
# ============================================
print("\n" + "="*70)
print("📌 5. Güvenli Erişim Yöntemleri")
print("-"*70)

liste = ['a', 'b', 'c']

print("--- Yöntem 1: len() Kontrolü ---")
indeks = 5
if indeks < len(liste):
    print(f"Öğe: {liste[indeks]}")
else:
    print(f"Hata: İndeks {indeks} çok büyük!")

print("\n--- Yöntem 2: try-except ---")
try:
    print(liste[10])
except IndexError:
    print("Hata: Geçersiz indeks!")

print("\n--- Yöntem 3: Liste Kontrolü ---")
if liste:  # Boş değil mi?
    print(f"Son öğe: {liste[-1]}")
else:
    print("Liste boş!")

print("\n--- Yöntem 4: get() (Dict için) ---")
# Listeler için yoktur ama dikkat edin
print("💡 Listeler için get() yok, dict'ler için var!")

# ============================================
# 6. Yaygın Hatalar ve Çözümleri
# ============================================
print("\n" + "="*70)
print("📌 6. Yaygın Hatalar ve Çözümleri")
print("-"*70)

print("""
HATA 1: Liste Uzunluğunu Unutma
❌ liste[len(liste)]  # Hata!
✅ liste[len(liste)-1] # Doğru
✅ liste[-1]           # En iyi


HATA 2: Range Hatası
❌ for i in range(len(liste)):
       print(liste[i+1])  # Son indekste hata!
✅ for i in range(len(liste)-1):
       print(liste[i+1])


HATA 3: Liste Boşken -1
❌ liste = []
   print(liste[-1])  # Hata!
✅ if liste:
       print(liste[-1])


HATA 4: Dinamik Liste
❌ for i in range(100):
       print(liste[i])  # Liste 100 öğeli mi?
✅ for item in liste:  # Döngü kullan
       print(item)


HATA 5: İndeks Hesaplama
❌ orta = len(liste) / 2
   print(liste[orta])  # float!
✅ orta = len(liste) // 2
   print(liste[orta])  # int

💡 Her zaman -1 güvenlidir (liste boş değilse)!
""")

# ============================================
# 7. Debug İpuçları
# ============================================
print("\n" + "="*70)
print("📌 7. Debug İpuçları")
print("-"*70)

print("""
Index Error Alınca:

1. Liste boyutunu yazdır
   print(f"Uzunluk: {len(liste)}")
   
2. Listeyi yazdır
   print(f"Liste: {liste}")
   
3. İndeksi yazdır
   print(f"İndeks: {indeks}")
   
4. Geçerli aralığı kontrol et
   print(f"Geçerli: 0-{len(liste)-1}")
   
5. Son öğeyi kontrol et
   print(f"Son öğe: {liste[-1] if liste else 'BOŞ'}")

💡 print() ile debug yapın!
""")

# Debug örneği
liste = ['a', 'b', 'c']
indeks = 5

print("\n--- Debug Bilgileri ---")
print(f"Liste: {liste}")
print(f"Uzunluk: {len(liste)}")
print(f"İstenen indeks: {indeks}")
print(f"Geçerli indeksler: 0 - {len(liste) - 1}")
print(f"İndeks geçerli mi? {0 <= indeks < len(liste)}")

# ============================================
# 8. Liste İpuçları
# ============================================
print("\n" + "="*70)
print("📌 8. Liste İpuçları ve Best Practices")
print("-"*70)

print("""
✅ İYİ PRATİKLER:

1. For döngüsü kullan (indeks yerine)
   ✅ for item in liste:
   ❌ for i in range(len(liste)):
   
2. -1 ile son öğe
   ✅ liste[-1]
   ❌ liste[len(liste)-1]
   
3. Önce kontrol et
   ✅ if liste:
          print(liste[0])
   
4. enumerate() kullan
   ✅ for i, item in enumerate(liste):
   
5. Slicing güvenlidir
   ✅ liste[:10]  # Hata vermez
   
6. len() ile kontrol
   ✅ if indeks < len(liste):

❌ KÖTÜ PRATİKLER:

1. Sabit indeks
   ❌ liste[10]  # Ya 10 yoksa?
   
2. Hesaplı indeks
   ❌ liste[len(liste)]  # Hata!
   
3. Boş liste kontrolsüz
   ❌ liste[0] # Boş olabilir!
   
4. Fazla indeks aritmetiği
   ❌ liste[i + j - k]  # Karışık!

💡 Basit tut, güvenli ol!
""")

# ============================================
# 9. Performans İpuçları
# ============================================
print("\n" + "="*70)
print("📌 9. Performans İpuçları")
print("-"*70)

print("""
Hızlı Liste İşlemleri:

✅ HIZLI:
• liste[0]           → O(1)
• liste[-1]          → O(1)
• liste.append(x)    → O(1)
• len(liste)         → O(1)
• item in liste      → O(n)

❌ YAVAŞ:
• liste.insert(0, x) → O(n)
• liste.remove(x)    → O(n)
• liste.pop(0)       → O(n)
• liste.sort()       → O(n log n)

Büyük Listeler İçin:
• Başa ekleme → collections.deque
• Sık arama → set kullan
• Sık sıralama → heap kullan

💡 Sondan işlem hızlıdır!
""")

# Performans örneği
import time

# Yavaş: Başa ekleme
liste1 = []
start = time.time()
for i in range(10000):
    liste1.insert(0, i)
yavas = time.time() - start

# Hızlı: Sona ekleme
liste2 = []
start = time.time()
for i in range(10000):
    liste2.append(i)
hizli = time.time() - start

print(f"\nBaşa ekleme: {yavas:.4f} sn")
print(f"Sona ekleme: {hizli:.4f} sn")
print(f"Fark: {yavas/hizli:.1f}x daha yavaş")

# ============================================
# 10. Liste Kopyalama Hataları
# ============================================
print("\n" + "="*70)
print("📌 10. Liste Kopyalama Hataları")
print("-"*70)

print("""
Yanlış Kopyalama:

❌ liste2 = liste1
   → Referans kopyası (aynı liste)
   
✅ liste2 = liste1.copy()
   → Gerçek kopya
   
✅ liste2 = liste1[:]
   → Slicing ile kopya
   
✅ liste2 = list(liste1)
   → list() ile kopya

💡 = operatörü kopyalamaz!
""")

# Hata örneği
print("\n--- Yanlış Kopyalama ---")
liste1 = [1, 2, 3]
liste2 = liste1  # Referans!

liste2[0] = 999
print(f"Liste1: {liste1}")  # Değişti!
print(f"Liste2: {liste2}")
print("⚠️ İkisi de değişti!")

# Doğru kopyalama
print("\n--- Doğru Kopyalama ---")
liste3 = [1, 2, 3]
liste4 = liste3.copy()

liste4[0] = 999
print(f"Liste3: {liste3}")  # Değişmedi!
print(f"Liste4: {liste4}")
print("✅ Sadece liste4 değişti!")

# ============================================
# 11. PEP 8 - Liste Stilleri
# ============================================
print("\n" + "="*70)
print("📌 11. PEP 8 - Liste Stil Rehberi")
print("-"*70)

print("""
PEP 8 Kuralları:

1. Liste isimleri çoğul
   ✅ students = ['Ali', 'Ayşe']
   ❌ student = ['Ali', 'Ayşe']
   
2. 4 boşluk girinti
   ✅ for item in liste:
          print(item)
   
3. Satır uzunluğu 79 karakter
   Uzun listeler:
   liste = [
       'öğe1',
       'öğe2',
       'öğe3',
   ]
   
4. Boşluk kullanımı
   ✅ liste[0]
   ❌ liste [0]
   
   ✅ [1, 2, 3]
   ❌ [1,2,3]
   
5. Anlamlı isimler
   ✅ students = ['Ali']
   ❌ x = ['Ali']

💡 Temiz kod = Okunabilir kod!
""")

# ============================================
# 12. Özet: Hatalardan Kaçınma
# ============================================
print("\n" + "="*70)
print("📌 12. Hatalardan Kaçınma Checklist")
print("-"*70)

print("""
Index Error'dan Kaçınma:

□ Liste boş mu kontrol et
  if liste:
  
□ İndeks geçerli mi kontrol et
  if 0 <= indeks < len(liste):
  
□ -1 kullan (son öğe için)
  liste[-1]
  
□ For döngüsü kullan
  for item in liste:
  
□ Slicing kullan (güvenli)
  liste[:10]
  
□ try-except kullan
  try:
      item = liste[i]
  except IndexError:
      print("Hata!")
      
□ Liste uzunluğunu print et
  print(f"Uzunluk: {len(liste)}")
  
□ Listeyi print et
  print(f"Liste: {liste}")

💡 Önce kontrol et, sonra eriş!
""")

# ============================================
# ÖZET
# ============================================
print("\n" + "="*70)
print("📚 INDEX HATALARI VE İPUÇLARI ÖZET")
print("="*70)
print("""
Index Error:

Sebep:
• Olmayan indekse erişme
• Off-by-one hatası
• Boş liste
• Yanlış hesaplama

Önleme:
✓ Liste boş mu? → if liste:
✓ İndeks geçerli mi? → if indeks < len(liste):
✓ -1 kullan → liste[-1]
✓ For döngüsü → for item in liste:
✓ Slicing → liste[:10] (güvenli)
✓ try-except → Hata yakala

Debug:
✓ print(len(liste))
✓ print(liste)
✓ print(indeks)
✓ print(f"Geçerli: 0-{len(liste)-1}")

Best Practices:
✓ For döngüsü kullan
✓ -1 ile son öğe
✓ enumerate() ile indeks
✓ Slicing güvenlidir
✓ Önce kontrol et
✓ Anlamlı isimler
✓ PEP 8'e uy

Kopyalama:
❌ liste2 = liste1        (referans)
✅ liste2 = liste1.copy() (kopya)
✅ liste2 = liste1[:]     (kopya)

Performans:
✓ Sona ekleme → append()
✓ Son öğe → pop()
✗ Başa ekleme → insert(0)
✗ İlk öğe → pop(0)

💡 İpuçları:
• Python 0'dan başlar
• -1 her zaman son öğe
• Boş liste kontrolü önemli
• print() ile debug yap
• Basit tut, güvenli ol
• Hata mesajlarını oku
• Pratik yap!

Tebrikler! 🎉
Listeleri tamamladınız!

Sırada:
→ If/Else koşulları
→ While döngüsü
→ Fonksiyonlar
""")
print("="*70)
