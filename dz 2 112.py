score = int(input("Введи кількість балів: "))

if 0 <= score <= 49:
    print("Оцінка: незадовільно")
elif 50 <= score <= 69:
    print("Оцінка: задовільно")
elif 70 <= score <= 89:
    print("Оцінка: добре")
elif 90 <= score <= 100:
    print("Оцінка: відмінно")
else:
    print("Некоректна кількість балів")
