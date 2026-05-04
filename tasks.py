#1

def find_length_of_longest_continuous_increasing_subsequence(nums):
    if not nums:
        return 0
    
    max_len = 1      # максимальная длина
    curr_len = 1     # текущая длина возрастающей последовательности
    
    for i in range(1, len(nums)):
        if nums[i] > nums[i-1]:
            curr_len += 1
            max_len = max(max_len, curr_len)
        else:
            curr_len = 1
    
    return max_len

# Примеры
print(find_length_of_longest_continuous_increasing_subsequence([3, 2, 8, 9, 5, 10]))  # 3
print(find_length_of_longest_continuous_increasing_subsequence([1, 2, 7, 9, 0, 10]))  # 4
print(find_length_of_longest_continuous_increasing_subsequence([8, 8, 8, 8]))         # 1

""" Пояснение:

curr_len отслеживает длину текущей непрерывной возрастающей подпоследовательности, заканчивающейся в nums[i].

При нарушении возрастания (nums[i] <= nums[i-1]) сбрасываем curr_len = 1.

max_len хранит максимальное значение curr_len за всё время.

Алгоритм однопроходный, что даёт O(n). """

#2

def generate_pascals_triangle(n):
    if n <= 0:
        return []
    
    triangle = [[1]]  # первая строка
    
    for i in range(1, n):
        prev_row = triangle[-1]
        new_row = [1]  # первый элемент
        
        # заполняем внутренние элементы
        for j in range(1, i):
            new_row.append(prev_row[j-1] + prev_row[j])
        
        new_row.append(1)  # последний элемент
        triangle.append(new_row)
    
    return triangle

# Пример
n = 5
triangle = generate_pascals_triangle(n)
for row in triangle:
    print(row)

""" Пояснение:

triangle[i] — i-я строка (индексация с 0).

Для построения строки i используем строку i-1.

Количество элементов в i-й строке равно i+1.

Общее число элементов ~ n²/2, поэтому сложность O(n²).

Можно уменьшить память до O(n), если хранить только предыдущую строку, но для вывода всего треугольника нужен O(n²). """

#3

def coin_change(coins, amount):
    INF = float('inf')
    dp = [INF] * (amount + 1)
    dp[0] = 0
    
    for x in range(1, amount + 1):
        for c in coins:
            if x - c >= 0:
                dp[x] = min(dp[x], dp[x - c] + 1)
    
    return dp[amount] if dp[amount] != INF else -1

# Примеры
print(coin_change([1, 2, 5], 11))   # 3 (5+5+1)
print(coin_change([2], 3))          # -1
print(coin_change([1], 0))          # 0

""" 
Пояснение корректности:

Оптимальная структура: минимальное количество монет для суммы x достигается, если мы возьмём какую-то монету c и затем оптимально разменяем x - c.

Перебор всех монет гарантирует, что мы рассмотрим все возможности.

Благодаря восходящему вычислению от 0 до amount мы гарантированно имеем оптимальные значения для меньших сумм. """


#4 

def longest_palindrome(s):
    if len(s) <= 1:
        return s
    
    start, max_len = 0, 1
    
    def expand_around_center(left, right):
        nonlocal start, max_len
        while left >= 0 and right < len(s) and s[left] == s[right]:
            curr_len = right - left + 1
            if curr_len > max_len:
                max_len = curr_len
                start = left
            left -= 1
            right += 1
    
    for i in range(len(s)):
        # палиндром нечётной длины (центр в i)
        expand_around_center(i, i)
        # палиндром чётной длины (центр между i и i+1)
        expand_around_center(i, i + 1)
    
    return s[start:start + max_len]

# Примеры
print(longest_palindrome("babad"))   # "bab" или "aba"
print(longest_palindrome("cbbd"))    # "bb"
print(longest_palindrome("a"))       # "a"
print(longest_palindrome("ac"))      # "a" или "c"


""" Пояснение:

Функция expand_around_center расширяет палиндром от заданного центра, пока возможно.

Перебираем все возможные центры (2n-1 штук).

Для каждого центра расширение в худшем случае требует O(n) шагов, итого O(n²).

Подход с DP даёт ту же сложность O(n²) по времени и O(n²) по памяти, поэтому метод расширения от центра предпочтительнее по памяти. """