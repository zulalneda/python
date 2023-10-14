message = "Hello There. My name is Sadık Turan."
print(message)

my_list = [1,2,3]
print(my_list)
my_list = ["bir", 2, True , 5.6]
print(my_list)

list1 = ["one", "two", "three"]
list2 = ["four", "five", "six"]

numbers = list1 + list2
print(numbers)
print(len(numbers))
print(message[0])
print(numbers[2]) #liste olduğu için three ifadesini yazdırdı.

userA = ["Sadık", 36]
userB = ["Çınar", 2]

users = userA + userB
print(users)

users = [userA, userB]    #liste içindeki elemanları listeli bir şekilde göstermek istiyorsak kullanırız.
print(users)
print(users[1])
print(users[1][0])

#a = users[1]

#print(a[0])