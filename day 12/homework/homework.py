info = []

name = input("Enter your name: ")
surname = input("Enter your surname: ")
age = int(input("Enter your age: "))
place = input("Enter your country: ")

info.append((name, surname, age, place))

print(info[1:3])

#დავალება 2

negative = int(input("Enter a negative number: "))
list = []
for i in range(0, negative, -1):
    list.append(i)

print(list)

#დავალება 3
list1 = ["whiplash", "shrek", "fast and furious 9", "breaking bad", "harry potter"]

print(list1[0:3])
print(list1[-1:-3])

#დავალება 4
academy = input("შეიყვანეთ აკადემიის სახელი: ")

if academy[0:1] == "G":
    print("GOA არის საუკეთესო არჩევანი თუ აკადემიას ეძებ")
else:
    print("არასწორი არჩევანია")
