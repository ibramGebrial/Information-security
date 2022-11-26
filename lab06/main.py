from math import gcd

def f(x,n):
  return (x*x +5)%n

def pollarda (n,a,b):
  a=f(a,n)%n
  b=f(f(b,n),n)%n
  d=gcd(a-b,n)
  if 1<d<n:
    p=d
    print(p," является нетривиальным делителем числа: ",n)
    exit()
  if d==n:
    print("Делитель не найдён")
  if d==1:
    pollarda(n,a,b)

c=1
a=c
b=c

pollarda(1359331,a,b)