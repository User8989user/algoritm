from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

""" Восстановление бинарного дерева из массива
Дан массив, представляющий бинарное дерево 
(например, в виде уровнями — level-order).
Необходимо восстановить структуру бинарного дерева.
Что нужно сделать:
Реализуйте функцию, которая строит дерево по переданному массиву. 
Объясните, как определяется связь родитель–потомок 
и какая структура данных используется для хранения узлов. """


def build_tree_from_level_order(arr):
    """
    Строит бинарное дерево из массива level‑order.
    :param arr: list, элементы могут быть None (отсутствие узла)
    :return: TreeNode — корень дерева
    """
    if not arr or arr[0] is None:
        return None

    root = TreeNode(arr[0])
    queue = deque([root])
    i = 1
    while queue and i < len(arr):
        node = queue.popleft()

        # Левый потомок
        if i < len(arr) and arr[i] is not None:
            node.left = TreeNode(arr[i])
            queue.append(node.left)
        i += 1

        # Правый потомок
        if i < len(arr) and arr[i] is not None:
            node.right = TreeNode(arr[i])
            queue.append(node.right)
        i += 1

    return root

"""
Объяснение:
Связь родитель–потомок определяется индексами в массиве: для узла
 с индексом i левый потомок — 2*i+1, правый — 2*i+2. 
 Мы строим дерево, обрабатывая узлы в порядке уровня, 
 чтобы корректно восстановить все связи.
 Хранение осуществляется в объектах TreeNode, связанных ссылками.
"""