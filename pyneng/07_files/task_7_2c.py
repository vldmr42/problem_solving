# -*- coding: utf-8 -*-
'''
Задание 7.2c

Переделать скрипт из задания 7.2b:
* передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

Внутри, скрипт должен отфильтровать те строки, в исходном файле конфигурации,
в которых содержатся слова из списка ignore.
И записать остальные строки в итоговый файл.

Проверить работу скрипта на примере файла config_sw1.txt.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

ignore = ['duplex', 'alias', 'Current configuration']

import sys
txt = ''
if __name__ == '__main__':
    filename_input = sys.argv[1]
    filename_output = sys.argv[2]
    with open(filename_input) as f:
        for line in f:
            # if line.startswith('!'):
            #     pass
            if any([item in ignore for item in line.split()]):
                continue
            else:
                txt += line
    with open(filename_output, 'w') as targ:
        targ.write(txt)