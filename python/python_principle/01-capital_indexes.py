def capital_indexes(value):
    index = 0
    up_list = []
    for char in value:
        if char.isupper():
            up_list.append(index)
        index += 1
    print(up_list)

value = "HeLlO"
capital_indexes(value)
