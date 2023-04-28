import random
import cProfile

def sort_bubble(list: list) -> list:
    for i in range(len(list)):
        argument = range(len(list) - i - 1)
        for j in argument:
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
                
    return list

def sort_comb(list: list) -> list:
    gap = len(list)
    shrink_coef = 1.1
    sorted = False
    while not sorted:
        gap = int(gap / shrink_coef)
        if gap <= 1:
            gap = 1
            sorted = True
        i = 0
        while i + gap < len(list):
            if list[i] > list[i + gap]:
                list[i], list[i + gap] = list[i + gap], list[i]
                sorted = False
            i += 1
    return list

def sort_insert(list: list) -> list:
    for i in range(1, len(list)):
        key = list[i]
        j = i - 1
        while j >= 0 and key < list[j]:
            list[j + 1] = list[j]
            j -= 1
        list[j + 1] = key
    return list

def sort_merge(list: list) -> list:
    if len(list) <= 1:
        return list
    middle = len(list) // 2
    left_half = list[:middle]
    right_half = list[middle:]
    left_sorted = sort_merge(left_half)
    right_sorted = sort_merge(right_half)
    return aux_merge(left_sorted, right_sorted)
    
def aux_merge(left_half, right_half):
    result = []
    left_index = 0
    right_index = 0
    while left_index < len(left_half) and right_index < len(right_half):
        if left_half[left_index] < right_half[right_index]:
            result.append(left_half[left_index])
            left_index += 1
        else:
            result.append(right_half[right_index])
            right_index += 1
    result += left_half[left_index:]
    result += right_half[right_index:]
    
    return result


amount = 10000
sample_list = []
for i in range(amount):
    sample_list.append(random.randint(0, amount**2))

print('bubble')
cProfile.run('sort_bubble(sample_list)')
print('comb')
cProfile.run('sort_comb(sample_list)')
print('insert')
cProfile.run('sort_insert(sample_list)')
print('merge')
cProfile.run('sort_merge(sample_list)')
