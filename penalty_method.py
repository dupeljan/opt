from one import Fletcher_Reeves
from math import *
EPS = 1e-5
DELTA = EPS / 2
EXAMPLE = 2

if EXAMPLE == 0 :
	FUNCTION = lambda x1, x2: x1**2 + 4*x2**2-x1*x2+x1
	G_ACTIVE = [lambda x1,x2: 2*x1+x2-1]
	G_PASSIVE = []
elif EXAMPLE == 1:
	FUNCTION = lambda x1, x2: x1**2 + 5*x2**2-x1*x2+x1
	G_ACTIVE = [lambda x1,x2: x1+x2-1]
	G_PASSIVE = []
elif EXAMPLE == 2:
	FUNCTION = lambda x1, x2: 3*x1**2 + 4*x2**2-x1*x2+x1
	G_ACTIVE = [lambda x1,x2: 2*x1+x2-1]
	G_PASSIVE = []


X0 = (1,1)  
R0 = 10

C = 2

def cut(x):
	if x < 0:
		return 0
	return x

def penalty_method(x0= X0,r0=R0,f= FUNCTION,g_active= G_ACTIVE,g_passive= G_PASSIVE,c=C,eps= EPS,k=0):
	p = lambda x1,x2,r: ((r**k)/2)*(sum(g(x1,x2)**2 for g in g_active) +
		sum(cut(g(x1,x2))**2 for g in g_passive) ) 
	F = lambda x1,x2,r: f(x1,x2) +  p(x1,x2,r)

	solver = Fletcher_Reeves(f= lambda x1,x2:F(x1,x2,r0))
	x_star = solver.solve(x0)[0]

	print("p",p(*x_star,r0))
	print("g_active",g_active[0](*x_star))
	print()
	if abs(p(*x_star,r0)) <= EPS:
		return x_star,k
	return penalty_method(x0= x_star,r0=c*r0,k=k+1)

def main():
	result = penalty_method()
	print(result)
	print("f",FUNCTION(*result[0]))

if __name__ == '__main__':
	main()