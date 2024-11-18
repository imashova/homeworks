my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

i = 0

while i < len(my_list):
    number = my_list[i]

    if number < 0:
        break
    if number > 0:
        print(number)

    i += 1


    # first = my_list[0]
    # if my_list > 0:
    #     print(my_list)