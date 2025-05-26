
P = float(input("Enter Principal Amount:"))
R = float(input("Enter Rate Amount:"))
T = float(input("Enter Time in years:"))
n = float(input("Enter number times interest is Compounded per years:"))
PMT = float(input("Enter Annuity Payment (PMT):"))

def si():
    # simple interest
    A = P * (1 + ((R/100) * T))
    return A

def ci():
    # Compound interest
    A = P * (1 + R / (100 * n)) ** (n * T)
    return A

def ap():
    # Annuity Plan
    A = PMT * (((1 + R/n) ** (n * T)) - 1) / (R/n)
    return A

simple_I = si()
compound_I = ci()
annuity_P = ap()

print(f"Total Amount of Simple Interest:{simple_I:.2f}")
print(f"Total Amount of Compound Interest:{compound_I:.2f}")
print(f"Total Amount of Annuity Plan:{annuity_P:.2f}")





