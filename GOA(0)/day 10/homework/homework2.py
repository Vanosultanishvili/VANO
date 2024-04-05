sqesi = str(input("ქალი ხართ თუ კაცი? "))
age = input(str("რამდენი წლის ბრძანდებით? "))

if sqesi != "კაცი" and int(age) > 60:
    print("პენსია გეკუთნით")
else:
    if sqesi != "ქალი" and int(age) > 65:
        print("პენსია გეკუთნით")

if sqesi == "ქალი" and int(age) < 60:
    print("პენსია არ გეკუთნით")

if sqesi == "კაცი" and int (age) < 65:
    print("პენსია არ გეკუთნით")

