/*check weather given number is perfect square or not*/
from math import sqrt
n=int(input("enter a number"))
def solve(n):
	sq_root=int(sqrt(n))
	return(sq_root*sq_root)==n
print(solve(n))
	

