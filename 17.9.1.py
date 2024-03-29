num_list = '25 16 32 9 4 30' # на вход подана последовательность чисел
 
num_person = int(input('Введите число\n')) # запрос числа от пользователя
 
def new_sort(num_list, num_person): # задаём функцию для обработки
    try:
        a = list(map(int, num_list.split())) # итоговая переменная преобразования последовательности в список
 
        while num_person <= min(a) or num_person >= max(a): # проверка на попадание числа в диапазон
            print('Число вне диапазона списка\n')
            num_person = int(input('Введите число\n'))
 
        a.append(num_person) # добавляем введенное число к списку
        a.sort()   # сортируем получившуюся последовательность
        return a
 
    except ValueError:          # проверка на ввод пользователем именно числа 
        print('Неверный ввод')
 
func_sort = new_sort(num_list, num_person)  # задаем предыдущую функцию как переменную для обработки
 
def binary_search(func_sort, num_person):  # создаем функцию для алгоритма двоичного поиска
    low = 0                                # устанавливаем нижнюю границу поиска
    high = len(func_sort) - 1              # устанавливаем верхнюю границу поиска 
 
    while low <= high:                     # задаем цикл для обработки
 
        middle = (low + high) // 2         # находим середину 
 
        if func_sort[middle] == num_person:
            return f'Индекс предыдущего элемента: {middle - 1}' # если введенное число в середине списка возвращаем индекс элемента, который стоит перед ним
        
        elif func_sort[middle] > num_person: # если середина больше введенного числа - ищем в левой половине последовательности
            high = middle - 1
        
        else:                               # иначе ищем в правой 
            low = middle + 1
 
    return None                             # выводим в случае не произошедшей проверки
 
print(binary_search(func_sort, num_person))  # выводим результат работы функции - индекс позиции элемента, который меньше введенного пользователем числа