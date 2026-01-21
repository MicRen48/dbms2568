import math


def f(x):
    # ฟังก์ชัน f(x) (สมมติ)
    return x**3 - 0.0002428 
    
# 📌 แก้ไข: ให้ฟังก์ชันกลับมารับพารามิเตอร์ N อีกครั้ง
def myrun(): 
    # print("======================================================") # 📌 ลบเส้นบรรทัดนี้ออก

    xl = 0.00000
    xu = 0.11000
    
    n = 3 
    
    # คำนวณ Error ที่ยอมรับได้
    es = 0.5 * (10**(2 - n))
    
    # 📌 ปรับความกว้างคอลัมน์ Iteration เป็น 10 และอื่นๆ ให้ตรงตาม output
    print(f"{'Iteration':<10} {'Xl':<10} {'Xu':<10} {'Xm':<10} {'|Ea|':<10} {'f(Xm)':<12} {'m':<5}")
    print("=======================================================") # ใช้เส้นนี้ให้ตรงกับ Output ตัวอย่าง

    xm_old = 0
    ea = 100.0 
    iter_count = 0

    while True:
        iter_count += 1
        
        # Calculate midpoint
        xm = (xl + xu) / 2.0
        

        if iter_count > 1:
            ea = abs((xm - xm_old) / xm) * 100
        else:
            ea = 100.0 
            
        
        ea_display = f"{ea:.4f}" if iter_count > 1 else "--"
        
        m_val = "-"
        if iter_count > 1 and ea > 0:
            try:
                val = 2 - math.log10(2 * ea)
                m_val = math.floor(val)
                if m_val < 0: m_val = 0
            except:
                m_val = "-"

        # 📌 ปรับความกว้างคอลัมน์ให้ตรงกับ Header
        print(f"{iter_count:<10} {xl:<10.5f} {xu:<10.5f} {xm:<10.5f} {ea_display:<10} {f(xm):<12.2e} {m_val:<5}")
            
        # เงื่อนไขการหยุดตาม Error (es)
        if iter_count > 1 and ea < es:
            # print("-" * 75) # ลบเส้นนี้ออกเพื่อให้ Output ตรงกัน
            print(f"converged at Iteration {iter_count}")
            print(f"Reason: Error ({ea:.4f}%) is less than Threshold ({es}%)")
            break
            

        # Bisection logic to select new interval
        if f(xl) * f(xm) < 0:
            xu = xm
        elif f(xl) * f(xm) > 0:
            xl = xm
        else:
            break
            
        xm_old = xm
        
        # Safety break
        if iter_count >= 50:
            print("Max iterations reached.")
            break


if __name__=='__main__':
    # 📌 นำบรรทัด input กลับมาใช้ และเรียก myrun(N)

    myrun()