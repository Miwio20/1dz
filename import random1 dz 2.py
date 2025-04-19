import random

secret = random.randint(1, 10)
tries = 3
print("Я загадав число від 1 до 10. Спробуй вгадати!")

while tries > 0:
    guess = int(input("Твоя спроба: "))
    if guess == secret:
        print("Правильно! Ти вгадав!")
        break
    elif guess > secret:
        print("Менше")
    else:
        print("Більше")
    tries -= 1

if guess != secret:
    print(f"На жаль, ти не вгадав. Чи2сло було: {secret}")
3