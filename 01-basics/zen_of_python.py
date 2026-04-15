# ========================================
# THE ZEN OF PYTHON
# ========================================
# Python Felsefesi ve İlkeleri
# Tim Peters tarafından yazıldı

print("="*70)
print("THE ZEN OF PYTHON - PYTHON'UN FELSEFESİ")
print("="*70)

# ============================================
# 1. Zen of Python Nedir?
# ============================================
print("\n📌 1. Zen of Python Nedir?")
print("-"*70)

print("""
Zen of Python:
• Python topluluğunun felsefesi
• Tim Peters tarafından yazıldı
• 19 temel ilke içerir
• Python'un tasarım felsefesini özetler
• Her Python programcısının bilmesi gereken ilkeler

Nasıl Görebilirim?
>>> import this
""")

# ============================================
# 2. Zen of Python'u Görelim
# ============================================
print("\n" + "="*70)
print("📌 2. Zen of Python - Orijinal İngilizce")
print("-"*70)

import this

# ============================================
# 3. Zen of Python - Türkçe Çevirisi
# ============================================
print("\n" + "="*70)
print("📌 3. Zen of Python - Türkçe Çevirisi")
print("-"*70)

zen_turkce = """
Python'un Zen'i, Tim Peters tarafından

1.  Güzel, çirkinden iyidir.
2.  Açık, kapalıdan iyidir.
3.  Basit, karmaşıktan iyidir.
4.  Karmaşık, iç içe geçmişten iyidir.
5.  Seyrek, yoğundan iyidir.
6.  Okunabilirlik önemlidir.
7.  Özel durumlar, kuralları çiğneyecek kadar özel değildir.
8.  Pratiklik, saflığı yener.
9.  Hatalar asla sessizce geçmemelidir.
10. Açıkça susturulmadıkça.
11. Belirsizlik karşısında, tahmin etme isteğini reddet.
12. Yapmanın tek bir yolu -- ve tercihen sadece bir bariz yolu -- olmalıdır.
13. Her ne kadar bu yol başta açık olmayabilir, sen Hollandalı değilsen.
14. Şimdi, hiçbir zamandan iyidir.
15. Her ne kadar hiçbir zaman, çoğu zaman *hemen* şimdiden daha iyidir.
16. Açıklaması zor bir uygulama ise, bu kötü bir fikirdir.
17. Açıklaması kolay bir uygulama ise, bu iyi bir fikir olabilir.
18. İsim uzayları harika bir fikirdir -- daha fazla yapalım!
"""

print(zen_turkce)

# ============================================
# 4. Önemli İlkeler - Detaylı Açıklama
# ============================================
print("\n" + "="*70)
print("📌 4. Önemli İlkeler - Detaylı Açıklama")
print("-"*70)

print("""
🔹 1. "Beautiful is better than ugly"
   Güzel, çirkinden iyidir.
   
   ✅ Güzel Kod:
   toplam = fiyat + vergi
   
   ❌ Çirkin Kod:
   t=f+v  # Ne anlama geliyor?
   
   💡 Kodunuz okunabilir ve anlaşılır olmalı!
""")

print("""
🔹 2. "Explicit is better than implicit"
   Açık, kapalıdan iyidir.
   
   ✅ Açık:
   fiyat_kdv_dahil = fiyat * 1.20
   
   ❌ Kapalı:
   fiyat = fiyat * 1.20  # Ne eklendi?
   
   💡 Ne yaptığınızı açıkça belirtin!
""")

print("""
🔹 3. "Simple is better than complex"
   Basit, karmaşıktan iyidir.
   
   ✅ Basit:
   if age >= 18:
       print("Yetişkin")
   
   ❌ Karmaşık:
   print("Yetişkin" if age >= 18 else "Çocuk" if age > 0 else "Hata")
   
   💡 Basit çözüm varsa, onu tercih edin!
""")

print("""
🔹 4. "Readability counts"
   Okunabilirlik önemlidir.
   
   ✅ Okunabilir:
   kullanici_adi = "Ali"
   kullanici_yasi = 25
   kullanici_aktif_mi = True
   
   ❌ Okunamaz:
   kAd="Ali";kYs=25;kAkt=True
   
   💡 6 ay sonra kodunuzu okuyabiliyor musunuz?
""")

print("""
🔹 5. "There should be one way to do it"
   Yapmanın tek bir -- tercihen sadece bir bariz -- yolu olmalıdır.
   
   Örnek: Liste oluşturma
   
   ✅ Python Yolu:
   sayilar = [1, 2, 3, 4, 5]
   
   ❌ Karmaşık Yol:
   sayilar = []
   sayilar.append(1)
   sayilar.append(2)
   ...
   
   💡 Python, işler için en iyi yolu sunar!
""")

print("""
🔹 6. "Now is better than never"
   Şimdi, hiçbir zamandan iyidir.
   
   💡 Mükemmel kod yazmayı beklemeyin!
   • Çalışan kod yazın
   • Sonra geliştirin
   • Sürekli öğrenin
   • Proje yapmaya başlayın
   
   ❌ "Python'u tamamen öğrenene kadar proje yapmayacağım"
   ✅ "Bildiğimle proje yaparken öğreniyorum"
""")

# ============================================
# 5. Pratik Örnekler
# ============================================
print("\n" + "="*70)
print("📌 5. Pratik Örnekler")
print("-"*70)

print("\n--- Örnek 1: Basitlik ---")
# ❌ Karmaşık
def toplam_karmasik(liste):
    sonuc = 0
    for i in range(len(liste)):
        sonuc = sonuc + liste[i]
    return sonuc

# ✅ Basit
def toplam_basit(liste):
    return sum(liste)

sayilar = [1, 2, 3, 4, 5]
print(f"Toplam: {toplam_basit(sayilar)}")
print("💡 Python'un yerleşik fonksiyonlarını kullanın!")

print("\n--- Örnek 2: Okunabilirlik ---")
x = 42  # Örnek değer

# ❌ Okunamaz
# if x>0and x<100and x%2==0:print("Çift")

# ✅ Okunabilir
if x > 0 and x < 100 and x % 2 == 0:
    print("Çift")

# ✅ Daha da iyi
sayı_geçerli = 0 < x < 100
sayı_çift = x % 2 == 0

if sayı_geçerli and sayı_çift:
    print("Geçerli çift sayı")

print("💡 Boşluklar ve mantıklı isimler kullanın!")

print("\n--- Örnek 3: Açıklık ---")
# ❌ Kapalı
def hesapla(x):
    return x * 1.08

# ✅ Açık
def kdv_dahil_fiyat_hesapla(fiyat):
    kdv_orani = 0.08
    return fiyat * (1 + kdv_orani)

fiyat = 100
print(f"KDV dahil: {kdv_dahil_fiyat_hesapla(fiyat):.2f} TL")
print("💡 İsimler ne yaptığınızı söylemeli!")

# ============================================
# 6. Zen İlkelerini Pratikte Kullanma
# ============================================
print("\n" + "="*70)
print("📌 6. Zen İlkelerini Pratikte Kullanma")
print("-"*70)

print("""
Kod Yazarken Kendinize Sorun:

1. Bu kod 6 ay sonra okunabilir mi?
   → Okunabilirlik

2. Bu kodu basitleştirebilir miyim?
   → Basitlik

3. Bu kodun ne yaptığı açık mı?
   → Açıklık

4. Bu çözüm karmaşık mı?
   → Basitlik > Karmaşıklık

5. Daha Python'cu bir yol var mı?
   → Pythonic kod

6. Bu hata sessizce geçiyor mu?
   → Hata yönetimi

💡 İyi kod yazmak = Zen ilkelerine uymak!
""")

# ============================================
# 7. Pythonic Kod Nedir?
# ============================================
print("\n" + "="*70)
print("📌 7. Pythonic Kod Nedir?")
print("-"*70)

print("""
Pythonic = Python'un felsefesine uygun kod

Özellikler:
✓ Basit
✓ Okunabilir
✓ Açık
✓ Elegant (zarif)
✓ Python'un özelliklerini kullanır
""")

print("\n--- Pythonic Örnekler ---")

# Liste içinden çift sayıları bulma

# ❌ Non-Pythonic
cift_sayilar_1 = []
for i in range(len([1, 2, 3, 4, 5])):
    if [1, 2, 3, 4, 5][i] % 2 == 0:
        cift_sayilar_1.append([1, 2, 3, 4, 5][i])

# ✅ Pythonic
cift_sayilar_2 = [x for x in [1, 2, 3, 4, 5] if x % 2 == 0]

print(f"Çift sayılar: {cift_sayilar_2}")
print("💡 List comprehension kullanın!")

# İki listenin kombinasyonu

# ❌ Non-Pythonic
isimler = ["Ali", "Ayşe", "Mehmet"]
yaslar = [25, 30, 35]
for i in range(len(isimler)):
    print(f"{isimler[i]} - {yaslar[i]} yaşında")

# ✅ Pythonic
print("\nPythonic yol:")
for isim, yas in zip(isimler, yaslar):
    print(f"{isim} - {yas} yaşında")

print("💡 zip() fonksiyonunu kullanın!")

# ============================================
# 8. Kod İnceleme Checklist
# ============================================
print("\n" + "="*70)
print("📌 8. Kod İnceleme Checklist")
print("-"*70)

print("""
Kodunuzu Yazarken Kontrol Edin:

✅ Okunabilirlik:
   □ Değişken isimleri anlamlı mı?
   □ Fonksiyon isimleri ne yaptığını söylüyor mu?
   □ Kod girintileri düzgün mü?
   □ Gereksiz karmaşıklık var mı?

✅ Basitlik:
   □ Daha basit bir yol var mı?
   □ Yerleşik fonksiyon kullanabilir miyim?
   □ Kod tekrarı var mı?
   □ Gereksiz değişken var mı?

✅ Açıklık:
   □ Kodun amacı açık mı?
   □ Sihirli sayılar (magic numbers) var mı?
   □ Yorumlar yeterli mi?
   □ Karmaşık mantık açıklanmış mı?

✅ Python Standartları:
   □ PEP 8'e uygun mu?
   □ Pythonic mi?
   □ Python'un özelliklerini kullanıyor muyum?
   □ Best practice'lere uygun mu?
""")

# ============================================
# 9. Anti-Patterns (Kaçınılması Gerekenler)
# ============================================
print("\n" + "="*70)
print("📌 9. Anti-Patterns (Kaçınılması Gerekenler)")
print("-"*70)

print("""
❌ YAPMAYIN:

1. Tek harfli değişkenler (döngüler hariç)
   x = 100  # Ne anlama geliyor?
   fiyat = 100  # ✅ Daha iyi

2. Sihirli sayılar
   sonuc = fiyat * 1.20  # 1.20 ne?
   KDV_ORANI = 0.20  # ✅ Daha iyi
   sonuc = fiyat * (1 + KDV_ORANI)

3. Aşırı karmaşık satırlar
   # ❌ 5 işlemi bir satırda
   # ✅ Adım adım yapın

4. Yorumsuz karmaşık kod
   # Karmaşık algoritmayı açıklayın!

5. Hata yönetimi yapmamak
   # Hatalar sessizce geçmemeli!

💡 Zen ilkelerine uyun, temiz kod yazın!
""")

# ============================================
# 10. Öğrenme Yolculuğunuzda Zen
# ============================================
print("\n" + "="*70)
print("📌 10. Öğrenme Yolculuğunuzda Zen")
print("-"*70)

print("""
Python Öğrenirken:

1. "Now is better than never"
   → Mükemmel olmayı beklemeyin, başlayın!
   
2. "Simple is better than complex"
   → Basit çözümlerle başlayın
   
3. "Readability counts"
   → Temiz kod yazma alışkanlığı kazanın
   
4. "Beautiful is better than ugly"
   → Kodunuzu güzelleştirmeye çalışın
   
5. Sürekli pratik yapın
   → Proje yapmaya devam edin

💡 Her gün biraz daha iyi kod yazın!
""")

# ============================================
# ÖZET
# ============================================
print("\n" + "="*70)
print("📚 ZEN OF PYTHON ÖZET")
print("="*70)
print("""
Zen of Python:

Ana İlkeler:
✓ Güzel > Çirkin
✓ Açık > Kapalı
✓ Basit > Karmaşık
✓ Okunabilirlik önemli
✓ Tek bir bariz yol
✓ Şimdi > Hiçbir zaman

Pratik Tavsiyeler:
✓ Anlamlı isimler kullanın
✓ Basit çözümler tercih edin
✓ Pythonic kod yazın
✓ PEP 8'e uyun
✓ Yerleşik fonksiyonları kullanın
✓ Kod tekrarından kaçının

Kendinize Sorun:
• Bu kod okunabilir mi?
• Daha basit yapabilir miyim?
• 6 ay sonra anlayabilir miyim?
• Pythonic mi?

Komut:
>>> import this

💡 Zen ilkeleri, iyi Python kodu yazmanın temelidir!
💡 Her proje, daha iyi kod yazma fırsatıdır!
💡 Sürekli öğrenin, pratik yapın, gelişin!
""")
print("="*70)

# Easter Egg: Zen of Python'un şifresi
print("\n🎁 BONUS: Easter Egg!")
print("-"*70)
print("""
Zen of Python'un kendisi bir Easter Egg!

Kod:
>>> import this

Bu kod, şifreli bir metni ROT13 ile çözer!

Dosya: Lib/this.py
Şifreli mesaj kodun içinde!

💡 Python, küçük sürprizlerle doludur!
""")
