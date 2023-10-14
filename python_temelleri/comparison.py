#a, b, c, d = 5, 5, 10, 4

#result = a==b #True
#print(result)

#a = int(input("1. sayı= "))
#b = int(input("2. sayı= "))
#result = (a >b)
#print(f"1. sayı {a} 2. sayıdan {b} büyüktür: {result}")



vize1 = int(input("1. vize: "))
vize2 = int(input("2. vize: "))
final = int(input("final: "))

result = (((vize1 + vize2) / 2) * 0,6) + (final * 0,4) 
print(f"dersten geçme durumunuz {result > 50} ")