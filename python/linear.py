import time
import random

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index if the target is found
    return -1  # Return -1 if the target is not found

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1  # Return -1 if the target is not found

def variance_calc(sample):
    sq_diff = []
    mean = sum(sample) / len(sample)
    for j in range(len(sample)):
        sq_diff.append((sample[j] - mean) ** 2)
    sum_sq_diff = sum(sq_diff)
    variance = sum_sq_diff / (len(sample) - 1)
    return variance
    

entrada = input("Linear(1) ou Binaria(2)?\n")

# Prompt the user to enter the size of the array
size = int(input("Tamanho: "))

# Fill the array with random elements from 1 to size
# arr = [random.randint(1, size) for _ in range(size)]

# Fill the array with ascending elements from 1 to size
arr = list(range(1, size+1))

linear_sample = []
binary_sample = []

# Prompt the user to enter the number they want to find
target = int(input("Elemento: "))

if entrada == "1":
    total_time = 0
    for _ in range(5):
        start_time = time.time()
        index = linear_search(arr, target)
        elapsed_time = time.time() - start_time
        total_time += elapsed_time
        linear_sample.append(elapsed_time)
    average_time = total_time / 5
    print(f"Tempo médio: {average_time * 1000:.2f} +/- {variance_calc(linear_sample) * 1000:.2f}ms")
else:
    arr.sort()
    total_time = 0
    for _ in range(5):
        start_time = time.time()
        index = binary_search(arr, target)
        elapsed_time = time.time() - start_time
        total_time += elapsed_time
        binary_sample.append(elapsed_time)
    average_time = total_time / 5
    print(f"Tempo médio: {average_time * 1000:.2f} +/- {variance_calc(binary_sample) * 1000:.2f}ms")

if index != -1:
    print("Elemento", target, "está na posição", index)
else:
    print("Elemento", target, "não foi encontrado")
