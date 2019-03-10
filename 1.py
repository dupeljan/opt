from math import sqrt
FUNCTION = lambda x: x*x + 3*x - 10
DELTA = 2e-1
EPS = 5e-1
GOLD_RAT_C = (1 + sqrt(5) ) / 2
A,B = (-2,8)

def dichotomy(a,b,f= FUNCTION,delta= DELTA , eps= EPS ):
	middle = ( a + b ) / 2
	if b - a < 2 * eps:
		return middle

	if f(middle - delta) < f(middle + delta):
		return dichotomy(a,middle - delta)
	else:
		return dichotomy(middle + delta,b)

def get_fib_num_more_than(val):
	a = 1
	b = 1
	i = 2
	while ( val > b):
		a,b = b,a+b
		i += 1
	return i

def fib(n):
    a = 1
    b = 1
    for __ in range(n):
        a, b = b, a + b
    return a

def Fibonacci(a,b,f= FUNCTION,delta= DELTA , eps= EPS):
	n = get_fib_num_more_than(abs((b - a) / ( 2 * eps)))
	y = a + (b-a)*fib(n-1)/fib(n)
	x = a + b - y
	fx = f(x)
	fy = f(y)
	for i in range (n-1):
		if fx < fy:
			b = y

			y = x
			fy = fx

			x = a + b - y
			fx = f(x)
		else:
			a = x

			x = y
			fx = fy

			y = a + b - x
			fy = f(y)
	y += delta
	if fx < f(y):
		return (a + y) / 2
	return (x + b) / 2


def golden_ratio(a,b,f= FUNCTION, eps= EPS):
	y = a + ( b - a ) / GOLD_RAT_C
	x = a + b - y
	fx = f(x)
	fy = f(y)
	while b - a > 2 * eps:

		if fx < fy:
			b = y

			y = x
			fy = fx

			x = a + b - y
			fx = f(x)
		else:
			a = x

			x = y
			fx = fy

			y = a + b - x
			fy = f(y)

	return (a + b) / 2



def main():
	print(dichotomy(A,B))
	print(Fibonacci(A,B))
	print(golden_ratio(A,B))	

if __name__ == '__main__':
 	main() 