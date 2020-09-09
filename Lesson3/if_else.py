"""
if <condition>:  - двоеточие обязательно
    operator_1
    operator_2

operator_3 - не будет включен в группу выше, нужен отступ от "if"
"""
a = 45
if a > 0:
    if a != 10:
        print('A is positive')
print('end')

"""
if <condition>:
    operators_N
else:
    operators_M
"""

b = 6
if b >= 0:
    print('number is positive')
else:
    print('number is negative')

c = 0
if c > 0:
    print('number is positive')
else:
    if c < 0:
        print('number is negative')
    else:
        print('number is zero')

a = -3
if a > 0:
    print('number is positive')
elif a < 0:
    print('number is negative')
else:
    print('number is zero')