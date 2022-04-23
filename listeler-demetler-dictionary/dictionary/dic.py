audiObj={
    "marka":"Audi",
    "model":"A3 Sedan",
    "modelYili":2022
}
sonuc=audiObj["marka"]
# sonuc = audiObj.get("marka") ////farklı gösterim
sonuc=audiObj.get("model")
print(audiObj);

# key-value ::: key bilgilerine ulaşım
for x in audiObj:
    print(x);

print("---------------------------");

# key-value ::: value bilgilerine ulaşım
for x in audiObj:
    print(audiObj[x]);
    
# values'e ulaşmanın 2. yol
for x in audiObj.values():
    print(x);

print("---------------------------");

# key-values değerlerine aynı anda ulaşmak için:
for x, y in audiObj.items():
    print(x,y)
    
print("---------------------------");

#aradığımız bir değerin listede olup olmadığını kontrol etmek için:
sonuc="marka" in audiObj
print(sonuc); # true-false döndürür.

print("---------------------------");

# listeye key-values ekleme
audiObj["renk"] = "siyah"
print(audiObj)

print("---------------------------");

#popitem(): rastgele bir değer siler.
audiObj.popitem();
print(audiObj);


print("---------------------------");

#clear(): bütün liste elemanlarını temizler.
#audiObj.clear()

#Eğer bizler audiObj üzerinden farklı bir adrese atama yapmak istiyorsak
#yeniAudi=audiObj diyip adresi farklı bir değişkene atarız.
#Bu olaya referans denir.

#Ancak kopyalama yapmak istiyorsak da metod kullanırız.
yeniAudiobj=audiObj.copy()
print("---------------------------");

#Bilgileri değiştrmek/güncellemek
audiObj.update({
    "marka":"Volvo",
    "renk":"Uzay Grisi"
})
print(audiObj)