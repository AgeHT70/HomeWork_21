# Формат вывода:
# Лещ: Единственный представитель рода лещей из семейства карповых.
# Пресноводная рыба
# Промысловый размер: 29 см

species = [
    {"specie": "Лещ", "len": "29", "sea": False,
     "desc": "Единственный представитель рода лещей из семейства карповых."},
    {"specie": "Щука", "len": "45", "sea": False,
     "desc": "Распространена в пресных водах Евразии и Северной Америки. Живет обычно в прибрежной зоне,"
             " в водных зарослях, в непроточных или слабопроточных водах. "},
    {"specie": "Треска", "len": "33", "sea": True,
     "desc": "Треска встречается от прибрежной полосы до континентального шельфа, но в открытом море над большими"
             " глубинами редко. Ее жизненный цикл привязан к морским течениям Северной Атлантики."},
    {"specie": "Камбала", "len": "25", "sea": True,
     "desc": " Тело плоское, сильно сжато с боков, глаза расположены не по бокам головы, а смещены на одну ее сторону."
             " Плавательного пузыря нет. "},
    {"specie": "Лосось", "len": "50", "sea": False,
     "desc": "Проходная форма обитает в северной части Атлантического океана. Заходит на нерест в реки от Португалии"
             " и Испании до Баренцева моря."},
]

s = input()
in_species = False

for i in range(len(species)):
    if species[i]['specie'].lower() == s.lower():
        in_species = True
        num_of_dict = i

if in_species:
    print(
        f"{species[num_of_dict]['specie']}: {species[num_of_dict]['desc']}\n{'Морская рыба' if species[num_of_dict]['sea'] else 'Пресноводная рыба'}\n"
        f"Промысловый размер: {species[num_of_dict]['len']} см")
else:
    print('Информация не найдена')