def password(num):
    passw = ''
    for i in range(1, 21):
        for j in range(i + 1, 21):
            if num % (i + j) == 0:
                passw += str(i) + str(j)
    return passw
num = int(input("Введите целое число от 3 до 20: "))
if 3 <= num <= 20:
    result = password(num)
    print('Пароль:', result)
else:
    print("Вы ввели неверное число.")