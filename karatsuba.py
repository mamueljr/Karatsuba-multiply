'''
ADALBERTO EMMANUEL ROJAS PEREA
TAREA 1
ANALISIS Y DISEÑO DE ALGORITMOS
ASESOR: DR. JESUS ROBERTO LOPEZ SANTILLAN
'''

# Creamos la funcion para el algoritmo de karatsuba


def alg_karatsuba(x, y):
    # verifica el tamaño de las variables, si este es de 1 regresa la multiplicacion
    if len(str(x)) == 1 or len(str(y)) == 1:
        return x*y
    else:
        n = max(len(str(x)), len(str(y)))
        nby2 = int(n / 2)
        # convertir a entero la variable a
        a = int(x / 10**(nby2))
        b = x % 10**(nby2)
        c = int(y / 10**(nby2))
        d = y % 10**(nby2)
        ac = alg_karatsuba(a, c)
        bd = alg_karatsuba(b, d)
        ad_plus_bc = alg_karatsuba(a+b, c+d) - ac - bd
        prod = ac * 10**(2*nby2) + (ad_plus_bc * 10**nby2) + bd
        return prod


n1 = int(input("teclea el primer valor:"))
n2 = int(input("teclea el segundo valor:"))
print(int(alg_karatsuba(n1, n2)))
