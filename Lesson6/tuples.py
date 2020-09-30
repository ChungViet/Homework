t = ()
print(t,type(t))
t = tuple()
print(t,type(t))
t = tuple('Hello World!')
print(t,type(t))
t = tuple([3,6,7,8,9])
print(t,type(t))

t= (4,5, 'rere', True, [4,6,7])
print(t,type(t))
print(t[4],type(t[-1]))
t[4][1]=0
print(t)

t = 40,
print(t,type(t))

a, b, c = (1, 3, 5)
print(a, b, c)
x = 5, 6, 78,
print(x,type(x))


# min, max, sum
print(min(x))
print(max(x))
print(sum(x))