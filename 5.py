"""
Задача флага 
Дан массив, состоящий из 0, 1 и 2.
Необходимо отсортировать его за линейное время.
Аналог задачи: Sort Colors 
Реализуйте алгоритм трёх указателей.
Кратко опишите, как поддерживаются границы для 0, 1 и 2 во время прохода по массиву.
 """


 def sort_colors(arr):
    low, mid, high = 0, 0, len(arr) - 1
    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:  # arr[mid] == 2
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
            # mid не увеличиваем, т.к. пришедший элемент может быть 0, 1 или 2

# Пример
a = [2, 0, 2, 1, 1, 0]
sort_colors(a)
print(a)  # [0, 0, 1, 1, 2, 2]