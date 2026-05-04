# 1

def max_sum_subarray_k(arr, k):
    n = len(arr)
    if k > n:
        return None
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i+1] = prefix[i] + arr[i]
    
    max_sum = float('-inf')
    for i in range(n - k + 1):
        current_sum = prefix[i+k] - prefix[i]
        if current_sum > max_sum:
            max_sum = current_sum
    return max_sum

# Пример
print(max_sum_subarray_k([1, 2, 3, 4, 5], 3))  # 12 (3+4+5)