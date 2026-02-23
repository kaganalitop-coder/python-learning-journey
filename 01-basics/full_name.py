# ========================================
# F-STRINGS - String İçinde Değişken Kullanımı
# ========================================

# F-string nedir?
# String içinde değişken kullanmanın modern yolu (Python 3.6+)
# f"{degisken_adi}" şeklinde kullanılır

print("=== 1. Basit F-String Kullanımı ===")
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)
# Çıktı: ada lovelace

print("\n" + "-"*50 + "\n")

# ÖRNEK 2: F-string ile selamlama mesajı
print("=== 2. F-String ile Selamlama ===")
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(f"Hello, {full_name.title()}!")
# Çıktı: Hello, Ada Lovelace!

print("\n" + "-"*50 + "\n")

# ÖRNEK 3: Mesajı değişkende saklamak
print("=== 3. Mesajı Değişkende Sakla ===")
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
message = f"Hello, {full_name.title()}!"
print(message)
# Çıktı: Hello, Ada Lovelace!

print("\n" + "-"*50 + "\n")

# ÖRNEK 4: F-string içinde işlem yapmak
print("=== 4. F-String İçinde İşlem ===")
yas = 25
isim = "Ali"
print(f"Merhaba {isim}! Sen {yas} yaşındasın.")
print(f"5 yıl sonra {yas + 5} yaşında olacaksın.")
print(f"10 yıl önce {yas - 10} yaşındaydın.")

print("\n" + "-"*50 + "\n")

# ÖRNEK 5: Birden fazla değişken
print("=== 5. Çoklu Değişkenler ===")
ad = "Ahmet"
soyad = "Yılmaz"
sehir = "İstanbul"
yas = 30

tanitim = f"Ben {ad} {soyad}, {yas} yaşındayım ve {sehir}'da yaşıyorum."
print(tanitim)

print("\n" + "-"*50 + "\n")

# ÖRNEK 6: F-string ile format kontrolü
print("=== 6. Sayı Formatlama ===")
fiyat = 19.99
urun = "Kitap"
print(f"{urun} fiyatı: {fiyat:.2f} TL")  # 2 ondalık basamak
print(f"İndirimli fiyat: {fiyat * 0.8:.2f} TL")  # %20 indirim

print("\n" + "-"*50 + "\n")

# ESKİ YÖNTEM: format() metodu
# Python 3.5 ve öncesi için
print("=== 7. ESKİ YÖNTEM: format() ===")
print("(Python 3.5 ve öncesi için)")

first_name = "ada"
last_name = "lovelace"

# Eski yöntem - format()
full_name_old = "{} {}".format(first_name, last_name)
print(full_name_old)

# Yeni yöntem - f-string (ÖNERİLEN)
full_name_new = f"{first_name} {last_name}"
print(full_name_new)

print("\n💡 İpucu: Python 3.6 ve sonrası için f-string kullanın, daha okunabilir!")

print("\n" + "-"*50 + "\n")

# GERÇEK HAYAT ÖRNEĞİ
print("=== 8. Gerçek Hayat Örneği ===")

kullanici_adi = "ali_kagan"
toplam_puan = 1250
seviye = 15

bilgi = f"""
{'='*40}
    KULLANICI PROFİLİ
{'='*40}
Kullanıcı Adı: {kullanici_adi}
Toplam Puan : {toplam_puan:,}
Seviye      : {seviye}
Durum       : {'🔥 Aktif' if toplam_puan > 1000 else 'Yeni'}
{'='*40}
"""
print(bilgi)

# ÖZET
print("\n" + "="*50)
print("F-STRING ÖZET:")
print("="*50)
print("✓ f'metni {degisken}' şeklinde kullanılır")
print("✓ Python 3.6 ve sonrası için önerilir")
print("✓ String içinde işlem yapabilirsiniz")
print("✓ Eski format() metodundan daha okunabilir")
print("="*50)
