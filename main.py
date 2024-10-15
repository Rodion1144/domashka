my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
list = []
n = 0
while n < len(my_list) and my_list[n] > 0:
    list.append(my_list[n])
    n += 1
print(list)
