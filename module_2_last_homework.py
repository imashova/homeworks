for element in range(3, 21):
    password = f'{element} - '
    for x in range(1, element):
        for y in range(x + 1, element):
            if element % (x+y) == 0:
                password += f'{x}{y} '
    print(password)
