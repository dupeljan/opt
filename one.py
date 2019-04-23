from zero import dichotomy
from math import *
import numpy as np

FUNCTION = lambda x1, x2: x1*x1 + 4 * x2*x2 - x1*x2 + x1
Hessian = np.array([[8/15,1/15],[1/15, 2/15]])  
X0 = (3,1)   
EPS = (1e-3,1e-3)
EPS_ZERO = 1e-10
M = 100 # iterations limit

def grad_diff(f,x,y,h=1e-5):
	return ( f( x + h, y ) - f( x - h, y ) ) / ( 2 * h ), ( f(x, y + h) - f(x, y - h) ) / ( 2 * h )

def norm(x):
	return sqrt(sum( [ y*y for y in x] ))

class Method_second:
	def __init__(self,f= FUNCTION,eps= EPS, eps_zero= EPS_ZERO ,m= M):
		self.f = f
		self.eps = eps
		self.m = m
		self.eps_zero = eps_zero

	def solve(self,x= X0,x_pred= 0,d_pred=np.array([0,0]), i= 0, is_valid = False):
		print("-----------iteraton----------",i)
		grad = grad_diff(self.f,*x)
		print("grad",grad)
		if norm ( grad ) < self.eps[0] or i > self.m:
			return x, i

		
		t = self.get_step( x= x, grad= grad, x_pred= x_pred, d_pred= d_pred, i= i  )#dichotomy(0,1,f= fi,delta= eps[0]/2,eps= eps[0])[0]
		print ("t ",t)
		
		
		x_new = np.array(x) - t
		print("new x", x_new)
		
		valid = False
		if norm(x_new - x) < self.eps[1] and abs(self.f(*x_new)- self.f(*x)) < self.eps[1]:
			if is_valid:
				return x_new, i
			else:
				valid = True
				
		print("d_pred ",d_pred)
		return self.solve(x= x_new,x_pred= x, i= i+1,is_valid= valid, d_pred= self.get_d(grad= grad, x_pred= x_pred, d_pred= d_pred, i= i ))

	def get_step(self,**kwarg):
		print("it's virtual method")
		return 1

	def get_d(self,**kwarg):
		#print("it's virtual method")
		return 0		

class Steepest_descent(Method_second):
	def get_step(self,**kwarg):
		fi = lambda t: self.f(*[xi-t*grad_i for (xi,grad_i) in zip(kwarg["x"],kwarg["grad"]) ])
		t = dichotomy(0,1,f= fi,delta= self.eps[0]/2,eps= self.eps[0])[0] 
		return np.dot(t,kwarg["grad"])

class Newton(Method_second):
	def get_step(self,**kwarg):
		return np.dot(Hessian, kwarg["grad"])

class Newton_Raphson(Method_second):
	def get_step(self,**kwarg):
		d = np.dot(Hessian, kwarg["grad"])
		fi = lambda t: self.f(*[xi-t*d_i for (xi,d_i) in zip(kwarg["x"],d) ])
		t = dichotomy(0,1,f= fi,delta= self.eps[0]/2,eps= self.eps[0])[0] 
		return  t * d	

class Fletcher_Reeves(Method_second):
	def get_step(self,**kwarg):
		d = self.get_d(grad= kwarg["grad"], x_pred= kwarg["x_pred"], d_pred= kwarg["d_pred"], i= kwarg["i"])
		print("de",d)
		fi = lambda t: self.f(*[xi + t * d_i for (xi,d_i) in zip(kwarg["x"],d) ])
		t = dichotomy(0,1,f= fi,delta= self.eps[0]/2, eps= self.eps[0])[0] 
		return - np.dot(t,d)

	def get_d(self,**kwarg):
		if kwarg['i'] :
			betta = ( norm ( kwarg["grad"] ) ** 2 ) / ( norm (  grad_diff( self.f,*kwarg["x_pred"] ) ) ** 2 ) 
		else:
			betta = 0
		
		return - np.array(kwarg["grad"]) + np.dot( betta,kwarg["d_pred"] )

def main():
	methods = {"Steepest_descent" : Steepest_descent(), "Newton" : Newton(), "Newton_Raphson" : Newton_Raphson(), "Fletcher_Reeves" : Fletcher_Reeves()}
	for key,method in methods.items():
		print('------------------')
		print(key,method.solve())

if __name__ == '__main__':
	main()