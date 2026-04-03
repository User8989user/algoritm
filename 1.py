import heapq
from collections import deque
from typing import List, Optional

# ------------------------------------------------------------
# 1. Проверка, является ли дерево полным (complete binary tree)
# ------------------------------------------------------------
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_complete_tree(root: Optional[TreeNode]) -> bool:
    """
    Проверяет, является ли бинарное дерево полным.
    Полное дерево: все уровни заполнены, кроме возможно последнего,
    который заполняется слева направо.
    Используем BFS (обход в ширину). Как только встречаем первый пустой узел,
    все последующие узлы на том же уровне должны быть пустыми.
    """
    if not root:
        return True
    queue = deque([root])
    found_null = False
    while queue:
        node = queue.popleft()
        if node is None:
            found_null = True
        else:
            if found_null:
                # Встретили непустой узел после пустого -> не полное
                return False
            queue.append(node.left)
            queue.append(node.right)
    return True

# ------------------------------------------------------------
# 2. Объединение K отсортированных массивов с помощью мин-кучи
# ------------------------------------------------------------
def merge_k_sorted_arrays(arrays: List[List[int]]) -> List[int]:
    """
    Объединяет K отсортированных массивов в один отсортированный.
    Используется мин-куча, содержащая кортежи (значение, индекс_массива, индекс_элемента).
    Сложность: O(N log K), где N — суммарное количество элементов,
    K — количество массивов. Память: O(K) для кучи.
    """
    result = []
    min_heap = []

    # Инициализация: кладём первый элемент каждого массива в кучу
    for i, arr in enumerate(arrays):
        if arr:
            heapq.heappush(min_heap, (arr[0], i, 0))

    while min_heap:
        val, arr_idx, elem_idx = heapq.heappop(min_heap)
        result.append(val)
        # Если в этом массиве есть следующий элемент, добавляем его
        if elem_idx + 1 < len(arrays[arr_idx]):
            next_val = arrays[arr_idx][elem_idx + 1]
            heapq.heappush(min_heap, (next_val, arr_idx, elem_idx + 1))

    return result

# ------------------------------------------------------------
# 3. K-ый наименьший / наибольший элемент в массиве (через кучу)
# ------------------------------------------------------------
def kth_smallest_heap(arr: List[int], k: int) -> int:
    """
    Находит k-ый наименьший элемент в массиве.
    Используем max-кучу размера k (через отрицательные значения).
    Время: O(n log k), память: O(k).
    """
    if k <= 0 or k > len(arr):
        raise ValueError("Некорректное k")
    max_heap = []
    for num in arr:
        heapq.heappush(max_heap, -num)
        if len(max_heap) > k:
            heapq.heappop(max_heap)
    return -max_heap[0]

def kth_largest_heap(arr: List[int], k: int) -> int:
    """
    Находит k-ый наибольший элемент в массиве.
    Используем min-кучу размера k.
    Время: O(n log k), память: O(k).
    """
    if k <= 0 or k > len(arr):
        raise ValueError("Некорректное k")
    min_heap = []
    for num in arr:
        heapq.heappush(min_heap, num)
        if len(min_heap) > k:
            heapq.heappop(min_heap)
    return min_heap[0]

# ------------------------------------------------------------
# 4. K-ый наименьший / наибольший элемент в BST (in-order обход)
# ------------------------------------------------------------
def kth_smallest_bst(root: Optional[TreeNode], k: int) -> int:
    """
    Итеративный in-order обход (левый-корень-правый) даёт возрастающую последовательность.
    Останавливаемся на k-м элементе.
    Время: O(h + k), где h — высота дерева.
    """
    stack = []
    node = root
    count = 0
    while stack or node:
        while node:
            stack.append(node)
            node = node.left
        node = stack.pop()
        count += 1
        if count == k:
            return node.val
        node = node.right
    raise ValueError("k больше размера дерева")

def kth_largest_bst(root: Optional[TreeNode], k: int) -> int:
    """
    Reverse in-order обход (правый-корень-левый) даёт убывающую последовательность.
    Время: O(h + k).
    """
    stack = []
    node = root
    count = 0
    while stack or node:
        while node:
            stack.append(node)
            node = node.right
        node = stack.pop()
        count += 1
        if count == k:
            return node.val
        node = node.left
    raise ValueError("k больше размера дерева")

# ------------------------------------------------------------
# 5. Вычисление balance factor для каждого узла BST
# ------------------------------------------------------------
class BalanceTreeNode(TreeNode):
    def __init__(self, val=0, left=None, right=None):
        super().__init__(val, left, right)
        self.balance_factor = 0

def compute_balance_factors(root: Optional[BalanceTreeNode]) -> int:
    """
    Рекурсивно вычисляет высоту поддерева и заполняет поле balance_factor
    для каждого узла: balance_factor = высота(левого) - высота(правого).
    Высота пустого узла = 0.
    Возвращает высоту текущего узла (максимальная длина пути до листа + 1).
    """
    if not root:
        return 0
    left_h = compute_balance_factors(root.left)
    right_h = compute_balance_factors(root.right)
    root.balance_factor = left_h - right_h
    return max(left_h, right_h) + 1

# ------------------------------------------------------------
# 6. Зеркальное отражение бинарного дерева
# ------------------------------------------------------------
def mirror_tree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    """
    Рекурсивно меняет местами левые и правые поддеревья каждого узла.
    Алгоритм корректен, так как для каждого узла обмениваются дети,
    и затем рекурсивно обрабатываются поддеревья.
    Временная сложность: O(n), где n — количество узлов.
    Пространственная сложность: O(h) из-за стека рекурсии (h — высота).
    """
    if not root:
        return None
    # Меняем местами левого и правого потомка
    root.left, root.right = root.right, root.left
    # Рекурсивно отражаем поддеревья
    mirror_tree(root.left)
    mirror_tree(root.right)
    return root

# Итеративная версия (стек) — тоже O(n), но без риска переполнения рекурсии
def mirror_tree_iterative(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root:
        return None
    stack = [root]
    while stack:
        node = stack.pop()
        node.left, node.right = node.right, node.left
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return root