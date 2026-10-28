a = int(input("введите возраст: "))
if a < 0:
    print("некорректный возраст")
elif a <= 12:
    print("ребенок")
elif a <= 17:
    print("подросток")
elif a <= 64:
    print("взрослый")
else:
    print("пожилой")
