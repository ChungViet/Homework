# По данному натуральному числу N найдите наибольшую целую степень двойки, не превосходящую N.
# Выведите показатель степени и саму степень.
# Операцию возведения в степень,
# а так же функцию возведения в степень использоваться НЕЛЬЗЯ!
chislo = 1
chislo_vstepen = 2
n = int(input('enter the number: '))
while chislo_vstepen <= n:
    chislo+=1
    chislo_vstepen *=2
print(chislo-1,chislo_vstepen//2, ' 2 **',chislo-1,'=',chislo_vstepen//2)

