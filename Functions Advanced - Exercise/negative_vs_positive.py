def find_numbers(string):
    current_list = [int(ch) for ch in string.split(" ")]
    positive = []
    negative = []
    for digit in current_list:
        if digit > 0:
            positive.append(digit)
        else:
            negative.append(digit)
    final_result = f"{sum(negative)}" + '\n' + f"{sum(positive)}" + '\n'
    if abs(sum(negative)) > abs(sum(positive)):
        final_result += "The negatives are stronger than the positives"
    else:
        final_result += "The positives are stronger than the negatives"
    return final_result


print(find_numbers(input()))