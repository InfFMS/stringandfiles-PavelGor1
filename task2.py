# Откройте текстовый файл task2.txt для чтения.
# Считайте его содержимое в строку.
# Найдите и замените все вхождения слова "Python" на слово "Питон" (регистр учитывать).
# Запишите обновленный текст в новый файл с другим именем.
# Выведите на экран сообщение о количестве произведённых замен
with open('task2.txt','r',encoding='utf8') as file:
    content=file.read()
s = content.count('Python')
new_content = content.replace('Python','Питон')
with open('update_task2.txt','w',encoding='utf8') as file:
    file.write(new_content)
print(s)