# Search examples
# 1)
# def linear_search(arr, number):
#     for item in arr:
#         if item == number:
#             return item
#     return None  
# numbers = [4, 2, 7, 1, 9, 3]
# result = linear_search(numbers, 7)
# print(result)


# 2)
# def binary_search(arr, number):
#     left = 0
#     right = len(arr) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if arr[mid] == number:
#             return arr[mid]
#         elif arr[mid] < number:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return None
# numbers = [1, 2, 3, 4, 7, 9]
# result = binary_search(numbers, 3)
# print(result) 


# 3)
# def ternary_search(arr, number):
#     left = 0
#     right = len(arr) - 1
#     while left <= right:
#         mid1 = left + (right - left) // 3
#         mid2 = right - (right - left) // 3
#         if arr[mid1] == number:
#             return arr[mid1]
#         if arr[mid2] == number:
#             return arr[mid2]
#         if number < arr[mid1]:
#             right = mid1 - 1
#         elif number > arr[mid2]:
#             left = mid2 + 1
#         else:
#             left = mid1 + 1
#             right = mid2 - 1
#     return None
# numbers = [1, 3, 5, 7, 9, 12, 15, 18, 21]
# result = ternary_search(numbers, 23)
# print(result)


#Sort examples
# 1)
# def bubble_sort(arr):
#     for i in range(len(arr)):
#         for j in range(0, len(arr) - i - 1):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#     return arr
# nums = [64, 34, 25, 12, 22, 11, 90]
# print(bubble_sort(nums))


# 2)
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     base_element = arr[len(arr) // 2]
#     left = [x for x in arr if x < base_element]    
#     middle = [x for x in arr if x == base_element] 
#     right = [x for x in arr if x > base_element]   
#     return quick_sort(left) + middle + quick_sort(right)
# nums = [10, 7, 8, 9, 1, 5]
# print(quick_sort(nums)) 


# 3) Selection sort
# def selection_sort(arr):
#     for i in range(len(arr)):
#         min_idx = i
#         for j in range(i + 1, len(arr)):
#             if arr[j] < arr[min_idx]:
#                 min_idx = j
#         arr[i], arr[min_idx] = arr[min_idx], arr[i]
#     return arr
# nums = [29, 10, 14, 37, 13]
# print(selection_sort(nums))