# рограмма запрашивает ввод, с клавиатуры, целые числа, пока не будет введён 0.
# Как только будет введён 0 (ноль), программа должна посчитать и вывести на экран:
#
#
#
# количество введённых чисел (завершающий 0 не считается)
# их сумму
# среднее арифметическое всех введённых чисел(не считая завершающего числа 0)
# определить максимальное и минимальное значение
# определить количество чётных и не чётных элементов в последовательности
suma=1
kolvo_chisel=0
max_chislo=0
min_chislo=0
chet_chisla=-1
nechet_chisla=1
n = int(input('enter the number: '))
while n != 0:
    n = int(input('enter the number: '))
    suma += n
    kolvo_chisel += 1
    if n > max_chislo:
        max_chislo = n
    if n < min_chislo:
        min_chislo = n
    if not n % 2:
        chet_chisla += 1
    if n % 2 != 0:
        nechet_chisla += 1

print('количество введенных числе=',kolvo_chisel)
print('сумма всех чисел =',suma)
print('среднее арифметическое=', suma / kolvo_chisel)
print('максимальное число =',max_chislo)
print('минимальное число =',min_chislo)
print('количество четных чисел =',chet_chisla)
print('количество нечетных чисел =',nechet_chisla)
