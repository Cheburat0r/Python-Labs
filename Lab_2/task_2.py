def find_common_participants(string1, string2, separate = ','):# TODO Напишите функцию find_common_participants
    list1 = string1.split(separate)
    list2 = string2.split(separate)
    common = list(set(list1).intersection(list2))
    return sorted(common)
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
print(find_common_participants(participants_first_group, participants_second_group, '|'))
# TODO Провеьте работу функции с разделителем отличным от запятой
