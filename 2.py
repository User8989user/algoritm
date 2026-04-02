""" Имеется два ксерокса, копирующих документ за x и y минут. 
Нужно найти минимальное время, за которое можно сделать N копий. 
Оба ксерокса работают одновременно, копии не делятся. """

def min_time_copy(n: int, x: int, y: int) -> int:
    left, right = 0, max(x,y)* (n - 1)
    while left + 1 < right:
        mid = (left + right) // 2
        copies = mid // x + mid // y
        if copies == n:
            return mid
        elif copies < n - 1:
            left = mid + 1
        else :
            right = mid
    return left + min(x,y)


if __name__ = "__main__":
    try:
        n = int(input("Введите количество копий: "))
        x = int(input("x = "))
        y = int(input("y = "))
        result = min_time_copy(n, x, y)
        print("Время для создания {n} копий равно {result}")


""" Объяснение:
Проверка условия достаточности: за время t первый ксерокс делает t // x копий, второй – t // y.
 Если их сумма ≥ N, значит за это время можно успеть сделать нужное количество.
 Бинарный поиск по времени даёт сложность O(log (max(x,y)*N)). """
