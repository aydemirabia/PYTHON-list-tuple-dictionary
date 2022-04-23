
'''KODLARI ÇALIŞTIRMAK İÇİN YORUM SATIRLARINI SİLİNİZ'''

# 1) 3 ürün bilgisini (id, ad, fiyat) kullanıcıdan aldığınız bilgilerle dictionary içinde saklayınız.
'''urunler={}
id=input("ID: ");
urunAd=input("Ürün Adı: ");
urunFiyat=input("Ürün Fiyat: ");

urunler.update({
    id:{
        "ad":"urunAd",
        "fiyat": "urunFiyat"
    }
})

urunler.update({
    id:{
        "ad":"urunAd",
        "fiyat": "urunFiyat"
    }
})
print(urunler)

urunler={}
id=input("ID: ");
urunAd=input("Ürün Adı: ");
urunFiyat=input("Ürün Fiyat: ");

urunler.update({
    id:{
        "ad":"urunAd",
        "fiyat": "urunFiyat"
    }
})

urunler.update({
    id:{
        "ad":"urunAd",
        "fiyat": "urunFiyat"
    }
})
print(urunler)'''


# 2) Ürün id bilgisini kullanıcıdan alıp ürün bilgisini kullanınız.
urunler = {
    '1': {
            'urunAd': 'LAPTOP',
            'urunFiyat': '2500'
    },
    '2': {
            'urunAd': 'CEP TELEFONU',
            'urunFiyat': '3000'
    }
}
id=input("ID: ");
urunler_=urunler.get(id);
print(urunler_);
