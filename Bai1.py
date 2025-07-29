# 1: Nhập list có N phần tử là số nguyên
N = 10
lst = [3, 6, 9, 6, 2, 6, 7, 8, 5, 4]  

# 2: Nhập X và đếm số lần X xuất hiện
X = 6
so_lan_xuat_hien = lst.count(X)

# 3: Thay thế phần tử từ vị trí 2 đến 7 (chỉ số 2 đến 7, tức là các phần tử thứ 3 đến thứ 8)
lst[2:8] = [8, 5, 4, 0, 1, 3]
lst_sau_thay_the = lst.copy()

# 4: Tìm số lớn nhất và nhỏ nhất
lon_nhat = max(lst_sau_thay_the)
nho_nhat = min(lst_sau_thay_the)

# 5: Nhập số Y và chèn vào đầu list
Y = 10
lst_sau_thay_the.insert(0, Y)

# 6: Kiểm tra list sau khi chèn Y có tăng, giảm hay không
if lst_sau_thay_the == sorted(lst_sau_thay_the):
    trang_thai = "TĂNG"
elif lst_sau_thay_the == sorted(lst_sau_thay_the, reverse=True):
    trang_thai = "GIẢM"
else:
    trang_thai = "NO"


    