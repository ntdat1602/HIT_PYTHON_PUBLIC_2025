# Nhập list a từ bàn phím
a = list(map(int, input("Nhập list a (các số cách nhau bởi dấu cách): ").split()))

# Nhập số dòng n và số cột m
n = int(input("Nhập số dòng n: "))
m = int(input("Nhập số cột m: "))

# Tính số phần tử cần có để tạo ma trận
k = len(a)

# Kiểm tra nếu có thể tạo ma trận
if n * m != k:
    print("NO")
else:
    # Tạo ma trận
    matrix = []
    for i in range(n):
        row = a[i * m:(i + 1) * m]
        matrix.append(row)

    # In ma trận kết quả
    print("Ma trận kết quả:")
    for row in matrix:
        print(row)


