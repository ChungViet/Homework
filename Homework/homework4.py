#n школьников делят k яблок поровну, неделящийся остаток остается в корзинке.
# Сколько яблок достанется каждому школьнику?
# Сколько яблок останется в корзинке?
# Программа получает на вход числа n и k и должна вывести искомое количество яблок (два числа).
shkolnikov = int(input('skolko shkolnikov? '))
yablok = int(input('Skolko yablok? '))
n = yablok // shkolnikov
k = yablok % shkolnikov
print(n , 'kazhdomu shkolniku')
print(k , 'v korzinu')