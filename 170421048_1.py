# FONKSIYONLAR #


def yeni_dizi_olustur():
    arr = []
    for i in range(20):
        arr.append([])
    for i in range(20):
        for j in range(20):
            arr[i].append("-")
    return arr


def printkoltuk():
    global koltuklar
    print("Koltuklar: ")
    for i in range(len(koltuklar)):
        for j in range(len(koltuklar[i])):
            print(koltuklar[i][j], end=" ")
        print()


def koltukdoldur(kategori):
    # koltuklar[vertical][horizontal]
    global koltuklar
    if kategori == 1:
        # 1. kategori koltuklar = koltuklar[0->9][5->14]
        for i in range(0, 9 + 1):
            for j in range(5, 14 + 1):
                if koltuklar[i][j] == "-":
                    koltuklar[i][j] = "x"
                    # Doldurulan koltugun yeri
                    return tuple([i + 1, j + 1])
    elif kategori == 3:
        # 3. kategori koltuklar = koltuklar[10->19][5->14]
        for i in range(10, 19 + 1):
            for j in range(5, 14 + 1):
                if koltuklar[i][j] == "-":
                    koltuklar[i][j] = "x"
                    return tuple([i + 1, j + 1])
    elif kategori == 2:
        # 2. kategori koltuklar = koltuklar[0->9][0->4] && koltuklar[0->9][15->19]
        for i in range(0, 9 + 1):
            for j in iki_dort_kategori_koltuklari:
                if koltuklar[i][j] == "-":
                    koltuklar[i][j] = "x"
                    return tuple([i + 1, j + 1])
    elif kategori == 4:
        # 4. kategori koltuklar = koltuklar[10->19][0->4] && koltuklar[10->19][15->19]
        for i in range(10, 19 + 1):
            for j in iki_dort_kategori_koltuklari:
                if koltuklar[i][j] == "-":
                    koltuklar[i][j] = "x"
                    return tuple([i + 1, j + 1])


def rezervasyon(adet, kategori):
    global koltuklar
    doldurulan_koltuklar = []
    for counter in range(adet):
        doldurulan_koltuklar.append(koltukdoldur(kategori))
    print("Rezerve edilen koltuklar (Sira-Koltuk) ", doldurulan_koltuklar)


def boskoltuksayisi(kategori):
    c = 0
    if kategori == 1:
        # 1. kategori koltuklar = koltuklar[0->9][5->14]
        for i in range(0, 9 + 1):
            for j in range(5, 14 + 1):
                if koltuklar[i][j] == "-":
                    c += 1
        return c
    elif kategori == 3:
        # 3. kategori koltuklar = koltuklar[10->19][5->14]
        for i in range(10, 19 + 1):
            for j in range(5, 14 + 1):
                if koltuklar[i][j] == "-":
                    c += 1
        return c
    elif kategori == 2:
        # 2. kategori koltuklar = koltuklar[0->9][0->4] && koltuklar[0->9][15->19]
        for i in range(0, 9 + 1):
            for j in iki_dort_kategori_koltuklari:
                if koltuklar[i][j] == "-":
                    c += 1
        return c
    elif kategori == 4:
        # 4. kategori koltuklar = koltuklar[10->19][0->4] && koltuklar[10->19][15->19]
        for i in range(10, 19 + 1):
            for j in iki_dort_kategori_koltuklari:
                if koltuklar[i][j] == "-":
                    c += 1
        return c


def ucrethesapla(adet, kategori):
    return fiyatlar[kategori] * adet


def indirimyap(ucret, adet, kategori):
    # if adet between dict_indirimler[kategori][0] and dict_indirimler[kategori][1] apply dict_indirimler[kategori][2]
    for indirim_listeleri in dict_indirimler[kategori]:
        # if adet >= indirim_listeleri[0] and adet <= indirim_listeleri[1]:
        if indirim_listeleri[0] <= adet <= indirim_listeleri[1]:
            ucret = ucret - (ucret * int(indirim_listeleri[2]) / 100)

    return ucret


def ciroekle(kazanc, kategori):
    global ciro
    ciro[kategori] += kazanc


def anamenu():
    print("*" * 20)
    print("ANA MENÜ".center(20, " "))
    print("*" * 20)
    print("1. Rezervasyon")
    print("2. Salonu Yazdır")
    print("3. Yeni Etkinlik")
    print("4. Toplam Ciro")
    print("0. Çıkış")
    print("*" * 20)


def ciroyazdir():
    global ciro
    print("Toplam Ciro")
    print("1. kategori: %d TL" % ciro[1])
    print("2. kategori: %d TL" % ciro[2])
    print("3. kategori: %d TL" % ciro[3])
    print("4. kategori: %d TL" % ciro[4])


# MAIN #
koltuklar = yeni_dizi_olustur()
# for dongusuyle erismek icin ikinci ve dorduncu kategorideki koltuklarin indexleri (index = numara - 1)
iki_dort_kategori_koltuklari = [4, 3, 2, 1, 0, 15, 16, 17, 18, 19]
ciro = {1: 0, 2: 0, 3: 0, 4: 0}
with open("indirim.txt", "r") as f:
    # satir = [x.strip() for x in f.readlines()]
    satir = f.readlines()
    for x in satir:
        i = satir.index(x)
        satir[i] = x.strip()

    M = int(satir[0].replace("M-", ""))
    fiyatlar = {1: None, 2: None, 3: None, 4: None}
    for key in fiyatlar.keys():
        # 1-200 yazısını 200 haline getiriyorum
        fiyat = satir[key].replace("%d-" % key, "")
        fiyatlar[key] = int(fiyat)

    # kullandigim verileri listeden kaldiriyorum
    for index in [4, 3, 2, 1, 0]:
        del satir[index]

    indirimler = []
    for x in satir:
        new_list = x.split("-")
        indirimler.append(new_list)

    dict_indirimler = {1: None, 2: None, 3: None, 4: None}
    # Dict: her key, [min_adet,max_adet,indirim_orani] seklinde 3 liste tutuyor
    # Program sonunda:
    # dict_indirimler = {1: [[5, 10, 10], [11, 20, 20], [21, 30, 25]], 2: [[5, 10, 5], [11, 20, 15], [21, 30, 20]],
    # 3: [[5, 15, 15], [16, 25, 20], [26, 30, 35]], 4: [[5, 10, 5], [11, 20, 10], [21, 30, 15]]}
    # olur.
    arr = [[], [], [], []]
    for x in indirimler:
        for element in x:
            i = x.index(element)
            if element == "M":
                x[i] = M
            else:
                x[i] = int(element)
        if x[0] == 1:
            arr[0].append(x)
        elif x[0] == 2:
            arr[1].append(x)
        elif x[0] == 3:
            arr[2].append(x)
        elif x[0] == 4:
            arr[3].append(x)
        else:
            pass

    for key, x in enumerate(arr):
        key += 1
        # key sirasiyla 1 2 3 4 oluyor
        for sublist in x:
            i = x.index(sublist)
            sublist.pop(0)
            x[i] = sublist
        dict_indirimler[key] = x

    del indirimler
    del arr
    del satir

print("Num: 170421048".center(20, "-"))

# MAIN LOOP #
while True:
    anamenu()
    secim = int(input("Seciminiz ? "))
    if secim == 0:
        break
    elif secim == 1:
        k = input("Kategori (1-4) ? ")
        while k not in "1234":
            print("Lütfen 1 ve 4 arasında değer giriniz ? ")
            k = input("Kategori (1-4) ? ")
        a = input("Adet (1-%d) ? " % M)
        while int(a) not in range(1, M + 1):
            print("Lütfen 1 ve %d arasında değer giriniz ? " % M)
            a = input("Adet (1-%d) ? " % M)
        k = int(k)
        a = int(a)
        if a > boskoltuksayisi(k):
            print("Rezervasyon talebi reddedildi.")
        else:
            rezervasyon(a, k)
            ucret = ucrethesapla(a, k)
            print("Bilet adedi: %d" % a)
            print("Toplam tutar: %d TL" % ucret)
            yeni_ucret = indirimyap(ucret, a, k)
            print("Yapilan indirim: %d TL" % (ucret - yeni_ucret))
            print("Net tutar: %d TL" % yeni_ucret)
            ciroekle(yeni_ucret, k)
    elif secim == 2:
        printkoltuk()
    elif secim == 3:
        koltuklar = yeni_dizi_olustur()
        ciro = {1: 0, 2: 0, 3: 0, 4: 0}
    elif secim == 4:
        ciroyazdir()
    else:
        print("Tekrar deneyiniz.")
