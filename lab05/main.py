import random

def ferma(n):
  print("Теста Ферма")
  a = random.randint(2, n - 2)
  r= a ** (n - 1) % n
  if r==1:
    print("Число n, вероятно, простое")
  else:
    print("Число n составное")

n= int(input("enter n(Odd number):  "))
ferma(n)

# функция для бинарного эксп
def modul(base, exponent, mod):
    x = 1
    y = base
    while (exponent > 0):
        if (exponent % 2 == 1):
            x = (x * y) % mod

        y = (y * y) % mod
        exponent = exponent // 2

    return x % mod


def jacobian(a, n):
    if (a == 0):
        return 0 

    ans = 1
    if (a < 0):
        a = -a
        if (n % 4 == 3):
         
            ans = -ans

    if (a == 1):
        return ans  

    while (a):
        if (a < 0):

     
            a = -a
            if (n % 4 == 3):
                
                ans = -ans

        while (a % 2 == 0):
            a = a // 2
            if (n % 8 == 3 or n % 8 == 5):
                ans = -ans

       
        a, n = n, a

        if (a % 4 == 3 and n % 4 == 3):
            ans = -ans
        a = a % n

        if (a > n // 2):
            a = a - n

    if (n == 1):
        return ans

    return 0

def solovoy(n):
  print("Тест Соловэя-Штрассена")
  a = random.randrange(2,n-2)
  r= (a**(n-1/2))%n
  if (r != 1 and r!=n-1):
    print("Число n составное")
    
  s=jacobian(a,n)
  if modul(r,s,n) == 1:
    print( "Число n составное")
  else:
    print("Число n, вероятно, простое")
  
def toBinary(n):
    r = []
    while (n > 0):
        r.append(n % 2)
        n = n / 2
        return r

def MillerRabin(n, s = 10):  
  
    for j in range(1, s + 1):
            a = random.randint(1, n - 1)
            b = toBinary(n - 1)
            d = 1
            for i in range(len(b) - 1, -1, -1):
                x = d
                d = (d * d) % n
                if d == 1 and x != 1 and x != n - 1:
                    print("Число n составное") # Составное
                if b[i] == 1:
                    d = (d * a) % n
                    if d != 1:
                        print("Число n составное") # Составное
                    print("Число n, вероятно, простое")

solovoy(n)  
MillerRabin(n)