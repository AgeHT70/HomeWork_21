fish = [

    {"specie": "Белуга", "water": "fresh"},
    {"specie": "Карась", "water": "fresh"},
    {"specie": "Красноперка", "water": "fresh"},

    {"specie": "Морской окунь", "water": "sea"},
    {"specie": "Тунец", "water": "sea"},
    {"specie": "Скумбрия", "water": "sea"},

]
sea_water = [fishes['specie'] for fishes in fish if fishes['water'] == 'sea']
fresh_water = [fishes['specie'] for fishes in fish if fishes['water'] == 'fresh']
print("Морские: ", end='')
print(*sea_water, sep=', ')
print("Пресноводные: ", end='')
print(*fresh_water, sep=', ')
