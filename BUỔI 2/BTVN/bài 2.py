# Bài 2: Giả sử bạn là kế toán cho một công ty. Bạn cần viết một chương trình để nhập lương nhân viên, tính thuế thu nhập và lương ròng (số tiền lương thực sự mà nhân viên đó nhận được). Với các thông số sau (mình chỉ đưa ra các con số này cho dễ tính toán):
# - 30% thuế thu nhập nếu lương là 15 triệu
# - 20% thuế thu nhập nếu lương từ 7 đến 15 triệu
# - 10% thuế thu nhập nếu lương dưới 7 triệu

luong = int ( input ( " Nhập lương : ")) 
if luong == 15000000 : 
    thue = luong * 0.3 
elif 7000000 <= luong <= 15000000 : 
    thue = luong * 0.2 
elif luong < 7000000 : 
    thue = luong * 0.1 

luong_rong = luong - thue 
print ( " Lương : " , luong ) 
print ( " Thuế thu nhập : " , thue ) 
print ( " Lương ròng : " , luong_rong )