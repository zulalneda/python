message = "Hello there. My name is Neda Özmen."
x = " Hello there. My name is Neda Özmen."
message = message.upper() #tüm string ifadenin elemanlarını büyük harfle yazdırır.
print(message)

message = message.lower() #tüm string ifadenin elemanlarını küçük harfle yazdırır.
print(message)

message = message.title() #her kelimenin baş harfi büyük yazılır.
print(message)

message = message.capitalize() #sadece ilk harf büyük yazılır.
print(message)

message = message.strip() #başta veya sonda olan boşlukları siler, daha düzgün hale getirir.
print(message)

message = message.split() #tüm elemanları teker teker gösterir.
print(message)

print(message[0]) #ayrılan dizideki ilk elemanı yazdırır.

message = " ".join(message) #teker teker ayrılan elemanları aralarında boşluk bıraktırarak birleştirir.
print(message)

x = x.split(".") #tüm elemanları noktalardan itibaren ayırıp gösterir.
print(x)

index = message.find("Sadık")  #cümlede Sadık kelimsei olmadığı için -1(yok) dedi.
print(index)

y = message.find("neda")
print(y)

isFound = message.startswith("H") #metnin "H" ile başlayıp başlamadığını teyit etmek amacıyla kullanılır.
print(isFound)

isFound = message.endswith(".") #metnin "." ile bitip bitmediğini teyit etmek amacıyla kullanılır.
print(isFound)

message = message.replace(" ", "*")
print(message)

message = message.replace("neda","Zülal")
print(message)

message = message.center(50,"*")   #50 birimlik bir yere yazdırır. yanına * koyduğumuzda da 50'den arta kalan kısımları * ile kaplar.
print(message)

