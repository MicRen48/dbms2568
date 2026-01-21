import numpy as np

# ฟังก์ชัน f(x) = (x - 1)^3 + 0.512
f = lambda x: (x-1)**3 + 0.512

# อนุพันธ์ f'(x) = 3 * (x - 1)^2
f_prime = lambda x: 3 * (x - 1)**2

# กำหนดจำนวน Iterations และค่าเริ่มต้น
N = 19   
X0 = 5.0 

# ----------------------------------------------------
# แก้ไข Syntax Error ที่บรรทัด Header: ลบ backslash ออกจาก f'(Xi)
# ----------------------------------------------------
print(f" i|{'Xi':>12}|{'f(Xi)':>12}|{'f\'(Xi)':>12}|") # <-- บรรทัดนี้ทำให้เกิด error
# แก้เป็น:
print(f" i|{'Xi':>12}|{'f(Xi)':>12}|{'f\'(Xi)':>12}|") # <-- แก้แล้ว
print("=" * 43) 

# Iteration 0 (แสดงค่าเริ่มต้น)
print(f"{0:>2}|{X0:12.6f}|{f(X0):12.6f}|{f_prime(X0):12.6f}|")

# ลูปคำนวณซ้ำ Newton-Raphson
for i in range(1, N):
    
    X_i = X0
    
    f_val = f(X_i)
    f_prime_val = f_prime(X_i)
    
    if abs(f_prime_val) < 1e-10: 
        print(f"Iteration {i:>2}: Error! f'(X) = {f_prime_val:.2e} ใกล้ 0 เกินไป")
        break
    
    Xn = X_i - (f_val / f_prime_val)
    X0 = Xn
    
    # แสดงผลลัพธ์ของ Iteration i
    print(f"{i:>2}|{Xn:12.6f}|{f(Xn):12.6f}|{f_prime(Xn):12.6f}|")

print("=" * 43)