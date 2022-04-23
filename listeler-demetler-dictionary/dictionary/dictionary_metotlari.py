'''
    oyuncu 1: 
        id => 1
        ad-soyad => Cristiano Ronaldo
        dogumYili => 1985
        uyruk => Portugal
        takımlar => Portugal
        gecmisTakimlar => Juventus, Real Madrid, Portugal
        
    oyuncu 2: 
        id => 2
        ad-soyad => Lionel Messi
        dogumYili => 1987
        uyruk => Argentino
        takımlar => Barcelona
        gecmisTakimlar => Argentino, Barcelona, Portugal
        
'''

# 1- Yukarıda verilen bilgileri liste içerisinde saklayınız.
# 2- id'e göre arama yapınız.
# 3- id'e göre bilgi kayıt siliniz.

'''oyuncu_1 = {
    "id":1,
    "adSoyad":"Cristiano Ronaldo",
    "dogumYili":1985,
    "uyruk":"Portugal",
    "takimlar":"Portugal",
    "gecmisTakimlar": ["Juventus", "Real Madrid" , "Portugal"]  
}
oyuncu_2 = {
    "id":1,
    "adSoyad":"Cristiano Ronaldo",
    "dogumYili":1985,
    "uyruk":"Portugal",
    "takimlar":"Portugal",
    "gecmisTakimlar": ["Juventus", "Real Madrid" , "Portugal"]  
}'''

# 1- Yukarıda verilen bilgileri liste içerisinde saklayınız.
'''
oyuncular={}
id=input("oyuncu id: ");
adSoyad=input("oyuncu adı: ");
uyruk=input("oyuncu uyruk: ");
dogumYili=input("oyuncu doğum yılı: ");
takım=input("oyuncu takım: ");
gecmisTakim=input("oyuncu geçmiş takımları: ")

oyuncular.update({
    id: {
        "name":adSoyad,
        "dogumYili":dogumYili,
        "uyruk":uyruk,
        "takim":takım,
        "gecmisTakimlar":gecmisTakim.split(',')
    }
})
print(oyuncular)
oyuncular={}
id=input("oyuncu id: ");
adSoyad=input("oyuncu adı: ");
uyruk=input("oyuncu uyruk: ");
dogumYili=input("oyuncu doğum yılı: ");
takım=input("oyuncu takım: ");
gecmisTakim=input("oyuncu geçmiş takımları: ")

oyuncular.update({
    id: {
        "name":adSoyad,
        "dogumYili":dogumYili,
        "uyruk":uyruk,
        "takim":takım,
        "gecmisTakimlar":gecmisTakim.split(',')
    }
})
print(oyuncular)
'''
# 1- Yukarıda verilen bilgileri liste içerisinde saklayınız.
oyuncular = {

        '1': 
            {'name': 'Cristiano Ronaldo', 'dogumYili': '1985', 'uyruk': 'Portugal', 'takim': 'Portugal', 'gecmisTakimlar': ['Juventus', 'Real Madrid ', ' Portugal']
        },

        '2':  {'name': 'Lionel Messi', 'dogumYili': '1987', 'uyruk': 'Argentino', 'takim': 'Barcelona', 'gecmisTakimlar': ['Argentino', ' Barcelona', ' Portugal']
        }
    }

# 2- id'e göre arama yapınız.
id=input("ID: ")
oyuncu=oyuncular.get(id)
print(oyuncu);

 # 3- id'e göre bilgi kayıt siliniz.
id=input("Silmek istediğiniz oyuncu: ");
oyuncular.pop(id);
print(oyuncular);