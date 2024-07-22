

file = open('1.txt', 'r', encoding='utf-8')
result = []

try:
    for i in file:
        try:
            result.append(int(i))
        except ValueError as ve:  # встретил строку
            print(f'Это не число: {ve}!!!! Продолжаем!!!!')
            continue

except Exception:
    print('Что это такое? Не понимаю.....')

else:
    print('Все хорошо!')  #

finally:
    file.close()
    print('Закрыл файл!!!')

print(result)