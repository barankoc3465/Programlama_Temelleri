# kullanıcı_adı=input("Kullanıcı adı: ")
# parola=input("Parola: ")

# if kullanıcı_adı=="admin" and parola=="12345":
#     cevap="Başarıyla Giriş Yapıldı."
# else:
#     cevap="Girişiniz Kabul Edilmedi."

# print(cevap)


# meslek=input("Meslek: ")
# maas=int(input("Maaş: "))

# if meslek=="Memur" and maas<13000:
#     prim=maas*0.05
# elif meslek=="Doktor" and maas>=12500:
#     prim=maas*0.1
# else:
#     prim=maas*0.15

# print("Prim: ",prim)


# meslek=input("Meslek: ")
# maas=int(input("Maaş: "))

# if meslek=="Mühendis" and maas>=23000:
#     prim=maas*0.15
# elif meslek=="Muhtar" and maas<=22000:
#     prim= maas*0.20
# else:
#     prim=maas*0.25

# print("Prim: ",prim)


# meslek=input("Meslek: ")
# maas=int(input("Maaş: "))
# medeni_hal=input("Medeni Hal: ")

# if maas>=40000 and meslek!="Doktor" and medeni_hal=="Evli":
#     prim=maas*0.25
# elif meslek=="Berber" and maas>25000 and maas<40000:
#     prim=maas*0.2
# else:
#     prim=maas*0.3

# print("Prim: ",prim)


# meslek=input("Meslek: ")
# maas=int(input("Maaş: "))

# if meslek=="Memur" or maas>13000:
#     prim=maas*0.05
# elif meslek=="Doktor" or maas<12500:
#     prim=maas*0.1
# else:
#     prim=maas*0.15

# print("Prim: ",prim)


# meslek=input("Meslek: ")
# maas=int(input("Maaş: "))

# if meslek=="Berber" or meslek=="Oyuncu" or maas<13000 or maas>16000:
#     prim=maas*0.1
# elif maas>18000 or maas<12000 or meslek!="Bakkal":
#     prim=maas*0.3
# else:
#     prim=maas*0.5

# print("Prim",prim)


# meslek=input("Meslek: ")
# maas=int(input("Maaş: "))

# if meslek=="Doktor" and maas>15000 and maas<=40000:
#     prim=maas*0.04
# elif maas<15000 or maas>40000 or meslek!="Berber":
#     prim=maas*0.1
# else:
#     prim=maas*0.12

# print("Prim",prim)


# meslek=input("Meslek: ")
# maas=int(input("Maaş: "))

# if maas>20000 and maas<50000 and meslek=="Avukat":
#     prim=maas*0.05
# elif meslek=="Oyuncu" or maas<60000 or maas>80000:
#     prim=maas*0.08
# else:
#     prim=maas*0.03

# print("Prim: ",prim)


# meslek=input("Meslek: ")
# maas=int(input("Maaş: "))

# if meslek=="Berber" or maas<10000 or maas>40000:
#     prim=maas*0.18
# elif maas>30000 and maas<60000 and meslek!="Oduncu":
#     prim=maas*0.15
# else:
#     prim=maas*0.13

# print("Prim: ",prim)


# meslek=input("Meslek: ")
# maas=int(input("Maaş: "))

# if (maas>20000 and maas<40000) or (meslek=="Avukat" or meslek=="Doktor"):
#     prim=maas*0.02
# elif meslek=="Berber" and (maas<20000 or maas>40000):
#     prim=maas*0.06
# else:
#     prim=maas*0.07

# print("Prim: ",prim)


# meslek=input("Meslek: ")
# maas=int(input("Maaş: "))

# if meslek!="Garson" and (maas<15000 or maas>25000):
#     prim=maas*0.04
# elif meslek=="Doktor" or (maas>15000 and maas<25000):
#     prim=maas*0.11
# else:
#     prim=maas*0.15

# print("Prim: ",prim)


# maas=int(input("Maaş: "))

# if (maas>10000 and maas<30000) or (maas>50000 and maas<80000):
#     prim=maas*0.1
# else:
#     prim=maas*0.2

# print("Prim: ",prim)


# devam=int(input('Devam: '))
# vize=int(input('Vize: '))
# final=int(input('Final: '))
# ortalama=vize*0.4+final*0.6

# if devam>5 or final<45 or ortalama<60:
#     print("Kaldı.")
# else:
#     print("Geçti.")


# devam=int(input('Devam: '))
# vize=int(input('Vize: '))
# final=int(input('Final: '))
# ortalama=vize*0.4+final*0.6

# if devam<=5 and final>=45 and ortalama>=60:
#     print("Geçti.")
# else:
#     print("Kaldı.")

