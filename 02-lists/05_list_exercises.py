# ========================================
# LİSTE ALIŞTIRMALARI
# ========================================
# Pratik yaparak öğren!

print("="*70)
print("LİSTE ALIŞTIRMALARI")
print("="*70)

# ============================================
# ALIŞTIRMA 1: İsimler
# ============================================
print("\n" + "="*70)
print("📝 Alıştırma 1: İsimler")
print("-"*70)
print("""
Görev:
1. Arkadaşlarınızın isimlerini içeren bir liste oluşturun
2. Her arkadaşınızın ismini tek tek yazdırın
3. Her isme özel bir mesaj ekleyin
""")

isimler = ['Ali', 'Ayşe', 'Mehmet', 'Zeynep']

print("\n✅ Çözüm:")
for isim in isimler:
    print(f"Merhaba, {isim}!")

# ============================================
# ALIŞTIRMA 2: Ulaşım Araçları
# ============================================
print("\n" + "="*70)
print("📝 Alıştırma 2: Ulaşım Araçları")
print("-"*70)
print("""
Görev:
1. Favori ulaşım araçlarınızı içeren bir liste oluşturun
2. Her biri için bir cümle yazın
   "I would like to own a Honda motorcycle."
""")

ulasim = ['motorsiklet', 'araba', 'bisiklet']

print("\n✅ Çözüm:")
for arac in ulasim:
    print(f"Bir {arac} sahibi olmak isterdim.")

# ============================================
# ALIŞTIRMA 3: Konuk Listesi
# ============================================
print("\n" + "="*70)
print("📝 Alıştırma 3: Konuk Listesi")
print("-"*70)
print("""
Görev:
1. Yemeğe davet etmek istediğiniz 3 kişilik liste
2. Her birine davetiye mesajı yazdırın
""")

konuklar = ['Einstein', 'Tesla', 'Atatürk']

print("\n✅ Çözüm:")
for konuk in konuklar:
    print(f"Sayın {konuk}, yemeğe davetlisiniz!")

# ============================================
# ALIŞTIRMA 4: Değişen Konuk Listesi
# ============================================
print("\n" + "="*70)
print("📝 Alıştırma 4: Değişen Konuk Listesi")
print("-"*70)
print("""
Görev:
1. Bir konuk gelemeyecek
2. Bu konuğu söyleyin
3. Yerine yeni konuk ekleyin
4. Yeni davetiyeler gönderin
""")

konuklar = ['Einstein', 'Tesla', 'Atatürk']
print(f"Orijinal konuklar: {konuklar}")

# Gelemeyecek konuk
gelemeyecek = konuklar[1]  # Tesla
print(f"\n{gelemeyecek} gelemeyecek. 😔")

# Yerine yeni konuk
konuklar[1] = 'Newton'
print(f"Yeni konuk listesi: {konuklar}")

print("\n✅ Yeni Davetiyeler:")
for konuk in konuklar:
    print(f"Sayın {konuk}, yemeğe davetlisiniz!")

# ============================================
# ALIŞTIRMA 5: Daha Fazla Konuk
# ============================================
print("\n" + "="*70)
print("📝 Alıştırma 5: Daha Fazla Konuk")
print("-"*70)
print("""
Görev:
1. Daha büyük masa buldunuz
2. Başa, ortaya ve sona birer konuk ekleyin
3. Yeni davetiyeler gönderin
""")

konuklar = ['Einstein', 'Newton', 'Atatürk']
print(f"Önceki konuklar: {konuklar}")

print("\nMüjde! Daha büyük masa buldum!")

# Eklemeler
konuklar.insert(0, 'Galileo')       # Başa
konuklar.insert(2, 'Curie')         # Ortaya
konuklar.append('Da Vinci')         # Sona

print(f"Yeni konuk listesi: {konuklar}")

print("\n✅ Yeni Davetiyeler:")
for konuk in konuklar:
    print(f"Sayın {konuk}, yemeğe davetlisiniz!")

print(f"\nToplam {len(konuklar)} konuk davetli!")

# ============================================
# ALIŞTIRMA 6: Daraltan Konuk Listesi
# ============================================
print("\n" + "="*70)
print("📝 Alıştırma 6: Daraltan Konuk Listesi")
print("-"*70)
print("""
Görev:
1. Masa gelmeyecek, sadece 2 kişilik yer var
2. pop() ile konukları çıkarın
3. Her çıkana özür dileyin
4. Kalan 2 konuğa hala davetli olduklarını söyleyin
5. del ile listeyi boşaltın
""")

konuklar = ['Galileo', 'Einstein', 'Curie', 'Newton', 'Atatürk', 'Da Vinci']
print(f"Toplam {len(konuklar)} konuk: {konuklar}")

print("\nÜzgünüm, masa gelmeyecek. Sadece 2 kişilik yer var. 😔")

# 4 konuğu çıkar
while len(konuklar) > 2:
    cikarilan = konuklar.pop()
    print(f"Özür dilerim {cikarilan}, yer kalmadı.")

print(f"\n✅ Kalan konuklar:")
for konuk in konuklar:
    print(f"Sayın {konuk}, hala davetlisiniz!")

# Listeyi boşalt
del konuklar[0]
del konuklar[0]
print(f"\nBoş liste: {konuklar}")

# ============================================
# ALIŞTIRMA 7: Dünyanın Gezi Yerleri
# ============================================
print("\n" + "="*70)
print("📝 Alıştırma 7: Gezi Yerleri")
print("-"*70)
print("""
Görev:
1. Görmek istediğiniz 5 yer
2. Orijinal sırayla yazdırın
3. sorted() ile alfabetik gösterin (orijinali koruyun)
4. Hala orijinal sırada olduğunu gösterin
5. sorted(reverse=True) ile ters alfabetik
6. reverse() ile sırayı tersine çevirin
7. Tekrar reverse() ile eski haline
8. sort() ile alfabetik (kalıcı)
9. sort(reverse=True) ile ters alfabetik (kalıcı)
""")

yerler = ['Tokyo', 'Paris', 'New York', 'İstanbul', 'Roma']

print("1. Orijinal liste:")
print(yerler)

print("\n2. Alfabetik (geçici):")
print(sorted(yerler))

print("\n3. Hala orijinal:")
print(yerler)

print("\n4. Ters alfabetik (geçici):")
print(sorted(yerler, reverse=True))

print("\n5. reverse() ile:")
yerler.reverse()
print(yerler)

print("\n6. Tekrar reverse():")
yerler.reverse()
print(yerler)

print("\n7. sort() ile alfabetik (kalıcı):")
yerler.sort()
print(yerler)

print("\n8. sort(reverse=True) ile (kalıcı):")
yerler.sort(reverse=True)
print(yerler)

# ============================================
# ALIŞTIRMA 8: Akşam Yemeği Davetlileri Sayısı
# ============================================
print("\n" + "="*70)
print("📝 Alıştırma 8: Davetli Sayısı")
print("-"*70)
print("""
Görev:
Önceki alıştırmalardaki her konuk listesi için
kaç kişi davet ettiğinizi yazdırın.
""")

# Her alıştırmadan
liste1 = ['Einstein', 'Tesla', 'Atatürk']
liste2 = ['Einstein', 'Newton', 'Atatürk']
liste3 = ['Galileo', 'Einstein', 'Curie', 'Newton', 'Atatürk', 'Da Vinci']

print(f"Alıştırma 3: {len(liste1)} kişi")
print(f"Alıştırma 4: {len(liste2)} kişi")
print(f"Alıştırma 5: {len(liste3)} kişi")

# ============================================
# ALIŞTIRMA 9: Pizza Sıralama
# ============================================
print("\n" + "="*70)
print("📝 Alıştırma 9: Pizza Sıralama")
print("-"*70)
print("""
Görev:
1. 5 favori pizza çeşidi
2. Orijinal sırayla
3. Alfabetik sırayla
4. Ters alfabetik sırayla
""")

pizzalar = ['Margarita', 'Pepperoni', 'Vejeteryan', 'Karışık', 'Sucuklu']

print("Orijinal:")
print(pizzalar)

print("\nAlfabetik:")
print(sorted(pizzalar))

print("\nTers alfabetik:")
print(sorted(pizzalar, reverse=True))

# ============================================
# ALIŞTIRMA 10: İlk 3 ve Son 3
# ============================================
print("\n" + "="*70)
print("📝 Alıştırma 10: İlk 3 ve Son 3")
print("-"*70)
print("""
Görev:
1-20 arası sayı listesi oluşturun
İlk 3, orta 3 ve son 3'ü yazdırın
""")

sayilar = list(range(1, 21))

print(f"Tüm sayılar: {sayilar}")
print(f"İlk 3: {sayilar[:3]}")
print(f"Orta 3: {sayilar[8:11]}")
print(f"Son 3: {sayilar[-3:]}")

# ============================================
# ALIŞTIRMA 11: Pizzalarım
# ============================================
print("\n" + "="*70)
print("📝 Alıştırma 11: Pizza Listesi")
print("-"*70)
print("""
Görev:
1. Favori pizzalarınızın listesi
2. for döngüsüyle her birini yazdırın
3. "I like pepperoni pizza" şeklinde
4. Liste dışında genel bir mesaj
""")

pizzalar = ['margarita', 'pepperoni', 'sucuklu']

print("✅ Çözüm:")
for pizza in pizzalar:
    print(f"I like {pizza} pizza.")

print("\nI really love pizza!")

# ============================================
# ALIŞTIRMA 12: Hayvanlar
# ============================================
print("\n" + "="*70)
print("📝 Alıştırma 12: Ortak Özellikleri Olan Hayvanlar")
print("-"*70)
print("""
Görev:
1. Ortak özelliği olan 3 hayvan listesi
2. Her biri için bir cümle
3. "A dog would make a great pet"
4. Liste dışında ortak özellik
""")

hayvanlar = ['köpek', 'kedi', 'tavşan']

print("✅ Çözüm:")
for hayvan in hayvanlar:
    print(f"Bir {hayvan} harika bir evcil hayvan olur.")

print("\nBu hayvanların hepsi harika evcil hayvan!")

# ============================================
# BONUS ALIŞTIRMA 13: Notlar
# ============================================
print("\n" + "="*70)
print("📝 BONUS: Not Analizi")
print("-"*70)
print("""
Görev:
1. 10 adet not oluşturun
2. En yüksek 3 notu bulun
3. En düşük 3 notu bulun
4. Ortalama hesaplayın
5. Geçme notunun üzerindeki notları bulun (60+)
""")

notlar = [85, 92, 78, 95, 88, 72, 90, 65, 82, 87]
print(f"Notlar: {notlar}")

# En yüksek 3
sirali = sorted(notlar, reverse=True)
print(f"\nEn yüksek 3: {sirali[:3]}")

# En düşük 3
print(f"En düşük 3: {sorted(notlar)[:3]}")

# Ortalama
ortalama = sum(notlar) / len(notlar)
print(f"Ortalama: {ortalama:.2f}")

# 60+ notlar
gecenler = [not_ for not_ in notlar if not_ >= 60]
print(f"Geçenler (60+): {gecenler}")
print(f"Geçen sayısı: {len(gecenler)}/{len(notlar)}")

# ============================================
# BONUS ALIŞTIRMA 14: Alışveriş Sepeti
# ============================================
print("\n" + "="*70)
print("📝 BONUS: Alışveriş Sepeti")
print("-"*70)
print("""
Görev:
Alışveriş sepeti simülasyonu:
1. Boş sepet ile başla
2. 5 ürün ekle
3. 2 ürün çıkar
4. Sepeti görüntüle
5. Toplam ürün sayısını göster
""")

sepet = []
print(f"Sepet: {sepet}")

# Ürün ekleme
urunler_ekle = ['Süt', 'Ekmek', 'Peynir', 'Zeytin', 'Domates']
for urun in urunler_ekle:
    sepet.append(urun)
    print(f"✅ {urun} sepete eklendi")

print(f"\nSepet: {sepet}")

# Ürün çıkarma
sepet.remove('Domates')
print(f"❌ Domates çıkarıldı")

cikarilan = sepet.pop(0)
print(f"❌ {cikarilan} çıkarıldı")

print(f"\nSon sepet: {sepet}")
print(f"Toplam {len(sepet)} ürün")

# ============================================
# ÖZET
# ============================================
print("\n" + "="*70)
print("📚 ALIŞTIRMALAR ÖZET")
print("="*70)
print("""
Tebrikler! Tamamladığınız alıştırmalar:

✓ Liste oluşturma
✓ Liste elemanlarına erişim
✓ append() ile ekleme
✓ insert() ile belirli yere ekleme
✓ del ile silme
✓ pop() ile çıkarma
✓ remove() ile değer ile silme
✓ sort() ile kalıcı sıralama
✓ sorted() ile geçici sıralama
✓ reverse() ile ters çevirme
✓ len() ile uzunluk
✓ Slicing ile dilimleme
✓ for döngüsü ile listeyi gezme

🎯 Şimdi Ne Yapmalı?

1. Bu alıştırmaları kendi verilerinizle yapın
2. Değişik senaryolar deneyin
3. Hataları görmekten korkmayın
4. Kendi alıştırmalarınızı oluşturun

💡 Pratik = Öğrenme
Her gün biraz pratik yapın!

Sırada:
→ Döngüler (for, while)
→ Koşullar (if, else, elif)
→ Fonksiyonlar
""")
print("="*70)
