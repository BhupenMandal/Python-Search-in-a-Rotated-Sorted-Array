def rotated_array_search(input_list, num):
    if not input_list or not num:
        return -1

    return binary_search(input_list, num, 0, len(input_list) - 1)


def binary_search(arr, target, start_index, end_index):
    if start_index > end_index:
        return -1

    mid_index = (start_index + end_index) // 2

    if arr[mid_index] == target:
        return mid_index

    if arr[start_index] <= arr[mid_index]:

        if arr[start_index] <= target <= arr[mid_index]:
            return binary_search(arr, target, start_index, mid_index)
        else:
            return binary_search(arr, target, mid_index + 1, end_index)

    elif arr[mid_index] < target < arr[end_index]:
        return binary_search(arr, target, mid_index + 1, end_index)

    return binary_search(arr, target, start_index, mid_index - 1)


def linear_search(input_list, number):
    if not input_list:
        return -1
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
test_function([[5, 1, 2, 3, 4], 1])

test_function([[], 6])


first_half = [x for x in range(2000, 5000)]
second_half = [y for y in range(0, 2000)]
rotated_arr = first_half + second_half


test_function([rotated_arr, 2555])

test_function([rotated_arr, 50000])

test_function([[], None])
test_function([None, 3])
test_function([None, None])
