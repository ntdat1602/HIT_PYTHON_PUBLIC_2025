# Bài 1: Cho biết tháng và năm, hãy in ra số ngày tương ứng có trong tháng đó.
# Chú ý tháng 2 của năm nhuận có 29 ngày.

while True   : 
    try : 
        month = int ( input("Nhập tháng ( 1 - 12 ) : ")) 
        if 0 < month < 13 : 
            break 
        else : 
            print ( "Nhập lại !!! ") 
    except ValueError : 
        print ( " Lỗi ") 
while True : 
    try : 
        year = int ( input("Nhập năm : ")) 
        if year > 0 : 
            break 
        else : 
            print ( "Nhập lại !!! ") 
    except ValueError : 
        print ( " Lỗi ") 

if month in  [1, 3, 5, 7, 8, 10, 12]:
     so_ngay = 31 
elif month in [4 , 6 , 9 , 11 ] : 
    so_ngay = 30 
elif month == 2 : 
    if ( year % 4 == 0 and year % 100 != 0 ) or ( year % 400 == 0 ) : 
        so_ngay = 29 
    else : 
        so_ngay = 28 

print ( f"Tháng {month } - Năm {year} có {so_ngay} ngày ")