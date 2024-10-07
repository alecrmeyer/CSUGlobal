def linearSearch(val, list):
    for i in range(len(list)):
        if list[i] == val:
            return i
    return -1

nums = [1, 5, 4, 3, 6, 4, 5, 3, 8, 7, 4]
print(linearSearch(5, nums))
print(linearSearch(12, nums))
