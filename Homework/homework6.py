#Дано целое, положительное, ТРЁХЗНАЧНОЕ число. Например: 123, 867, 374.
# Необходимо его перевернуть. Например, если ввели число 123,
# то должно получиться на выходе ЧИСЛО 321. ВАЖНО!
# Работать только с числами. Строки, оператор IF и циклы использовать НЕЛЬЗЯ!
a = int(input('введите трехзначное число '))
m = ( a % 10 )* 100 + ((a // 10) * 10 - (a // 100) * 100) + a // 100
print(m)