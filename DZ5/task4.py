# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.


def main(txt):
    encond = ''
    prev_char = ''
    count = 1
    if not txt:
        return ''

    for char in txt:
        if char != prev_char:
            if prev_char:
                encond += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    else:
        encond += str(count) + prev_char
        return encond


with open('DZ5\encoding.txt', 'r') as my_file:
    my_txt = my_file.readline()
    txt_compress = my_txt.split()

with open('coding.txt', 'w', encoding='UTF-8') as my_file:
    my_file.write(f'{main(my_txt)}')

