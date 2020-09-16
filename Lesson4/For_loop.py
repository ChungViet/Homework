#for
"""
for <variable переменная> in <iterable_ibj объек , который мы можем перчислять>:
    operator_1
    operator_2
operator_N
for _ in <iterable_ibj>:
    operator_1
    operator_2
operator_N
"""
# i = 1
# for color in 'red', 'orange', 'yellow', 'green', 'cyan', 'blue', 'violet': #коллекция, набор некоторых значений которые будет перебирать цикл for
#     if color == 'yellow':
#         continue
#     print('#', i, 'color in rainbow is ', color, sep='')     #sep='' убрать пробелл принта или добавить что-нибудь еще
#     i += 1

# функция range(start, stop, step)
#10 - 20
#range(10,20, 2)

#stop only
#range(20)
#start = 0 , step = 1
# r = range(10,100)
# print(r)
# for i in r:
#     print(i, end=' ')
# for i in range(10,100):
#     print(i, end=' ')       #end='' символ в конце можно \n, \t
# for i in range(10,100, 2):
#     print(i, end=' ')
# for i in range(11,50,2):
#     print(i, end=' ')
# print()
# for i in range(50):
#     if i == 35:
#         break
#     print(i,end=' ')
suma=0
begin = int(input('start number: '))
end = int(input('end number: '))
for num in range(begin,end+1):
    if not num % 2:
        suma+=num

print('suma: ',suma)





