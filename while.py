my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
i = 0
while my_list[1] >= my_list[0]:
    if int(my_list[i]) > 0:
        print(my_list[i])
        i += 1
    elif int(my_list[i]) == 0:
        my_list.remove(my_list[i])

    else:
        print('остановка цикла')
        break