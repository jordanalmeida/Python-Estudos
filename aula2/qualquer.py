def teste1 (a,b):
    print('a =',a)
    print('b =',b)
    return a,b
def teste2 (a,b,c = 'oi'):
    print('a =',a)
    print('b =',b)
    print('c =',c)
    return a,b

def soma(a , b):
    return a+b

def soma2(*a):
    resultado = 0
    for i in a:
        # resultado = resultado + i 
        resultado += i
    return resultado