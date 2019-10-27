set_counter = 0
keep_going = True
number_of_strings = int(input())

while keep_going:
    set_counter += 1
    strings = []
    for string in range(number_of_strings):
        strings.append(input())
    print(f"SET {set_counter}")
    for index in range(number_of_strings):
        if index < number_of_strings / 2:
            print(strings[index * 2])
            # print(f"index:{index} first half, show {index * 2}")
        else:
            print(strings[(number_of_strings - index) * 2 - 1])
            # print(f"index:{index} second half, show {(number_of_strings - index) * 2 -1 }")
    number_of_strings = int(input())
    keep_going = number_of_strings > 0
