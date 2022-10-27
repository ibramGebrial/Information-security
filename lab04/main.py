a=int(input("Enter a: "))
b=int(input("Enter b: "))

def evklid_nod(a,b):
  while a!=0 and b !=0:
    if a > b:
      a = a%b

    else:
      b = b%a
  return a+b


print("Алгоритм Евклида: ", evklid_nod(a,b))


def evklid_binary(a,b):
  g=1
  while a%2 == 0 and  b%2 == 0:
    a=a/2
    b=b/2
    g=2*g
  u=a
  v=b
  while u !=0:
    if u % 2 ==0:
      u= u/2
    if v % 2 ==0:
      v= v/2

    if u>=v:
      u=u-v

    else:
      v=v-u
  d= g*v
  return d

print("Бинарный алгоритм Евклида:  ",evklid_binary(a,b))

def evklid_extend(a,b):
  if a== 0:
    return(b,0,1)
  else:
    div,x,y= evklid_extend(b%a,a)
  return(div,y-(b//a)*x,x)

print("Расширенный алгоритм Евклида:  ",evklid_extend(a,b))

def evklid_binary_extend(a,b):
  g=1
  while a%2 == 0 and  b%2 == 0:
    a=a/2
    b=b/2
    g=2*g
  u=a
  v=b
  A=1
  B=0
  C=0
  D=1
  
  while u !=0:
    if u % 2 ==0:
      u= u/2
      if A%2==0 and B%2==0:
        A=A/2
        B=B/2
      else:
        A=(A+b)/2
        B=(B-a)/2
    if v % 2 ==0:
      v= v/2
      if C%2==0 and D%2==0:
        C=C/2
        D=D/2
      else:
        C=(C+b)/2
        D=(D-a)/2
    if u>=v:
      u=u-v
      A=A-C
      B=B-D
      
    else:
      v=v-u
      C=C-A
      D=D-B
  d= g*v
  x=C
  y=D
  return d,x,y

print("Расширенный бинарный алгоритм Евклида:  ",evklid_binary_extend(a,b))