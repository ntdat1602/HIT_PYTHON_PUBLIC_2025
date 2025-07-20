# Bài 3: Đếm số lượng chữ số và tính tổng chữ số của N!. 
# Nhập vào n, đếm số lượng chữ số của n và tổng các chữ số của n, sau đó in ra kết quả.

n = int(input("Nhập số nguyên N: "))

so_chu_so = len(str(abs(n))) 
tong_chu_so = sum(int(chu) for chu in str(abs(n)))

print("Số chữ số:", so_chu_so)
print("Tổng chữ số:", tong_chu_so)
