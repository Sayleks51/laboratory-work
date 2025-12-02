numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим

count_of_numbers = len(numbers)

skip_None_1 = numbers[:4]

skip_None_2 = numbers[5:]

skip_None_3 = skip_None_1 + skip_None_2

sum_of_numbers = sum(skip_None_3)

average_of_numbers = round(sum_of_numbers/count_of_numbers, 2)

numbers[4] = average_of_numbers

print("Измененный список:", numbers)
