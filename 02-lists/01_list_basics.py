# ========================================
# LİSTELER (LISTS) - TEMEL KAVRAMLAR
# ========================================
# Liste: Sıralı veri koleksiyonu

print("="*70)
print("LİSTELER (LISTS) - TEMEL KAVRAMLAR")
print("="*70)

# ============================================
# 1. Liste Nedir?
# ============================================
print("\n📌 1. Liste Nedir?")
print("-"*70)

print("""
Liste (List):
• Birden fazla öğeyi tek bir değişkende saklama
• Sıralı koleksiyon
• Değiştirilebilir (mutable)
• Farklı tiplerde öğeler içerebilir
• Köşeli parantez [] ile gösterilir

Özellikler:
✓ Sıralı (ordered)
✓ Değiştirilebilir (mutable)
✓ İndekslenebilir (indexed)
✓ Tekrarlayan öğeler olabilir
✓ Farklı veri tiplerini içerebilir
""")

# ============================================
# 2. Liste Oluşturma
# ============================================
print("\n" + "="*70)
print("📌 2. Liste Oluşturma")
print("-"*70)

# Boş liste
bos_liste = []
print(f"Boş liste: {bos_liste}")

# String listesi
meyveler = ['elma', 'armut', 'muz', 'çilek']
print(f"\nMeyveler: {meyveler}")

# Sayı listesi
sayilar = [1, 2, 3, 4, 5]
print(f"Sayılar: {sayilar}")

# Karışık tip liste
karisik = ['Ali', 25, True, 3.14, 'Python']
print(f"Karışık: {karisik}")

# Liste içinde liste
matris = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f"Matris: {matris}")

print("\n💡 Liste oluşturmak için köşeli parantez [] kullanılır!")

# ============================================
# 3. Liste Uzunluğu
# ============================================
print("\n" + "="*70)
print("📌 3. Liste Uzunluğu")
print("-"*70)

sehirler = ['İstanbul', 'Ankara', 'İzmir', 'Bursa', 'Antalya']
print(f"Şehirler: {sehirler}")
print(f"Kaç şehir var? {len(sehirler)} şehir")

print("\n💡 len() fonksiyonu liste uzunluğunu verir!")

# ============================================
# 4. Listeye Erişim (Indexing)
# ============================================
print("\n" + "="*70)
print("📌 4. Listeye Erişim (Indexing)")
print("-"*70)

bisikletler = ['trek', 'cannondale', 'redline', 'specialized']
print(f"Bisikletler: {bisikletler}")

print("\n--- Pozitif İndeks ---")
print(f"İlk bisiklet (indeks 0): {bisikletler[0]}")
print(f"İkinci bisiklet (indeks 1): {bisikletler[1]}")
print(f"Üçüncü bisiklet (indeks 2): {bisikletler[2]}")
print(f"Dördüncü bisiklet (indeks 3): {bisikletler[3]}")

print("\n💡 Python'da indeksler 0'dan başlar!")
print("   [0]  [1]  [2]  [3]")
print("    ↓    ↓    ↓    ↓")
print(f"   {bisikletler}")

# ============================================
# 5. Negatif İndeks
# ============================================
print("\n" + "="*70)
print("📌 5. Negatif İndeks")
print("-"*70)

print(f"Bisikletler: {bisikletler}")

print("\n--- Negatif İndeks (Sondan Başlar) ---")
print(f"Son bisiklet (indeks -1): {bisikletler[-1]}")
print(f"Sondan ikinci (indeks -2): {bisikletler[-2]}")
print(f"Sondan üçüncü (indeks -3): {bisikletler[-3]}")
print(f"Sondan dördüncü (indeks -4): {bisikletler[-4]}")

print("\n💡 Negatif indeks sondan başlar!")
print("   [-4]   [-3]   [-2]   [-1]")
print("     ↓      ↓      ↓      ↓")
print(f"    {bisikletler}")

# ============================================
# 6. Liste Öğelerini Kullanma
# ============================================
print("\n" + "="*70)
print("📌 6. Liste Öğelerini Kullanma")
print("-"*70)

# String metodlarıyla kullanma
print(f"İlk bisiklet (büyük harf): {bisikletler[0].title()}")
print(f"Son bisiklet (büyük harf): {bisikletler[-1].upper()}")

# F-string ile kullanma
mesaj = f"İlk bisikletim {bisikletler[0].title()} idi."
print(f"\n{mesaj}")

# Matematiksel işlemler
fiyatlar = [1500, 2000, 1800, 2200]
print(f"\nFiyatlar: {fiyatlar}")
print(f"İlk ürün fiyatı: {fiyatlar[0]} TL")
print(f"KDV dahil: {fiyatlar[0] * 1.20} TL")

# ============================================
# 7. Gerçek Hayat Örnekleri
# ============================================
print("\n" + "="*70)
print("📌 7. Gerçek Hayat Örnekleri")
print("-"*70)

# Alışveriş listesi
print("--- Alışveriş Listesi ---")
alisveris = ['süt', 'ekmek', 'yumurta', 'peynir', 'zeytin']
print(f"Alışveriş listesi: {alisveris}")
print(f"Toplam {len(alisveris)} ürün alınacak")
print(f"İlk alınacak: {alisveris[0]}")

# Öğrenci notları
print("\n--- Öğrenci Notları ---")
notlar = [85, 90, 78, 92, 88]
print(f"Notlar: {notlar}")
print(f"İlk sınav: {notlar[0]}")
print(f"Son sınav: {notlar[-1]}")
print(f"Ortalama: {sum(notlar) / len(notlar):.2f}")

# Takım oyuncuları
print("\n--- Takım Oyuncuları ---")
oyuncular = ['Ahmet', 'Mehmet', 'Ayşe', 'Fatma', 'Ali']
print(f"Takım: {oyuncular}")
print(f"Kaptan: {oyuncular[0]}")
print(f"Kaleci: {oyuncular[-1]}")

# To-Do listesi
print("\n--- Yapılacaklar Listesi ---")
yapilacaklar = [
    'Python çalış',
    'Proje yap',
    'Kod oku',
    'Alıştırma çöz'
]
print("Bugün yapılacaklar:")
for i, gorev in enumerate(yapilacaklar, 1):
    print(f"  {i}. {gorev}")

# ============================================
# 8. Liste Özellikleri
# ============================================
print("\n" + "="*70)
print("📌 8. Liste Özellikleri")
print("-"*70)

# Sıralı
print("--- Sıralı (Ordered) ---")
liste1 = [1, 2, 3]
liste2 = [3, 2, 1]
print(f"Liste 1: {liste1}")
print(f"Liste 2: {liste2}")
print(f"Aynı mı? {liste1 == liste2}")  # False - sıra önemli!

# Tekrarlayan öğeler
print("\n--- Tekrarlayan Öğeler Olabilir ---")
tekrar = ['elma', 'armut', 'elma', 'muz', 'elma']
print(f"Liste: {tekrar}")
print(f"'elma' kaç tane? {tekrar.count('elma')}")

# Farklı tipler
print("\n--- Farklı Tipler ---")
karisik_liste = [
    'Metin',           # string
    42,                # integer
    3.14,              # float
    True,              # boolean
    [1, 2, 3],         # list
    None               # None
]
print(f"Karışık liste: {karisik_liste}")
print("💡 Liste her tür veriyi içerebilir!")

# ============================================
# 9. Liste İçinde Liste
# ============================================
print("\n" + "="*70)
print("📌 9. Liste İçinde Liste (Nested Lists)")
print("-"*70)

# İç içe liste
ogrenciler = [
    ['Ali', 25, 'İstanbul'],
    ['Ayşe', 22, 'Ankara'],
    ['Mehmet', 27, 'İzmir']
]

print("Öğrenci Listesi:")
print(ogrenciler)

print("\n--- Erişim ---")
print(f"İlk öğrenci: {ogrenciler[0]}")
print(f"İlk öğrencinin adı: {ogrenciler[0][0]}")
print(f"İlk öğrencinin yaşı: {ogrenciler[0][1]}")
print(f"İlk öğrencinin şehri: {ogrenciler[0][2]}")

# Matris örneği
print("\n--- Matris Örneği ---")
matris = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("Matris:")
for satir in matris:
    print(satir)

print(f"\nOrta eleman: {matris[1][1]}")  # 5

# ============================================
# 10. Liste Kopyalama
# ============================================
print("\n" + "="*70)
print("📌 10. Liste Kopyalama")
print("-"*70)

# ❌ Yanlış yol - Referans kopyalama
liste_orjinal = [1, 2, 3]
liste_yanlis = liste_orjinal  # Referans kopyası!
liste_yanlis[0] = 999

print("--- Yanlış Kopyalama ---")
print(f"Orijinal: {liste_orjinal}")  # [999, 2, 3] - Değişti!
print(f"Kopya: {liste_yanlis}")      # [999, 2, 3]
print("⚠️ İkisi de değişti!")

# ✅ Doğru yol - Gerçek kopyalama
liste_orjinal2 = [1, 2, 3]
liste_dogru = liste_orjinal2.copy()  # Gerçek kopya
liste_dogru[0] = 999

print("\n--- Doğru Kopyalama ---")
print(f"Orijinal: {liste_orjinal2}")  # [1, 2, 3] - Değişmedi!
print(f"Kopya: {liste_dogru}")         # [999, 2, 3]
print("✅ Sadece kopya değişti!")

# ============================================
# 11. Liste Kontrolleri
# ============================================
print("\n" + "="*70)
print("📌 11. Liste Kontrolleri")
print("-"*70)

meyveler = ['elma', 'armut', 'muz', 'çilek']

# in operatörü
print("--- 'in' Operatörü ---")
print(f"Meyveler: {meyveler}")
print(f"'elma' var mı? {'elma' in meyveler}")
print(f"'üzüm' var mı? {'üzüm' in meyveler}")

# not in operatörü
print("\n--- 'not in' Operatörü ---")
print(f"'üzüm' yok mu? {'üzüm' not in meyveler}")

# Kullanım örneği
if 'elma' in meyveler:
    print("\n✅ Elma listede var!")

if 'üzüm' not in meyveler:
    print("❌ Üzüm listede yok!")

# ============================================
# 12. Liste İstatistikleri
# ============================================
print("\n" + "="*70)
print("📌 12. Liste İstatistikleri")
print("-"*70)

sayilar = [85, 92, 78, 90, 88, 95, 82]
print(f"Notlar: {sayilar}")

print(f"\nToplam: {sum(sayilar)}")
print(f"En yüksek: {max(sayilar)}")
print(f"En düşük: {min(sayilar)}")
print(f"Ortalama: {sum(sayilar) / len(sayilar):.2f}")
print(f"Öğrenci sayısı: {len(sayilar)}")

# ============================================
# ÖZET
# ============================================
print("\n" + "="*70)
print("📚 LİSTELER ÖZET")
print("="*70)
print("""
Liste (List):

Oluşturma:
✓ Boş liste: []
✓ Dolu liste: ['a', 'b', 'c']
✓ Karışık tip: ['Ali', 25, True]

Erişim:
✓ İlk öğe: liste[0]
✓ Son öğe: liste[-1]
✓ İkinci öğe: liste[1]
✓ Sondan ikinci: liste[-2]

Özellikler:
✓ Sıralı (ordered)
✓ Değiştirilebilir (mutable)
✓ İndeksli (indexed)
✓ Tekrarlayan öğeler olabilir
✓ Farklı tipler içerebilir

Fonksiyonlar:
✓ len(liste) - Uzunluk
✓ sum(liste) - Toplam
✓ max(liste) - En büyük
✓ min(liste) - En küçük

Operatörler:
✓ in - İçinde mi?
✓ not in - İçinde değil mi?

💡 İpuçları:
• İndeksler 0'dan başlar
• Negatif indeks sondan başlar
• Liste kopyalarken .copy() kullan
• Anlamlı liste isimleri kullan (çoğul!)
• Liste içinde liste olabilir

Sırada:
→ Liste değiştirme
→ Ekleme/çıkarma işlemleri
→ Liste metodları
""")
print("="*70)
