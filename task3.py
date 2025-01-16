# Откройте текстовый файл task3.txt для чтения.
# Извлеките все уникальные слова из файла (слова разделяются пробелами и знаками пунктуации).
# Подсчитайте, сколько раз каждое уникальное слово встречается в тексте.
# Запишите результаты в новый файл в формате:
# слово1: количество
# слово2: количество
#
# Убедитесь, что слова записаны в алфавитном порядке.
with open('task3.txt','r', encoding='utf8') as f:
    l=f.read()
for char in '.,!?;:"()[]{}':
    l = l.replace(char, '')
l = l.split()
word_count = {}
for word in l:
    if word in word_count:
        word_count[word] +=1
    else:
        word_count[word]=1
with open("task3_new.txt",'w',encoding = 'utf8') as f:
    for word in sorted(word_count):
        f.write(f'{word}:{word_count[word]}\n')
