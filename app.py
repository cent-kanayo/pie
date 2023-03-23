# def linear_search(list, target):
#     for i in range(0, len(list)):
#         if list[i] == target:
#             return i
#     return None

# def binary_search(list, target):  
#     first = 0
#     last = len(list)
#     while first <= last:
#         midpoint = (first + last) // 2
#         if list[midpoint] == target:
#             return midpoint
#         elif list[midpoint] < target:
#             first = midpoint + 1
#         elif list[midpoint] > target:
#             last = midpoint - 1
#     return None

# recursive binary search 
def recursive_binary_search(list, target):
    if len(list) == 0:
        return False
    else:
        midpoint = len(list) // 2
    if list[midpoint] == target:
        return True
    else:
        if list[midpoint] < target:
           return recursive_binary_search(list[midpoint+1:], target)
        else:
            return recursive_binary_search(list[:midpoint], target)

def acertain(index):
    if index is not None:
        print("Index found at: ", index)
    else:
        print("Index not found in list")

acertain(recursive_binary_search([10, 20, 30, 40, 50], 33  ))

for i in range(0, 10):
    print("Hello", i)

print("hello world")

print("Hello from cyclobold")
print("hello from the linked file")

