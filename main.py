import time
import numpy as np
from sort import bubble_sort
from sort import insertion_sort
from sort import shell_sort
from sort import merge_sort
from sort import quick_sort

a = 1
b = 5000
r = 2000
k = np.random.randint(a, b, (r))
cop = k.copy()
# buble = copy
# insertion = copy
#print('lista da lista original', len(k))
#print('lista', k.tolist())

print('          Início do Programa:')
print('-'*40)
print('Chaves originais:')
print (k)

print('-'*40)
print('Executando o Bubble Sort, aguarde ...')
print (k)
bubble = k
p1 = time.time()
bubble_sort(bubble)
u1 = time.time()
t = bubble
#print('lista ordenada Bubble sort', bubble.tolist())
k = cop.copy()

print('Executando o Insertion Sort, aguarde ...')
print (k)
insertion = k
p2 = time.time()
insertion_sort(insertion)
u2 = time.time()
v = insertion
#print('lista ordenada Insertion sort', insertion.tolist())
k = cop.copy()


print('Executando o Shell Sort, aguarde ...')
print (k)
shell = k
p3 = time.time()
shell_sort(shell)
u3 = time.time()
w = shell
#print('lista ordenada Shell sort', shell.tolist())
k = cop.copy()


print('Executando o Merge Sort, aguarde ...')
print (k)
marge = k
p4 = time.time()
merge_sort(marge)
u4 = time.time()
y = marge
#print('lista ordenada Merge sort', marge.tolist())
k = cop.copy()


print('Executando o Quick Sort, aguarde ...')
print (k)
quick = k
p5 = time.time()
s = np.array(quick_sort(quick.tolist()))
u5 = time.time()
z = s
#print('lista ordenada Quick sort', s.tolist())
k = cop.copy()

print()
print('          Chaves ordenadas:')
print('-'*40)
print('Chaves organizadas pelo Bubble Sort:')
print(t)
print('Chaves organizadas pelo Insertion Sort:')
print(v)
print('Chaves organizadas pelo shell_sort Sort:')
print(w)
print('Chaves organizadas pelo Merge Sort:')
print(y)
print('Chaves organizadas pelo Quick Sort:')
print(z)

print()
print('          Tempo de execução:')
print('-'*40)
print('Bubble Sort com {:.3f} segundos'.format(u1 - p1))
print('Insertion Sort com {:.3f} segundos'.format(u2 - p2))
print('Shell Sort com {:.3f} segundos'.format(u3 - p3))
print('Merge Sort com {:.3f} segundos'.format(u4 - p4))
print('Quick Sort com {:.3f} segundos'.format(u5 - p5))

print()
print('             fim do Programa:')
