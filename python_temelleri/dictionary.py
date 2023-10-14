#key - value
#41 => Kocaeli 34=> İstanbul

sehirler = ["Kocaeli","İstanbul"]
plakalar = [41, 34]
#print(plakalar[sehirler.index("Kocaeli")])

plakalar = { "Kocaeli" : 41, "İstanbul" : 34} #key - value
#print(plakalar["Kocaeli"])
#print(plakalar["İstanbul"])

plakalar["Ankara"] = 6 #tuple olan bilgiye 


print(plakalar)







users = {
    "sadikturan": {
        "age": 36,
        "roles":["user"],
        "email": "sadik@gmail.com",
        "address": "kocaeli",
        "phone": "1231231"
    },
    "cinarturan":{
        "age": 2,
        "roles": ["admin","user"],
        "email":"cinar@gmail.com",
        "address": "kocaeli",
        "phone": "3213211"
    }
}

print(users["cinarturan"]["roles"][0])