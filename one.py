from zero import dichotomy
from math import *
import numpy as np

FUNCTION = lambda x1, x2: x1*x1 + 4 * x2*x2 - x1*x2 + x1
Hessian = np.array([[8/15,1/15],[1/15, 2/15]])  
X0 = (3,1)   
EPS = (1e-3,1e-3)
M = 100 # iterations limit

def grad_diff(f,x,y,h=1e-5):
	return ( f( x + h, y ) - f( x - h, y ) ) / ( 2 * h ), ( f(x, y + h) - f(x, y - h) ) / ( 2 * h )

def norm(x):
	return sqrt(sum( [ y*y for y in x] ))

#class method_second:
#	def solve(self,f= FUNCTION,x= X0,eps= EPS,m= M, i= 0, is_valid = False):

# Метод наискорейшего спуска
def steepest_descent(f= FUNCTION,x= X0,eps= EPS,m= M, i= 0, is_valid = False):
	grad = grad_diff(f,*x)
	print("grad",grad)
	if norm ( grad ) < eps[0] or i > M:
		return x, i
	
	fi = lambda t: f(*[xi-t*grad_i for (xi,grad_i) in zip(x,grad) ])
	t = dichotomy(0,1,f= fi,delta= eps[0]/2,eps= eps[0])[0]
	print ("t ",t)
	x = np.array(x)
	x_new = x - t * np.array(grad)
	print("new x", x_new)
	valid = False
	if norm(x_new - x) <eps[1] and abs(f(*x_new)-f(*x)) < eps[1]:
		if is_valid:
			return x_new, i
		else:
			valid = True
	return steepest_descent(f=f,x= x_new,eps= eps,m= m,i= i+1,is_valid= valid)


def main():
	print(steepest_descent())
if __name__ == '__main__':
	main()