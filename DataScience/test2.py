L = [1, 4, 0, 3, 5, 7]


def min_list(list):
    minimum = list[0]
    for i in list:
        if minimum > i:
            minimum = i
    return minimum


def max_list(list):
    maximum = list[0]
    for i in list:
        if maximum < i:
            maximum = i

    return maximum


def sorted_list(list):

    new_list = []
    while list:
        minim = min_list(list)

        list.remove(minim)
        new_list.append(minim)

    return new_list


# print(sorted_list(L))


def reverse_list(list):
    new_list = []
    while list:
        maxim = max_list(list)

        list.remove(maxim)
        new_list.append(maxim)

    return new_list


print(reverse_list(L))
