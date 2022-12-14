from random import uniform

N = int(input("Введите размерность массива: "))               #По заданию даём пользователю ввести размерность массива
massive = [0] * N                                             #Создаём массив с заданной размерностью
for i in range(N):
    massive[i] = uniform(0.01, 99.99)                         #Генерируем рандомные вещественные числа в массиве
print("Рандомный массив с заданной размерностью: ", massive)  #Выводим массив (входные данные)
maximum = massive[0]                                          #Переменная для поиска максимума
ind = 0                                                       #Переменная для поиска позиции макимума
for i in range(len(massive)):                                 #Перебираем все элементы созданного массива
    if massive[i] > maximum:                                  #Находим максимальный элемент путём сравнения
        maximum = massive[i]                                  #Запоминаем максимальный элемент
        ind = i                                               #Запоминаем индекс макимального элемента
print("Максимальный элемент массива: ", maximum,"и его индекс: ", ind)
for index, item in enumerate(massive):                        #Рассматриваем все индексы и значения массива
    if index > ind:                                           #Сравниваем Все индексы с индексом максимального элемента
        massive[index] = round(0, 1)                          #Все элементы после макимального элемента превращаем в 0

print(massive)
