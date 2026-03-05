"""
Решение 8 задач по алгоритмам на связных списках и массивах.
Все функции реализованы с учётом требований:
    - работа in-place, где требуется
    - использование двух указателей
    - сложность O(n) или O(n+m)
    - без лишних аллокаций
"""

# ---------- Базовые структуры и утилиты ----------
class Node:
    """Узел односвязного списка"""
    def __init__(self, val):
        self.val = val
        self.next = None

def print_list(head):
    """Печатает односвязный список в виде a->b->c"""
    vals = []
    while head:
        vals.append(str(head.val))
        head = head.next
    print("->".join(vals) if vals else "None")

# ---------- Задача 1. Разворот односвязного списка ----------
def reverse_list(head):
    """
    Разворачивает список in-place, изменяя ссылки между узлами.
    Возвращает новую голову.
    """
    prev = None
    curr = head
    while curr:
        next_node = curr.next   # запоминаем следующий
        curr.next = prev        # разворачиваем текущий узел
        prev = curr             # сдвигаем prev
        curr = next_node         # переходим к следующему
    return prev

# ---------- Задача 2. Найти середину списка ----------
def find_middle(head):
    """
    Находит середину списка за один проход (метод двух указателей).
    Для чётного количества узлов возвращает первый из двух центральных.
    """
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

# ---------- Задача 3. Удалить элемент из односвязного списка ----------
def remove_elements(head, val):
    """
    Удаляет все узлы со значением val in-place.
    Возвращает новую голову.
    """
    # удаляем совпадения в начале списка
    while head and head.val == val:
        head = head.next

    if not head:
        return None

    prev = head
    curr = head.next
    while curr:
        if curr.val == val:
            prev.next = curr.next   # пропускаем текущий узел
        else:
            prev = curr
        curr = curr.next
    return head

# ---------- Задача 4. Является ли одна строка исходной для другой (подпоследовательность) ----------
def is_subsequence(a, b):
    """
    Проверяет, можно ли получить строку b из строки a добавлением символов
    (т.е. является ли a подпоследовательностью b).
    """
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] == b[j]:
            i += 1
        j += 1
    return i == len(a)

# ---------- Задача 5. Поиск пары с заданной суммой в отсортированном массиве ----------
def has_pair_with_sum(arr, target):
    """
    Проверяет, есть ли в отсортированном массиве два элемента,
    сумма которых равна target, используя два указателя.
    """
    left, right = 0, len(arr) - 1
    while left < right:
        s = arr[left] + arr[right]
        if s == target:
            return True
        if s < target:
            left += 1
        else:
            right -= 1
    return False

# ---------- Задача 6. Проверка строки на палиндром ----------
def is_palindrome(s):
    """
    Проверяет, является ли строка палиндромом с помощью двух указателей.
    """
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

# ---------- Задача 7. Удаление дубликатов из отсортированного массива (in-place) ----------
def remove_duplicates(nums):
    """
    Удаляет дубликаты из отсортированного массива nums in-place.
    Возвращает новую длину массива (первые new_len элементов содержат результат).
    """
    if not nums:
        return 0

    slow = 0
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]
    return slow + 1

# ---------- Задача 8. Слияние двух отсортированных списков (без создания новых узлов) ----------
def merge_two_lists(l1, l2):
    """
    Сливает два отсортированных односвязных списка в один отсортированный.
    Использует только существующие узлы, возвращает голову нового списка.
    """
    dummy = Node(0)   # фиктивный узел для удобства
    tail = dummy

    while l1 and l2:
        if l1.val < l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    tail.next = l1 if l1 else l2
    return dummy.next

# ---------- ТЕСТИРОВАНИЕ ----------
if __name__ == "__main__":
    print("=" * 60)
    print("1. Разворот односвязного списка")
    head1 = Node(1)
    head1.next = Node(2)
    head1.next.next = Node(3)
    head1.next.next.next = Node(4)
    print("   Исходный:", end=" ")
    print_list(head1)
    rev = reverse_list(head1)
    print("   Развёрнутый:", end=" ")
    print_list(rev)

    print("\n" + "=" * 60)
    print("2. Найти середину списка")
    head2 = Node(1)
    head2.next = Node(2)
    head2.next.next = Node(3)
    head2.next.next.next = Node(4)
    head2.next.next.next.next = Node(5)
    print("   Список:", end=" ")
    print_list(head2)
    mid = find_middle(head2)
    print(f"   Середина: {mid.val}")

    print("\n" + "=" * 60)
    print("3. Удалить элемент из списка (удаляем 2)")
    head3 = Node(1)
    head3.next = Node(2)
    head3.next.next = Node(3)
    head3.next.next.next = Node(2)
    head3.next.next.next.next = Node(4)
    print("   Исходный:", end=" ")
    print_list(head3)
    head3 = remove_elements(head3, 2)
    print("   После удаления 2:", end=" ")
    print_list(head3)

    print("\n" + "=" * 60)
    print("4. Является ли одна строка исходной для другой")
    a1, b1 = "abc", "ahbgdc"
    print(f"   a='{a1}', b='{b1}' -> {is_subsequence(a1, b1)}")
    a2, b2 = "axc", "ahbgdc"
    print(f"   a='{a2}', b='{b2}' -> {is_subsequence(a2, b2)}")

    print("\n" + "=" * 60)
    print("5. Поиск пары с заданной суммой в отсортированном массиве")
    arr5 = [2, 7, 11, 15]
    target5 = 9
    print(f"   Массив: {arr5}, target={target5} -> {has_pair_with_sum(arr5, target5)}")
    target5 = 10
    print(f"   Массив: {arr5}, target={target5} -> {has_pair_with_sum(arr5, target5)}")

    print("\n" + "=" * 60)
    print("6. Проверка строки на палиндром")
    s6 = "racecar"
    print(f"   '{s6}' -> {is_palindrome(s6)}")
    s6 = "hello"
    print(f"   '{s6}' -> {is_palindrome(s6)}")

    print("\n" + "=" * 60)
    print("7. Удаление дубликатов из отсортированного массива in-place")
    nums7 = [1, 1, 2, 2, 3, 4, 4]
    print(f"   Исходный массив: {nums7}")
    new_len = remove_duplicates(nums7)
    print(f"   После удаления: {nums7[:new_len]}")

    print("\n" + "=" * 60)
    print("8. Слияние двух отсортированных списков")
    # список 3->6->8
    l8_1 = Node(3)
    l8_1.next = Node(6)
    l8_1.next.next = Node(8)
    # список 4->7->9->11
    l8_2 = Node(4)
    l8_2.next = Node(7)
    l8_2.next.next = Node(9)
    l8_2.next.next.next = Node(11)

    print("   Список A:", end=" ")
    print_list(l8_1)
    print("   Список B:", end=" ")
    print_list(l8_2)

    merged = merge_two_lists(l8_1, l8_2)
    print("   Объединённый:", end=" ")
    print_list(merged)

    print("\n" + "=" * 60)
    print("Все задачи выполнены.")