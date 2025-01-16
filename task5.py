# Откройте текстовый файл task5.txt для чтения.
# Найдите самое длинное слово в тексте. Если таких слов несколько, выберите первое из них.
# Запишите это слово и его длину в новый файл в формате:
# Самое длинное слово: слово
# Его длина: длина
#
# Выведите это слово и длину в консоль.
mx = 0
s = ''
with open('task5.txt','r',encoding='utf8') as f:
    l = f.read()
    for char in '.,!?;:"()[]{}':
        l = l.replace(char, '')
    l = l.split()
    for i in range(len(l)):
        if len(l[i]) > mx:
            mx = len(l[i])
            s = l[i]

with open('update_task5.txt','w',encoding='utf8') as f:
    f.write(f'Самое длинное слово:{s}\n')
    f.write(f'Его длина:{mx}')
with open('update_task5.txt','r',encoding='utf8') as f:
    result = f.read()
print(result)