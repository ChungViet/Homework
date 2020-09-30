# """
# функции
# chr()   из кода в символ
# ord()  из символа в код
# """
# # 0x26bd
# print(chr(0x26bd))
# print('\u26bd') # \u - 2 байта  \U - 4 байта (маленькая u и большая U соответственно)
# print(chr(9917))
#
# print(ord('⚽'))
# print(hex(ord('⚽')))
#
# wave = '~'
# boat = '\U0001f6a3'
# seagull = '\u033c'
# fish = '\U0001f41f'
# penguin = '\U0001f427'
# wale = '\U0001f40b'
# octopus = '\U0001f419'
#
# seagull_row = wave * 11 + seagull + wave * 14 + '\n'
# row = wave * 10 + boat + wave * 15 + '\n'
# fish_row = wave *4 + fish + wave * 21 + '\n'
# wale_row = wave * 10 + wale + wave * 15 + '\n'
# penguin_row = wave * 7 + penguin + wave * 15 + '\n'
# octopus_row = wave * 17 + octopus + wave * 8 + '\n'
# see = seagull_row + row + fish_row + wale_row + penguin_row + octopus_row
# print(see)
#
# print('\u2764')
# print('hello ' * 5)

# n1 = input('enter the num1: ')
# n2 = input('enter the num2: ')
# print(n1+n2)
# print(int(n2)+int(n2))


# индекс всегда с 0, инлекс последнего символ = кол-во всех символов минус 1
#  0  1  2  3  4
#  H  E  L  L  O
# -5 -4 -3 -2 -1
# s = 'Process finished with exit code 0'
# print(s[0])
# print(s[-1])
# s[0] = '7'  ERROOR
# print(s[35]) ERROR
# print(s[-55]) ERROR

# срез
# str[start: stop: step]

# print(s[8: 16: 1])
# print(s[8:])
# print(s[: 16])
# print(s[::2])
# print(s[8:432432])  # от 8го индекса до конца, 434342 не существует
# print(s[::-1])      # перевернуть
# print('12345'[::-1])  # перевернуть
#
# # функция len - кол-во символов строке
# for i in range(0,len(s),2):
#     print(s[i], end='')
# print()
# print(s[::2])


# for symbol in s:
#     print(symbol , end=' ')  # получем только символ
# print() # опустить курсор вниз, а то будет печатать в данной строке
#
# for i in range(len(s)):
#     print(s[i], end=' ')     # тут получаем еще индес символов
# print()


# len(str) получает получить кол-во символов в строке
# find(sub, start, end)    получает выполнить поиск
# sub обязательный параметр, остальное не обязательно
# rfind ( sub , start , end) искать с конца

# s = 'Process finished with exit code 0'
# print('total symbols in s=', len(s))
# idx = s.find('i')
# idx = s.find('i',idx +1)
# print('index for letter i =',idx)
# idx = s.find('i',idx +1)
# print('index for letter next i =',idx)
# idx = s.find('i',idx +1)
# print('index for letter next i =',idx)
# idx = s.find('i',idx +1)
# print('index for letter next i =',idx)
#
# print(s.find('finished'))

#функция replace (old , new, count)
# old - что заменяем , new  - на что заменяем,  count - сколько замен
# print(s.replace('i','I',2))
# print(s.replace('finished','finished'.upper()))
# .upper все с большой
# count(str)
# print('сколько букв i=',s.count('i'))
# print('how many finished we have =',s.count('finished'))

# capitalize() все в нижний регистр кроме первого символа
# s = 'prOceSs FiNisHed wiTh eXit code 0'
# print('1st lettr cap, else not = ',s.capitalize())

#upper
#lower
# print(s.upper())
# print(s.lower())

#title
# print(s.title())

#strip(str) удаляет в начале и в конце
# s = '3333                   Hello World!     33333'
# print("'" + s + "'")
# print("'" + s.strip('3').strip().upper() + "'")

s = 'prOceSs     FINisHed           wITh        eXit         cOde 0'
#split() делит
#join() объединяет
lst = s.split('i')
#lst = s.lower().split('i')
print(lst)
s = ' '.join(lst)
print(s)



