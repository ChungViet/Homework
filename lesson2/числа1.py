#вещественный тип
print(4.7)
print(0.1 + 0.1 + 0.1)
a = 3 ** 100 #возвышение в степень
print(a + 0.1)
# 2.23 * 10 ^ -308 = 2.23e-308   min чилсо
# 1.79 * 10 ^ 308 = 1.79e308     min число
#inf    -inf                     бесконечность
#nan            ??
# комплексные числ
print(2+3j , type(2+3j))

#string - строки
r = ' hi buddy , today is good day '
s1 = 'hello '
s2 = 'world!'
s3 = s1 + s2
print(s3)
s4 = s1 * 5
print(s4)
# escape символы
"""
\n   new line
\r
\t   tab
\b   backspace
\'   '
\"   "
\\   \
\a   alarm - ascii bell
"""
t1 = ' Hello \'world\'!'
t2 = "Hello \"world\"!"
t3 = '\n'
print(t1,t3,t2)

# текст  - многострочные набор символов
u = """
        fdffdff
        fdfsd
        fdsf
    """
print(u)
u1 = """
fds
^&*%$^*&(
     """
print(u1)

