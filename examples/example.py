import shutil

import columnify


given: list[str] = [
    "Canidae",
    "Felidae",
    "Cat",
    "Cattle",
    "Dog",
    "Donkey",
    "Goat",
    "Guinea pig",
    "Horse",
    "Pig",
    "Rabbit",
    "Fancy rat varieties",
    "laboratory rat strains",
]

print('Default:')
print(columnify.columnify(given, shutil.get_terminal_size().columns))

print('--')

print('Horizon first:')
print(columnify.columnify(given, shutil.get_terminal_size().columns, horizon_first=True))

print('--')

print('center():')
print(columnify.columnify(given, shutil.get_terminal_size().columns, align_func_name='center'))

print('--')

print('rjust():')
print(columnify.columnify(given, shutil.get_terminal_size().columns, align_func_name='rjust'))

print('--')

print('Custom delimiter ( | ):')
print(columnify.columnify(given, shutil.get_terminal_size().columns, delimiter=' | '))

print('--')

print('Indent (4 spaces):')
print(columnify.columnify(given, shutil.get_terminal_size().columns, indent=4))
