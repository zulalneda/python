def toplama(numara1,numara2):
    return (numara1 + numara2)

x = int(input("İlk numarayı giriniz: "))
y = int(input("İkinci numarayı giriniz: "))
print(toplama(x,y))


while True:
    try:
        benimInt = int(input("Numaranızı giriniz: "))
    except:
        print("Lütfen gerçek bir numara giriniz.")
        continue
    else:
        print("Teşekkürler")
        break
    finally:
        print("bizi tercih ettiğiniz için çok teşekkür ederiz. ")

        

