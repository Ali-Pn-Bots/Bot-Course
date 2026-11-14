# p = 800000
# c = 5
# dc = 15/100
# t = p * c
# dc_a = t * dc
# fp = t - dc_a
# print(fp)

# p = 10000
# c = int(input("count : "))
# t = p * c
# t *= 0.9
# print("Price :",t)
# print("Final_Price :",int(final_price))

# n1 = float(input("Number1 : "))
# n2 = float(input("Number2 : "))
# print(n1 * n2)

# n = input("Name : ")
# a = int(input("Age : "))
# print(a + 5)

# p = int(input("Price : "))
# c = int(input("Count : "))
# t = p * c
# print(f"Total is {t}")

# If,Elif,Else
# a = int(input("age : "))
# if a >= 18:
#     print("mature")
# else:
#     print("immature")

# g = int(input("grade : "))
# if g >= 20 or g <= 0:
#     print("Error")
# elif g >= 10:
#     print("Pass")
# else:
#     print("Fail")

# For
# for i in range(0,10,2):
#     print(i,end = " ")

# fruits = ['apple', 'banana', 'orange']
# for fruit in fruits:
#     print(f"{fruit} is fruit")

# names = ['Ali', 'Reza', 'Farhad']
# for name in names:
#     print(f"Hello {name}")

# s = 0
# for i in range(101):
#     s += i
# print(f"sum is {s}")

# for i in range(10):
#     print(i)

# i = 1
# while i <= 10:
#        print(i)
#        i += 1

# for i in range(1,11):
#     print(f"3 * {i} = {3 * i}")

# sum = 0
# for i in range(0,101,2):
#     sum += i
# print(f"Even_Sum is {sum}")
#
# n = int(input("Number : "))
# p = 1
# for i in range(1,n + 1):
#     p *= i
# print(f"Fuck is {p}")

# While
# i = 1
# while i <= 10:
#        print(i)
#        i += 1

# i = 1
# while True:
#     print(i)
#     if i == 3:
#         break
#     else:
#         i += 1
# print("Break")

# for i in range(10):
#     if i % 2 != 0:
#         continue
#     print(i)

# while True:
#     n1 = float(input("Number1 : "))
#     n2 = float(input("Number2 : "))
#     print(["+","-","*","/","Stop"])
#     ch = input("Choose One : ")
#     if ch == "+":
#         print(n1 + n2)
#     elif ch == "-":
#         print(n1 - n2)
#     elif ch == "*":
#         print(n1 * n2)
#     elif ch == "/":
#         if n2 == 0:
#             print("Error")
#         else:
#             print(n1 / n2)
#     elif ch == "stop":
#         print("Bye!")
#         break
#     else:
#         print("Error")

# s = 0
# while True:
#     n = int(input("Number : "))
#     if n == 0:
#         break
#     else:
#         s += n
# print(f"Sum is {s}")

# for n in range(1,21):
#     if n % 3 == 0:
#         continue
#     print(n,end=" ")

# chance = 3
# print(f"Chance = {chance}")
# while chance != 0:
#     password = int(input("Password : "))
#     if password == 1234:
#         print("Welcome!")
#         break
#     else:
#         chance -= 1
#         print(f"Chance = {chance}")
# else:
#     print("Siktir!")

# N = []
# while True:
#     n = float(input("Number : "))
#     if n == 00:
#         break
#     else:
#         N.append(n)
# print(f"Avg is {sum(N)/len(N)}")

# List
# names = ["Ali","Reza","Farhad"]
# print(names)
# print(*names,sep = ",")
# print(names[0])
# print(names[1])
# print(len(names))
# names[1] = "Hesam"
# names.append("Javad")
# names.insert(0,"Mehran")
# names.remove("Farhad")
# last = names.pop()
# print(last)
# print(names)

# fruits = ["apple","banana","orange"]
# for f in fruits:
#     print(f"{fruit} is Fruit")

# names = ['Mehran', 'Ali', 'Hesam']
# for i,n in enumerate(names):
#     print(f"{name} in {[i]}")
#
# fruits = ["apple","banana","orange"]
# print("apple" in fruits)  # True
# print("cherry" in fruits) # False

# numbers = [5,2,1,4,3]
# numbers.sort()
# print(numbers)
# numbers.reverse()
# print(numbers)
#
# numbers = [5,2,1,4,3]
# numbers.sort(reverse=True)
# print(numbers)

# Dict
# customer = {"name" : "Hesam",
#             "age" : '21',
#             "phone" : "09146407338"
#             }
# print(customer)
# print(customer.get("age"))
# print(customer.get("email"))
# print(customer.get("email","Email Is Not Exist"))
# print(customer.get("name"))
# customer["Age"] = 22
# customer["city"] = "Tabriz"
# del customer["phone"]
# print(customer)

# customer = {"name" : "Hesam","age" : '21',"phone" : "09146407338"}
# if "phone" in customer:
#     print(f"The Phone Exists : {customer["phone"]}")
# else:
#     print("The Phone Doesn't Exist!")

# customer = {"name" : "Hesam",
#             "age" : '21',
#             "phone" : "09146407338",
#             "city" : "Tabriz"
#             }
# for key in customer.keys():
#     print(key,end = "|")
# print()
# for value in customer.values():
#     print(value,end = "|")
# print()
# for key,value in customer.items():
#     print(key,":",value)

# customers = [{"name" : "Hesam","age" : '21',"city" : "Tabriz"},
#              {"name" : "Alireza","age" : '53',"city" : "Tabriz"},
#              {"name" : "Horieh","age" : '46',"city" : "Tabriz"}]
# for c in customers:
#     print(c["name"],"from",c["city"])

# customers = [{"name" : "Hesam","age" : 21,"city" : "Tabriz"},
#              {"name" : "Alireza","age" : 53,"city" : "Tehran"},
#              {"name" : "Horieh","age" : 46,"city" : "Tehran"}]
# tehran = []
# for c in customers:
#     if c["city"] == "Tehran":
#         tehran.append(c)
# print(f"Count Of Tehrani Customers : {len(tehran)}")
# for c in tehran:
#     print(c["name"])

# product = {"name" : "PS5 PRO","price" : 400000000,"stock" : 7}
# print(product.get("name"))
# print(product.get("price"))
# print(product.get("stock"))
# print(product.get("discount"))
# product["price"] *= 1/1
# product["stock"] -= 5
# product["color"] = "White"
# del product["stock"]
# for key,value in product.items():
#     print(key,"=",value)

# products = [{"name" : "PS5","price" : 100000000,"stock" : 0},
#              {"name" : "PS5 Slime","price" : 200000000,"stock" : 3},
#              {"name" : "Ps5 Pro","price" : 400000000,"stock" : 1}]
# for p in products:
#     if p["stock"] > 0:
#         print(p["name"])


# products = [{"name" : "PS5","price" : 100000000,"stock" : 0},
#              {"name" : "PS5 Slime","price" : 200000000,"stock" : 3},
#              {"name" : "Ps5 Pro","price" : 400000000,"stock" : 1}]
# t = []
# for p in products:
#     p["price"] *= p["stock"]
#     t.append(p["price"])
# print(f"{sum(t):,.0f}")

# name = input("Name : ")
# age = input("Age : ")
# if age.isdigit() == True:
#     age = int(age)
# else:
#     print("Siktir")
# city = input("City : ")
# customer = {"Name" : name,"Age" : age,"City" : city}
# print(customer)


# age = input("Age : ")
# if age.isdigit() == True:
#     customer["Age"] = age
# else:
#     print("Siktir")

# with open("note_1.txt","w",encoding = "utf-8") as f:
#     f.write("First\nSecond")
#
# with open("note_1.txt","a",encoding = "utf-8") as f:
#     f.write("\nThird")
#
# with open("note_1.txt","r",encoding = "utf-8") as f:
#     print(f.read())

# with open("note_1.txt","r",encoding="utf-8") as f:
#     for i,line in enumerate(f,start=1):
#         print(f"line_{i} : {line.strip()}")

# try:
#     with open("nope.txt","r",encoding = "utf-8") as f:
#        print(f.read())
# except FileNotFoundError:
#        print("File Not Found")

# with open("todo.txt","w",encoding="utf-8") as f:
#     f.write("Wake Up\nGo To Work\nDo Work")
#
# with open("todo.txt","a",encoding = "utf-8") as f:
#     f.write("\nBack To Home")
#
# with open("todo.txt","r",encoding = "utf-8") as f:
#     print(f.read())
#
# with open("todo.txt","r",encoding="utf-8") as f:
#     for i,line in enumerate(f,start=1):
#         print(f"line_{i} : {line.strip()}")
#
# try:
#     with open("missing.txt","r",encoding = "utf-8") as f:
#        print(f.read())
# except FileNotFoundError:
#        print("File Not Found,Please Create It")

# note = input("note : ")
# with open("Note.txt","a",encoding = "utf-8") as f:
#     f.write(note + "\n")
# print("\n---note---")
# with open("Note.txt","r",encoding = "utf-8") as f:
#     print(f.read())































