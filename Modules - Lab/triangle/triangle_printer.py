def print_triangle(size):
    result = []
    for num in range(1, size + 1):
        current_result = ''
        for current_num in range(1, num + 1):
            current_result += f'{current_num} '
        result.append(current_result)
    for num in range(size - 1, 0, - 1):
        current_result = ''
        for current_num in range(1, num + 1):
            current_result += f'{current_num} '
        result.append(current_result)
    return '\n'.join(result)