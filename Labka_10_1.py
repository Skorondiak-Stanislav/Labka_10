"""
13.	Об’єкт “Впорядкований масив” (елементами масиву є цілі числа, які завжди впорядковані за зростанням)
поля
	для зберігання кількості елементів масиву;
	масив елементів;
методи
	виведення на екран;
	додавання нового елемента;
	видалення вказаного елемента;
	знаходження елемента, з використанням бінарного пошуку.

"""
import random
class Ordered_array:
    a = []
    n = int(input("Введіть кількість елементів списку="))
    z = list(random.randint(1,100) for el in range(1, n+1))
    z.sort()
    a.append(z)
    print(a)
    b = int(input("Введіть новий елемент:"))
    z.append(b)
    z.sort()
    print(a)
    m = int(input("Вкажіть елемент для видалення:"))
    for i in range(len(a)):
        for j in range(len(a[i])):
            if m == a[i][j]:
                k = j
    for el in a:
        el.pop(k)

    print(a)