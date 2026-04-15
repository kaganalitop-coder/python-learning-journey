# ========================================
# LİSTE METODLARI VE İŞLEMLER
# ========================================
# Ekleme, Çıkarma, Değiştirme

print("="*70)
print("LİSTE METODLARI VE İŞLEMLER")
print("="*70)

# ============================================
# 1. Listeyi Değiştirme
# ============================================
print("\n📌 1. Liste Öğesini Değiştirme")
print("-"*70)

# Tek öğe değiştirme
motorsikletler = ['honda', 'yamaha', 'suzuki']
print(f"Önce: {motorsikletler}")

motorsikletler[0] = 'ducati'
print(f"Sonra: {motorsikletler}")

print("\n💡 İndeks ile erişip değiştirin: liste[0] = 'yeni_değer'")

# Birden fazla öğe değiştirme
sayilar = [1, 2, 3, 4, 5]
print(f"\nÖnce: {sayilar}")
sayilar[0] = 10
sayilar[2] = 30
sayilar[4] = 50
print(f"Sonra: {sayilar}")

# ============================================
# 2. append() - Sona Ekleme
# ============================================
print("\n" + "="*70)
print("📌 2. append() - Sona Ekleme")
print("-"*70)

# Sona öğe ekleme
motorsikletler = ['honda', 'yamaha', 'suzuki']
print(f"Önce: {motorsikletler}")

motorsikletler.append('ducati')
print(f"Sonra: {motorsikletler}")

print("\n💡 append() sona ekler!")

# Boş liste ile başlayıp doldurma
print("\n--- Boş Listeden Başlama ---")
sehirler = []
print(f"Başlangıç: {sehirler}")

sehirler.append('İstanbul')
sehirler.append('Ankara')
sehirler.append('İzmir')
print(f"Son durum: {sehirler}")

# Pratik kullanım: Kullanıcıdan veri alma simülasyonu
print("\n--- Dinamik Liste Oluşturma ---")
favori_meyveler = []
favori_meyveler.append('elma')
favori_meyveler.append('muz')
favori_meyveler.append('çilek')

print(f"Favori meyvelerim: {favori_meyveler}")
print(f"Toplam {len(favori_meyveler)} meyve eklendi")

# ============================================
# 3. insert() - İstediğin Yere Ekleme
# ============================================
print("\n" + "="*70)
print("📌 3. insert() - İstediğin Yere Ekleme")
print("-"*70)

# Başa ekleme
motorsikletler = ['honda', 'yamaha', 'suzuki']
print(f"Önce: {motorsikletler}")

motorsikletler.insert(0, 'ducati')
print(f"Başa eklendi: {motorsikletler}")

# Ortaya ekleme
print(f"\nÖnce: {motorsikletler}")
motorsikletler.insert(2, 'kawasaki')
print(f"Ortaya eklendi: {motorsikletler}")

# Sona ekleme (append gibi)
motorsikletler.insert(len(motorsikletler), 'bmw')
print(f"Sona eklendi: {motorsikletler}")

print("\n💡 insert(indeks, değer) istediğin yere ekler!")
print("   Diğer öğeler sağa kayar")

# Pratik örnek
print("\n--- Öncelikli Görev Ekleme ---")
gorevler = ['Market', 'Spor', 'Kitap okuma']
print(f"Görevler: {gorevler}")

# Acil görev en başa
gorevler.insert(0, '🔥 ACİL: Rapor yaz')
print(f"Acil görev eklendi: {gorevler}")

# ============================================
# 4. del - Silme (İndeks ile)
# ============================================
print("\n" + "="*70)
print("📌 4. del - Silme (İndeks ile)")
print("-"*70)

# İlk öğeyi silme
motorsikletler = ['honda', 'yamaha', 'suzuki', 'ducati']
print(f"Önce: {motorsikletler}")

del motorsikletler[0]
print(f"İlk öğe silindi: {motorsikletler}")

# Son öğeyi silme
print(f"\nÖnce: {motorsikletler}")
del motorsikletler[-1]
print(f"Son öğe silindi: {motorsikletler}")

# Ortadakini silme
sehirler = ['İstanbul', 'Ankara', 'İzmir', 'Bursa']
print(f"\nÖnce: {sehirler}")
del sehirler[1]  # Ankara'yı sil
print(f"İkinci öğe silindi: {sehirler}")

print("\n💡 del liste[indeks] kalıcı olarak siler!")
print("   Silinen değere erişemezsiniz!")

# ============================================
# 5. pop() - Çıkar ve Kullan
# ============================================
print("\n" + "="*70)
print("📌 5. pop() - Çıkar ve Kullan")
print("-"*70)

# Son öğeyi çıkarma
motorsikletler = ['honda', 'yamaha', 'suzuki']
print(f"Önce: {motorsikletler}")

cikarilan = motorsikletler.pop()
print(f"Sonra: {motorsikletler}")
print(f"Çıkarılan: {cikarilan}")

print(f"\nSon motorim {cikarilan.title()} idi.")

# İstediğin öğeyi çıkarma
print("\n--- İndeks ile pop() ---")
motorsikletler = ['honda', 'yamaha', 'suzuki', 'ducati']
print(f"Önce: {motorsikletler}")

ilk_motor = motorsikletler.pop(0)
print(f"Sonra: {motorsikletler}")
print(f"İlk motorim {ilk_motor.title()} idi.")

# Pratik kullanım: Stack (Yığın)
print("\n--- Stack Kullanımı ---")
kitap_yigini = ['Kitap 1', 'Kitap 2', 'Kitap 3']
print(f"Yığın: {kitap_yigini}")

okunan = kitap_yigini.pop()
print(f"Okunan: {okunan}")
print(f"Kalan: {kitap_yigini}")

print("\n💡 pop() çıkarır VE döndürür!")
print("   del'den farkı: değeri kullanabilirsiniz")

# ============================================
# 6. remove() - Değer ile Silme
# ============================================
print("\n" + "="*70)
print("📌 6. remove() - Değer ile Silme")
print("-"*70)

# Değer ile silme
motorsikletler = ['honda', 'yamaha', 'suzuki', 'ducati']
print(f"Önce: {motorsikletler}")

motorsikletler.remove('ducati')
print(f"Sonra: {motorsikletler}")

# Sebep belirterek silme
print("\n--- Sebep Belirterek Silme ---")
motorsikletler = ['honda', 'yamaha', 'suzuki', 'ducati']
print(f"Liste: {motorsikletler}")

cok_pahali = 'ducati'
motorsikletler.remove(cok_pahali)
print(f"Güncel liste: {motorsikletler}")
print(f"\n{cok_pahali.title()} çok pahalı, listeden çıkardım.")

# ⚠️ Dikkat: İlk eşleşeni siler
print("\n--- ⚠️ İlk Eşleşeni Siler ---")
meyveler = ['elma', 'muz', 'elma', 'çilek', 'elma']
print(f"Önce: {meyveler}")

meyveler.remove('elma')
print(f"Sonra: {meyveler}")
print("💡 Sadece ilk 'elma' silindi!")

# Tüm 'elma'ları silme
print("\n--- Tüm 'elma'ları Silme ---")
meyveler = ['elma', 'muz', 'elma', 'çilek', 'elma']
print(f"Önce: {meyveler}")

while 'elma' in meyveler:
    meyveler.remove('elma')

print(f"Sonra: {meyveler}")
print("💡 Tüm 'elma'lar silindi!")

# ============================================
# 7. clear() - Tümünü Sil
# ============================================
print("\n" + "="*70)
print("📌 7. clear() - Tümünü Sil")
print("-"*70)

# Listeyi tamamen temizleme
liste = [1, 2, 3, 4, 5]
print(f"Önce: {liste}")

liste.clear()
print(f"Sonra: {liste}")
print("💡 Liste boş ama hala var!")

# ============================================
# 8. Metodları Karşılaştırma
# ============================================
print("\n" + "="*70)
print("📌 8. Silme Metodlarını Karşılaştırma")
print("-"*70)

print("""
del liste[0]          : İndeks ile sil, değer kaybolur
liste.pop()           : Son öğeyi çıkar ve kullan
liste.pop(0)          : İndeks ile çıkar ve kullan
liste.remove('değer') : Değer ile ilk eşleşeni sil
liste.clear()         : Tümünü sil

Hangisini Kullanmalıyım?

✓ del         : Sadece sil, değer gereksiz
✓ pop()       : Çıkar ve değeri kullan
✓ remove()    : Değeri biliyorum, indeks bilmiyorum
✓ clear()     : Hepsini temizle
""")

# Pratik karşılaştırma
print("\n--- Pratik Karşılaştırma ---")

# del - Değeri umursamadan silme
sayilar1 = [1, 2, 3, 4, 5]
del sayilar1[0]
print(f"del kullanımı: {sayilar1}")

# pop() - Değeri kullanarak silme
sayilar2 = [1, 2, 3, 4, 5]
cikarilan = sayilar2.pop(0)
print(f"pop kullanımı: {sayilar2}, Çıkarılan: {cikarilan}")

# remove() - Değer ile silme
sayilar3 = [1, 2, 3, 4, 5]
sayilar3.remove(3)
print(f"remove kullanımı: {sayilar3}")

# ============================================
# 9. Pratik Örnekler
# ============================================
print("\n" + "="*70)
print("📌 9. Pratik Örnekler")
print("-"*70)

# Örnek 1: Alışveriş listesi
print("--- Alışveriş Listesi ---")
alisveris = []

# Ürün ekleme
alisveris.append('süt')
alisveris.append('ekmek')
alisveris.append('yumurta')
print(f"Liste: {alisveris}")

# Acil ürün en başa
alisveris.insert(0, '🔥 Su')
print(f"Acil eklendi: {alisveris}")

# Aldık, çıkaralım
alinan = alisveris.pop(0)
print(f"Alındı: {alinan}")
print(f"Kalan: {alisveris}")

# Örnek 2: To-Do List
print("\n--- To-Do List ---")
gorevler = ['E-posta yanıtla', 'Rapor yaz', 'Toplantı']
print(f"Görevler: {gorevler}")

# Yeni görev
gorevler.append('Kod oku')
print(f"Yeni görev: {gorevler}")

# İlk görevi tamamla
tamamlanan = gorevler.pop(0)
print(f"✅ Tamamlandı: {tamamlanan}")
print(f"Kalan: {gorevler}")

# Örnek 3: Oyuncu Değişimi
print("\n--- Oyuncu Değişimi ---")
kadrolar = ['Ali', 'Veli', 'Can', 'Mehmet', 'Ahmet']
print(f"İlk kadro: {kadrolar}")

# Sakatlık
sakatli = kadrolar.pop(2)
print(f"⚠️ Sakatlık: {sakatli}")

# Yerine yeni oyuncu
kadrolar.insert(2, 'Yusuf')
print(f"Yeni kadro: {kadrolar}")

# ============================================
# ÖZET
# ============================================
print("\n" + "="*70)
print("📚 LİSTE METODLARI ÖZET")
print("="*70)
print("""
Liste Değiştirme:
✓ liste[0] = 'yeni'      : Öğeyi değiştir

Ekleme:
✓ liste.append(x)        : Sona ekle
✓ liste.insert(i, x)     : İndekse ekle

Silme:
✓ del liste[i]           : İndeks ile sil
✓ liste.pop()            : Son öğeyi çıkar
✓ liste.pop(i)           : İndeks ile çıkar
✓ liste.remove(x)        : Değer ile sil (ilk)
✓ liste.clear()          : Hepsini sil

Farklar:
del      → Sil, değer kaybolur
pop()    → Çıkar ve döndür
remove() → Değer ile sil

💡 İpuçları:
• append() en sık kullanılır
• pop() değeri kullanmak istiyorsanız
• remove() indeks bilmiyorsanız
• del hızlı silme için
• clear() tümünü temizlemek için

Sırada:
→ Liste sıralama (sort)
→ Liste düzenleme
→ Slicing (dilimleme)
""")
print("="*70)
