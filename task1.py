# Откройте текстовый файл для чтения task1.txt.
# Подсчитайте:
# Общее количество строк в файле.
# Общее количество слов во всем тексте файла.
# Общее количество символов (включая пробелы).
# Выведите полученную статистику на экран.
file =open('task1.txt', encoding ='utf8')
lines = 0
simvols = 0
for line in file:
    lines += 1
    simvols += len(line)
file.close()
file = open('task1.txt',encoding='utf8')
a= file.read()
a = a.split("—")
word = " ".join(a)
words = len(word.split())
print(' Общее количество строк в файле:',lines)
print('Общее количество слов во всем тексте файла.',words)
print('Общее количество символов',simvols)
