def bisect(f, a, b, e):
  while abs(b - a) > e:
    m = (a + b) / 2
    if f(m) == 0:
      return m
    elif f(m) * f(a) < 0:
      b = m
    else:
      a = m
  return (a + b) / 2
def newton(f, df, x0, e):
  while abs(f(x0)) > e:
    x0 -= f(x0) / df(x0)
  return x0
def secant(f, x0, x1, e):
  while abs(x1 - x0) > e:
    x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
    x0 = x1
    x1 = x2
  return x2
def f(x):
  return x + x**2 - 10
def df(x):
  return 1 + 2 * x
x0 = 1
x1 = 2
e = 1e-5
root_bisection = bisect(f, 0, 10, e)
root_newton = newton(f, df, x0, e)
root_secant = secant(f, x0, x1, e)
print("метод половинного деления:", root_bisection)
print("методом ньютона:", root_newton)
print("методом секущих:", root_secant)