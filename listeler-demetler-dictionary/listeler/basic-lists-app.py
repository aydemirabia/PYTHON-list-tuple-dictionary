# Programlama Dilleri ile ilgili liste oluşturun.
progLang=["Java","Python","C++","C","C#","Kotlin"];

# Liste elemanın sayısını bulunuz.
print(len(progLang));

# Listenin ilk ve son elemanı nedir?
print(progLang[0]);
print(progLang[-1]);

# Listeye PHP ekleyiniz.
print(progLang+["PHP"]);

# PHP değerini Scala ile değiştiriniz.
progLang[-1]="Scala";
print(progLang);

# Swift listenin bir elemanı mıdır?
if "Swift" in progLang:
    print("Evet");
else:
    print("Hayır");
    
# Listenin ilk 2 elemanını alınız.
print(progLang[0:2])

# Listenin son 2 elemanına Go ve Ruby dillerini ekleyiniz.
print(progLang[-2:])
progLang[-2:]+=["Go","Ruby"]
print(progLang)

# Listenin son 2 elemanını siliniz.
print(progLang)
del progLang[-2:]
print(progLang);

# Listenin elemanlarını tersten yazdırın.
print(progLang);
print(progLang[::-1])