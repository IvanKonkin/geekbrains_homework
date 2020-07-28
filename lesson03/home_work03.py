def result(a, b, c):
    result_list = [a, b, c]
    result_list.remove(min(a, b, c))
    return sum(result_list)


print(result(13, 36, 46))
