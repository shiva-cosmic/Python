# Write a python program using function to convert celsius to fahrenheit.

# Formula: c/5 = (f - 32)/9

def f_to_c(f):
    return 5*(f-32)/9

f = int(input("Enter temperature in F: "))

print(f"{f_to_c(f)} Degree C")