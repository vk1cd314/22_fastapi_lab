def f_x(x):
    return x**3 - x - 1

x_lower = 50
x_upper = -50

def bisection_method(a, b, accuracy=0.0001):
    f_a = f_x(a)
    f_b = f_x(b)
    if (f_a > 0 and f_b > 0) or (f_a < 0 and f_b < 0):
        print("No roots exist within the interval")
        return
    c = a
    f_c = 100000000000
    absolute_errors = []
    relative_errors = []
    approximations = []
    
    while abs(f_c) > accuracy:
        f_a = f_x(a)
        c = (b + a) / 2
        f_c = f_x(c)
        if f_c * f_a > 0:
            a = c
        else:
            b = c

        if c != 0:
            approximations.append(c)
        
        if c == 0:
            relative_errors.append(None)
        else:
            relative_errors.append(f_c / c)
    
    for i in range(1, len(approximations)):
        absolute_errors.append(abs(approximations[i] - approximations[i - 1]))
        if approximations[i] != 0:
            relative_errors.append(absolute_errors[len(absolute_errors) - 1] / approximations[i])
    
    return c, absolute_errors, relative_errors

b_root, b_absolute_errors, b_relative_errors = bisection_method(x_lower, x_upper)
print(f"Bisection Method:")
print(f"Root approximation = {b_root:.5f}")

def false_position(a, b, accuracy=0.01):
    f_a = f_x(a)
    f_b = f_x(b)
    
    if (f_a > 0 and f_b > 0) or (f_a < 0 and f_b < 0):
        print("No roots exist within the interval")
        return
    
    c = a
    f_c = 100000000000
    absolute_errors = []
    relative_errors = []
    approximations = []
    
    while abs(f_c) > accuracy:
        f_a = f_x(a)
        f_b = f_x(b)
        c = (a * f_b - b * f_a) / (f_b - f_a)
        
        if c != 0:
            approximations.append(c)
        
        f_c = f_x(c)
        if f_c * f_a <= 0:
            b = c
        else:
            a = c

    for i in range(1, len(approximations)):
        absolute_errors.append(abs(approximations[i] - approximations[i - 1]))
        if approximations[i] != 0:
            relative_errors.append(absolute_errors[len(absolute_errors) - 1] / approximations[i])
    
    return c, absolute_errors, relative_errors

f_root, f_absolute_errors, f_relative_errors = false_position(x_lower, x_upper)
print("\nFalse Position Method:")
print(f"Root approximation = {f_root:.5f}")

import matplotlib.pyplot as plt

plt.bar(range(1, len(b_absolute_errors) + 1), b_absolute_errors)
plt.xlabel("Iterations")
plt.ylabel("Absolute Error for Bisection Method")
plt.title("Error vs Iteration Graph - Bisection Method")
plt.show()

plt.bar(range(1, len(f_absolute_errors) + 1), f_absolute_errors)
plt.xlabel("Iterations")
plt.ylabel("Absolute Error for False Position Method")
plt.title("Error vs Iteration Graph - False Position Method")
plt.show()

plt.bar(range(1, len(b_relative_errors)), b_relative_errors[1:])
plt.xlabel("Iterations")
plt.ylabel("Relative Error for Bisection Method")
plt.title("Relative Error vs Iteration Graph - Bisection Method")
plt.show()

plt.bar(range(1, len(f_relative_errors) + 1), f_relative_errors)
plt.xlabel("Iterations")
plt.ylabel("Relative Error for False Position Method")
plt.title("Relative Error vs Iteration Graph - False Position Method")
plt.show()

plt.plot(range(1, len(b_absolute_errors) + 1), b_absolute_errors, label="Bisection Method")
plt.plot(range(1, len(f_absolute_errors) + 1), f_absolute_errors, label="False Position Method")
plt.ylabel("Absolute Error")
plt.xlabel("Iterations")
plt.legend()
plt.show()

plt.plot(range(1, len(b_relative_errors) + 1), b_relative_errors, label="Bisection Method")
plt.plot(range(1, len(f_relative_errors) + 1), f_relative_errors, label="False Position Method")
plt.ylabel("Relative Error")
plt.xlabel("Iterations")
plt.legend()
plt.show()