
n = input("Введите номер билета (шестизначный): ")


if len(n) == 6 and n.isdigit():

    first_half = n[:3]
    second_half = n[3:]

    sum_first_half = sum(int(digit) for digit in first_half)
    sum_second_half = sum(int(digit) for digit in second_half)

    if sum_first_half == sum_second_half:
        print("yes")
    else:
        print("no")
else:
    print("Неверный ввод. Пожалуйста, введите шестизначный номер билета.")

