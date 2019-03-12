from math import sqrt
FUNCTION = lambda x: x*x - 2*x + 5
EPS = 1e-5#5e-1
DELTA =  EPS / 2#2e-1
GOLD_RAT_C = (1 + sqrt(5) ) / 2
A,B = (-2,8)


def dichotomy(a,b,f= FUNCTION,delta= DELTA , eps= EPS, i = 0 ):
	middle = ( a + b ) / 2
	if b - a < 2 * eps:
		return (middle,i)
	if f(middle - delta) < f(middle + delta):
		return dichotomy(a,middle - delta, i= i+1)
	else:
		return dichotomy(middle + delta,b, i= i+1)


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
		return ((a + y) / 2,n)
	return ((x + b) / 2 , n)


def golden_ratio(a,b,f= FUNCTION, eps= EPS):
	y = a + ( b - a ) / GOLD_RAT_C
	x = a + b - y
	fx = f(x)
	fy = f(y)
	i = 0
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
		i += 1

	return ((a + b) / 2 , i)



def main():
	print("dichotomy ",dichotomy(A,B))
	print("Fibonacci ",Fibonacci(A,B))
	print("golden_ratio ",golden_ratio(A,B))	

if __name__ == '__main__':
 	main() 