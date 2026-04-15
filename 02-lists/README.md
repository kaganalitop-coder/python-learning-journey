# 📋 Listeler (Lists)

Bu bölümde Python'da listeleri detaylı bir şekilde öğreneceksiniz.

## 📚 İçerik

### 1. Liste Temelleri (`01_list_basics.py`)
- Liste nedir?
- Liste oluşturma
- Liste uzunluğu
- İndeksleme (pozitif ve negatif)
- Liste öğelerini kullanma
- Gerçek hayat örnekleri

### 2. Liste Metodları (`02_list_methods.py`)
- Liste öğesini değiştirme
- `append()` - Sona ekleme
- `insert()` - İstediğin yere ekleme
- `del` - İndeks ile silme
- `pop()` - Çıkar ve kullan
- `remove()` - Değer ile silme
- `clear()` - Tümünü sil

### 3. Liste Düzenleme (`03_list_organization.py`)
- `sort()` - Kalıcı sıralama
- `sorted()` - Geçici sıralama
- `reverse()` - Tersine çevirme
- Özel sıralama (key parametresi)
- Pratik örnekler

### 4. Liste Dilimleme (`04_list_slicing.py`)
- Slicing nedir?
- Temel slicing
- Negatif indekslerle slicing
- Step (adım) kullanımı
- Pratik örnekler
- Slicing ile kopyalama

### 5. Alıştırmalar (`05_list_exercises.py`)
- 14 pratik alıştırma
- Gerçek hayat senaryoları
- Çözümlü örnekler

### 6. For Döngüleri (`06_for_loops.py`) ⭐ YENİ
- For döngüsü nedir?
- Döngü nasıl çalışır?
- Indentation (girinti) kuralları
- Yaygın girinti hataları
- İç içe döngüler
- enumerate() kullanımı

### 7. Range ve Sayılar (`07_range_numbers.py`) ⭐ YENİ
- range() fonksiyonu
- Sayısal listeler oluşturma
- min(), max(), sum() fonksiyonları
- Kareler ve küpler
- Büyük sayılarla çalışma
- Matematiksel işlemler

### 8. List Comprehensions (`08_list_comprehensions.py`) ⭐ YENİ
- List comprehension nedir?
- Tek satırda liste oluşturma
- Koşullu comprehension
- Dictionary ve Set comprehension
- Performans karşılaştırması
- Ne zaman kullanmalı?

### 9. Tuples (`09_tuples.py`) ⭐ YENİ
- Tuple nedir?
- Liste vs Tuple
- Değiştirilemez (immutable) yapı
- Tuple unpacking
- Pratik kullanım alanları
- Performans avantajları

### 10. Hatalar ve İpuçları (`10_tips_and_errors.py`) ⭐ YENİ
- Index hataları
- Off-by-one hatası
- Güvenli erişim yöntemleri
- Debug teknikleri
- PEP 8 stil rehberi
- Best practices

## 🎯 Öğrenme Hedefleri

Bu bölümü tamamladığınızda:
- ✅ Liste oluşturabilecek
- ✅ Liste öğelerine erişebilecek
- ✅ Liste metodlarını kullanabilecek
- ✅ Listeyi sıralayabilecek
- ✅ Slicing ile listeyi dilimleyebilecek
- ✅ Liste kopyalayabilecek
- ✅ For döngüsü kullanabilecek
- ✅ range() ile sayısal listeler oluşturabilecek
- ✅ List comprehension yazabilecek
- ✅ Tuple kullanabilecek
- ✅ Index hatalarını önleyebileceksiniz

## 🚀 Nasıl Çalışılır?

1. **Sırayla ilerleyin**: `01` ile başlayın, `05` ile bitirin
2. **Kodu çalıştırın**: Her dosyayı çalıştırıp çıktıları inceleyin
3. **Deneyin**: Kodları değiştirip ne olduğunu görün
4. **Alıştırma yapın**: `05_list_exercises.py` çok önemli!

## 💡 Önemli Kavramlar

### Liste Özellikleri
- **Sıralı** (ordered): Sıra önemli
- **Değiştirilebilir** (mutable): Değiştirilebilir
- **İndeksli** (indexed): `liste[0]` ile erişim
- **Tekrar edebilir**: Aynı öğe olabilir

### Temel Syntax
```python
# Oluşturma
meyveler = ['elma', 'armut', 'muz']

# Erişim
ilk_meyve = meyveler[0]
son_meyve = meyveler[-1]

# Ekleme
meyveler.append('çilek')

# Silme
meyveler.remove('armut')

# Sıralama
meyveler.sort()

# Dilimleme
ilk_iki = meyveler[:2]
```

## 📖 Önerilen Çalışma Sırası

### Temel Seviye (Öncelikli)
1. 📄 `01_list_basics.py` (30 dk)
2. 📄 `02_list_methods.py` (30 dk)
3. 📄 `03_list_organization.py` (20 dk)
4. 📄 `04_list_slicing.py` (30 dk)
5. 📄 `05_list_exercises.py` (60 dk) ⭐ ÖNEMLİ

### İleri Seviye (Yeni!)
6. 📄 `06_for_loops.py` (40 dk) ⭐ ÖNEMLİ
7. 📄 `07_range_numbers.py` (30 dk)
8. 📄 `08_list_comprehensions.py` (30 dk) ⭐ İLERİ
9. 📄 `09_tuples.py` (25 dk)
10. 📄 `10_tips_and_errors.py` (20 dk)

**Toplam süre**: ~5.5 saat

## 🎓 İpuçları

1. **Her dosyayı çalıştırın**: Teorik okumak yetmez!
2. **Kodları değiştirin**: Farklı değerler deneyin
3. **Hata yapın**: Hatalardan öğrenin
4. **Alıştırma yapın**: Pratik = Öğrenme
5. **Kendi örneklerinizi yazın**: Gerçek verilerle çalışın

## 🔗 Bağlantılar

- **Önceki**: [01-basics](../01-basics/)
- **Sonraki**: [03-control-flow](../03-control-flow/)

## 📝 Notlar

- Liste Python'un en çok kullanılan veri yapısıdır
- İndeksler 0'dan başlar
- Negatif indeks sondan başlar
- Slicing çok güçlü bir özelliktir
- `sort()` kalıcı, `sorted()` geçicidir

## ❓ Sık Sorulan Sorular

**S: Liste ve tuple farkı nedir?**
C: Liste değiştirilebilir `[]`, tuple değiştirilemez `()`

**S: İndeks 0'dan neden başlar?**
C: Çoğu programlama dilinde bu standarttır

**S: append() ve extend() farkı nedir?**
C: `append()` tek öğe ekler, `extend()` liste ekler

**S: sort() None neden döndürür?**
C: Çünkü orijinal listeyi değiştirir, yeni liste oluşturmaz

## 🎯 Sonraki Adım

Listeleri öğrendikten sonra:
→ `03-control-flow` ile devam edin
→ Koşullar ve döngüleri öğrenin
→ Listelerle döngüleri birleştirin

---

**Mutlu kodlamalar!** 🐍✨
