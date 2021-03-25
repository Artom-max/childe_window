# Прочитаем
# Демонстрирует чтение из текстового файла
# encoding='utf8' - этот параметр нужен для чтения кирилицы
# 'r' -Чтение из текстового файла. Если файл не существует, Python сообщит об ошибке
# 'w' - запись в текстовый файл. Если файл существует, его содержимое будет заменено.
# Если файл не существует, он будет создан
# 'a' - Доэапись в текстовый файл. Если файл существует, новые данные будут дописаны
# в конец. Если файл не существует, он будет создан
# 'r+' - Чтение и запись в текстовый файл. Если файл не существует, Python сообщит об
# ошибке
# 'w+' - Запись и чтение из текстового файла. Если файл существует, его содержимое будет
# заменено. Если файл не существует, он будет создан
# 'a+' - Доэапись и чтение из текстового файла. Если файл существует, новые данные будут
# дописаны в конец. Если файл не существует, он будет создан


print("Открываю и закрываю файл:")
text_file = open('text_file', 'r', encoding='utf8')
text_file.close()

print('\nчитаю файл посимвольно:')
text_file = open('text_file', 'r', encoding='utf8')
print(text_file.read(1))  # read
print(text_file.read(5))  # указывается число симфолов которые буду прочтены
text_file.close()  # метод read запоминает на каком символе вы остановились

print('\nчитаю целиком:')
text_file = open('text_file', 'r', encoding='utf8')
whole_thing = text_file.read()
print(whole_thing)
text_file.close()

print('\nчитаю одну строку посимвольно:')
text_file = open('text_file', 'r', encoding='utf8')
print(text_file.readline(1))
print(text_file.readline(5))
text_file.close()

print('\nчитаю строку целиком:')
text_file = open('text_file', 'r', encoding='utf8')
print(text_file.readline())
print(text_file.readline())
print(text_file.readline())
text_file.close()

print('\nчитаю весь файл в список:')
text_file = open('text_file', 'r', encoding='utf8')
lines = text_file.readlines()  # преобразует в список
print(lines)
for line in lines:
    print(line)
text_file.close()

print("\nчитаю весь файл посточно")
text_file = open('text_file', 'r', encoding='utf8')
for line in text_file:
    print(line)
text_file.close()

print('\nСоздаем новый текстовый файл методом write():')
text_file = open('Text_file_write', 'w', encoding='utf8')
text_file.write('строка 1\n')
text_file.write('строка 2\n')
text_file.write('этой строке достается номер 3\n')
text_file.close()

print('\nСоздаем новый текстовый файл методом writelines():')
text_file = open('Text_file_writelines', 'w', encoding='utf8')
lines_2 = ['Строка 1\n'
           'Это строка 2\n'
           'этой строке достался номер 3\n']
text_file.writelines(lines_2)
text_file.close()

input('\nНжмите Enter для выхода')
# описание методов:
# close() - закрывает файл. закрытый файл недОСJ)'пен для чтения и записи до тех
# пор, пока не будет открыт снова
# read([число]) - Читает указанное количество символов из файла и возвращает их в виде строки. Если число не указано,
# метод возвратит все символы, начиная с текущей позиции и до конца файла
# readline([число]) - кущей позиции и до конца файла
# readline([чиcлo]) Читает указанное количество символов из текущей сrроки файла и воэвращает их в виде строки. Если
# число не указано, метод возвратит все символы,
# начиная с текущей позиции и до конца строки
# readlines([число]) - Читает все строки файла и возвращает список, элементами которого они все
# являются
# write(строка) - записывает строку в файл
# writelines(список строк) -записывает список строк текста в файл
