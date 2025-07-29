# 1. Nhập chuỗi
s1 = input("Nhập chuỗi s1: ")
s2 = input("Nhập chuỗi s2: ")

# 2. In ra đảo ngược của s1
print("Đảo ngược s1:", s1[::-1])

# 3. Nhập a, b và xử lý đảo ngược đoạn s2[a:b+1]
a = int(input("Nhập a (>= 1): ")) - 1  
b = int(input("Nhập b (<= độ dài s2): "))  

if 0 <= a < b <= len(s2):
    s2 = s2[:a] + s2[a:b][::-1] + s2[b:]
    print("s2 sau khi đảo đoạn từ a đến b:", s2)
else:
    print("Giá trị a, b không hợp lệ.")

# 4. Tạo s3: xóa ký tự ở vị trí chẵn (0, 2, 4,...)
s3 = ''.join([s1[i] for i in range(len(s1)) if i % 2 == 1])
print("s3 (xóa ký tự ở vị trí chẵn của s1):", s3)

# 5. Tạo s4: đan xen các ký tự của s1 và s2
s4 = ''
for i in range(max(len(s1), len(s2))):
    if i < len(s1):
        s4 += s1[i]
    if i < len(s2):
        s4 += s2[i]
print("s4 (đan xen s1 và s2):", s4)
