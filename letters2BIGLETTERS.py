# -*- coding: utf-8 -*-

from config import letters

file_output = open('output.txt', 'w')
print('Use pls only characters of English alphabet. Other characters will not be displayed. Be patient')

word = input('Please input word: ')
print()
word = word.lower()

for string in range(len(letters['a'])):
    for char in word:
        if char in ('qwertyuiopasdfghjklzxcvbnm ,.-+'):             # Проверка на допустимые символы
            for char_for_print in letters[char][string]:
                if char_for_print == '':
                    file_output.write(' ')
                else:
                    file_output.write(char.upper())
            file_output.write(' ')
        else:
            continue
    file_output.write('\n')

