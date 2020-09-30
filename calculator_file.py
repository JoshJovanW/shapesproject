def persegi(a):
    return (a**2)

def persegi_Panjang(a,b):
    return (a*b)

def segitiga_Siku(a,b):
    return((a*b)/2)

def segitiga_Samakaki(a,b):
    return(a*b)

def lingkaran(a):
    return(3.14*(a**2))

print("luas bentuk apa yang mau dicari? antara persegi, persegi panjang, segitiga siku-siku, segitiga atau lingkaran")

bentuk = input()

if bentuk == "persegi panjang":
    print("berapa panjang lebarnya?")

    a = int(input())

    print("berapa panjang tingginya?")

    b = int(input())

    print(persegi_Panjang(a,b))

elif bentuk == "persegi":
    print("berapa panjang sisi?")

    a = int(input())

    print(persegi(a))

elif bentuk == "segitiga siku-siku":
    print("berapa lebar basenya?")

    a = int(input())

    print("berapa panjang tingginya?")

    b = int(input())

    print(segitiga_Siku(a,b))

elif bentuk == "segitiga":
    print("berapa panjang basenya?")
    a = int(input())
    print("berapa panjang tingginya?")
    b = int(input())
    print(segitiga_Samakaki(a,b))

elif bentuk == "lingkaran":
    print("brp radiusnya")
    a = int(input())
    print(lingkaran(a))

else:
    print("terima kasih")
