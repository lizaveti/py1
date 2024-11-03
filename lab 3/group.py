# TODO Напишите функцию find_common_participants
def find_common_participants(str1, str2, delimiter=','):
    list1 = str1.split(delimiter)
    list2 = str2.split(delimiter)

    common = list(set(list1) & set(list2))

    return sorted(common)


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(str1=participants_first_group, str2=participants_second_group, delimiter='|'))
