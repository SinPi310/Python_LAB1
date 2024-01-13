import random

N = 10
numbers = [random.randint(1, 100) for _ in range(N)]

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

sorted_numbers = sorted(numbers)

numbers_bubble_sort = numbers.copy()

bubble_sort(numbers_bubble_sort)

print("losowe liczby:", numbers)
print("Posortowane (sortowanie bąbelkowe):", numbers_bubble_sort)
print("Posortowane (sorted()):", sorted_numbers)
