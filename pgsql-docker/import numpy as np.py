import numpy as np
from scipy import integrate
import math

# 1. Define the function to integrate
def f(x):
    return (300 * x) / (1 + np.exp(x))

# 2. Integration limits
a = 0
b = 10

# 3. Calculate True Value using scipy for error calculation
true_value, _ = integrate.quad(f, a, b)

print(f"True Value: {true_value:.6f}")
print("-" * 65)
# Note: |Et| column represents the Absolute Relative Error Percentage
print(f"{'n':>5} {'ApproxV':>12} {'Et':>12} {'|Et|%':>10} {'m':>5}")
print("=" * 65)

# 4. Start Trapezoidal Rule loop
n = 1

while True:
    # Calculate segment width (h)
    h = (b - a) / n
    
    # Generate points
    x_points = np.linspace(a, b, n + 1)
    y_points = f(x_points)
    
    # Trapezoidal Rule Formula
    sum_mid = np.sum(y_points[1:-1])
    approx_val = (h / 2) * (y_points[0] + 2 * sum_mid + y_points[-1])
    
    # Error Calculations
    Et = true_value - approx_val             # True Error
    abs_Et_pct = abs(Et / true_value) * 100  # Absolute Relative Error (%)
    
    # Calculate Significant Digits (m)
    # Formula: m = floor(2 - log10(error%))
    if abs_Et_pct > 0:
        m = math.floor(2 - math.log10(abs_Et_pct))
    else:
        m = 0
        
    if m < 0:
        m = 0

    # Print row
    print(f"{n:5d} {approx_val:12.3f} {Et:12.3f} {abs_Et_pct:10.3f} {int(m):5d}")

    # Stop when significant digits reach 4
    if m >= 4:
        break
        
    # Double the segments for the next iteration
    n *= 2