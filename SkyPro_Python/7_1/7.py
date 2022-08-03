# Информация о пользователях
# Ключи словаря: f i o pass birthday phone position
# Пользователи для добавления


information_for_add = """Киселёв / Всеволод / Эдуардович / 342 020 / 14 ноября 2001 года / +7 (908) 161-64-28 / \
главный инженер
Довлатова / Эмилия /  Ефимовна / 342 000 / 18 мая 2001 года / +7 (924) 588-50-15 / технолог
Аверин / Мартын / Егорович / 217 340 / 12 февраля 1981 года / +7 (933) 768-22-15 / технолог
Князева / Августа / Егоровна / 320 021 / 2 июля 1984 года / +7 (965) 886-27-01 / расфасовщик
Шанская / Аграфена / Семёновна / 116 404 / 7 июля 1982 года / +7 (954) 940-47-96 / психолог для рыб"""

employees = {}

inform_list = information_for_add.split('\n')
employees_list = [information.strip().split('/') for information in inform_list]

for employee in employees_list:
    employee_dict = {'f': employee[0].strip(),
                     'i': employee[1].strip(),
                     'o': employee[2].strip(),
                     'pass': employee[3].strip(),
                     'birthday': employee[4].strip(),
                     'phone': employee[5].strip(),
                     'position': employee[6].strip()}

    employees[employee[0]] = employee_dict.copy()

for employee in employees.values():
    for key, value in employee.items():
        print(key, value)
    print("-")
