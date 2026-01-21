import math

# --- 1. Define the function f(x) ---
def f(x):
    """
    The function to be integrated: f(x) = 5 * x * e^(-2*x)
    """
    return 5.0 * x * math.exp(-2.0 * x)

# --- 2. Set integration parameters ---
a = 0.1     # Lower limit (จากค่าที่คุณระบุในโจทย์ก่อนหน้า)
b = 1.3     # Upper limit (จากค่าที่คุณระบุในโจทย์ก่อนหน้า)
n = 4       # Number of segments

# --- 3. Calculate step size (h) ---
h = (b - a) / n
print(f"Lower limit (a): {a}")
print(f"Upper limit (b): {b}")
print(f"Number of segments (n): {n}")
print(f"Step size (h): {h:.4f}")
print("-" * 30)

# --- 4. Simpson's 1/3 Rule Calculation ---

# Initialize sum variables
integral_sum = 0.0

# Calculate the value at the start point (f(x_0))
x0 = a
f_x0 = f(x0)
integral_sum += f_x0
print(f"x_{0} = {x0:.4f}, f(x_{0}) = {f_x0:.6f}")

# Loop through the intermediate points (x_1 to x_{n-1})
for i in range(1, n):
    x_i = a + i * h
    f_xi = f(x_i)
    
    if i % 2 != 0:
        # Odd-indexed points (i=1, 3, 5) get a multiplier of 4
        integral_sum += 4 * f_xi
        multiplier = 4
    else:
        # Even-indexed points (i=2, 4) get a multiplier of 2
        integral_sum += 2 * f_xi
        multiplier = 2
        
    print(f"x_{i} = {x_i:.4f}, f(x_{i}) = {f_xi:.6f} (Mult: {multiplier})")

# Calculate the value at the end point (f(x_n))
xn = b
f_xn = f(xn)
integral_sum += f_xn
print(f"x_{n} = {xn:.4f}, f(x_{n}) = {f_xn:.6f}")
print("-" * 30)

# Apply the final formula: Integral ≈ (h/3) * Sum
x_approx = (h / 3.0) * integral_sum

# --- 5. Output the result ---
print(f"The approximate value of the integral x is: {x_approx:.6f}")