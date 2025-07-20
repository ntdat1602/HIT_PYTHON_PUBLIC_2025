# Bài 4: Hà Nội là vùng đất mà cư dân cực kỳ thích uống bia, vì thế để tăng số lượng bia bán ra,
# các cửa hàng bia ở đây đưa ra khuyến mại như sau:cứ 3 vỏ chai sẽ được đổi lấy 1 chai bia mới.
# Biết rằng, mỗi chai bia có giá 28 xu, nhiệm vụ của bạn là xác định với N xu cho trước,
# bạn có thể mua được tối đa bao nhiêu chai bia, tính cả việc đổi thưởng bằng vỏ chai?

n = int(input("Nhập số xu: "))

# Mỗi chai giá 28 xu
gia_chai = 28

# Bước 1: Mua được bao nhiêu chai ban đầu
chai_mua = n // gia_chai
tong_chai = chai_mua
vo_chai = chai_mua

# Bước 2: Đổi vỏ lấy chai mới
while vo_chai >= 3:
    doi_duoc = vo_chai // 3
    tong_chai += doi_duoc
    vo_chai = doi_duoc + (vo_chai % 3)

# In kết quả
print("Số chai bia có thể mua được là:", tong_chai)
