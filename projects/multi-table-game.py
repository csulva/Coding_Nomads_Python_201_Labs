def multi_table(number):
    for x in range(1, 10):
        if number > 0 and number < 11:
            number = int(number)
            print(f'{x} * {number} = {x * number}\n')
            x += 1
        else:
            print("can't compute.")
    x = 10
    print(f'{x} * {number} = {x * number}')
multi_table(3)