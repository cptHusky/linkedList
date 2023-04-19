import random

def sort_bubble(list: list) -> list:
    for i in range(len(list)):
        argument = range(len(list) - i - 1)
        for j in argument:
            print(f'|{i=}|{j=}|\n'
                  f'|{argument=}|\n'
                  f'            {list}')
            print(f'        comparing list[{j}] and list[{j + 1}] {list[j], list[j + 1]}')
            if list[j] > list[j + 1]:
                print(f'        SWAPPING {j} AND {j + 1} {list[j], list[j + 1]}')
                list[j], list[j + 1] = list[j + 1], list[j]
                
    return list




amount = 6
a = []
for i in range(amount):
    a.append(random.randint(0, amount**2))



a = [5, 4, 3, 2, 1]
print(a)
print(sort_bubble(a))
