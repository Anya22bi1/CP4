from random import randint

N = int(input("Введите размерность массива А: "))
n = int(input("Введите размерность массива В: "))
A = [0] * N
B = [0] * n
for i in range(N):
    A[i] = randint(0, 10)
for l in range(n):
    B[l] = randint(0, 10)
print(A, B)
C = set(A) & set(B)  #Создаём сет общих элементов
print(set(A), set(B), C)
