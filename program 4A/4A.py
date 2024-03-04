def insertion_sort(arr):
 for i in range(1, len(arr)):
 key = arr[i]
 j = i - 1
 while j >= 0 and key < arr[j]:
 arr[j + 1] = arr[j]
 j -= 1
 arr[j + 1] = key
arr = input("Enter a list of numbers separated by commas: ").split(",")
arr = [int(x) for x in arr]
print("Original list:", arr)
insertion_sort(arr)
print("Sorted list:", arr)