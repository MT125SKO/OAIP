#1
import numpy as np

# Исходные матрицы A и b
A = np.array([[3.96, -1.5, 0, -0.99, -1.4, 0],
              [3.96, 18.3, 1.6, 6.93, 4.3,1.5],
              [0,  4.5, -13, 4.29, -1.4,2.3],
              [3.96, 0.4, 0, 5.94, 1.5,0],
              [5.94, 3.1, 3.4, 0.99, 14.4, 0.9],
              [-2.97,-1.2,8 ,4.95,-2.7,12.7]])
b = np.array([11.95, -64.89, -38.57, -23.82, -84.83,30.35])
D = np.diag(np.diag(A)) #  Ax=b x=Сx+d для метода итераций
C = np.dot(np.linalg.inv(D), D - A)
d = np.dot(np.linalg.inv(D), b)
if np.linalg.norm(C) >= 1:
    print("Условие сходимости нет.")
else:
    print("Условие сходимости есть")
x = np.zeros_like(b)  # Начальное приближение
for _ in range(10): # 10 итераций метода Якоби
    x = np.dot(C, x) + d
exact_solution = np.linalg.solve(A, b) # метода Гаусса

abs_error = np.linalg.norm(x - exact_solution) # Вычисление погрешностей
rel_error = abs_error / np.linalg.norm(x)

print("\ решение (после 10 итераций метода Якоби):")
print(x)
print("\nАбсолютная погрешность:", abs_error)
print("Относительная погрешность:", rel_error)

#2
import numpy as np

# Исходные матрицы A и b
A = np.array([[3.96, -1.5, 0, -0.99, -1.4, 0],
              [3.96, 18.3, 1.6, 6.93, 4.3,1.5],
              [0,  4.5, -13, 4.29, -1.4,2.3],
              [3.96, 0.4, 0, 5.94, 1.5,0],
              [5.94, 3.1, 3.4, 0.99, 14.4, 0.9],
              [-2.97,-1.2,8 ,4.95,-2.7,12.7]])
b = np.array([32.83, 91.31, 29.91, 98.8, 57.97,37.29])
D = np.diag(np.diag(A)) #  Ax=b x=Сx+d для метода итераций
C = np.dot(np.linalg.inv(D), D - A)
d = np.dot(np.linalg.inv(D), b)
if np.linalg.norm(C) >= 1:
    print("Условие сходимости нет.")
else:
    print("Условие сходимости есть")
x = np.zeros_like(b)  # Начальное приближение
for _ in range(10): # 10 итераций метода Якоби
    x = np.dot(C, x) + d
exact_solution = np.linalg.solve(A, b) # метода Гаусса

abs_error = np.linalg.norm(x - exact_solution) # Вычисление погрешностей
rel_error = abs_error / np.linalg.norm(x)

print("\ решение (после 10 итераций метода Якоби):")
print(x)
print("\nАбсолютная погрешность:", abs_error)
print("Относительная погрешность:", rel_error)  