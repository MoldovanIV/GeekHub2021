# Написати функцію, яка приймає два параметри: ім'я файлу та кількість символів.
# На екран повинен вивестись список із трьома блоками - символи з початку, із середини та з кінця файлу.

def row_funct(file,number):
    with open(file) as f:
        rowf = f.read()
        if (len(rowf) // 3) <= number:
            return "Введена кількість символів не є коректною"
    if len(rowf) % 2 != 0 and number % 2 != 0:
        num_prob = (len(rowf) - 3 * number) // 2
        center = rowf[number + num_prob:number + num_prob + number]
        return f'{rowf[:number]}{" "*num_prob}{center}{" "*num_prob}{rowf[-number:]}'
    elif len(rowf) % 2 == 0 and number % 2 == 0:
        num_prob = (len(rowf) - 3 * number) // 2
        center = rowf[number + num_prob:number + num_prob + number]
        return f'{rowf[:number]}{" "*num_prob}{center}{" "*num_prob}{rowf[-number:]}'
    else:
        if len(rowf) % 2 != 0 and number % 2 == 0:
            rowf = rowf[:-1]
            num_prob = (len(rowf) - 3 * number) // 2
            center = rowf[number + num_prob:number + num_prob + number]
            return f'{rowf[:number]}{" "*num_prob}{center}{" "*num_prob}{rowf[-number:]}'
        elif len(rowf) % 2 == 0 and number % 2 != 0:
            rowf = rowf[:-1]
            num_prob = (len(rowf) - 3 * number) // 2
            center = rowf[number + num_prob:number + num_prob + number]
            return f'{rowf[:number]}{" "*num_prob}{center}{" "*num_prob}{rowf[-number:]}'
print(row_funct('row.txt',3)) 
