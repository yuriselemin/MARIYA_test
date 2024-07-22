

file = open('1.txt')
result = []

try:
    for i in file:
        try:
            result.append(int(i))
        except ValueError as ve:  # встретил строку
            print('Это не число!!!! Продолжаем!!!!')
            continue

except Exception:
    print('Что это такое? Не понимаю.....')

else:
    print('Все хорошо!')  #

finally:
    file.close()
    print('Закрыл файл!!!')

print(result)