from matplotlib import mlab
l = [32, 53, 433, -2, 431, -13, -4, 0, 733, -10, 13]


def search_minimum(list) -> int:
    min_val = list[0]
    counter = 0
    indx = 0
    for i in list:
        counter += 1
        if min_val >= i:
            min_val = i
            indx = counter - 1

    return min_val, indx


minimum = search_minimum(l)
print(minimum)


def search_maximum(list):
    max_val = list[0]
    indx = 0
    counter = 0
    for i in list:
        counter += 1
        if max_val <= i:
            max_val = i
            indx = counter - 1

    return max_val, indx


maximum = search_maximum(l)
print(maximum)

# print(max(l))
# print(min(l))


def list_sorted(list):
    min = search_minimum(list)
    new_list = []
    for i in list:
        new_list.append(min)
        print(min)


print(list_sorted(l))
