# -*- coding: utf-8 -*-

from config import letters, number_of_lines

file_output = open('output.txt', 'w')

strkeys = ''.join(letters.keys())

print('Please use only characters of " {} ". Other characters will not be displayed. Be patient'.format(strkeys))

word = input('Please input word: ')
print()                                         # Переход на новую строку
word = word.lower()

for string in range(number_of_lines):            # Вывожу построчно
    for char in word:
        if char in letters.keys():              # Проверка на допустимые символы
            for char_for_print in letters[char][string]:
                if char_for_print == '':
                    file_output.write(' ')
                else:
                    file_output.write(char.upper())
            file_output.write(' ')
        else:
            continue
    file_output.write('\n')
