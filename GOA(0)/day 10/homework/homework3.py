age = input("enter ur age: ")
dadage = input("enter ur dads age: ")

if int(dadage) % int(age) <= 2:
    print("bingo")
else:
    print("mouse")