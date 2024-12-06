# toplam=0
# print("72'den büyük sayılar seçiniz.")
# for i in range(5):
#     sayi=int(input(str(i+1)+".Sayıyı giriniz: "))
#     if sayi>72:
#         toplam=toplam+sayi

# print("Sonucumuz: ",toplam)


# toplam=0
# print("6 sayı seçiniz.")

# for i in range(6):
#     sayi=int(input(str(i+1)+".Sayıyı giriniz: "))
#     toplam=toplam+sayi

# ortalama=toplam/(i+1)
# print("Sonucumuz: ",ortalama)


# ogrenci_sayisi=int(input("Öğrenci sayısını giriniz: "))
# genelortalama=0

# for i in range(ogrenci_sayisi):
#     vize=int(input(str(i+1)+".Öğrencinin vize notu: "))
#     final=int(input(str(i+1)+".Öğrencinin final notu: "))
#     ortalama=vize*(40/100)+final*(60/100)
#     print(str(i+1)+".Öğrencinin dönem sonu ortalaması: ",ortalama)
#     genelortalama=(genelortalama+ortalama)

# genelortalama=genelortalama/(i+1)
# print(str(i+1)+"Öğrenci için sınıf ortalaması: ",int(genelortalama))


# toplam=0
# adet=0

# for i in range(7):
#     sayi=int(input(str(i+1)+".Sayıyı giriniz: "))
#     if sayi<=100 and sayi>=50:
#         toplam=toplam+sayi
#         adet=adet+1
        
# if adet==0:
#     ortalama=0
# else:    
#     ortalama=toplam/adet
# print(ortalama)


# while True:
#     sayi=int(input("Bir sayı giriniz: "))
#     if sayi<0:
#         print("Girdiğiniz sayı 0'dan küçük olamaz, Lütfen tekrar giriniz.")
#         continue
#     for i in range(sayi-1,0,-1):
#         if sayi%i==0:
#             toplam+=i
#             adet+=1
#             print(toplam)
#             if adet==3:
#                 break
#     break

# if toplam==sayi and adet==3:
#     print(sayi,"Sayısı Yarı Mükemmel Sayıdır.")
# else:
#     print(sayi,"Sayısı Yarı Mükemmel Sayı Değildir.")


