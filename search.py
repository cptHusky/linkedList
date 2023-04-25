def search_binary(input_list: list, value: int | str) -> int | None:
    left, right = 0, len(input_list) - 1
    while left <= right:
        mid = (left + right) // 2
        print(left, mid, right)
        if input_list[mid] == value:
            return mid
        elif input_list[mid] < value:
            left = mid + 1
        else:
            right = mid - 1
    return None
