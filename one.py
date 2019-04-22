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

class Method_second:
	def __init__(self,f= FUNCTION,eps= EPS,m= M):
		self.f = f
		self.eps = eps
		self.m = m

	def solve(self,x= X0, i= 0, is_valid = False):
		grad = grad_diff(self.f,*x)
		print("grad",grad)
		if norm ( grad ) < self.eps[0] or i > self.m:
			return x, i

		
		t = self.get_step( x= x, grad= grad )#dichotomy(0,1,f= fi,delta= eps[0]/2,eps= eps[0])[0]
		print ("t ",t)
		
		
		x_new = np.array(x) - t
		print("new x", x_new)
		
		valid = False
		if norm(x_new - x) < self.eps[1] and abs(self.f(*x_new)- self.f(*x)) < self.eps[1]:
			if is_valid:
				return x_new, i
			else:
				valid = True
		return self.solve(x= x_new,i= i+1,is_valid= valid)

	def get_step(self,**kwarg):
		print("it's virtual method")
		return 1

class Steepest_descent(Method_second):
	def get_step(self,**kwarg):
		fi = lambda t: self.f(*[xi-t*grad_i for (xi,grad_i) in zip(kwarg["x"],kwarg["grad"]) ])
		t = dichotomy(0,1,f= fi,delta= self.eps[0]/2,eps= self.eps[0])[0] 
		return np.dot(t,kwarg["grad"])

class Newton(Method_second):
	def get_step(self,**kwarg):
		return np.dot(Hessian, kwarg["grad"])

#Error here
class Newton_Raphson(Method_second):
	def get_step(self,**kwarg):
		d = -1 * np.dot(Hessian, kwarg["grad"])
		fi = lambda t: self.f(*[xi-t*d_i for (xi,d_i) in zip(kwarg["x"],d) ])
		t = dichotomy(0,1,f= fi,delta= self.eps[0]/2,eps= self.eps[0])[0] 
		return  -1 * t * d	
		

# Метод наискорейшего спуска
'''
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
'''

def main():
	m = Newton_Raphson()
	print(m.solve())
if __name__ == '__main__':
	main()