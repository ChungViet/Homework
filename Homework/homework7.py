# По данному целому числу N распечатайте все квадраты натуральных чисел, не превосходящие N, в порядке возрастания.
n = int(input('enter the number: '))
for x in range(1,n):
    x = x ** 2
    if x >= n:
        break
    print(x, end=' ')

# n = int(input('enter the number: '))
# x = 1
# while x ** 2 <= n:
#     print(x**2,end=' ')
#     x+=1