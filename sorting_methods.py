import random

def bubble_sort(arr, n):
    flag = False
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                flag = False
            else:
                flag = True
        if flag:
            break

    return arr

def selection_sort(arr, n):
    n = len(arr)
    lowest_index = 0
    for i in range(n):
        lowest_index = i
        for j in range(i + 1, n):
            if a[j] < a[lowest_index]:
                lowest_index = j
        a[i], a[lowest_index] = a[lowest_index], a[i]

    return arr

def shell_sort(arr, n):
    interval = n // 2
    while interval > 0:
        for i in range(interval, n):
            temp = arr[i]
            j = i
            while j>= interval and arr[j - interval] > temp:
                arr[j] = arr[j - interval]
                j -= interval

            arr[j] = temp
        interval //= 2

array_bubble = [random.randint(-100, 100) for i in range(100)]
array_selection = [random.randint(-100, 100) for i in range(100)]
array_shell = [random.randint(-100, 100) for i in range(100)]

print(f"*** unsorted list ***\n {array_bubble}\n *** sorted list by bubble sort ***\n {bubble_sort(array_bubble, len(array_bubble))}")
print(f"*** unsorted list ***\n {array_selection}\n *** sorted list by bubble sort ***\n {bubble_sort(array_selection, len(array_selection))}")
print(f"*** unsorted list ***\n {array_shell}\n *** sorted list by bubble sort ***\n {bubble_sort(array_shell, len(array_shell))}")


