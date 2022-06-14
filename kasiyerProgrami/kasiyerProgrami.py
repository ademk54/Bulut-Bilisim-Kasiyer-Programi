TOPLAMFİYAT=0
PORTAKAL=3.0
ELMA=2.0
KİVİ=3.5
CİLEK=1.5

#Satın alınan ürünün fiyatını kilosuna göre hesaplama fonksiyonları.
def tekürünfiyathesaplama(fiyat, kilo):
    global TOPLAMFİYAT
    urun1 = fiyat * kilo
    TOPLAMFİYAT = urun1
    return(TOPLAMFİYAT)

def ikiürünfiyathesaplama(fiyat1, fiyat2, kilo1, kilo2):
    global TOPLAMFİYAT
    urun1 = fiyat1 * kilo1
    urun2 = fiyat2 * kilo2
    TOPLAMFİYAT = urun1 + urun2
    return(TOPLAMFİYAT)
def ucurunfiyathesaplama(fiyat1, fiyat2, fiyat3, kilo1, kilo2, kilo3):
    global TOPLAMFİYAT
    urun1 = fiyat1 * kilo1
    urun2 = fiyat2 * kilo2
    urun3 = fiyat3 * kilo3
    TOPLAMFİYAT = urun1 + urun2 + urun3
    return(TOPLAMFİYAT)
def dorturunhesaplama(fiyat1, fiyat2, fiyat3, fiyat4, kilo1, kilo2, kilo3, kilo4):
    global TOPLAMFİYAT
    urun1 = fiyat1 * kilo1
    urun2 = fiyat2 * kilo2
    urun3 = fiyat3 * kilo3
    urun4 = fiyat4 * kilo4
    TOPLAMFİYAT = urun1 + urun2 + urun3 + urun4
    return (TOPLAMFİYAT)


while True:
    print("-----------------------------------------------------\nMarketimizdeki ürünlerimizin kilo başı fiyatları:\nPortakal=3.0Tl\nElma=2.0Tl\nKivi=3.5Tl\nCilek=1.5Tl")
    urun_listesi = ["Portakal, Elma, Kivi, Cilek"]
    print("-----------------------------------------------------\nÜrün listemiz:",urun_listesi, end="\n\nCIKIS YAPMAK ICIN [-1] GİRİNİZ.\n")
    urunsayısı = int(input("(DİKKAT:Eğer 1 adet ürün alıcaksanız 1, 2 adet ürün alıcaksanız 2, 3 adet ürün alıcaksanız 3, 4 adet ürün alıcaksanız 4 giriniz.)\n\nMarketimizde 4 adet ürün vardır, kaç adet ürün satın alıcaksanız giriniz: "))

#ÇIKIŞ KOMUTU.
    if(urunsayısı == -1):
        print("Cikis yaptiniz.")
        break

#TEK ÜRÜN İÇİN KULLANILACAK KODLAR.
    elif (urunsayısı == 1):
        print("-----------------------------------------------------\nÜrünlerimizin kodları:\n\nPortakal[1]\nElma[2]\nKivi[3]\nCilek[4]\n\n-----------------------------------------------------")
        x= int(input("Satin almak istediginiz urun kodunu giriniz: "))
        y= float(input("Satin almak istediginiz urunun kilosunu giriniz: "))

        if (x == 1):
            tekürünfiyathesaplama(PORTAKAL, y)
            donendeger = TOPLAMFİYAT
            print("-----------------------------------------------------\nOdenecek Tutar:", donendeger,end="\n-----------------------------------------------------\n\n\n(DİKKAT!! ŞUAN FARKLI BİR SATIN ALMA İŞLEMİNE GEÇTİNİZ.)\n\n\n")

        elif (x == 2):
            tekürünfiyathesaplama(ELMA, y)
            donendeger = TOPLAMFİYAT
            print("-----------------------------------------------------\nOdenecek Tutar:", donendeger,end="\n-----------------------------------------------------\n\n\n(DİKKAT!! ŞUAN FARKLI BİR SATIN ALMA İŞLEMİNE GEÇTİNİZ.)\n\n\n")

        elif (x == 3):
            tekürünfiyathesaplama(KİVİ, y)
            donendeger = TOPLAMFİYAT
            print("-----------------------------------------------------\nOdenecek Tutar:", donendeger,end="\n-----------------------------------------------------\n\n\n(DİKKAT!! ŞUAN FARKLI BİR SATIN ALMA İŞLEMİNE GEÇTİNİZ.)\n\n\n")

        elif (x == 4):
            tekürünfiyathesaplama(CİLEK, y)
            donendeger = TOPLAMFİYAT
            print("-----------------------------------------------------\nOdenecek Tutar:", donendeger,end="\n-----------------------------------------------------\n\n\n(DİKKAT!! ŞUAN FARKLI BİR SATIN ALMA İŞLEMİNE GEÇTİNİZ.)\n\n\n")

#İKİ ÜRÜN İÇİN KULLANILACAK KODLAR.
    elif (urunsayısı==2):
        print("-----------------------------------------------------\nÜrünlerimizin kodları:\n\nPortakal[1]\nElma[2]\nKivi[3]\nCilek[4]\n\n-----------------------------------------------------")
        x1 = int(input("1. Urunun kodunu giriniz: "))
        x2 = int(input("2. Urunun kodunu giriniz: "))
        y1 = float(input("1. Urunun kilosunu giriniz: "))
        y2 = float(input("2. Urunun kilosunu giriniz: "))

    #X1==1
        if (x1 == 1) and (x2 == 2):
            ikiürünfiyathesaplama(PORTAKAL, ELMA, y1, y2)
            donendeger2 = TOPLAMFİYAT
            print("-----------------------------------------------------\nOdenecek Tutar: ", donendeger2,end="\n-----------------------------------------------------\n\n\n(DİKKAT!! ŞUAN FARKLI BİR SATIN ALMA İŞLEMİNE GEÇTİNİZ.)\n\n\n")

        elif (x1 == 1) and (x2 == 3):
            ikiürünfiyathesaplama(PORTAKAL, KİVİ, y1, y2)
            donendeger2 = TOPLAMFİYAT
            print("-----------------------------------------------------\nOdenecek Tutar: ", donendeger2,end="\n-----------------------------------------------------\n\n\n(DİKKAT!! ŞUAN FARKLI BİR SATIN ALMA İŞLEMİNE GEÇTİNİZ.)\n\n\n")

        elif (x1 == 1) and (x2 == 4):
            ikiürünfiyathesaplama(PORTAKAL, CİLEK, y1, y2)
            donendeger2 = TOPLAMFİYAT
            print("-----------------------------------------------------\nOdenecek Tutar: ", donendeger2,end="\n-----------------------------------------------------\n\n\n(DİKKAT!! ŞUAN FARKLI BİR SATIN ALMA İŞLEMİNE GEÇTİNİZ.)\n\n\n")

    #X1==2
        elif (x1 == 2) and (x2 == 1):
            ikiürünfiyathesaplama(ELMA, PORTAKAL, y1, y2)
            donendeger2 = TOPLAMFİYAT
            print("-----------------------------------------------------\nOdenecek Tutar: ", donendeger2,end="\n-----------------------------------------------------\n\n\n(DİKKAT!! ŞUAN FARKLI BİR SATIN ALMA İŞLEMİNE GEÇTİNİZ.)\n\n\n")

        elif (x1 == 2) and (x2 == 3):
            ikiürünfiyathesaplama(ELMA, KİVİ, y1, y2)
            donendeger2 = TOPLAMFİYAT
            print("-----------------------------------------------------\nOdenecek Tutar: ", donendeger2,end="\n-----------------------------------------------------\n\n\n(DİKKAT!! ŞUAN FARKLI BİR SATIN ALMA İŞLEMİNE GEÇTİNİZ.)\n\n\n")

        elif (x1 == 2) and (x2 == 4):
            ikiürünfiyathesaplama(ELMA, CİLEK, y1, y2)
            donendeger2 = TOPLAMFİYAT
            print("-----------------------------------------------------\nOdenecek Tutar: ", donendeger2,end="\n-----------------------------------------------------\n\n\n(DİKKAT!! ŞUAN FARKLI BİR SATIN ALMA İŞLEMİNE GEÇTİNİZ.)\n\n\n")

    #X1==3
        elif (x1 == 3) and (x2 == 1):
            ikiürünfiyathesaplama(KİVİ, PORTAKAL, y1, y2)
            donendeger2 = TOPLAMFİYAT
            print("-----------------------------------------------------\nOdenecek Tutar: ", donendeger2,end="\n-----------------------------------------------------\n\n\n(DİKKAT!! ŞUAN FARKLI BİR SATIN ALMA İŞLEMİNE GEÇTİNİZ.)\n\n\n")

        elif (x1 == 3) and (x2 == 2):
            ikiürünfiyathesaplama(KİVİ, ELMA, y1, y2)
            donendeger2 = TOPLAMFİYAT
            print("-----------------------------------------------------\nOdenecek Tutar: ", donendeger2,end="\n-----------------------------------------------------\n\n\n(DİKKAT!! ŞUAN FARKLI BİR SATIN ALMA İŞLEMİNE GEÇTİNİZ.)\n\n\n")

        elif (x1 == 3) and (x2 == 4):
            ikiürünfiyathesaplama(KİVİ, CİLEK, y1, y2)
            donendeger2 = TOPLAMFİYAT
            print("-----------------------------------------------------\nOdenecek Tutar: ", donendeger2,end="\n-----------------------------------------------------\n\n\n(DİKKAT!! ŞUAN FARKLI BİR SATIN ALMA İŞLEMİNE GEÇTİNİZ.)\n\n\n")

    #X1==4
        elif (x1 == 4) and (x2 == 1):
            ikiürünfiyathesaplama(CİLEK,PORTAKAL , y1, y2)
            donendeger2 = TOPLAMFİYAT
            print("-----------------------------------------------------\nOdenecek Tutar: ", donendeger2,end="\n-----------------------------------------------------\n\n\n(DİKKAT!! ŞUAN FARKLI BİR SATIN ALMA İŞLEMİNE GEÇTİNİZ.)\n\n\n")

        elif (x1 == 4) and (x2 == 2):
            ikiürünfiyathesaplama(CİLEK,ELMA , y1, y2)
            donendeger2 = TOPLAMFİYAT
            print("-----------------------------------------------------\nOdenecek Tutar: ", donendeger2,end="\n-----------------------------------------------------\n\n\n(DİKKAT!! ŞUAN FARKLI BİR SATIN ALMA İŞLEMİNE GEÇTİNİZ.)\n\n\n")

        elif (x1 == 4) and (x2 == 3):
            ikiürünfiyathesaplama(CİLEK,KİVİ , y1, y2)
            donendeger2 = TOPLAMFİYAT
            print("-----------------------------------------------------\nOdenecek Tutar: ", donendeger2,end="\n-----------------------------------------------------\n\n\n(DİKKAT!! ŞUAN FARKLI BİR SATIN ALMA İŞLEMİNE GEÇTİNİZ.)\n\n\n")

#ÜÇ ÜRÜN İÇİN KULLANILACAK KODLAR.
    elif (urunsayısı == 3):
        print("-----------------------------------------------------\nÜrünlerimizin kodları:\n\nPortakal[1]\nElma[2]\nKivi[3]\nCilek[4]\n\n-----------------------------------------------------")
        x1 = int(input("1. Urunun kodunu giriniz: "))
        x2 = int(input("2. Urunun kodunu giriniz: "))
        x3 = int(input("3. Urunun kodunu giriniz: "))
        y1 = float(input("1. Urunun kilosunu giriniz: "))
        y2 = float(input("2. Urunun kilosunu giriniz: "))
        y3 = float(input("3. Urunun kilosunu giriniz: "))

    #X1==1
        if (x1 == 1) and (x2 == 2) and (x3 == 3):
            ucurunfiyathesaplama(PORTAKAL, ELMA, KİVİ, y1, y2 ,y3)
            donendeger3 = TOPLAMFİYAT
            print("-----------------------------------------------------\nOdenecek Tutar: ", donendeger3, end="\n-----------------------------------------------------\n\n\n(DİKKAT!! ŞUAN FARKLI BİR SATIN ALMA İŞLEMİNE GEÇTİNİZ.)\n\n\n")

        elif (x1 == 1) and (x2 == 2) and (x3 == 4):
            ucurunfiyathesaplama(PORTAKAL, ELMA, CİLEK, y1, y2 ,y3)
            donendeger3 = TOPLAMFİYAT
            print("-----------------------------------------------------\nOdenecek Tutar: ", donendeger3, end="\n-----------------------------------------------------\n\n\n(DİKKAT!! ŞUAN FARKLI BİR SATIN ALMA İŞLEMİNE GEÇTİNİZ.)\n\n\n")

        elif (x1 == 1) and (x2 == 3) and (x3 == 2):
            ucurunfiyathesaplama(PORTAKAL, KİVİ, ELMA, y1, y2 ,y3)
            donendeger3 = TOPLAMFİYAT
            print("-----------------------------------------------------\nOdenecek Tutar: ", donendeger3, end="\n-----------------------------------------------------\n\n\n(DİKKAT!! ŞUAN FARKLI BİR SATIN ALMA İŞLEMİNE GEÇTİNİZ.)\n\n\n")

        elif (x1 == 1) and (x2 == 3) and (x3 == 4):
            ucurunfiyathesaplama(PORTAKAL, KİVİ, CİLEK, y1, y2 ,y3)
            donendeger3 = TOPLAMFİYAT
            print("-----------------------------------------------------\nOdenecek Tutar: ", donendeger3, end="\n-----------------------------------------------------\n\n\n(DİKKAT!! ŞUAN FARKLI BİR SATIN ALMA İŞLEMİNE GEÇTİNİZ.)\n\n\n")

        elif (x1 == 1) and (x2 == 4) and (x3 == 2):
            ucurunfiyathesaplama(PORTAKAL, CİLEK, ELMA, y1, y2 ,y3)
            donendeger3 = TOPLAMFİYAT
            print("-----------------------------------------------------\nOdenecek Tutar: ", donendeger3, end="\n-----------------------------------------------------\n\n\n(DİKKAT!! ŞUAN FARKLI BİR SATIN ALMA İŞLEMİNE GEÇTİNİZ.)\n\n\n")

        elif (x1 == 1) and (x2 == 4) and (x3 == 3):
            ucurunfiyathesaplama(PORTAKAL, CİLEK, KİVİ, y1, y2 ,y3)
            donendeger3 = TOPLAMFİYAT
            print("-----------------------------------------------------\nOdenecek Tutar: ", donendeger3, end="\n-----------------------------------------------------\n\n\n(DİKKAT!! ŞUAN FARKLI BİR SATIN ALMA İŞLEMİNE GEÇTİNİZ.)\n\n\n")

    #X1==2
        elif (x1 == 2) and (x2 == 3) and (x3 == 1):
            ucurunfiyathesaplama(ELMA, KİVİ, PORTAKAL, y1, y2 ,y3)
            donendeger3 = TOPLAMFİYAT
            print("-----------------------------------------------------\nOdenecek Tutar: ", donendeger3, end="\n-----------------------------------------------------\n\n\n(DİKKAT!! ŞUAN FARKLI BİR SATIN ALMA İŞLEMİNE GEÇTİNİZ.)\n\n\n")

        elif (x1 == 2) and (x2 == 1) and (x3 == 4):
            ucurunfiyathesaplama(ELMA, PORTAKAL, CİLEK, y1, y2 ,y3)
            donendeger3 = TOPLAMFİYAT
            print("-----------------------------------------------------\nOdenecek Tutar: ", donendeger3, end="\n-----------------------------------------------------\n\n\n(DİKKAT!! ŞUAN FARKLI BİR SATIN ALMA İŞLEMİNE GEÇTİNİZ.)\n\n\n")

        elif (x1 == 2) and (x2 == 3) and (x3 == 1):
            ucurunfiyathesaplama(ELMA, KİVİ, PORTAKAL, y1, y2, y3)
            donendeger3 = TOPLAMFİYAT
            print("-----------------------------------------------------\nOdenecek Tutar: ", donendeger3, end="\n-----------------------------------------------------\n\n\n(DİKKAT!! ŞUAN FARKLI BİR SATIN ALMA İŞLEMİNE GEÇTİNİZ.)\n\n\n")

        elif (x1 == 2) and (x2 == 3) and (x3 == 4):
            ucurunfiyathesaplama(ELMA, KİVİ, CİLEK, y1, y2, y3)
            donendeger3 = TOPLAMFİYAT
            print("-----------------------------------------------------\nOdenecek Tutar: ", donendeger3, end="\n-----------------------------------------------------\n\n\n(DİKKAT!! ŞUAN FARKLI BİR SATIN ALMA İŞLEMİNE GEÇTİNİZ.)\n\n\n")

        elif (x1 == 2) and (x2 == 4) and (x3 == 1):
            ucurunfiyathesaplama(ELMA, CİLEK, PORTAKAL, y1, y2, y3)
            donendeger3 = TOPLAMFİYAT
            print("-----------------------------------------------------\nOdenecek Tutar: ", donendeger3, end="\n-----------------------------------------------------\n\n\n(DİKKAT!! ŞUAN FARKLI BİR SATIN ALMA İŞLEMİNE GEÇTİNİZ.)\n\n\n")

        elif (x1 == 2) and (x2 == 4) and (x3 == 3):
            ucurunfiyathesaplama(ELMA, CİLEK, KİVİ, y1, y2, y3)
            donendeger3 = TOPLAMFİYAT
            print("-----------------------------------------------------\nOdenecek Tutar: ", donendeger3, end="\n-----------------------------------------------------\n\n\n(DİKKAT!! ŞUAN FARKLI BİR SATIN ALMA İŞLEMİNE GEÇTİNİZ.)\n\n\n")

    #X1==3
        elif (x1 == 3) and (x2 == 1) and (x3 == 2):
            ucurunfiyathesaplama(KİVİ, PORTAKAL, ELMA, y1, y2, y3)
            donendeger3 = TOPLAMFİYAT
            print("-----------------------------------------------------\nOdenecek Tutar: ", donendeger3, end="\n-----------------------------------------------------\n\n\n(DİKKAT!! ŞUAN FARKLI BİR SATIN ALMA İŞLEMİNE GEÇTİNİZ.)\n\n\n")

        elif (x1 == 3) and (x2 == 1) and (x3 == 4):
            ucurunfiyathesaplama(KİVİ, PORTAKAL, CİLEK, y1, y2, y3)
            donendeger3 = TOPLAMFİYAT
            print("-----------------------------------------------------\nOdenecek Tutar: ", donendeger3, end="\n-----------------------------------------------------\n\n\n(DİKKAT!! ŞUAN FARKLI BİR SATIN ALMA İŞLEMİNE GEÇTİNİZ.)\n\n\n")

        elif (x1 == 3) and (x2 == 2) and (x3 == 1):
            ucurunfiyathesaplama(KİVİ, ELMA, PORTAKAL, y1, y2, y3)
            donendeger3 = TOPLAMFİYAT
            print("-----------------------------------------------------\nOdenecek Tutar: ", donendeger3, end="\n-----------------------------------------------------\n\n\n(DİKKAT!! ŞUAN FARKLI BİR SATIN ALMA İŞLEMİNE GEÇTİNİZ.)\n\n\n")

        elif (x1 == 3) and (x2 == 2) and (x3 == 4):
            ucurunfiyathesaplama(KİVİ, ELMA, CİLEK, y1, y2, y3)
            donendeger3 = TOPLAMFİYAT
            print("-----------------------------------------------------\nOdenecek Tutar: ", donendeger3, end="\n-----------------------------------------------------\n\n\n(DİKKAT!! ŞUAN FARKLI BİR SATIN ALMA İŞLEMİNE GEÇTİNİZ.)\n\n\n")

        elif (x1 == 3) and (x2 == 4) and (x3 == 1):
            ucurunfiyathesaplama(KİVİ, CİLEK, PORTAKAL, y1, y2, y3)
            donendeger3 = TOPLAMFİYAT
            print("-----------------------------------------------------\nOdenecek Tutar: ", donendeger3, end="\n-----------------------------------------------------\n\n\n(DİKKAT!! ŞUAN FARKLI BİR SATIN ALMA İŞLEMİNE GEÇTİNİZ.)\n\n\n")

        elif (x1 == 3) and (x2 == 4) and (x3 == 2):
            ucurunfiyathesaplama(KİVİ, CİLEK, ELMA, y1, y2, y3)
            donendeger3 = TOPLAMFİYAT
            print("-----------------------------------------------------\nOdenecek Tutar: ", donendeger3, end="\n-----------------------------------------------------\n\n\n(DİKKAT!! ŞUAN FARKLI BİR SATIN ALMA İŞLEMİNE GEÇTİNİZ.)\n\n\n")

    #X1==4
        elif (x1 == 4) and (x2 == 1) and (x3 == 2):
            ucurunfiyathesaplama(CİLEK, PORTAKAL, ELMA, y1, y2, y3)
            donendeger3 = TOPLAMFİYAT
            print("-----------------------------------------------------\nOdenecek Tutar: ", donendeger3, end="\n-----------------------------------------------------\n\n\n(DİKKAT!! ŞUAN FARKLI BİR SATIN ALMA İŞLEMİNE GEÇTİNİZ.)\n\n\n")

        elif (x1 == 4) and (x2 == 1) and (x3 == 3):
            ucurunfiyathesaplama(CİLEK, PORTAKAL, KİVİ, y1, y2, y3)
            donendeger3 = TOPLAMFİYAT
            print("-----------------------------------------------------\nOdenecek Tutar: ", donendeger3, end="\n-----------------------------------------------------\n\n\n(DİKKAT!! ŞUAN FARKLI BİR SATIN ALMA İŞLEMİNE GEÇTİNİZ.)\n\n\n")

        elif (x1 == 4) and (x2 == 2) and (x3 == 1):
            ucurunfiyathesaplama(CİLEK, ELMA, PORTAKAL, y1, y2, y3)
            donendeger3 = TOPLAMFİYAT
            print("-----------------------------------------------------\nOdenecek Tutar: ", donendeger3, end="\n-----------------------------------------------------\n\n\n(DİKKAT!! ŞUAN FARKLI BİR SATIN ALMA İŞLEMİNE GEÇTİNİZ.)\n\n\n")

        elif (x1 == 4) and (x2 == 2) and (x3 == 3):
            ucurunfiyathesaplama(CİLEK, ELMA, KİVİ, y1, y2, y3)
            donendeger3 = TOPLAMFİYAT
            print("-----------------------------------------------------\nOdenecek Tutar: ", donendeger3, end="\n-----------------------------------------------------\n\n\n(DİKKAT!! ŞUAN FARKLI BİR SATIN ALMA İŞLEMİNE GEÇTİNİZ.)\n\n\n")

        elif (x1 == 4) and (x2 == 3) and (x3 == 1):
            ucurunfiyathesaplama(CİLEK, KİVİ, PORTAKAL, y1, y2, y3)
            donendeger3 = TOPLAMFİYAT
            print("-----------------------------------------------------\nOdenecek Tutar: ", donendeger3, end="\n-----------------------------------------------------\n\n\n(DİKKAT!! ŞUAN FARKLI BİR SATIN ALMA İŞLEMİNE GEÇTİNİZ.)\n\n\n")

        elif (x1 == 4) and (x2 == 3) and (x3 == 2):
            ucurunfiyathesaplama(CİLEK, KİVİ, ELMA, y1, y2, y3)
            donendeger3 = TOPLAMFİYAT
            print("-----------------------------------------------------\nOdenecek Tutar: ", donendeger3, end="\n-----------------------------------------------------\n\n\n(DİKKAT!! ŞUAN FARKLI BİR SATIN ALMA İŞLEMİNE GEÇTİNİZ.)\n\n\n")

#DÖRT ÜRÜN İÇİN KULLANILACAK KODLAR (DİĞER KOŞULLARA GÖRE DAHA FARKLI ÇALIŞAN BİR SİSTEM, KULLANICIYI NUMARALARI SIRASIYLA GİRMEK ZORUNDA BIRAKIYOR).
    elif (urunsayısı == 4):
        print("-----------------------------------------------------\nÜrünlerimizin kodları:\n\nPortakal[1]\nElma[2]\nKivi[3]\nCilek[4]\n\n-----------------------------------------------------")
        print("(DİKKAT!! Ürünlerin hepsini satın alma seçeneğini seçtiniz lütfen ürün kodlarını 1-2-3-4 şeklinde sırasıyla giriniz.)\n")
        x1 = int(input("1. Urunun kodunu giriniz: "))
        if (x1 == 1):
            x2 = int(input("2. Urunun kodunu giriniz: "))
            if (x2 == 2):
                x3 = int(input("3. Urunun kodunu giriniz: "))
                if(x3 == 3):
                    x4 = int(input("4. Urunun kodunu giriniz: "))
                    if (x4 == 4):
                        y1 = float(input("1. Urunun kilosunu giriniz: "))
                        y2 = float(input("2. Urunun kilosunu giriniz: "))
                        y3 = float(input("3. Urunun kilosunu giriniz: "))
                        y4 = float(input("4. Urunun kilosunu giriniz: "))
                        dorturunhesaplama(PORTAKAL, ELMA, KİVİ, CİLEK, y1, y2, y3, y4)
                        donendeger4 = TOPLAMFİYAT
                        print("-----------------------------------------------------\nOdenecek Tutar: ", donendeger4, end="\n-----------------------------------------------------\n\n\n(DİKKAT!! ŞUAN FARKLI BİR SATIN ALMA İŞLEMİNE GEÇTİNİZ.)\n\n\n")
                    elif (x4 != 4):
                        while (x4 != 4):
                            print("-----------------------------------------------------\n\n\n\n(DİKKAT!! Geçersiz değer girdiniz lüften ürünleri sırasıyla 1-2-3-4 şeklinde giriniz.)\n\n\n")
                            break
                elif (x3 != 3):
                    while (x3 != 3):
                        print("-----------------------------------------------------\n\n\n\n(DİKKAT!! Geçersiz değer girdiniz lüften ürünleri sırasıyla 1-2-3-4 şeklinde giriniz.)\n\n\n")
                        break
            elif (x2 != 2):
                while (x2 != 2):
                    print("-----------------------------------------------------\n\n\n\n(DİKKAT!! Geçersiz değer girdiniz lüften ürünleri sırasıyla 1-2-3-4 şeklinde giriniz.)\n\n\n")
                    break
        elif (x1 != 1):
            while (x1 != 1):
                print("-----------------------------------------------------\n\n\n\n(DİKKAT!! Geçersiz değer girdiniz lüften ürünleri sırasıyla 1-2-3-4 şeklinde giriniz.)\n\n\n")
                break

#GEÇERSİZ DEĞER GİRİLDİĞİNDE ÇALIŞACAK KOD.
    else:
        print("\n-----------------------------------------------------\n\n\n\n(DİKKAT!! SATIN ALMAK İSTEDİĞİNİZ ÜRÜN SAYISI MARKETİMİZDE MEVCUT DEĞİLDİR, LÜTFEN GEÇERLİ ÜRÜN SAYISI GİRİNİZ.)\n\n\n")