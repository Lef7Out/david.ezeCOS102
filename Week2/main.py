
import cmath
import numpy as np

print(" Root Finder for Polynomial Equations ")
print("1. Quadratic Equation (Ax² + Bx + C = 0)")
print("2. Cubic Equation (Ax³ + Bx² + Cx + D = 0)")
print("3. Quartic Equation (Ax⁴ + Bx³ + Cx² + Dx + E = 0)")

def solve_quadratic(a, b, c):
    if a == 0:
        print("Not a quadratic equation.")
        return
    disc = cmath.sqrt(b**2 - 4*a*c)
    root1 = (-b + disc) / (2*a)
    root2 = (-b - disc) / (2*a)
    print(f"Roots of the quadratic equation: {root1}, {root2}")

def solve_cubic(a, b, c, d):
    if a == 0:
        print("Not a cubic equation.")
        return
    coefficients = [a, b, c, d]
    roots = np.roots(coefficients)
    print("Roots of the cubic equation:")
    for r in roots:
        print(r)

def solve_quartic(a, b, c, d, e):
    if a == 0:
        print("Not a quartic equation.")
        return
    coefficients = [a, b, c, d, e]
    roots = np.roots(coefficients)
    print("Roots of the quartic equation:")
    for r in roots:
        print(r)
        
print(" Root Finder for Polynomial Equations ")
print("1. Quadratic Equation (Ax² + Bx + C = 0)")
print("2. Cubic Equation (Ax³ + Bx² + Cx + D = 0)")
print("3. Quartic Equation (Ax⁴ + Bx³ + Cx² + Dx + E = 0)")

choice = input("Choose the type of equation to solve (1/2/3): ")

if choice == '1':
    a = float(input("Enter coefficient A: "))
    b = float(input("Enter coefficient B: "))
    c = float(input("Enter coefficient C: "))
    solve_quadratic(a, b, c)

elif choice == '2':
    a = float(input("Enter coefficient A: "))
    b = float(input("Enter coefficient B: "))
    c = float(input("Enter coefficient C: "))
    d = float(input("Enter coefficient D: "))
    solve_cubic(a, b, c, d)

elif choice == '3':
    a = float(input("Enter coefficient A: "))
    b = float(input("Enter coefficient B: "))
    c = float(input("Enter coefficient C: "))
    d = float(input("Enter coefficient D: "))
    e = float(input("Enter coefficient E: "))
    solve_quartic(a, b, c, d, e)

else:
    print("Invalid choice. Please select 1, 2, or 3.")
