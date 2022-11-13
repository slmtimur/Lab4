from timeit import timeit
from task1_sorts import quick_sort
from task1_sorts import comb_sort

n = int(input("Введите кол-во элементов в массиве: "))
arr = list(map(int, input("Введите элементы массива: ").split()))

num = int(input("\nВыберите номер способа сортировки:\n 1) Быстрая сортировка\n 2) Сортировка расчёской\n"))
if num == 1:
    print("Результат работы быстрой сортировки:")
    print(*quick_sort(arr, n))
elif num == 2:
    print("Результат работы сортировки расчёской:")
    print(*comb_sort(arr, n))
else:
    print("Номер неверный")

print("\nСкорость работы быстрой сортировки -", timeit("quick_sort(arr, n)", number=100000, globals=globals()))
print("Скорость работы сортировки расчёской -", timeit("comb_sort(arr, n)", number=100000, globals=globals()))