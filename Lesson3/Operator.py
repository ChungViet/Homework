#арифметические операторы
"""
    +   сложение                A + B        'Hello' + 'World' = 'Hello World'
    -   вычитание               A - B
    *   умножение               A * B        'Hello' * 3 = 'Hello Hello Hello;
    /   деление                 A / B         10/3 = 3.3333
    //  целочисленное деление   A // B        10//3=3.0
    %   остаток от деления      A % B         10%3 = 1

    +   унарный плюс            +A
    -   унарный минус           -B

    ** возвышение в степень     A ** B        A ** B ** C
"""

#операторы сравнения
"""
    >   больше                  A > B
    <   меньше                  A < B
    >=  больше либо равно       A >= B
    <=  меньше либо равно       A <= B    
    !=  не равно                A != B    
    ==  строгое равенство       A == B

"""
#лоигческие операторы
"""
    not     логическое отрицание(не)  not A    унарный
    and     логическое "и"            A and B  бинарные
    or      логическое "или"          A or B   бинарный  

    А      В          A and B      A or B      not A
    True   True       True         True        False 
    True   False      False        True        False 
    False  True       False        True        True  
    False  False      False        False       True     
"""
# битовые операции
"""
    &       битовое И                   A & B
    |       битовое Или                 A | B
    ^       битовое исключающее ИЛИ     A ^ B
    ~       битовое не                  ~ A

    A       B           A ^ B
    True    True        False
    True    False       True
    False   True        True                
    False   False       False
"""
# операторы сдвига
"""
    >>      битовый сдвиг вправо        A >> B  деление на 2
    <<      битовый сдвиг влево         A << B  умножение на 2
"""

a=3
print(a<<2)

# оперчаторы присваивания
"""
    =       присваивание        A = B
    
    A = A + 3                   A += 3

    +           +=
    -           -=
    *           *=
    /           /=
    //          //=
    %           %=
    **          **=
    >>          >>=
    <<          <<=
    &           &=
    |           |=
    ^           ^=    
"""

a = 6
b = 5
c = 7

# a and b or not C  procedence python 6.17

