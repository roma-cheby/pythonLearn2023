def find_insert_position(mas, number):
    ans = 0
    if len(mas) == 0 or mas[0] > number:
        return 0
    elif number > mas[-1]:
        return len(mas) - 1

    right = len(mas) - 1
    left = 0

    while left < right:
        middle = (left + right) // 2
        if number < mas[middle]:
            right = middle
        else:
            left = middle + 1

    return left

print(find_insert_position([1, 2, 3, 3, 3, 5], 4))